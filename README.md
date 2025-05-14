# 📊 Suicide Rate Analysis Dashboard

This is an interactive **data visualization dashboard** built with **Streamlit** that analyzes worldwide suicide statistics using data from the **WHO Suicide Statistics dataset**.

## 🔍 Features

- 🌐 View **total suicides worldwide** for any selected year
- 📍 Filter by **country** and **year**
- 📈 Visualize suicide trends by **gender** and **age group**
- 🗂 View raw filtered data for deeper insight
- 🚫 Handles cases where suicide data is not available

---

## 📦 Requirements

Before running the app, make sure you have the following Python packages installed:

```bash
pip install streamlit pandas matplotlib seaborn

📁 Dataset
The dashboard uses the WHO Suicide Statistics Dataset. Make sure the file is named: who_suicide_statistics.csv and placed in the same directory as suicide_dashboard.py.

🚀 Running the App
In your terminal or command prompt, run: streamlit run suicideDataAnalysis.py
This will open the app in your web browser.

🧠 Insights You Can Gain
Gender-wise differences in suicide rates
Which age groups are most affected
Year-wise and country-wise trends in suicide data
