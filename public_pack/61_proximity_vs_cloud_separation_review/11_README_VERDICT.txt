61_proximity_vs_cloud_separation_review

判定:
  PROXIMITY_CLOUD_SEPARATION_REVIEW_READY_WEAK_VISIBLE_PROXIMITY

目的:
  physical proximity / BSSID / RSSI / Wi-Fi / Bluetooth / CommCenter / Baseband / PLMN と、
  Cloud / Trust / Backup seam を分離する。

主要数値:
  56_context_rows_seen: 250000
  56_proximity_context_rows_kept: 242662
  raw_files_seen: 17934
  raw_files_relevant: 9759
  raw_files_scanned: 9759
  context_rows_total: 492662
  observation_rows_total: 25
  shared_bssid_candidate_count: 0
  shared_plmn_candidate_count: 0
  cluster_physical_supported_count: 0
  cluster_cloud_supported_count: 0
  cluster_telecom_supported_count: 0
  cluster_mixed_count: 0
  errors: 0

見るべきCSV:
  04_shared_bssid_plmn_candidate_matrix.csv
  05_daily_proximity_cloud_matrix.csv
  06_c2025aug_cluster_proximity_cloud_alignment.csv
  07_device_proximity_cloud_summary.csv
  08_normal_vs_control_proximity_cloud_interpretation.csv
  09_claim_boundary_proximity_cloud.csv

このscriptで言えること:
  - 物理近接系 / Telecom系 / Cloud-Trust系の分離
  - C2025AUGクラスタが物理接触寄りかCloud/Trust寄りかの整理
  - shared BSSID / PLMN候補

このscriptだけでは言えないこと:
  - BSSIDが出た = 攻撃者接近確定
  - Cloud/Trustが出た = server-side制御確定
  - Apple関与確定
  - hidden MDM確定
  - 攻撃者意図確定

次:
  62_evidence_preservation_suppression_review
