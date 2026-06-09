63b_normal_control_raw_diff_audit

判定:
  NORMAL_CONTROL_RAW_DIFF_AUDIT_PASSED_USE_63

final_score:
  90
  VERY_STRONG

目的:
  63_normal_control_stress_test の答え合わせ。
  63のsummary合成scoreを、58/60/61/62の元CSVから再計算して差分監査する。

重要:
  raw全量再スキャンではない。
  63の過剰評価・summary由来の誤増幅を確認するための検算。

主要結果:
  device_severe_diff_count: 0
  device_minor_diff_count: 3
  group_severe_diff_count: 0
  group_minor_diff_count: 0
  strong_user_core_devices_recomputed: 12G
  medium_user_core_devices_recomputed: 
  strong_comparison_devices_recomputed: 
  medium_comparison_devices_recomputed: 
  errors: 0

見るべきCSV:
  01_device_score_recompute_diff.csv
  02_group_stress_recompute_diff.csv
  03_source_support_by_device.csv
  04_top_trigger_pressure_source_rows.csv
  05_control_risk_review.csv
  06_hypothesis_diff_review.csv
  07_claim_boundary_63b.csv

63bで言えること:
  - 63のscoreが元CSVと一致しているか
  - 63のsummary合成が過剰評価ではないか
  - control/comparison候補をclean controlとして使えるか

63bで言えないこと:
  - 攻撃確定
  - Apple関与確定
  - hidden MDM確定
  - server-side制御確定
  - 攻撃者意図確定

次:
  64_normal_hypothesis_collapse_table
