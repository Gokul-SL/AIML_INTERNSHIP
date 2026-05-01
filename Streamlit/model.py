import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib


data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,10,11,12],
    "Pass": [0,0,0,0,1,1,1,1,1,1,1,1]
}


df = pd.DataFrame(data)


X = df[["Hours_Studied"]]
y = df["Pass"]


model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")