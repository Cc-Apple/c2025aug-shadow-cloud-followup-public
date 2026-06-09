57_trust_graph_lineage_review

判定:
  TRUST_GRAPH_LINEAGE_PARTIAL_REVIEW_READY

目的:
  56_big_remaining_marker_index の索引から、
  Trust Graph Lineage 章を切り出して精査する。

入力:
  D:\Desktop\1\56_big_remaining_marker_index

56側:
  status: DONE
  final_verdict: BIG_REMAINING_MARKER_INDEX_READY
  trust_graph_lineage は十分強い材料あり

主要数値:
  context_rows_seen: 250000
  trust_context_rows: 80187
  trust_context_sampled_rows: 80187
  trust_file_rows: 6341
  strong_device_count: 1
  medium_device_count: 0
  errors: 0

見るべきCSV:
  03_trust_family_summary.csv
  04_trust_keyword_summary_top300.csv
  05_device_trust_graph_lineage_summary.csv
  06_device_month_trust_graph_timeline.csv
  08_normal_vs_control_trust_graph_interpretation.csv

このscriptで言えること:
  - Trust / Apple ID / AuthKit / Keychain / ScreenTime / Cloud bridge 系の濃淡
  - どの端末でTrust Graph Lineageが強いか
  - 58でsealするための材料整理

このscriptだけでは言えないこと:
  - hidden MDM確定
  - Apple関与確定
  - server-side制御確定
  - 攻撃者意図確定
  - Trust Graph悪用確定

次:
  58_trust_graph_lineage_seal
