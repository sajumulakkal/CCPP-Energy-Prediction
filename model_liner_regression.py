import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_power_plant_model():
    # 1. Load the dataset
    try:
        df = pd.read_csv('CCPP_data.csv')
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("Error: 'CCPP_data.csv' not found. Please ensure it's in this folder.")
        return

    # 2. Define Features (X) and Target (y)
    X = df[['AT', 'V', 'AP', 'RH']]
    y = df['PE']

    # 3. Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train the Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Show standard performance metrics
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    rmse = (mean_squared_error(y_test, predictions))**0.5

    print("\n" + "="*35)
    print("      MODEL TRAINING COMPLETE")
    print("="*35)
    print(f"R-squared Score: {r2:.4f}")
    print(f"Avg Error (RMSE): {rmse:.2f} MW")
    print("="*35)

    # 6. INTERACTIVE LOOP
    while True:
        print("\n" + "-"*35)
        print("--- NEW PREDICTION SCENARIO ---")
        print("Enter readings or type 'q' to exit.")
        
        try:
            # Check for exit command first
            user_input_check = input("1. Temperature (AT) [1.81 - 37.11 °C]: ").lower().strip()
            if user_input_check in ['q', 'quit', 'exit']:
                print("\nExiting program. Goodbye!")
                break
            
            user_at = float(user_input_check)
            user_v  = float(input("2. Exhaust Vacuum (V) [25.36 - 81.56 cm Hg]: "))
            user_ap = float(input("3. Ambient Pressure (AP) [992.89 - 1033.30 mbar]: "))
            user_rh = float(input("4. Relative Humidity (RH) [25.56 - 100.16 %]: "))

            # Convert input into a format the model understands (a DataFrame)
            user_data = pd.DataFrame([[user_at, user_v, user_ap, user_rh]], 
                                     columns=['AT', 'V', 'AP', 'RH'])

            # Predict!
            user_pred = model.predict(user_data)

            print("\n" + "*"*40)
            print(f"  ESTIMATED POWER OUTPUT (PE): {user_pred[0]:.2f} MW")
            print("*"*40)
            
        except ValueError:
            print("\n[!] Error: Please enter numerical values or 'q' to exit.")

if __name__ == "__main__":
    run_power_plant_model()
