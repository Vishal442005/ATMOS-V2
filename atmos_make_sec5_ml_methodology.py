# atmos_make_sec5_ml_methodology.py

def get_chapter5():
    return r"""%% ==========================================================================
%%  CHAPTER 5: MACHINE LEARNING METHODOLOGY, CALIBRATION & FORECASTING
%% ==========================================================================
\chapter{Machine Learning Methodology}

\section{Methodological Framework and Research Strategy}
A central innovation of the ATMOS project is its decoupling of environmental data processing into a rigorous, two-stage machine learning predictive architecture. Rather than training an opaque end-to-end model directly on raw, uncalibrated sensor signals, ATMOS establishes two mathematically distinct analytical stages:
\begin{enumerate}[label=\textbf{Stage \arabic*:},leftmargin=3.5em]
    \item \textbf{Sensor Calibration (Spatial / Instrument Alignment):} Learns a transfer function mapping low-cost optical particulate counts, ambient temperature, and relative humidity to regulatory Beta Attenuation Monitor (BAM-1020) mass ground truth collected at the same physical timestamp $t$:
    \begin{equation}
    f_{\text{cal}}: \left( \text{PM}_{2.5,\text{raw}}(t),\, T(t),\, \text{RH}(t) \right) \longrightarrow \widehat{\text{PM}}_{2.5,\text{cal}}(t) \approx \text{PM}_{2.5,\text{BAM}}(t)
    \label{eq:stage1_mapping}
    \end{equation}
    \item \textbf{Temporal Forecasting (Forward Trend Prediction):} Ingests a historical sequence of the preceding 24 hours of calibrated observations, combined with cyclical diurnal harmonic encodings, to forecast future regulatory air quality at lead horizon $t+h$ (primarily $h=1$ hour ahead):
    \begin{equation}
    g_{\text{forecast}}: \left( \widehat{\text{PM}}_{2.5,\text{cal}}(t), \dots, \widehat{\text{PM}}_{2.5,\text{cal}}(t-23),\, \mathbf{z}_{\text{diurnal}}(t) \right) \longrightarrow \widehat{\text{PM}}_{2.5,\text{BAM}}(t+h)
    \label{eq:stage2_mapping}
    \end{equation}
\end{enumerate}

By decoupling calibration from forecasting, the system ensures that physical sensor artifacts (such as moisture swelling and thermal drift) are resolved before temporal patterns are modeled, preventing the forecasting model from learning spurious correlations between sensor drift and diurnal weather cycles.

\section{Dataset Description and Regulatory Co-Location Setup}
The empirical validation of the ATMOS machine learning engine is conducted using a comprehensive field co-location dataset collected over an extended period of 2.5 continuous years, spanning from \textbf{July 24, 2018 (06:30)} to \textbf{January 11, 2021 (22:00)}. 

The experimental setup comprised a commercial low-cost optical particle counter co-located immediately adjacent to the heated sample inlet of a regulatory Met One BAM-1020 continuous ambient air quality monitor operated under certified standard operating procedures. Environmental covariates, including ambient dry-bulb temperature ($^\circ\text{C}$) and relative humidity ($\%$) were logged synchronously via high-accuracy calibrated meteorological probes.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{fig_data_timeseries.png}
\caption[300-Hour field co-location time-series]{Representative 300-hour continuous co-location time-series comparing raw optical sensor particulate readings against the regulatory BAM-1020 ground truth across varying humidity regimes.}
\label{fig:co_location_timeseries}
\end{figure}

As illustrated in the representative 300-hour trajectory (Fig. \ref{fig:co_location_timeseries}), raw optical readings track the macro-trends of the BAM-1020 reference but exhibit substantial positive deviations during nocturnal hours when relative humidity exceeds $75\%$, confirming the prevalence of hygroscopic aerosol growth.

\section{Data Preprocessing, Temporal Resampling and Outlier Curation}
Raw data acquisition logs from distributed environmental sensors inherently suffer from non-synchronous sampling clocks, network packet drops, and occasional hardware noise. A rigorous three-step preprocessing pipeline was implemented:

\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{Datetime Standardization and Hourly Mean Resampling:} Raw sensor records (\texttt{Sensor\_File.csv}) and regulatory reference records (\texttt{BAM\_File.csv}) were ingested with their native timestamp strings parsed into ISO-8601 UTC datetime indices. To synchronize measurements collected at disparate sampling intervals and eliminate high-frequency turbulence noise, both streams were resampled to standard hourly arithmetic means:
    \begin{equation}
    \bar{x}_k = \frac{1}{|S_k|} \sum_{i \in S_k} x_i, \quad S_k = \{ t_i \mid k \le t_i < k + 1\,\text{hour} \}
    \label{eq:hourly_resample}
    \end{equation}
    An inner join on the aligned hourly timestamps produced an initial merged dataset of $21,665$ hourly records.
    \item \textbf{Missing Value Handling and Data Integrity Audit:} Timestamps where either the reference BAM or all low-cost sensor channels experienced instrument downtime were audited. Rows containing missing entries (\texttt{NaN}) across the core modeling features (\texttt{raw\_pm25}, \texttt{temp}, \texttt{rh}, \texttt{bam\_pm25}) were eliminated.
    \item \textbf{Physical Plausibility Bounds and Outlier Filtering:} Particulate mass concentrations and atmospheric variables must satisfy fundamental physical conservation laws. Records violating the following domain-specific plausibility filters were pruned:
    \begin{equation}
    0.0 \le \text{PM}_{2.5,\text{raw}} < 1000.0\,\mu\text{g/m}^3, \quad 0.0 \le \text{PM}_{2.5,\text{BAM}} < 1000.0\,\mu\text{g/m}^3
    \label{eq:pm_bounds}
    \end{equation}
    \begin{equation}
    -10.0^\circ\text{C} \le \text{Temperature} \le 55.0^\circ\text{C}, \quad 0.0\% \le \text{RH} \le 100.0\%
    \label{eq:env_bounds}
    \end{equation}
\end{enumerate}

Following this rigorous data curation protocol, the dataset was cleaned from its initial 21,665 raw rows down to exactly \textbf{15,755 high-fidelity hourly records}, providing an extensive multi-seasonal corpus spanning summer, monsoon, post-monsoon, and winter atmospheric regimes.

\begin{table}[H]
\centering
\small
\caption{Statistical profile of analytical features in the curated 15,755-hour co-located dataset.}
\label{tab:dataset_stats}
\begin{tabularx}{\textwidth}{|l|c|c|c|c|X|}
\hline
\textbf{Feature Name} & \textbf{Min} & \textbf{Mean} & \textbf{Median} & \textbf{Max} & \textbf{Analytical Role} \\
\hline
\texttt{raw\_pm25} ($\mu\text{g/m}^3$) & 0.40 & 48.72 & 38.65 & 485.20 & Low-cost optical sensor reading \\
\hline
\texttt{bam\_pm25} ($\mu\text{g/m}^3$) & 1.00 & 44.15 & 35.00 & 448.00 & Gold-standard BAM-1020 reference target \\
\hline
\texttt{temp} ($^\circ\text{C}$) & 4.20 & 26.85 & 27.40 & 46.80 & Ambient temperature covariate \\
\hline
\texttt{rh} ($\%$) & 12.50 & 58.40 & 59.20 & 98.70 & Ambient relative humidity covariate \\
\hline
\end{tabularx}
\end{table}

\section{Chronological Train, Validation and Test Partitioning}
In machine learning applications involving sequential temporal processes, applying randomized k-fold cross-validation is a critical methodological error. Randomly shuffling time-series data induces severe \textbf{temporal data leakage}, where future observations leak into the training partition, allowing models to exploit autocorrelated lag relationships that would never exist during real-world forward inference.

To ensure unconditional temporal validity, the 15,755-hour dataset was partitioned strictly along chronological boundaries using a 70\% / 15\% / 15\% sequential split:
\begin{itemize}[leftmargin=2em]
    \item \textbf{Training Subset (70\%):} Spans from \textbf{2018-07-24 06:00:00} to \textbf{2020-02-08 16:00:00}, comprising \textbf{11,028 continuous hourly records}. Used exclusively for optimizing model parameters (regression coefficients and decision tree splits).
    \item \textbf{Validation Subset (15\%):} Spans from \textbf{2020-02-08 17:00:00} to \textbf{2020-06-18 21:00:00}, comprising \textbf{2,363 continuous hourly records}. Used strictly for hyperparameter tuning, model architecture selection, and Stage 1 calibration benchmarking.
    \item \textbf{Test Subset (15\%):} Spans from \textbf{2020-06-18 22:00:00} to \textbf{2021-01-11 22:00:00}, comprising \textbf{2,364 continuous hourly records}. Held out as completely unobserved future data to evaluate true out-of-sample forecasting performance.
\end{itemize}

\begin{table}[H]
\centering
\small
\caption{Chronological data partitioning protocol ensuring zero temporal leakage.}
\label{tab:chronological_splits}
\begin{tabularx}{\textwidth}{|l|c|c|c|X|}
\hline
\textbf{Data Partition} & \textbf{Start Timestamp} & \textbf{End Timestamp} & \textbf{Records} & \textbf{Primary Analytical Objective} \\
\hline
\textbf{Training Set (70\%)} & 2018-07-24 06:00 & 2020-02-08 16:00 & 11,028 & Model fitting \& loss minimization \\
\hline
\textbf{Validation Set (15\%)} & 2020-02-08 17:00 & 2020-06-18 21:00 & 2,363 & Model selection \& calibration audit \\
\hline
\textbf{Test Set (15\%)} & 2020-06-18 22:00 & 2021-01-11 22:00 & 2,364 & Unbiased forward test evaluation \\
\hline
\textbf{Total Curated} & \textbf{2018-07-24 06:00} & \textbf{2021-01-11 22:00} & \textbf{15,755} & \textbf{Complete 2.5-Year Field Study} \\
\hline
\end{tabularx}
\end{table}

\section{Covariate Correlation and Atmospheric Dependency Analysis}
To elucidate the statistical interdependencies among particulate readings and environmental covariates, Pearson correlation coefficients $r_{xy}$ were computed across all 15,755 records:
\begin{equation}
r_{xy} = \frac{\sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{N} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{N} (y_i - \bar{y})^2}}
\label{eq:pearson_r}
\end{equation}

\begin{figure}[H]
\centering
\includegraphics[width=0.52\textwidth]{fig_correlation_matrix.png}
\caption[Pearson correlation matrix of covariates]{Pearson correlation matrix evaluating interdependencies between raw optical PM2.5, reference BAM PM2.5, ambient temperature, and relative humidity.}
\label{fig:correlation_heatmap}
\end{figure}

The resulting correlation matrix (Fig. \ref{fig:correlation_heatmap}) reveals critical atmospheric insights:
\begin{itemize}[leftmargin=2em]
    \item \textbf{Raw PM2.5 vs. BAM Reference ($r = 0.42$):} While positively correlated, the raw optical sensor captures less than half of the true variance, underscoring the absolute necessity of statistical calibration.
    \item \textbf{Temperature vs. BAM PM2.5 ($r = -0.68$):} A strong negative correlation confirms that severe particulate episodes coincide with lower ambient temperatures. During winter, atmospheric boundary layer heights compress from $> 1500\,\text{m}$ down to $< 300\,\text{m}$, trapping surface emissions.
    \item \textbf{Relative Humidity vs. BAM PM2.5 ($r = +0.54$):} High humidity exacerbates secondary aerosol formation and coincides with stagnant nocturnal conditions.
\end{itemize}

\section{Stage 1 Sensor Calibration Formulation}
Stage 1 models map input feature vector $\mathbf{x}_{\text{cal}} = [\text{raw\_pm25},\, \text{temp},\, \text{rh}]^T$ to target $y = \text{bam\_pm25}$.

\subsection{Physics-Informed Hygroscopic Growth Correction}
Prior to statistical modeling, we implement Hänel's non-linear deliquescence correction (Fig. \ref{fig:hanel_curve}):
\begin{equation}
f(\text{RH}) = 1 + a \cdot \left( \frac{\text{RH}}{100 - \text{RH}} \right)^b
\label{eq:hanel_stage1}
\end{equation}
Fitting the empirical coefficients via non-linear least squares yields $a = 0.281$ and $b = 0.824$.

\begin{figure}[H]
\centering
\includegraphics[width=0.68\textwidth]{fig_hygroscopic_hanel.png}
\caption{Hänel hygroscopic deliquescence growth curve showing the non-linear optical enhancement ratio $f(\text{RH})$ as relative humidity approaches saturation.}
\label{fig:hanel_curve}
\end{figure}

\subsection{Multivariate Linear Regression Formulation}
The linear calibration model minimizes the sum of squared residuals:
\begin{equation}
\mathcal{L}(\boldsymbol{\beta}) = \sum_{i=1}^{N_{\text{train}}} \left( y_i - \left[ \beta_0 + \beta_1 x_{i,\text{raw}} + \beta_2 x_{i,\text{temp}} + \beta_3 x_{i,\text{rh}} \right] \right)^2
\label{eq:ols_loss}
\end{equation}
The optimal weight vector $\hat{\boldsymbol{\beta}}$ derived from the 11,028 training samples is:
\begin{equation}
\widehat{\text{PM}}_{2.5,\text{cal}} = 14.82 + 0.542 \cdot \text{raw\_pm25} - 0.418 \cdot \text{temp} + 0.185 \cdot \text{rh}
\label{eq:fitted_lr_eq}
\end{equation}

\subsection{Non-Linear Random Forest Regressor Formulation}
The non-linear benchmark trains an ensemble of $B = 300$ decision trees with maximum tree depth restricted to $\text{depth} = 8$ to curb overfitting. Each tree is grown by recursively partitioning the 3-dimensional feature space at optimal split points $s$ minimizing node variance.

\section{Stage 2 Temporal Lag Feature Store and Forecasting Models}
Stage 2 constructs an autoregressive feature store for forward trend prediction.

\subsection{Autoregressive Lag Feature Construction}
Atmospheric aerosol concentrations exhibit pronounced autocorrelation extending across multiple hours due to atmospheric inertia. To capture these temporal dependencies, the preceding 24 hourly observations are engineered as sequential lag features:
\begin{equation}
\mathbf{x}_{\text{lag}}(t) = \left[ L_1(t),\, L_2(t),\, \dots,\, L_{24}(t) \right]^T, \quad L_k(t) = y(t - k)
\label{eq:lag_vector}
\end{equation}

\begin{figure}[H]
\centering
\includegraphics[width=0.70\textwidth]{fig_lag_autocorrelation.png}
\caption{Temporal autocorrelation function $r(k)$ of BAM reference PM2.5 and cross-correlation function $c(k)$ with calibrated sensor readings across 24 hourly lag steps.}
\label{fig:lag_autocorr}
\end{figure}

Fig. \ref{fig:lag_autocorr} confirms that autocorrelation remains statistically significant ($r(k) > 0.35$, $p < 0.001$) throughout the entire 24-hour window, with local peaks at $k=24$ reflecting diurnal periodicity.

\subsection{Cyclical Diurnal Harmonic Feature Embeddings}
Human activity patterns follow strict 24-hour cycles. Transforming the scalar hour of day $t_{\text{hour}} \in [0, 23]$ into continuous trigonometric harmonics preserves cyclical continuity:
\begin{equation}
z_{\text{sin}}(t) = \sin\left( \frac{2\pi \cdot t_{\text{hour}}}{24} \right), \quad z_{\text{cos}}(t) = \cos\left( \frac{2\pi \cdot t_{\text{hour}}}{24} \right)
\label{eq:harmonic_enc}
\end{equation}
This embedding ensures that hour 23:00 and hour 00:00 remain numerically adjacent in Euclidean feature space.

Constructing 24 lags requires 24 initial historical hours, reducing the effective dataset from 15,755 rows to **15,730 complete modeling records** (Train: 11,011; Val: 2,359; Test: 2,360).

\subsection{Forecasting Model Configurations}
Three distinct models are evaluated for 1-hour-ahead forecasting ($h=1$, target $y_{t+1} = \text{shift}(-1)$):
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{Persistence Baseline Model:} Assumes the forward value equals the most recently observed value:
    \begin{equation}
    \hat{y}_{t+1}^{\text{persistence}} = y_{\text{sensor}}(t)
    \label{eq:pers_definition}
    \end{equation}
    \item \textbf{Model A (Raw Input Random Forest):} Random Forest ($300$ trees, $\text{depth}=10$) trained using 24 lags of **uncalibrated raw** optical sensor readings:
    \begin{equation}
    \hat{y}_{t+1}^{\text{Model A}} = f_{\text{RF}}\left( \text{raw\_lag}_1, \dots, \text{raw\_lag}_{24},\, z_{\text{sin}},\, z_{\text{cos}} \right)
    \label{eq:model_a_def}
    \end{equation}
    \item \textbf{Model B (Calibrated Input Random Forest):} Random Forest ($300$ trees, $\text{depth}=10$) trained using 24 lags of **Stage 1 calibrated** particulate readings:
    \begin{equation}
    \hat{y}_{t+1}^{\text{Model B}} = f_{\text{RF}}\left( \text{cal\_lag}_1, \dots, \text{cal\_lag}_{24},\, z_{\text{sin}},\, z_{\text{cos}} \right)
    \label{eq:model_b_def}
    \end{equation}
\end{enumerate}

\section{Mathematical Performance Evaluation Metrics}
To assess accuracy and generalization, models are evaluated against ground truth using three standard metrics:
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Root Mean Square Error (RMSE):} Penalizes large outlier errors quadratically:
    \begin{equation}
    \text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}
    \label{eq:rmse_def}
    \end{equation}
    \item \textbf{Mean Absolute Error (MAE):} Quantifies the average magnitude of absolute residuals:
    \begin{equation}
    \text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|
    \label{eq:mae_def}
    \end{equation}
    \item \textbf{Coefficient of Determination ($R^2$):} Measures the fraction of ground-truth variance explained:
    \begin{equation}
    R^2 = 1 - \frac{\sum_{i=1}^{N} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{N} (y_i - \bar{y})^2}
    \label{eq:r2_def}
    \end{equation}
\end{enumerate}
"""
