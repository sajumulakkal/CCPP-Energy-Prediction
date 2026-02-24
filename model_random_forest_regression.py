import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def run_final_power_plant_model():
    # 1. Load the dataset
    try:
        df = pd.read_csv('CCPP_data.csv')
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("Error: 'CCPP_data.csv' not found. Ensure the file is in this folder.")
        return

    # 2. Define Features (X) and Target (y)
    X = df[['AT', 'V', 'AP', 'RH']]
    y = df['PE']

    # 3. Split data (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train Random Forest
    print("\nTraining Final Random Forest Model... please wait.")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # 5. Evaluate
    predictions = rf_model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    rmse = (mean_squared_error(y_test, predictions))**0.5

    print("\n" + "="*40)
    print("      FINAL MODEL PERFORMANCE")
    print("="*40)
    print(f"R-squared Score: {r2:.4f}")
    print(f"Average Error (RMSE): {rmse:.2f} MW")
    print("-" * 40)

    # 6. Feature Importance
    print("Sensor Importance (Relative Impact):")
    for name, imp in zip(X.columns, rf_model.feature_importances_):
        print(f"{name}: {imp:.4f}")
    
    # 7. Save results
    output = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
    output.to_csv('model_results.csv', index=False)
    print("\n[✔] Test results saved to 'model_results.csv'")
    print("="*40)

    # --- INTERACTIVE LOOP START ---
    while True:
        print("\n" + "-"*40)
        print(">>> CUSTOM SCENARIO PREDICTOR")
        print("Enter readings or type 'q' to exit.")
        
        try:
            # Check for exit command at the first input
            at_raw = input("Enter Ambient Temperature (AT) in °C: ").lower().strip()
            if at_raw in ['q', 'quit', 'exit']:
                print("\nExiting Predictor. Great work on the model!")
                break
            
            at_input = float(at_raw)
            v_input  = float(input("Enter Exhaust Vacuum (V) in cm Hg: "))
            ap_input = float(input("Enter Ambient Pressure (AP) in mbar: "))
            rh_input = float(input("Enter Relative Humidity (RH) %: "))

            user_scenario = pd.DataFrame([[at_input, v_input, ap_input, rh_input]], 
                                         columns=['AT', 'V', 'AP', 'RH'])
            
            custom_pred = rf_model.predict(user_scenario)
            
            print("\n" + "*"*40)
            print(f"  PREDICTED POWER OUTPUT: {custom_pred[0]:.2f} MW")
            print("*"*40)
            
        except ValueError:
            print("\n[!] Error: Please enter numerical values or 'q' to exit.")
    # --- INTERACTIVE LOOP END ---

if __name__ == "__main__":
    run_final_power_plant_model()
