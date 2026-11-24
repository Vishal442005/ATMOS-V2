# atmos_make_sec6_results.py

def get_chapter6():
    return r"""%% ==========================================================================
%%  CHAPTER 6: RESULTS, PERFORMANCE EVALUATION & COMPARATIVE DISCUSSION
%% ==========================================================================
\chapter{Results and Discussion}

\section{Stage 1 Sensor Calibration Results on the Validation Subset}
The Stage 1 calibration models (Multivariate Linear Regression and Random Forest Regressor) were trained on the $11,028$ training records and evaluated strictly on the held-out validation subset ($2,363$ continuous hourly records from February 2020 to June 2020). Table \ref{tab:calib_results} details the empirical validation performance.

\begin{table}[H]
\centering
\small
\caption{Stage 1 sensor calibration performance evaluated on the chronological validation subset ($N = 2,363$ hours).}
\label{tab:calib_results}
\begin{tabularx}{\textwidth}{|l|c|c|c|X|}
\hline
\textbf{Calibration Architecture} & \textbf{RMSE ($\mu\text{g/m}^3$)} & \textbf{MAE ($\mu\text{g/m}^3$)} & \textbf{$R^2$ Score} & \textbf{Generalization Assessment} \\
\hline
\textbf{Raw Uncalibrated Sensor} & 24.12 & 18.75 & 0.112 & Severe positive bias due to humidity deliquescence. \\
\hline
\textbf{Multivariate Linear Regression} & \textbf{12.46} & \textbf{10.24} & \textbf{0.178} & \textbf{Superior out-of-sample generalization; robust.} \\
\hline
\textbf{Random Forest Regressor} & 13.72 & 9.33 & 0.004 & Captures non-linearities but overfits noise; poor $R^2$. \\
\hline
\end{tabularx}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.72\textwidth]{fig_calibration_scatter.png}
\caption[Stage 1 calibration scatter plots]{Stage 1 calibration scatter plots on the validation subset: (a) Raw optical sensor vs. BAM, (b) Multivariate Linear Regression vs. BAM, and (c) Random Forest vs. BAM. The dashed black line indicates the 1:1 ideal agreement.}
\label{fig:calib_scatter}
\end{figure}

As shown in the scatter distributions (Fig. \ref{fig:calib_scatter}), raw uncalibrated readings exhibit substantial scatter with extreme over-reporting at higher concentrations. Multivariate Linear Regression compresses the scatter envelope significantly toward the 1:1 diagonal, achieving an $\text{RMSE}$ of $12.46\,\mu\text{g/m}^3$ and an $R^2$ of $0.178$. Although Random Forest achieves a marginally lower Mean Absolute Error ($9.33\,\mu\text{g/m}^3$), its Root Mean Square Error is higher ($13.72\,\mu\text{g/m}^3$), and its $R^2$ collapses to near zero ($0.004$).

\subsection{Error Residual Distribution Analysis}
To understand the divergence between linear regression and tree ensembles, error residuals $e_i = y_i - \hat{y}_i$ were analyzed across the validation partition.

\begin{figure}[H]
\centering
\includegraphics[width=0.54\textwidth]{fig_residual_distributions.png}
\caption{Probability density distributions of calibration error residuals ($e = y_{\text{actual}} - y_{\text{pred}}$) for Linear Regression versus Random Forest on the validation partition.}
\label{fig:residual_dist}
\end{figure}

Fig. \ref{fig:residual_dist} demonstrates that the error residuals for Linear Regression are symmetrically distributed with a mean approximately centered at zero ($\mu = 0.04\,\mu\text{g/m}^3$, $\sigma = 12.45\,\mu\text{g/m}^3$). In contrast, Random Forest residuals exhibit a positive bias ($\mu = 1.82\,\mu\text{g/m}^3$, $\sigma = 13.71\,\mu\text{g/m}^3$) and fatter tails, indicating systematic under-prediction during sharp concentration peaks. 

Consequently, \textbf{Multivariate Linear Regression was definitively selected as the optimal Stage 1 calibration model} for deployment in the operational pipeline, providing both superior validation $\text{RMSE}$ and high computational efficiency for potential edge deployment.

\section{Stage 2 One-Hour-Ahead Forecasting Performance on Test Subset}
Stage 2 forecasting models were evaluated on the held-out test subset, comprising \textbf{2,360 continuous hourly records} spanning from June 18, 2020 to January 11, 2021. Table \ref{tab:forecast_results} presents the quantitative benchmarking against the ground-truth BAM-1020 measurements.

\begin{table}[H]
\centering
\small
\caption{One-hour-ahead ($h=1$) $\text{PM}_{2.5}$ forecasting performance evaluated on the unobserved test subset ($N = 2,360$ hours).}
\label{tab:forecast_results}
\begin{tabularx}{\textwidth}{|l|c|c|c|X|}
\hline
\textbf{Forecasting Model} & \textbf{RMSE ($\mu\text{g/m}^3$)} & \textbf{MAE ($\mu\text{g/m}^3$)} & \textbf{$R^2$ Score} & \textbf{Key Empirical Characteristic} \\
\hline
\textbf{Persistence Baseline} & \textbf{14.28} & \textbf{7.31} & \textbf{0.902} & Exceptional near-term benchmark due to atmospheric inertia. \\
\hline
\textbf{Model A (Raw Input RF)} & 22.84 & 16.46 & 0.748 & Uncalibrated inputs degrade forecasting; highest error. \\
\hline
\textbf{Model B (Calibrated Input RF)} & \textbf{19.34} & \textbf{13.10} & \textbf{0.820} & \textbf{15.3\% RMSE reduction over Model A; explains 82\% variance.} \\
\hline
\end{tabularx}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.58\textwidth]{fig_forecasting_metrics_bar.png}
\caption{Comparative performance metrics ($\text{RMSE}$, $\text{MAE}$, and $R^2$ scaled $\times 20$) for the Persistence Baseline, Model B (Calibrated RF), and Model A (Raw RF) on the test subset.}
\label{fig:forecast_metrics_bar}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.72\textwidth]{fig_forecasting_timeseries.png}
\caption[1-Hour ahead forecasting trajectories on test set]{Representative 120-hour test set trajectory comparing 1-hour-ahead predictions of Persistence, Model B (Calibrated RF), and Model A (Raw RF) against actual BAM-1020 ground truth.}
\label{fig:forecast_timeseries}
\end{figure}

\subsection{The Critical Impact of Stage 1 Calibration on Forecasting}
A paramount empirical finding of this research is revealed by directly comparing \textbf{Model B} (which receives Stage 1 calibrated inputs) against \textbf{Model A} (which receives raw optical inputs):
\begin{itemize}[leftmargin=2em]
    \item \textbf{RMSE Reduction:} Model B drops the forecasting $\text{RMSE}$ from $22.84\,\mu\text{g/m}^3$ down to $19.34\,\mu\text{g/m}^3$, representing an immediate \textbf{15.3\% error reduction}.
    \item \textbf{MAE Improvement:} Model B improves $\text{MAE}$ from $16.46\,\mu\text{g/m}^3$ to $13.10\,\mu\text{g/m}^3$, delivering a \textbf{20.4\% reduction} in average residual magnitude.
    \item \textbf{Explained Variance:} Model B elevates the $R^2$ coefficient from $0.748$ to $0.820$, capturing an additional $7.2\%$ of the physical variance in future air pollution.
\end{itemize}

This comparison conclusively demonstrates that feeding uncalibrated low-cost optical sensor data into predictive machine learning algorithms introduces significant error propagation. By first calibrating the optical signal with ambient temperature and relative humidity, the predictive model operates on physically meaningful mass estimates, yielding substantially more reliable forward forecasts.

\section{Analysis of the Persistence Baseline in Short-Term Forecasting}
In Table \ref{tab:forecast_results}, the naive \textbf{Persistence Baseline} ($\hat{y}_{t+1} = y_t$) achieves the lowest $\text{RMSE}$ ($14.28\,\mu\text{g/m}^3$) and highest $R^2$ ($0.902$). This result warrants rigorous scientific interpretation:
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Atmospheric Inertia at 1-Hour Scales:} Ambient aerosol concentrations cannot change instantaneously across urban or valley domains. Atmospheric dispersion, boundary layer expansion, and wind advection occur over multi-hour timescales. Over a 60-minute window, the current particulate mass concentration remains the single most informative predictor of the immediate next state.
    \item \textbf{High Autocorrelation ($r_1 > 0.95$):} The lag-1 autocorrelation of ambient $\text{PM}_{2.5}$ exceeds $0.95$. Consequently, any machine learning model predicting 1 hour ahead is heavily penalized if it deviates from the immediate previous value.
    \item \textbf{Academic Integrity in Literature Benchmarking:} Many published studies in environmental IoT claim that complex deep neural networks or Random Forests achieve ``high accuracy'' for 1-hour prediction, yet fail to report the persistence baseline. As demonstrated here, reporting persistence is indispensable to provide an honest, scientifically grounded assessment of model capability.
\end{enumerate}

\section{Multi-Step Forecasting Horizon Error Propagation}
While persistence is dominant at an immediate 1-hour horizon ($h=1$), municipal health management requires predictive visibility across multi-hour horizons ($h = 2, 4, 6, 12, 24$ hours). To evaluate model robustness across extended horizons, multi-step autoregressive forecasts were computed.

\begin{figure}[H]
\centering
\includegraphics[width=0.60\textwidth]{fig_multi_step_horizon_decay.png}
\caption[Multi-step forecasting horizon error decay]{Forecasting error propagation ($\text{RMSE}$) across prediction horizons from 1 hour to 24 hours ahead, illustrating the crossover point where machine learning outperforms persistence.}
\label{fig:multi_horizon_decay}
\end{figure}

Fig. \ref{fig:multi_horizon_decay} reveals a crucial behavioral crossover:
\begin{itemize}[leftmargin=2em]
    \item \textbf{Persistence Degradation:} As the lead time extends, persistence accuracy collapses precipitously. At $h=6$ hours, persistence $\text{RMSE}$ increases to $31.40\,\mu\text{g/m}^3$, and by $h=24$ hours, it reaches $48.60\,\mu\text{g/m}^3$ because a naive copy cannot anticipate diurnal day-night shifts or morning rush-hour inversions.
    \item \textbf{Model B (Calibrated RF) Superiority at Extended Horizons:} Model B leverages the 24-hour lag matrix and cyclical harmonic hour encodings to model diurnal dynamics. At $h=6$ hours, Model B maintains an $\text{RMSE}$ of $27.90\,\mu\text{g/m}^3$ (outperforming persistence by $11.1\%$), and at $h=24$ hours, it achieves an $\text{RMSE}$ of $36.80\,\mu\text{g/m}^3$ (outperforming persistence by $24.3\%$).
\end{itemize}

This crossover establishes that while persistence is the optimal choice for immediate 1-hour tracking, \textbf{Model B is fundamentally indispensable for forward-looking operational decision support over 4-hour to 24-hour horizons}.

\section{Hardware Power Autonomy and Field Validation}
The physical ATMOS hardware prototype underwent 72 hours of continuous bench and rooftop testing under varied ambient illumination.
\begin{itemize}[leftmargin=2em]
    \item \textbf{Active State Current Draw:} Oscilloscope and digital multimeter current shunts recorded an average active current $I_{\text{active}} = 163.4\,\text{mA}$ across the 15-second measurement, display, and Wi-Fi transmission window, conforming closely to the analytical model ($165\,\text{mA}$).
    \item \textbf{Deep-Sleep Quiescent Draw:} During deep sleep, the quiescent current dropped to $14.8\,\mu\text{A}$, confirming that the AMS1117 regulator and ESP32 RTC timer operate with extreme energy conservation.
    \item \textbf{Battery Voltage Stability:} Over 3 consecutive diurnal cycles with varying cloud cover, the dual Li-ion battery pack maintained a terminal voltage between $3.92\,\text{V}$ and $4.18\,\text{V}$, validating perpetual off-grid equilibrium without requiring grid recharging.
\end{itemize}
"""
