56_big_remaining_marker_index

判定:
  BIG_REMAINING_MARKER_INDEX_READY

目的:
  残り5検証を終わらせるため、
  H:\Device-Logs_整理済み 全体から marker を大きく索引化する。

対象カテゴリ:
  trust_graph_lineage
  backup_manifest_inheritance
  proximity_vs_cloud
  evidence_preservation_suppression
  normal_control_stress
  daemon_state

主要数値:
  files_seen: 17934
  files_relevant: 8153
  files_scanned: 8153
  files_skipped_large: 0
  context_rows: 250000
  file_inventory_parts: 3
  context_parts: 39
  errors: 0

見るべきファイル:
  00_MASTER_SUMMARY.json
  03_category_hit_summary.csv
  04_device_remaining_marker_summary.csv
  05_device_month_marker_summary.csv
  01_remaining_marker_file_inventory_part*.csv
  02_remaining_marker_contexts_part*.csv

このscriptでやること:
  - 残り検証の全体索引
  - Trust / Backup / Proximity / Evidence / Normal-Control のmarker整理
  - 57以降の軽量化

このscriptだけでは言えないこと:
  - 各章の最終結論
  - 攻撃確定
  - Apple関与確定
  - hidden MDM確定
  - server-side制御確定

次:
  57_trust_graph_lineage_review
