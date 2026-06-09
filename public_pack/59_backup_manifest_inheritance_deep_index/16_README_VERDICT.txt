59_backup_manifest_inheritance_deep_index

判定:
  BACKUP_MANIFEST_INHERITANCE_DEEP_INDEX_READY

目的:
  Backup / Manifest / RTCR / Snapshot / iMazing 継承を深掘り索引化する。

入力:
  H:\Manifest
  D:\Desktop\1\56_big_remaining_marker_index
  D:\Desktop\1\58_trust_graph_lineage_seal

安全設計:
  00〜ff実体群は読まない
  Snapshot本文は読まず、Snapshot directory metadataのみ記録
  Manifest.db / plist / backup marker / 56索引を中心に読む

主要数値:
  files_seen: 45458
  files_kept: 45458
  exact Manifest.db: 137
  sqlite_ok: 7
  opaque_manifestdb: 130
  backup_generation_rows: 12060
  transition_rows: 128
  same_size_different_hash_groups: 5
  same_hash_repetition_groups: 27
  56_backup_context_rows_total: 199881
  errors: 0

見るべきCSV:
  03_exact_manifestdb_deep_inventory.csv
  06_manifestdb_state_transitions.csv
  07_manifestdb_transition_summary.csv
  08_manifestdb_same_size_hash_patterns.csv
  10_backup_marker_summary_from_56.csv
  13_device_backup_manifest_inheritance_summary.csv
  14_normal_vs_control_backup_manifest_interpretation.csv

このscriptで言えること:
  - Backup / Manifest継承章の深掘り索引ができたか
  - Manifest.dbのSQLite/opaque/entropy/hash/世代遷移
  - 56側のRTCR/backup markerとの接続
  - 60 sealへ進めるか

このscriptだけでは言えないこと:
  - tampering確定
  - Apple関与確定
  - hidden MDM確定
  - server-side制御確定
  - 攻撃者意図確定

次:
  60_backup_manifest_inheritance_seal
