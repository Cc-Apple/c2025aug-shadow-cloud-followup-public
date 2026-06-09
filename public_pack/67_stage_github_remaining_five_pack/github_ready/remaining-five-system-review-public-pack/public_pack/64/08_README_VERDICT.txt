64_normal_hypothesis_collapse_table

判定:
  NORMAL_HYPOTHESIS_COLLAPSE_TABLE_READY_STRONG_STRESS

collapse_strength_score:
  100

目的:
  63/63bをもとに、通常説明がどこまで崩れたかを人間可読の表にする。

63/63b結果:
  63 final_verdict: NORMAL_CONTROL_STRESS_TEST_MEDIUM_HIGH_NORMAL_EXPLANATIONS_STRESSED
  63 final_score: 70
  63b final_verdict: NORMAL_CONTROL_RAW_DIFF_AUDIT_PASSED_USE_63
  63b device_severe_diff_count: 0
  63b group_severe_diff_count: 0

中核:
  12G score: 94

補助:
  15G score: 51
  mini1 score: 51

64の結論:
  通常説明は一部残る。
  しかし、単一端末不具合・物理接触だけ・通常同期だけ・通常負荷だけでは説明がかなり苦しい。
  63bで63の差分監査も通過しているため、64の表は65 final sealへ使える。

言えること:
  - 通常仮説は複合軸で強く圧迫される
  - 12Gが中核
  - 15G / mini1 が中程度補助
  - 物理接触説だけでは弱い
  - 暗号ON backup説明は残るが、Backup/Manifest構造は強い

言えないこと:
  - 攻撃確定
  - Apple関与確定
  - hidden MDM確定
  - server-side制御確定
  - 攻撃者意図確定

次:
  65_remaining_five_system_final_seal
