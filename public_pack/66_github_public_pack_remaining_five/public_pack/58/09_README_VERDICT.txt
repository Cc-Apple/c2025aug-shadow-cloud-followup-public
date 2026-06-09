58_trust_graph_lineage_seal

判定:
  TRUST_GRAPH_LINEAGE_SEALED_MEDIUM_12G_CORE

final_score:
  64
  MEDIUM_HIGH

目的:
  57_trust_graph_lineage_review をsealする。

57結果:
  status: DONE
  final_verdict: TRUST_GRAPH_LINEAGE_PARTIAL_REVIEW_READY
  trust_context_rows: 80187
  trust_file_rows: 6341
  strong_device_count: 1
  medium_device_count: 0
  error_rows: 0

58の読み:
  core_device: 12G
  core_device_score: 84

結論:
  Trust Graph Lineage は 12G-core partial model としてsealする。
  12Gでは apple_id/account, trusted_device, keychain/escrow, cloud_trust_bridge が同時に出る。
  ただし strong_device_count=1 のため、全端末横断のTrust Graph確定とは言わない。
  family hit は _productFamily = iPhone ノイズが大きいため FamilyControls直接証拠としては扱わない。

言えること:
  - Trust Graph Lineageの主戦場は12G
  - 12G-core partial seal は妥当
  - cloud_trust_bridge / trusted_device / apple_id_account / keychain_escrow は有効線
  - SFA / cloud trust negative/state は補助証拠

言えないこと:
  - hidden MDM確定
  - Apple関与確定
  - server-side制御確定
  - 攻撃者意図確定
  - Trust Graph悪用確定
  - family hitをそのままFamilyControls証拠とすること

次:
  59_backup_manifest_inheritance_deep_index
