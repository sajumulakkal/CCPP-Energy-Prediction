# 📊 EXECUTIVE SUMMARY: CCPP Energy Output Forecasting

## 📌 Project Overview
The objective of this project was to develop a high-precision machine learning model to predict the **Net Hourly Electrical Energy Output (PE)** of a Combined Cycle Power Plant (CCPP). By leveraging ambient environmental sensors, we provide a tool to help operators optimize power generation and ensure grid stability.

<p align="center">
  <img src="https://raw.githubusercontent.com/sajumulakkal/CCPP-Energy-Prediction/main/CCCP.png" width="600" alt="Combined Cycle Power Plant Diagram">
</p>



---

## 🌡️ The Data
The dataset consists of **9,568 data points** collected over six years, featuring four primary environmental predictors:

* **Ambient Temperature (AT):** 1.81°C to 37.11°C.
* **Exhaust Vacuum (V):** Steam turbine pressure readings.
* **Ambient Pressure (AP):** Atmospheric pressure in millibars.
* **Relative Humidity (RH):** Moisture percentage.

---

## 📈 Model Comparison & Performance
We evaluated three distinct algorithms to determine the most effective forecasting method. Performance was measured using **R-squared ($R^2$)** and **Root Mean Squared Error (RMSE)**.

| Model | $R^2$ Score | RMSE (Error) | Verdict |
| :--- | :--- | :--- | :--- |
| **Linear Regression** | 0.9301 | 4.50 MW | Good baseline, highly interpretable. |
| **Neural Network (MLP)** | 0.9429 | 3.90 MW | Complex, but prone to over-extrapolation. |
| **Random Forest** | **0.9637** | **3.25 MW** | **Winner: Highest accuracy and stability.** |

---

## 💡 Key Engineering Insights
* **Temperature is King:** Ambient Temperature (AT) accounts for **~90%** of the model's predictive power. As AT increases, PE decreases significantly due to lower air density.
* **Non-Linearity Matters:** The Random Forest outperformed Linear Regression by **3.3%**, proving that the plant’s efficiency responds to weather changes in complex, non-linear ways.
* **Operational Value:** With an average error of only **3.25 MW** (on a 495 MW scale), this model allows for energy forecasting with **>99% accuracy** relative to the plant's capacity.

---

## 🎬 Video Presentation Scenarios
*Use these test cases during your demonstration to show the model's sensitivity.*

### Scenario A: The "Ideal" Winter Morning (Peak Performance)
* **Narrative:** *"Let's look at the plant's performance on a cold, crisp morning. High air density means maximum efficiency."*
* **Inputs:** `AT: 5.0` | `V: 40.0` | `AP: 1020.0` | `RH: 30.0`
* **Expected Result:** **~485.00 MW to 490.00 MW**
* **Action:** *"As you can see, we are near the maximum capacity of the plant."*

### Scenario B: The "Heatwave" Afternoon (The Dramatic Drop)
* **Narrative:** *"Now, watch what happens during a summer heatwave. As the temperature climbs, the gas turbine struggles to compress the thin, hot air."*
* **Inputs:** `AT: 35.0` | `V: 75.0` | `AP: 1000.0` | `RH: 90.0`
* **Expected Result:** **~425.00 MW to 430.00 MW**
* **Action:** *"We just saw a drop of nearly 60 Megawatts! That is enough power to fuel roughly 40,000 homes lost just due to weather conditions."*

---

## 🏁 Conclusion
The **Random Forest Regressor** is the recommended model for deployment. It provides the most reliable predictions across the widest range of weather conditions, offering a robust tool for real-time power plant monitoring.
