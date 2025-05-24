import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="WAMZ Macroeconomic Dashboard", layout="wide")

# Title
st.title("📊 WAMZ Macroeconomic Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")

# Define WAMZ countries
wamz_countries = ["Ghana", "Nigeria", "Sierra Leone", "The Gambia", "Guinea", "Liberia"]
selected_countries = st.sidebar.multiselect("Select countries", wamz_countries, default=wamz_countries)

# Macroeconomic indicators
indicators = ["GDP (USD Billion)", "Inflation Rate (%)", "Exchange Rate (Local/USD)", "Current Account (% GDP)"]
selected_indicator = st.sidebar.selectbox("Select Indicator", indicators)

# Generate mock macroeconomic data
def load_mock_data():
    years = list(range(2015, 2025))
    data = []

    for country in wamz_countries:
        for year in years:
            data.append({
                "Country": country,
                "Year": year,
                "GDP (USD Billion)": round(10 + 5 * wamz_countries.index(country) + (year - 2015) * 0.5, 2),
                "Inflation Rate (%)": round(5 + wamz_countries.index(country) * 2 + (year - 2015) * 0.3, 2),
                "Exchange Rate (Local/USD)": round(5 + wamz_countries.index(country) * 3 + (year - 2015) * 0.4, 2),
                "Current Account (% GDP)": round(-5 + wamz_countries.index(country) * 1 + (year - 2015) * 0.2, 2)
            })
    return pd.DataFrame(data)

# Load and filter data
df = load_mock_data()
df_filtered = df[df["Country"].isin(selected_countries)]

# Plot line chart
fig = px.line(
    df_filtered,
    x="Year",
    y=selected_indicator,
    color="Country",
    markers=True,
    title=f"{selected_indicator} Trends in WAMZ Countries"
)

fig.update_layout(title_x=0.5, height=500)
st.plotly_chart(fig, use_container_width=True)

# Show raw data
with st.expander("🔍 Show Raw Data"):
    st.dataframe(df_filtered)
