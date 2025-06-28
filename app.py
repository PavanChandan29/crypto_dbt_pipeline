import streamlit as st
import pandas as pd
import psycopg2
import subprocess
import plotly.express as px
import plotly.graph_objects as go

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="crypto_data",
    user="postgres",
    password="12345678",  # Replace with your actual password
    host="localhost",
    port="5432"
)

# Streamlit config
st.set_page_config(page_title="Crypto Analytics", layout="wide")

# Header layout
col_logo, col_title = st.columns([1, 8])
with col_logo:
    st.image("dbt_logo.jpg", width=300)
with col_title:
    st.title("\U0001F680 dbt-Powered Crypto Data Dashboard")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Top 10 Cryptos", "Tracked Tokens", "Database Objects", "Test Results", "\U0001F4C8 Data Flow"
])

# --- TAB 1 ---
with tab1:
    st.subheader("\U0001F4CA Top 10 Cryptocurrencies by Market Cap")

    top10_df = pd.read_sql("SELECT * FROM crypto_top10", conn)
    top10_df["market_cap_b"] = top10_df["market_cap"] / 1e9

    concise_df = top10_df[["symbol", "price_usd", "market_cap_b"]].copy()
    concise_df.columns = ["Symbol", "Price (USD)", "Market Cap (B)"]

    st.dataframe(concise_df, use_container_width=False)

    st.markdown("### \U0001F4C9 Log Scale Bar Chart")
    colors = [
        "#76C7C0", "#F4C542", "#F49E42", "#DDA0DD", "#90EE90",
        "#87CEFA", "#FF69B4", "#C5E384", "#77DD77", "#B39EB5"
    ]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=concise_df["Symbol"],
        y=concise_df["Market Cap (B)"],
        text=[f"${val:,.1f}B" for val in concise_df["Market Cap (B)"]],
        textposition="auto",
        marker_color=colors
    ))
    fig.update_layout(
        yaxis_type="log",
        xaxis_title="<b>Token</b>",
        yaxis_title="<b>Market Cap (B)</b>",
        height=450,
        margin=dict(l=40, r=40, t=40, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", size=12, color="white")
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_yaxes(
    type="log",
    tickvals=[10, 100, 1000, 2000],
    ticktext=["$10B", "$100B", "$1T", "$2T"]
)


    st.plotly_chart(fig, use_container_width=False)

    st.markdown("### \U0001F967 Market Share Pie Chart")
    pie_fig = px.pie(
        concise_df,
        names="Symbol",
        values="Market Cap (B)",
        hole=0.3
    )
    pie_fig.update_layout(
        height=400,
        margin=dict(l=40, r=40, t=40, b=40),
        font=dict(family="Arial", size=12, color="white")
    )
    st.plotly_chart(pie_fig, use_container_width=False)

# --- TAB 2 ---
with tab2:
    st.subheader("\U0001F3AF Tracked Tokens (AVAX, ETH, BTC, SOL)")
    tracked_df = pd.read_sql("SELECT * FROM track_main_tokens", conn)
    st.dataframe(tracked_df, use_container_width=True)

# --- TAB 3 ---
with tab3:
    st.subheader("\U0001F5C2 Available Tables & Views")
    db_objects = pd.read_sql("""
        SELECT table_name, table_type
        FROM information_schema.tables
        WHERE table_schema = 'public'
          AND table_catalog = 'crypto_data'
        ORDER BY table_type, table_name;
    """, conn)
    st.dataframe(db_objects, use_container_width=True)

# --- TAB 4 ---
with tab4:
    st.subheader("\u2705 dbt Test Results")
    with st.spinner("Running dbt tests..."):
        result = subprocess.run(["dbt", "test", "--select", "crypto_top10", "track_main_tokens"],
                                capture_output=True, text=True)
        st.code(result.stdout)
        if result.returncode == 0:
            st.success("All tests passed! \U0001F389")
        else:
            st.error("Some tests failed. See output above.")

# --- TAB 5: Data Flow ---
with tab5:
    st.subheader("\U0001F4C8 End-to-End Data Flow Overview")

    st.markdown("""
    <div style="line-height: 2;">
    <b>\U0001F7E0 1. Data Source:</b> CoinMarketCap API<br>
    <span style="margin-left: 25px;">• Extracted using Python (requests + dotenv)</span><br>
    <span style="margin-left: 25px;">• Columns like price, market cap, symbol</span><br><br>

    <b>\U0001F535 2. Load to Database:</b><br>
    <span style="margin-left: 25px;">• Stored in PostgreSQL table: <code>crypto_raw</code></span><br>
    <span style="margin-left: 25px;">• Loaded via SQLAlchemy using pandas.to_sql</span><br><br>

    <b>\U0001F7E3 3. Transform Using dbt:</b><br>
    <span style="margin-left: 25px;">• <code>crypto_top10</code> selects top-ranked tokens</span><br>
    <span style="margin-left: 25px;">• <code>track_main_tokens</code> filters for AVAX, BTC, ETH, SOL</span><br><br>

    <b>\U0001F9EA 4. Data Quality Tests:</b><br>
    <span style="margin-left: 25px;">• <code>not_null</code> on market_cap</span><br>
    <span style="margin-left: 25px;">• <code>accepted_values</code> on symbols (top 10 / tracked)</span><br><br>

    <b>\U0001F4CA 5. Visualization:</b><br>
    <span style="margin-left: 25px;">• Streamlit charts & dashboards</span><br>
    <span style="margin-left: 25px;">• Bar chart (log scale), pie chart, test output, DB explorer</span>
    </div>
    """, unsafe_allow_html=True)

# Close DB connection
conn.close()