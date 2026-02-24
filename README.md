# ⚡ Combined Cycle Power Plant (CCPP) Energy Prediction

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![ML Framework](https://img.shields.io/badge/focus-Machine%20Learning-green)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

## 📌 Project Overview
This project utilizes Machine Learning to predict the **Net Hourly Electrical Energy Output (PE)** of a Combined Cycle Power Plant using environmental sensor data. By comparing three distinct regression architectures, we identify the most accurate method for forecasting energy production based on ambient atmospheric conditions.


![CCPP Diagram](https://raw.githubusercontent.com/sajumulakkal/CCPP-Energy-Prediction/main/CCCP.png)


### Why this matters?
In a CCPP, load prediction is vital for grid stability. Since performance is highly dependent on ambient conditions (Temperature, Humidity, etc.), manual calculations are often insufficient. This project automates that process with high precision.

---

## 📊 Dataset Features
The model is trained on **9,568 samples** collected from a real-world power plant over 6 years.

| Feature | Description | Range |
| :--- | :--- | :--- |
| **AT** | Ambient Temperature | 1.81°C to 37.11°C |
| **V** | Exhaust Vacuum | 25.36 to 81.56 cm Hg |
| **AP** | Ambient Pressure | 992.89 to 1033.30 mbar |
| **RH** | Relative Humidity | 25.56% to 100.16% |
| **PE (Target)** | Net Hourly Electrical Energy Output | 420.26 to 495.76 MW |

---

## 🛠️ Installation & Setup

### 1. Prerequisites
* Python 3.11+
* Virtual Environment (Recommended)

### 2. Setup
Clone the repository and install the necessary dependencies:
```bash
git clone [https://github.com/your-username/ccpp-energy-prediction.git](https://github.com/your-username/ccpp-energy-prediction.git)
cd ccpp-energy-prediction
pip install -r requirements.txt
