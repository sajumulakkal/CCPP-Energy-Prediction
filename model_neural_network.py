import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score

# Suppress technical warnings for a cleaner UI
warnings.filterwarnings("ignore", category=UserWarning)

def run_neural_network_final():
    # 1. Load Data
    try:
        df = pd.read_csv('CCPP_data.csv')
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("Error: 'CCPP_data.csv' not found.")
        return

    X = df[['AT', 'V', 'AP', 'RH']]
    y = df['PE']

    # 2. Scaling (Essential for Neural Networks)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 4. Train Neural Network
    print("\nTraining Neural Network (100, 50 layers)...")
    model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # 5. Evaluate
    preds = model.predict(X_test)
    print("\n" + "="*40)
    print(f"      NEURAL NETWORK PERFORMANCE")
    print("="*40)
    print(f"R-squared Score: {r2_score(y_test, preds):.4f}")
    print("="*40)

    # --- INTERACTIVE LOOP START ---
    while True:
        print("\n" + "-"*40)
        print(">>> NEURAL NETWORK PREDICTOR")
        print("Enter readings or type 'q' to exit.")
        
        try:
            # Check for exit command at the first input
            at_raw = input("Enter Ambient Temp (AT) in °C: ").lower().strip()
            if at_raw in ['q', 'quit', 'exit']:
                print("\nShutting down Neural Network. Goodbye!")
                break
            
            at = float(at_raw)
            v  = float(input("Enter Exhaust Vacuum (V) in cm Hg: "))
            ap = float(input("Enter Ambient Pressure (AP) in mbar: "))
            rh = float(input("Enter Relative Humidity (RH) %: "))
            
            # 6. Format and Scale the user input
            user_input = pd.DataFrame([[at, v, ap, rh]], columns=['AT', 'V', 'AP', 'RH'])
            user_scaled = scaler.transform(user_input)
            
            # 7. Predict
            res = model.predict(user_scaled)
            
            print("\n" + "*"*40)
            print(f"  PREDICTED POWER OUTPUT: {res[0]:.2f} MW")
            print("*"*40)
            
            # Boundary check logic
            if res[0] > 495.76 or res[0] < 420.26:
                print("(!) WARNING: Result is outside historical ranges.")
                
        except ValueError:
            print("\n[!] Error: Please enter numerical values or 'q' to exit.")
    # --- INTERACTIVE LOOP END ---

if __name__ == "__main__":
    run_neural_network_final()
