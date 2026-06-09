62_evidence_preservation_suppression_review

判定:
  EVIDENCE_PRESERVATION_SUPPRESSION_REVIEW_READY_STRONG_CANDIDATES

目的:
  証拠保存妨害・保存性低下候補を構造整理する。
  pressure / logging deletion / capture failure / backup failure / trigger chain を分ける。

主要数値:
  56_context_rows_seen: 250000
  56_evidence_context_rows_kept: 123242
  raw_files_seen: 17934
  raw_files_relevant: 8536
  raw_files_scanned: 8536
  context_rows_total: 373242
  daily_matrix_rows: 339
  strong_device_count: 4
  medium_device_count: 0
  strong_trigger_pressure_cooccurrence_count: 167
  capture_backup_preservation_risk_count: 36
  strong_incident_day_pressure_count: 0
  errors: 0

見るべきCSV:
  03_daily_evidence_pressure_matrix.csv
  04_device_evidence_pressure_summary.csv
  05_process_marker_summary.csv
  06_trigger_pressure_cooccurrence.csv
  07_incident_day_evidence_pressure_alignment.csv
  08_normal_vs_control_evidence_pressure_interpretation.csv
  09_claim_boundary_evidence_pressure.csv

このscriptで言えること:
  - 証拠保存性低下候補の端末別・日別整理
  - pressure と trigger chain の同時性候補
  - backup/snapshot失敗やcapture失敗の補助線

このscriptだけでは言えないこと:
  - pressure/log deletion = 攻撃確定
  - screenshot失敗 = 意図的阻止確定
  - Apple関与確定
  - hidden MDM確定
  - server-side制御確定
  - 攻撃者意図確定

次:
  63_normal_control_stress_test
