63_normal_control_stress_test

判定:
  NORMAL_CONTROL_STRESS_TEST_MEDIUM_HIGH_NORMAL_EXPLANATIONS_STRESSED

final_score:
  70
  STRONG

目的:
  56/58/60/61/62を横断し、通常解釈がどこまで耐えるかstress testする。

重要:
  これは攻撃証明ではない。
  normal/control baselineも完全clean controlとは限らない。

主要結果:
  strong_user_core_devices: 12G
  medium_user_core_devices: 
  strong_comparison_devices: 
  medium_comparison_devices: 
  stressed_hypothesis_count: 5
  group_strong_stress_count: 4
  group_medium_stress_count: 1
  errors: 0

見るべきCSV:
  02_device_axis_score_matrix.csv
  03_group_stress_comparison.csv
  04_normal_hypothesis_stress_table.csv
  05_control_device_baseline_review.csv
  06_abnormal_cluster_vs_control_boundary.csv
  07_claim_boundary_normal_control.csv

63で言えること:
  - 通常解釈に対する横断stress評価
  - user coreとcomparison/control候補の軸別差分
  - 単一端末不具合説・物理接触説・通常同期説の弱点整理

63で言えないこと:
  - 攻撃確定
  - Apple関与確定
  - hidden MDM確定
  - server-side制御確定
  - 攻撃者意図確定

次:
  64_normal_hypothesis_collapse_table
