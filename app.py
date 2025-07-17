
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("Customer_Segments_and_Recommendations.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    customer_id = request.form["customer_id"]
    try:
        customer_id = float(customer_id)
        customer = df[df["CustomerID"] == customer_id]
        if not customer.empty:
            row = customer.iloc[0]
            return render_template("result.html",
                                   customer_id=row["CustomerID"],
                                   segment=row["Customer_Segment"],
                                   recommendation=row["Recommendation"],
                                   rec1=row["Rec1_Description"],
                                   rec2=row["Rec2_Description"],
                                   rec3=row["Rec3_Description"])
        else:
            return render_template("result.html", error="Customer ID not found.")
    except Exception as e:
        return render_template("result.html", error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
