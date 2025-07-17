# 🧠 Customer Segmentation & Recommendation System

A full-fledged **Data Science project** that clusters customers based on behavior and generates **personalized product recommendations**. The solution includes a **Flask-based web app** and an **interactive Power BI dashboard** for deep business insights.

---

## 📊 Power BI Dashboard

The Power BI dashboard provides a detailed view of customer segments and their behavior. It includes:

- 📌 **Segment KPIs**: Avg. Spend, Total Transactions, Recency
- 📈 **Cluster Distribution**: Bar and Pie Charts for segment sizes
- 📉 **Segment-wise Spend & Transaction Comparison**
- 🔍 **Interactive Drill-down**: Filter by Segment, Country, or Customer ID
- ✅ **Recommendations Table**: Easily view suggested product categories per customer

> All visuals are arranged in multiple pages to maintain clarity, aesthetics, and focus per insight.

---

## 🧠 Highlights & Learnings

- Real-world **customer segmentation** using RFM metrics and KMeans clustering
- Built a **rule-based recommendation engine** tailored to each segment
- Developed a clean and responsive **Flask Web App** for user interaction
- Integrated **Power BI** for executive-level visualization and storytelling
- Mastered **PCA**, **feature scaling**, and **unsupervised learning**

---

## 💡 Recommendations Logic

Customers are grouped into clusters using unsupervised learning (KMeans). Based on each segment's behavior (e.g., high spenders vs low frequency), products from specific categories are recommended.

---

## 🔍 Dataset Details

- 📁 **File**: `Customer_Segments_and_Recommendations.csv`
- 📌 **Source**: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- 💡 **Key Features Used**:
  - `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`
  - Engineered features: `Total_Spend`, `Recency`, `Frequency`, `InvoiceDay`, `Hour`, `Month`, `Year`, `Segment`, `Recommendations`

---

## 🔗 Flask Web App

- 🌐 Enter a **Customer ID**
- ⚡ Get **Cluster Segment Info** and **Recommended Product Categories**
- ✅ Built using Flask, HTML, CSS (within Jupyter Notebook for portability)
- 📦 All files are hosted locally, no external dependencies

---

## 📒 Jupyter Notebook

All code, from EDA to clustering to recommendation logic, is included in:

- `Flask_App_Customer_Segmentation.ipynb`

It covers:
- Data preprocessing
- Feature engineering
- RFM calculation
- PCA for dimensionality reduction
- KMeans clustering
- Customer profiling
- Exporting results to CSV

---

## 📁 Dataset Sample Output

The CSV output includes enriched records with:

| CustomerID | Total_Spend | Frequency | Recency | Customer_Segment | Recommendations |
|------------|-------------|-----------|---------|------------------|------------------|
| 13047      | 12456.5     | 17        | 14      | Segment 2        | Kitchenware, Decor |
| 17850      | 456.7       | 2         | 92      | Segment 0        | Stationery, Office Supplies |


---

## 🧩 Future Improvements

- 🛍️ Integrate **Market Basket Analysis** for more specific product combos
- 🧠 Use **Collaborative Filtering** for smarter recommendations
- 🌐 Deploy to cloud (Render/Heroku) for public access
- 📦 Add downloadable PDF reports from dashboard or app
- 📊 Include seasonal trends and time-series forecasting

---

## 📬 Contact

**Tejas Jain**  
📧 Email: tejasjain056@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/tejas-jain)  
🐙 GitHub: [@056tejas](https://github.com/056tejas)
