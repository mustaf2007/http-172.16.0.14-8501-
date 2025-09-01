import streamlit as st
import matplotlib.pyplot as plt

# Title and description
st.title("Somalia Economic Key Findings 2024")
st.markdown("""
- Somalia’s GDP growth: 4.1% in 2024 (constant 2022 prices), close to 4.2% in 2023.
- GDP levels (current prices): $11,966 million in 2024, up from $10,957 million in 2023.
- GDP per capita (current prices): $737 in 2024, up from $694 in 2023.
- Strong household consumption and fixed investment growth financed by overseas remittances and grants.
- Imports surged, partially offset by export growth, especially in agricultural products.
- Livestock exports contracted but remain high due to demand from Middle East.
- Gross national disposable income (GNDI) reached $18,226 million in 2024.
""")

# Data for plots
years = ['2023', '2024']

gdp_growth = [4.2, 4.1]
gdp_levels = [10957, 11966]
gdp_per_capita = [694, 737]
household_consumption_growth = 8.8
capital_formation_growth = 21.1
export_growth = 42.3
import_growth = 28.5
gndi_2024 = 18226

# GDP Growth plot
st.subheader("GDP Growth Rate (Constant 2022 Prices)")
fig, ax = plt.subplots()
ax.bar(years, gdp_growth, color=['lightblue', 'cornflowerblue'])
for i, v in enumerate(gdp_growth):
    ax.text(i, v + 0.05, f"{v}%", ha='center')
ax.set_ylim(0, max(gdp_growth) + 1)
ax.set_ylabel('Percentage (%)')
st.pyplot(fig)

# GDP Levels
st.subheader("GDP Levels (Current Prices in Million USD)")
fig, ax = plt.subplots()
ax.bar(years, gdp_levels, color=['lightgreen', 'forestgreen'])
for i, v in enumerate(gdp_levels):
    ax.text(i, v + 200, f"${v}M", ha='center')
ax.set_ylabel("Million USD")
st.pyplot(fig)

# GDP Per Capita
st.subheader("GDP Per Capita (Current Prices in USD)")
fig, ax = plt.subplots()
ax.bar(years, gdp_per_capita, color=['lightcoral', 'indianred'])
for i, v in enumerate(gdp_per_capita):
    ax.text(i, v + 10, f"${v}", ha='center')
ax.set_ylabel("USD")
st.pyplot(fig)

# Household Consumption and Capital Formation Growth
st.subheader("Household Consumption & Capital Formation Growth (2024)")
fig, ax = plt.subplots()
labels = ['Household Consumption', 'Capital Formation']
values = [household_consumption_growth, capital_formation_growth]
colors = ['mediumslateblue', 'darkorange']
ax.bar(labels, values, color=colors)
for i, v in enumerate(values):
    ax.text(i, v + 0.5, f"{v}%", ha='center')
ax.set_ylim(0, max(values) + 10)
ax.set_ylabel('% Growth')
st.pyplot(fig)

# Export and Import Growth
st.subheader("Export and Import Growth Rates (2024)")
fig, ax = plt.subplots()
labels = ['Exports', 'Imports']
values = [export_growth, import_growth]
colors = ['seagreen', 'tomato']
ax.bar(labels, values, color=colors)
for i, v in enumerate(values):
    ax.text(i, v + 0.5, f"{v}%", ha='center')
ax.set_ylim(0, max(values) + 10)
ax.set_ylabel('% Growth')
st.pyplot(fig)

# Display GNDI as a key metric
st.subheader("Gross National Disposable Income (GNDI) 2024")
st.metric(label="GNDI (Million USD)", value=f"${gndi_2024:,}")

# Additional notes
st.markdown("""
**Notes:**

- Remittances and international aid contribute significantly to household incomes and financing imports.
- Livestock exports remain robust despite contraction, driven by Middle East demand.
- Trade deficit widened in 2024 due to surge in imports.
- Remittances act countercyclically sustaining consumption and investment during economic downturns.
""")
