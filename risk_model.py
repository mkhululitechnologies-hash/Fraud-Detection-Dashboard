import pandas as pd

# Load dataset
df = pd.read_csv("FraudShield_Banking_Data.csv")

# Convert Yes/No to 1/0
df["Is_International_Transaction"] = df["Is_International_Transaction"].map({"Yes":1,"No":0})
df["Unusual_Time_Transaction"] = df["Unusual_Time_Transaction"].map({"Yes":1,"No":0})

# Fill numeric columns with 0
num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(0)

# Fill text columns with "Unknown"
text_cols = df.select_dtypes(include=['object', 'string']).columns
df[text_cols] = df[text_cols].fillna("Unknown")

# Create Risk Score
df["Risk_Score"] = (
    df["Is_International_Transaction"] * 2 +
    df["Unusual_Time_Transaction"] * 2 +
    df["Previous_Fraud_Count"] * 3
)

# Create Risk Level
def classify_risk(score):
    if score >= 5:
        return "High Risk"
    elif score >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Risk_Level"] = df["Risk_Score"].apply(classify_risk)

# Save new dataset
df.to_csv("FraudShield_Enhanced.csv", index=False)

print("DONE - New dataset created")