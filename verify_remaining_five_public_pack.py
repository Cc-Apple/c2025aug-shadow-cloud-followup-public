# -*- coding: utf-8 -*-

from pathlib import Path
import hashlib
import csv
import json
import datetime
import re
import sys


ROOT = Path(__file__).resolve().parent
INVENTORY = ROOT / "PACK_INVENTORY.csv"
REPORT_JSON = ROOT / "VERIFY_REPORT.json"
REPORT_CSV = ROOT / "VERIFY_REPORT.csv"

MAX_FILE_SIZE = 2 * 1024 * 1024

DANGEROUS_EXTS = {
    ".ips",
    ".synced",
    ".ca",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".gz",
    ".tar",
    ".tgz",
    ".7z",
    ".rar",
    ".session",
    ".bin",
    ".plist",
    ".log",
    ".trace",
    ".heic",
    ".jpg",
    ".jpeg",
    ".png",
    ".mov",
    ".mp4",
}

DANGEROUS_NAME_PATTERNS = [
    "raw",
    "manifest_body",
    "snapshot_body",
    "payload",
    "00-ff",
    "00_ff",
    "backup_payload",
    "contexts_part",
    "context_part",
    "file_inventory_part",
    "bodies",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_inventory():
    if not INVENTORY.exists():
        return []

    rows = []
    with INVENTORY.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def is_hex_payload_name(path: Path) -> bool:
    name = path.name.lower()

    if re.fullmatch(r"[0-9a-f]{2}", name):
        return True

    if re.fullmatch(r"[0-9a-f]{40}", name):
        return True

    if re.fullmatch(r"[0-9a-f]{64}", name):
        return True

    return False


def add_issue(issues, severity, category, path, detail):
    issues.append({
        "severity": severity,
        "category": category,
        "path": str(path).replace("\\", "/"),
        "detail": detail,
    })


def check_inventory_hashes(issues):
    rows = read_inventory()

    if not rows:
        add_issue(issues, "ERROR", "inventory", INVENTORY, "PACK_INVENTORY.csv not found or empty")
        return 0, 0

    checked = 0
    failed = 0

    for r in rows:
        rel = r.get("relative_path", "").replace("/", "\\")
        expected = (r.get("sha256") or "").lower().strip()

        if not rel or not expected:
            failed += 1
            add_issue(issues, "ERROR", "inventory_row", rel, "missing relative_path or sha256")
            continue

        path = ROOT / "public_pack" / rel

        if not path.exists():
            failed += 1
            add_issue(issues, "ERROR", "missing_file", path, "file listed in inventory but not found")
            continue

        actual = sha256_file(path).lower()
        checked += 1

        if actual != expected:
            failed += 1
            add_issue(issues, "ERROR", "sha256_mismatch", path, f"expected={expected} actual={actual}")

    return checked, failed


def check_raw_leakage(issues):
    scanned = 0
    dangerous = 0
    too_large = 0

    skip_verify_outputs = {
        "VERIFY_REPORT.json",
        "VERIFY_REPORT.csv",
    }

    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue

        if p.name in skip_verify_outputs:
            continue

        scanned += 1
        suffix = p.suffix.lower()
        lower_path = str(p).lower()

        if suffix in DANGEROUS_EXTS:
            dangerous += 1
            add_issue(issues, "ERROR", "dangerous_extension", p, suffix)

        for pat in DANGEROUS_NAME_PATTERNS:
            if pat in lower_path:
                dangerous += 1
                add_issue(issues, "WARN", "dangerous_name_pattern", p, pat)
                break

        if is_hex_payload_name(p):
            dangerous += 1
            add_issue(issues, "WARN", "hex_payload_like_name", p, "hex-like payload filename")

        try:
            size = p.stat().st_size
        except Exception as e:
            add_issue(issues, "WARN", "stat_error", p, repr(e))
            continue

        if size > MAX_FILE_SIZE:
            too_large += 1
            add_issue(issues, "ERROR", "too_large", p, f"{size} bytes")

    return scanned, dangerous, too_large


def write_csv_report(rows):
    fields = ["severity", "category", "path", "detail"]

    with REPORT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_json_report(obj):
    REPORT_JSON.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    issues = []

    checked, failed = check_inventory_hashes(issues)
    scanned, dangerous, too_large = check_raw_leakage(issues)

    error_count = sum(1 for x in issues if x["severity"] == "ERROR")
    warn_count = sum(1 for x in issues if x["severity"] == "WARN")

    status = "PASS" if error_count == 0 else "FAIL"

    report = {
        "status": status,
        "generated_local_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "root": str(ROOT),
        "inventory_path": str(INVENTORY),
        "inventory_hash_checked": checked,
        "inventory_hash_failed": failed,
        "files_scanned": scanned,
        "dangerous_candidate_count": dangerous,
        "too_large_count": too_large,
        "error_count": error_count,
        "warn_count": warn_count,
        "claim_boundary": "strong multi-axis structure, not proof of tampering or attribution",
        "issues": issues,
    }

    write_json_report(report)
    write_csv_report(issues)

    print("VERIFY:", status)
    print("inventory_hash_checked:", checked)
    print("inventory_hash_failed:", failed)
    print("files_scanned:", scanned)
    print("dangerous_candidate_count:", dangerous)
    print("too_large_count:", too_large)
    print("error_count:", error_count)
    print("warn_count:", warn_count)
    print("report_json:", REPORT_JSON)
    print("report_csv:", REPORT_CSV)

    if status != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()