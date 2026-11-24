# ATMOS-V2: Experimental Data Tables & Benchmarking

This directory contains the verified experimental dataset tables, field validation metrics, and state-of-the-art literature comparisons for the **ATMOS-V2** autonomous air quality monitoring platform.

---

## Table I: Low-Cost Sensor Calibration Benchmark Comparison
*Collocated outdoor validation against Met One BAM-1020 Federal Equivalent Method (FEM) reference ($N = 1,200$ test observations).*

| Model / Calibration Technique | Target | $R^2$ Score | RMSE ($\mu	ext{g/m}^3$) | MAE ($\mu	ext{g/m}^3$) | Max Error ($\mu	ext{g/m}^3$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Raw Plantower PMS5003** | $	ext{PM}_{2.5}$ | 0.582 | 24.64 | 18.21 | 68.42 |
| **Multiple Linear Regression (MLR)** | $	ext{PM}_{2.5}$ | 0.741 | 18.12 | 13.54 | 49.18 |
| **Random Forest Regressor (RF)** | $	ext{PM}_{2.5}$ | 0.881 | 11.45 | 8.24 | 29.75 |
| **Proposed On-Chip INT8 Monotonic GBDT** | $	ext{PM}_{2.5}$ | **0.924** | **8.73** | **5.92** | **21.30** |

- **CSV Download:** [`table1_calibration_metrics.csv`](table1_calibration_metrics.csv)

---

## Table II: Microclimate Hygroscopic Growth Breakdown across Relative Humidity Bins
*Quantifying the impact of aerosol deliquescence and efflorescence across distinct ambient humidity regimes.*

| Relative Humidity (RH) Bin | Sample Count ($N$) | Raw $R^2$ | Raw RMSE ($\mu	ext{g/m}^3$) | Calibrated $R^2$ | Calibrated RMSE ($\mu	ext{g/m}^3$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **$	ext{RH} < 50\%$** (Dry Regime) | 320 | 0.784 | 14.20 | **0.941** | **6.85** |
| **$50\% \le 	ext{RH} < 70\%$** (Pre-Deliquescence) | 450 | 0.692 | 18.65 | **0.932** | **7.42** |
| **$70\% \le 	ext{RH} < 85\%$** (Deliquescence Window) | 280 | 0.485 | 31.10 | **0.915** | **9.68** |
| **$	ext{RH} \ge 85\%$** (Supersaturation / Dense Fog) | 150 | 0.312 | 42.80 | **0.884** | **11.95** |

- **CSV Download:** [`table2_humidity_breakdown.csv`](table2_humidity_breakdown.csv)

---

## Table III: Multi-Step Air Quality Forecasting Performance Comparison
*Multi-horizon forecasting accuracy comparing ATMOS-V2 BiLSTM-Attention against standard baselines across lead times from $t+1\,	ext{h}$ to $t+24\,	ext{h}$.*

| Model Architecture | $t+1	ext{h}$ RMSE | $t+1	ext{h}$ MAE | $t+6	ext{h}$ RMSE | $t+6	ext{h}$ MAE | $t+12	ext{h}$ RMSE | $t+12	ext{h}$ MAE | $t+24	ext{h}$ RMSE | $t+24	ext{h}$ MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Naïve Persistence** | 6.45 | 4.82 | 11.19 | 8.54 | 15.30 | 11.82 | 19.86 | 15.40 |
| **ARIMA(2,1,2)** | 5.85 | 4.31 | 10.12 | 7.65 | 13.25 | 10.15 | 16.92 | 13.10 |
| **Random Forest** | 5.12 | 3.75 | 8.45 | 6.20 | 10.52 | 7.95 | 12.85 | 9.80 |
| **ATMOS-V2 BiLSTM-Attention** | **4.48** | **3.18** | **5.39** | **3.84** | **6.18** | **4.45** | **7.40** | **5.32** |

- **Performance Gain at 24h:** **62.7% error reduction** compared to naïve persistence.
- **CSV Download:** [`table3_forecasting_performance.csv`](table3_forecasting_performance.csv)

---

## Table IV: Comprehensive Benchmarking Comparison Against Representative Literature (2018–2026)
*Comparative evaluation of hardware cost, autonomy architecture, reference instrument validation, and predictive forecasting capacity.*

| System / Study | Year | Hardware Cost | Power Architecture | Reference Instrument | $R^2$ ($	ext{PM}_{2.5}$) | Forecasting Capacity |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Zheng et al. [12]** | 2018 | ~\$120 | Grid / Mains Only | Met One BAM-1020 FEM | 0.68--0.72 | None (Static Sensing) |
| **Magi et al. [26]** | 2020 | ~\$250 | Grid / Mains Only | TEOM Federal Standard | 0.77 | None (Static Sensing) |
| **Kumar et al. [7]** | 2023 | ~\$95 | Solar 5W + Lead-Acid | Portable Optical FEM | 0.81 | None (Static Sensing) |
| **Ali et al. [27]** | 2024 | ~\$80 | Solar 3W + 18650 | Co-located Reference | 0.84 | 1h--3h ARIMA Baseline |
| **Sengupta et al. [15]** | 2026 | ~\$350 | Grid / Mains Only | UK AURN Reference | 0.89 | None (Calibration Focus) |
| **Yun et al. [16]** | 2026 | ~\$110 | USB 5V Mains | Indoor Reference Standard | 0.86 | None (Transferability Focus) |
| **ATMOS-V2 (This Work)** | **2026** | **<\$65** | **Solar 2W + 18650 Li-ion** | **Met One BAM-1020 FEM** | **0.924** | **Multi-Horizon 1h--24h LSTM** |

- **CSV Download:** [`table4_literature_benchmark.csv`](table4_literature_benchmark.csv)
