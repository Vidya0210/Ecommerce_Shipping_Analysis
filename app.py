
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components





# ==================================================
# PREMIUM HYBRID THEME - NAVY BLUE + WHITE
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #FFFFFF !important;
    color: #17243A !important;
}

/* Hide Streamlit default elements */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Main layout */
.block-container {
    padding-top: 1.3rem;
    padding-bottom: 2rem;
    max-width: 1550px;
}

/* Text colors */
.stApp p,
.stApp label,
.stApp span,
.stApp li,
.stMarkdown,
.stCaption {
    color: #17243A;
}

/* HERO HEADER */
.hero {
    background: linear-gradient(110deg, #4776C5, #7299D6);
    padding: 32px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: none;
    border: 1px solid #A9C4EB;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 30px;
    font-weight: 800;
}

.hero p {
    color: #E5EDFA !important;
    font-size: 14px;
}

/* SECTION HEADINGS */
.section-title {
    font-size: 21px;
    font-weight: 800;
    color: #101B35 !important;
    margin: 22px 0 15px 0;
    padding-bottom: 10px;
    border-bottom: 2px solid #DCE6F5;
}

h1, h2, h3, h4, h5, h6 {
    color: #17243A !important;
}

/* PREMIUM KPI CARDS */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #FFFFFF, #EAF1FC) !important;
    border: 1px solid #C5D5ED !important;
    border-radius: 18px !important;
    padding: 22px 20px !important;
    min-height: 125px;
    box-shadow: 0 6px 20px rgba(23, 36, 58, 0.09) !important;
    transition: all 0.25s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(38, 63, 112, 0.16) !important;
    border-color: #526DCE !important;
}

div[data-testid="stMetric"] label {
    color: #526078 !important;
    font-size: 13px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #17243A !important;
    font-size: 27px !important;
    font-weight: 800 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    font-weight: 650 !important;
}

/* CUSTOM KPI CARDS */
.metric-card {
    background: linear-gradient(145deg, #FFFFFF, #EAF1FC);
    border: 1px solid #C5D5ED;
    border-radius: 18px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 6px 20px rgba(23, 36, 58, 0.08);
    transition: all 0.25s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(38, 63, 112, 0.15);
}

.metric-label {
    color: #526078 !important;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .6px;
}

.metric-value {
    color: #17243A !important;
    font-size: 29px;
    font-weight: 800;
    margin-top: 10px;
}

.metric-note {
    color: #718096 !important;
    font-size: 12px;
    margin-top: 6px;
}

/* INSIGHT CARDS */
.insight-card {
    background: linear-gradient(120deg, #FFFFFF, #F0F5FC);
    border: 1px solid #DCE5F2;
    border-left: 5px solid #526DCE;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 13px;
    box-shadow: 0 4px 14px rgba(20, 40, 75, 0.06);
    color: #17243A !important;
    font-size: 14px;
}

.insight-card b {
    color: #101B35 !important;
}

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    gap: 9px;
    background: #E5ECF6;
    padding: 8px;
    border-radius: 13px;
}

.stTabs [data-baseweb="tab"] {
    color: #34445E !important;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: #FFFFFF !important;
    color: #263F70 !important;
    border-radius: 9px;
}

/* DATA TABLES */
div[data-testid="stDataFrame"] {
    border: 1px solid #DCE5F2;
    border-radius: 13px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(20, 40, 75, 0.05);
}

/* ==========================================
   PURCHASE DATE RANGE - FORCE LIGHT INPUT
   ========================================== */

/* Keep the date widget in light color mode */
div[data-testid="stDateInput"] {
    color-scheme: light !important;
    background: #FFFFFF !important;
}

/* BaseWeb input shell used by Streamlit date_input */
div[data-testid="stDateInput"] [data-baseweb="input"],
div[data-testid="stDateInput"] [data-baseweb="base-input"],
div[data-testid="stDateInput"] [data-baseweb="input"] > div,
div[data-testid="stDateInput"] [data-baseweb="base-input"] > div {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1px solid #C5D8F2 !important;
    border-radius: 9px !important;
    box-shadow: none !important;
    color-scheme: light !important;
}

/* Date text itself */
div[data-testid="stDateInput"] input,
div[data-testid="stDateInput"] input[type="text"] {
    appearance: none !important;
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    color: #17243A !important;
    -webkit-text-fill-color: #17243A !important;
    border: 0 !important;
    box-shadow: none !important;
    color-scheme: light !important;
    opacity: 1 !important;
}

/* Calendar button and icon */
div[data-testid="stDateInput"] button {
    background: #FFFFFF !important;
    color: #4776C5 !important;
    border: 0 !important;
}

div[data-testid="stDateInput"] svg {
    color: #4776C5 !important;
    fill: #4776C5 !important;
}

/* Focus state */
div[data-testid="stDateInput"] [data-baseweb="input"]:focus-within,
div[data-testid="stDateInput"] [data-baseweb="base-input"]:focus-within {
    border-color: #4776C5 !important;
    box-shadow: none !important;
}

/* INPUT FIELDS */
.stSelectbox,
.stDateInput {
    background: #FFFFFF !important;
    border-radius: 10px;
}

input, textarea {
    color: #17243A !important;
}

/* RADIO NAVIGATION */
.stRadio div[role="radiogroup"] label {
    color: #17243A !important;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(110deg, #263F70, #405F9C);
    color: #FFFFFF !important;
    border: none;
    border-radius: 10px;
    padding: 9px 19px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #101B35;
    color: #FFFFFF !important;
    box-shadow: 0 5px 14px rgba(38, 63, 112, 0.20);
}

/* CAPTIONS */
.stCaption {
    color: #526078 !important;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #718096 !important;
    font-size: 12px;
    padding: 25px 0 5px 0;
    border-top: 1px solid #DCE5F2;
    margin-top: 25px;
}

/* MOBILE RESPONSIVE */
@media (max-width: 768px) {
    .hero {
        padding: 22px;
    }

    .hero h1 {
        font-size: 23px;
    }

    .metric-value {
        font-size: 24px;
    }
}


</style>
""", unsafe_allow_html=True)



# ==================================================
# FILE PATHS
# ==================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "processed"
CHART_DIR = BASE_DIR / "outputs" / "charts"


# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data
def load_csv(filename):
    path = DATA_DIR / filename

    if path.exists():
        return pd.read_csv(path)

    return pd.DataFrame()


orders = load_csv("delivery_kpi_results.csv")
states = load_csv("state_delivery_report.csv")
sellers = load_csv("seller_performance_report.csv")
monthly = load_csv("monthly_handoff_report.csv")
handoff = load_csv("carrier_handoff_results.csv")


# ==================================================
# HELPER FUNCTIONS
# ==================================================
def find_column(data, possible_names):
    for name in possible_names:
        if name in data.columns:
            return name
    return None


def format_percent(value):
    return f"{value:.2f}%"


def plot_layout(fig, height=380):
    fig.update_layout(
        height=height,
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter", color="#34445E"),
        margin=dict(l=20, r=20, t=55, b=25),
        legend=dict(
            orientation="h",
            y=1.12,
            x=0
        )
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#EDF1F6")

    return fig


def show_metric(label, value, note, icon):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{icon} &nbsp; {label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def normalize_status(series):
    return (
        series.astype(str)
        .str.strip()
        .str.lower()
        .str.replace("_", "-", regex=False)
        .str.replace(r"\s+", "-", regex=True)
    )


def calculate_kpis(data):
    if data.empty:
        return {
            "total": 0,
            "on_time": 0,
            "delayed": 0,
            "on_time_rate": 0,
            "delay_rate": 0,
            "average_days": 0
        }

    status_col = find_column(
        data, ["delivery_status", "status"]
    )

    days_col = find_column(
        data, ["delivery_days", "delivery_duration_days"]
    )

    if status_col:
        status = normalize_status(data[status_col])

        on_time = int(
            status.isin(["on-time", "ontime"]).sum()
        )

        delayed = int(
            status.isin(["delayed", "late"]).sum()
        )
    else:
        on_time = 0
        delayed = 0

    classified = on_time + delayed

    on_time_rate = (
        on_time / classified * 100 if classified else 0
    )

    delay_rate = (
        delayed / classified * 100 if classified else 0
    )

    if days_col:
        average_days = pd.to_numeric(
            data[days_col], errors="coerce"
        ).mean()

        if pd.isna(average_days):
            average_days = 0
    else:
        average_days = 0

    return {
        "total": len(data),
        "on_time": on_time,
        "delayed": delayed,
        "on_time_rate": on_time_rate,
        "delay_rate": delay_rate,
        "average_days": average_days
    }


def make_monthly_report(data):
    date_col = find_column(
        data,
        ["order_purchase_timestamp", "purchase_timestamp"]
    )

    status_col = find_column(
        data,
        ["delivery_status", "status"]
    )

    days_col = find_column(
        data,
        ["delivery_days", "delivery_duration_days"]
    )

    if not date_col:
        return pd.DataFrame()

    temp = data.copy()

    temp[date_col] = pd.to_datetime(
        temp[date_col], errors="coerce"
    )

    temp = temp.dropna(subset=[date_col])

    if temp.empty:
        return pd.DataFrame()

    temp["Month"] = (
        temp[date_col].dt.to_period("M").astype(str)
    )

    aggregation = {
        "Orders": (date_col, "count")
    }

    if status_col:
        temp["_on_time"] = normalize_status(
            temp[status_col]
        ).isin(["on-time", "ontime"])

        temp["_delayed"] = normalize_status(
            temp[status_col]
        ).isin(["delayed", "late"])

        aggregation["On-Time Orders"] = (
            "_on_time", "sum"
        )

        aggregation["Delayed Orders"] = (
            "_delayed", "sum"
        )

    if days_col:
        temp["_delivery_days"] = pd.to_numeric(
            temp[days_col], errors="coerce"
        )

        aggregation["Average Delivery Days"] = (
            "_delivery_days", "mean"
        )

    report = (
        temp.groupby("Month")
        .agg(**aggregation)
        .reset_index()
        .sort_values("Month")
    )

    if "On-Time Orders" in report.columns:
        report["On-Time Rate"] = (
            report["On-Time Orders"] /
            (report["On-Time Orders"] + report["Delayed Orders"])
            * 100
        )

    if "Delayed Orders" in report.columns:
        report["Delay Rate"] = (
            report["Delayed Orders"] /
            (report["On-Time Orders"] + report["Delayed Orders"])
            * 100
        )

    return report


def compare_kpis(current, previous):
    if previous["total"] == 0:
        return {
            "orders": "No previous-period data",
            "on_time": "No previous-period data",
            "delay": "No previous-period data",
            "days": "No previous-period data"
        }

    return {
        "orders": (
            f"{current['total'] - previous['total']:+,} orders"
        ),
        "on_time": (
            f"{current['on_time_rate'] - previous['on_time_rate']:+.2f} pp"
        ),
        "delay": (
            f"{current['delay_rate'] - previous['delay_rate']:+.2f} pp"
        ),
        "days": (
            f"{current['average_days'] - previous['average_days']:+.2f} days"
        )
    }


# ==================================================
# CHECK REQUIRED DATA
# ==================================================
if orders.empty:
    st.error(
        "Delivery KPI data is missing or empty. "
        "Please check data/processed/delivery_kpi_results.csv."
    )
    st.stop()


# ==================================================
# PREPARE MAIN DATASET
# ==================================================
orders = orders.copy()

purchase_date_col = find_column(
    orders,
    ["order_purchase_timestamp", "purchase_timestamp"]
)

delivery_days_col = find_column(
    orders,
    ["delivery_days", "delivery_duration_days"]
)

status_col = find_column(
    orders,
    ["delivery_status", "status"]
)

if purchase_date_col:
    orders[purchase_date_col] = pd.to_datetime(
        orders[purchase_date_col],
        errors="coerce"
    )

if delivery_days_col:
    orders[delivery_days_col] = pd.to_numeric(
        orders[delivery_days_col],
        errors="coerce"
    )


# ==================================================
# HEADER
# ==================================================
st.markdown("""
<div class="hero">
    <h1>📦 E-Commerce Shipping Intelligence</h1>
    <p>
        Advanced delivery analytics • Logistics intelligence
        • Seller performance • Business insights
    </p>
</div>
""", unsafe_allow_html=True)


# ==================================================
# NAVIGATION
# ==================================================
page = st.radio(
    "Navigation",
    [
        "Executive Overview",
        "Delivery Analytics",
        "Geographical Insights",
        "Seller Performance",
        "Logistics Intelligence",
        "Business Insights"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")


# ==================================================
# GLOBAL DATE FILTER
# ==================================================
st.markdown("### 📅 Dashboard Filters")

filtered_orders = orders.copy()
previous_orders = pd.DataFrame()

if purchase_date_col:
    valid_dates = orders[purchase_date_col].dropna()

    if not valid_dates.empty:
        min_date = valid_dates.min().date()
        max_date = valid_dates.max().date()

        filter_col1, filter_col2 = st.columns([2, 1])

        with filter_col1:
            selected_dates = st.date_input(
                "Select purchase date range",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date,
                key="purchase_date_range"
            )

        with filter_col2:
            st.metric(
                "Available Date Range",
                f"{(max_date - min_date).days + 1:,} days"
            )

        if isinstance(selected_dates, (tuple, list)):
            if len(selected_dates) == 2:
                start_date, end_date = selected_dates
            elif len(selected_dates) == 1:
                start_date = selected_dates[0]
                end_date = selected_dates[0]
            else:
                start_date, end_date = min_date, max_date
        else:
            start_date = selected_dates
            end_date = selected_dates

        if start_date > end_date:
            start_date, end_date = end_date, start_date

        start_timestamp = pd.Timestamp(start_date)
        end_timestamp = (
            pd.Timestamp(end_date) + pd.Timedelta(days=1)
        )

        filtered_orders = orders[
            (orders[purchase_date_col] >= start_timestamp) &
            (orders[purchase_date_col] < end_timestamp)
        ].copy()

        # Previous period has the same number of days.
        period_days = (end_date - start_date).days + 1

        previous_start = (
            start_timestamp - pd.Timedelta(days=period_days)
        )

        previous_end = start_timestamp

        previous_orders = orders[
            (orders[purchase_date_col] >= previous_start) &
            (orders[purchase_date_col] < previous_end)
        ].copy()

        st.caption(
            f"Showing {start_date} to {end_date}. "
            "Monthly trends use the order purchase month."
        )
    else:
        st.warning("Purchase dates could not be read.")
else:
    st.info("Purchase date column not found. Showing all records.")


# ==================================================
# KPI CALCULATIONS
# ==================================================
kpi = calculate_kpis(filtered_orders)
previous_kpi = calculate_kpis(previous_orders)

comparison = compare_kpis(kpi, previous_kpi)

monthly_report = make_monthly_report(filtered_orders)


# ==================================================
# PAGE 1: EXECUTIVE OVERVIEW
# ==================================================
if page == "Executive Overview":

    st.markdown(
        '<div class="section-title">Executive Overview</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Monitor delivery operations and compare current performance "
        "with the previous equal-length period."
    )

    # KPI CARDS
    st.markdown("### 📊 Key Performance Indicators")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Orders",
            f"{kpi['total']:,}",
            comparison["orders"]
        )

    with c2:
        st.metric(
            "On-Time Rate",
            format_percent(kpi["on_time_rate"]),
            comparison["on_time"]
        )

    with c3:
        st.metric(
            "Delayed Orders",
            f"{kpi['delayed']:,}",
            comparison["delay"]
        )

    with c4:
        st.metric(
            "Average Delivery",
            f"{kpi['average_days']:.2f} days",
            comparison["days"],
            delta_color="inverse"
        )

    st.caption(
        "Comparison values are changes from the previous period. "
        "For rates, pp means percentage points."
    )

    # DELIVERY HEALTH
    st.markdown("### 🚚 Delivery Health")

    left, right = st.columns([1, 1.5])

    with left:
        if kpi["on_time"] + kpi["delayed"] > 0:

            pie_data = pd.DataFrame({
                "Delivery Status": ["On-Time", "Delayed"],
                "Orders": [kpi["on_time"], kpi["delayed"]]
            })

            fig = px.pie(
                pie_data,
                names="Delivery Status",
                values="Orders",
                hole=0.68,
                title="On-Time vs Delayed Orders",
                color="Delivery Status",
                color_discrete_map={
                    "On-Time": "#16A085",
                    "Delayed": "#E76F51"
                }
            )

            fig.update_traces(
                textinfo="percent+label",
                hole=0.68
            )

            st.plotly_chart(
                plot_layout(fig, 370),
                width="stretch"
            )
        else:
            st.info("No classified delivery status available.")

    with right:
        if not monthly_report.empty and "On-Time Rate" in monthly_report:

            fig = px.line(
                monthly_report,
                x="Month",
                y="On-Time Rate",
                markers=True,
                title="Monthly On-Time Delivery Trend",
                hover_data=["Orders", "On-Time Orders", "Delayed Orders"]
            )

            fig.update_traces(
                line=dict(color="#526DCE", width=3),
                marker=dict(size=8)
            )

            fig.add_hline(
                y=90,
                line_dash="dash",
                line_color="#E76F51",
                annotation_text="90% reference"
            )

            fig.update_yaxes(
                title="On-Time Rate (%)",
                range=[0, 105]
            )

            st.plotly_chart(
                plot_layout(fig, 370),
                width="stretch"
            )
        else:
            st.info("Monthly delivery data is not available.")

    # PERIOD COMPARISON
    st.markdown("### 📈 Current vs Previous Period")

    if previous_kpi["total"] > 0:
        comparison_data = pd.DataFrame({
            "Period": ["Previous Period", "Selected Period"],
            "On-Time Rate": [
                previous_kpi["on_time_rate"],
                kpi["on_time_rate"]
            ],
            "Delay Rate": [
                previous_kpi["delay_rate"],
                kpi["delay_rate"]
            ]
        })

        fig = go.Figure()

        fig.add_trace(go.Bar(
            name="On-Time Rate",
            x=comparison_data["Period"],
            y=comparison_data["On-Time Rate"],
            marker_color="#16A085"
        ))

        fig.add_trace(go.Bar(
            name="Delay Rate",
            x=comparison_data["Period"],
            y=comparison_data["Delay Rate"],
            marker_color="#E76F51"
        ))

        fig.update_layout(
            barmode="group",
            title="Delivery Rate Comparison",
            yaxis_title="Rate (%)"
        )

        st.plotly_chart(
            plot_layout(fig, 350),
            width="stretch"
        )
    else:
        st.info(
            "There is no data for the previous comparison period."
        )

    # INSIGHTS
    st.markdown("### 💡 Quick Performance Summary")

    st.markdown(f"""
    <div class="insight-card">
        <b>Delivery performance:</b>
        {kpi['on_time_rate']:.2f}% of classified orders were delivered on time.
    </div>

    <div class="insight-card">
        <b>Delayed orders:</b>
        {kpi['delayed']:,} orders were delayed in the selected period.
    </div>

    <div class="insight-card">
        <b>Average delivery:</b>
        Orders took approximately {kpi['average_days']:.2f} days to reach customers.
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# PAGE 2: DELIVERY ANALYTICS
# ==================================================
elif page == "Delivery Analytics":

    st.markdown(
        '<div class="section-title">Advanced Delivery Analytics</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Explore delivery duration, monthly performance, "
        "and order delivery patterns."
    )

    # MONTHLY PERFORMANCE
    st.markdown("### 📅 Monthly Performance Trends")

    if not monthly_report.empty:

        trend_tabs = st.tabs([
            "On-Time Rate",
            "Average Delivery",
            "Delayed Orders"
        ])

        with trend_tabs[0]:
            if "On-Time Rate" in monthly_report.columns:

                fig = px.line(
                    monthly_report,
                    x="Month",
                    y="On-Time Rate",
                    markers=True,
                    title="Monthly On-Time Delivery Rate",
                    text="On-Time Rate"
                )

                fig.update_traces(
                    line=dict(color="#16A085", width=3),
                    texttemplate="%{text:.1f}%",
                    textposition="top center"
                )

                fig.update_yaxes(
                    title="On-Time Rate (%)",
                    range=[0, 105]
                )

                st.plotly_chart(
                    plot_layout(fig, 400),
                    use_container_width=True
                )

        with trend_tabs[1]:
            if "Average Delivery Days" in monthly_report.columns:

                fig = px.bar(
                    monthly_report,
                    x="Month",
                    y="Average Delivery Days",
                    color="Average Delivery Days",
                    color_continuous_scale="Blues",
                    title="Average Delivery Duration by Month"
                )

                fig.update_yaxes(
                    title="Average Days"
                )

                st.plotly_chart(
                    plot_layout(fig, 400),
                    use_container_width=True
                )

        with trend_tabs[2]:
            if "Delayed Orders" in monthly_report.columns:

                fig = px.bar(
                    monthly_report,
                    x="Month",
                    y="Delayed Orders",
                    color="Delayed Orders",
                    color_continuous_scale="Reds",
                    title="Monthly Delayed Orders"
                )

                st.plotly_chart(
                    plot_layout(fig, 400),
                    use_container_width=True
                )

        st.markdown("### Monthly Performance Table")

        st.dataframe(
            monthly_report,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("Monthly performance data is not available.")

    # DELIVERY DURATION DISTRIBUTION
    st.markdown("### ⏱️ Delivery Duration Distribution")

    if delivery_days_col:

        delivery_data = filtered_orders.copy()

        delivery_data[delivery_days_col] = pd.to_numeric(
            delivery_data[delivery_days_col],
            errors="coerce"
        )

        delivery_data = delivery_data.dropna(
            subset=[delivery_days_col]
        )

        if not delivery_data.empty:

            fig = px.histogram(
                delivery_data,
                x=delivery_days_col,
                nbins=35,
                title="Distribution of Delivery Duration",
                color_discrete_sequence=["#526DCE"]
            )

            fig.update_layout(
                xaxis_title="Delivery Days",
                yaxis_title="Number of Orders"
            )

            st.plotly_chart(
                plot_layout(fig, 380),
                use_container_width=True
            )

    # WEEKDAY VS WEEKEND
    st.markdown("### 📆 Weekday vs Weekend Analysis")

    if purchase_date_col:

        weekday_data = filtered_orders.copy()

        weekday_data["Day Type"] = (
            weekday_data[purchase_date_col]
            .dt.dayofweek
            .apply(
                lambda x: "Weekend" if x >= 5 else "Weekday"
            )
        )

        weekday_report = (
            weekday_data.groupby("Day Type")
            .size()
            .reset_index(name="Orders")
        )

        if not weekday_report.empty:

            fig = px.bar(
                weekday_report,
                x="Day Type",
                y="Orders",
                color="Day Type",
                title="Orders Purchased on Weekdays vs Weekends",
                color_discrete_map={
                    "Weekday": "#526DCE",
                    "Weekend": "#16A085"
                },
                text_auto=True
            )

            st.plotly_chart(
                plot_layout(fig, 330),
                use_container_width=True
            )

    # DATA PREVIEW
    with st.expander("View Delivery Dataset"):
        st.dataframe(
            filtered_orders.head(100),
            use_container_width=True
        )


# ==================================================
# PAGE 3: GEOGRAPHICAL INSIGHTS
# ==================================================
elif page == "Geographical Insights":

    st.markdown(
        '<div class="section-title">Geographical Insights</div>',
        unsafe_allow_html=True
    )

    if not states.empty:

        state_data = states.copy()

        rate_col = find_column(
            state_data, ["on_time_rate"]
        )

        state_col = find_column(
            state_data, ["customer_state", "state"]
        )

        count_col = find_column(
            state_data, ["total_orders", "order_count"]
        )

        if rate_col and state_col:

            state_data[rate_col] = pd.to_numeric(
                state_data[rate_col],
                errors="coerce"
            )

            state_data = state_data.dropna(
                subset=[rate_col]
            )

            # TOP AND BOTTOM STATES
            left, right = st.columns(2)

            if not state_data.empty:

                with left:
                    best = state_data.nlargest(5, rate_col)

                    fig = px.bar(
                        best.sort_values(rate_col),
                        x=rate_col,
                        y=state_col,
                        orientation="h",
                        title="Top 5 States",
                        color_discrete_sequence=["#16A085"]
                    )

                    st.plotly_chart(
                        plot_layout(fig, 350),
                        use_container_width=True
                    )

                with right:
                    worst = state_data.nsmallest(5, rate_col)

                    fig = px.bar(
                        worst.sort_values(rate_col),
                        x=rate_col,
                        y=state_col,
                        orientation="h",
                        title="Bottom 5 States",
                        color_discrete_sequence=["#E76F51"]
                    )

                    st.plotly_chart(
                        plot_layout(fig, 350),
                        use_container_width=True
                    )

            # STATE COMPARISON
            fig = px.bar(
                state_data.sort_values(rate_col),
                x=rate_col,
                y=state_col,
                orientation="h",
                color=rate_col,
                color_continuous_scale="Teal",
                title="On-Time Delivery Rate by State",
                hover_data=[count_col] if count_col else None
            )

            fig.update_layout(
                xaxis_title="On-Time Rate (%)",
                yaxis_title="Customer State"
            )

            st.plotly_chart(
                plot_layout(fig, 550),
                use_container_width=True
            )

        st.markdown("### State Performance Table")

        st.dataframe(
            state_data.sort_values(
                rate_col, ascending=False
            ) if rate_col else state_data,
            use_container_width=True,
            hide_index=True
        )

        map_file = CHART_DIR / "brazil_delivery_map.html"

        if map_file.exists():
            st.markdown("### 🗺️ Interactive Brazil Delivery Map")

            st.iframe(
            map_file.read_text(encoding="utf-8"),
            height=570,
        )
    
        else:
            st.warning(
                "Brazil map HTML was not found in outputs/charts."
            )

    else:
        st.warning("State performance data is not available.")


# ==================================================
# PAGE 4: SELLER PERFORMANCE
# ==================================================
elif page == "Seller Performance":

    st.markdown(
        '<div class="section-title">Seller Performance</div>',
        unsafe_allow_html=True
    )

    if not sellers.empty:

        seller_data = sellers.copy()

        rate_col = find_column(
            seller_data, ["on_time_rate"]
        )

        seller_col = find_column(
            seller_data, ["seller_id"]
        )

        if rate_col and seller_col:

            seller_data[rate_col] = pd.to_numeric(
                seller_data[rate_col],
                errors="coerce"
            )

            seller_data = seller_data.dropna(
                subset=[rate_col]
            )

            top = seller_data.nlargest(10, rate_col).copy()
            bottom = seller_data.nsmallest(10, rate_col).copy()

            top["Seller"] = (
                top[seller_col].astype(str).str[:12]
            )

            bottom["Seller"] = (
                bottom[seller_col].astype(str).str[:12]
            )

            left, right = st.columns(2)

            with left:
                fig = px.bar(
                    top.sort_values(rate_col),
                    x=rate_col,
                    y="Seller",
                    orientation="h",
                    title="Top 10 Sellers",
                    color_discrete_sequence=["#16A085"]
                )

                st.plotly_chart(
                    plot_layout(fig, 430),
                    use_container_width=True
                )

            with right:
                fig = px.bar(
                    bottom.sort_values(rate_col),
                    x=rate_col,
                    y="Seller",
                    orientation="h",
                    title="Bottom 10 Sellers",
                    color_discrete_sequence=["#E76F51"]
                )

                st.plotly_chart(
                    plot_layout(fig, 430),
                    use_container_width=True
                )

        st.markdown("### Seller Performance Details")

        st.dataframe(
            seller_data,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.warning("Seller performance data is not available.")


# ==================================================
# PAGE 5: LOGISTICS INTELLIGENCE
# ==================================================
elif page == "Logistics Intelligence":

    st.markdown(
        '<div class="section-title">Logistics Intelligence</div>',
        unsafe_allow_html=True
    )

    if not handoff.empty:

        handoff_data = handoff.copy()

        handoff_col = find_column(
            handoff_data,
            ["handoff_days", "purchase_to_carrier_days"]
        )

        transit_col = find_column(
            handoff_data,
            ["carrier_transit_days", "transit_days"]
        )

        if handoff_col and transit_col:

            handoff_data[handoff_col] = pd.to_numeric(
                handoff_data[handoff_col],
                errors="coerce"
            )

            handoff_data[transit_col] = pd.to_numeric(
                handoff_data[transit_col],
                errors="coerce"
            )

            handoff_avg = handoff_data[handoff_col].mean()
            transit_avg = handoff_data[transit_col].mean()

            a, b = st.columns(2)

            with a:
                show_metric(
                    "Purchase to Carrier",
                    f"{handoff_avg:.2f} days",
                    "Average handoff duration",
                    "📤"
                )

            with b:
                show_metric(
                    "Carrier to Customer",
                    f"{transit_avg:.2f} days",
                    "Average transit duration",
                    "🚚"
                )

            stage_data = pd.DataFrame({
                "Delivery Stage": [
                    "Purchase to Carrier",
                    "Carrier to Customer"
                ],
                "Average Days": [
                    handoff_avg,
                    transit_avg
                ]
            })

            fig = px.bar(
                stage_data,
                x="Delivery Stage",
                y="Average Days",
                color="Delivery Stage",
                title="Average Time by Delivery Stage",
                text_auto=".2f"
            )

            st.plotly_chart(
                plot_layout(fig, 370),
                use_container_width=True
            )

    else:
        st.warning("Carrier handoff data is not available.")

    # MONTHLY HANDOFF TREND
    if not monthly.empty:

        avg_handoff_col = find_column(
            monthly, ["average_handoff_days"]
        )

        avg_transit_col = find_column(
            monthly, ["average_transit_days"]
        )

        month_col = find_column(
            monthly, ["month"]
        )

        if month_col and (
            avg_handoff_col or avg_transit_col
        ):

            fig = go.Figure()

            if avg_handoff_col:
                fig.add_trace(go.Scatter(
                    x=monthly[month_col],
                    y=monthly[avg_handoff_col],
                    mode="lines+markers",
                    name="Purchase to Carrier"
                ))

            if avg_transit_col:
                fig.add_trace(go.Scatter(
                    x=monthly[month_col],
                    y=monthly[avg_transit_col],
                    mode="lines+markers",
                    name="Carrier to Customer"
                ))

            fig.update_layout(
                title="Monthly Logistics Performance",
                xaxis_title="Month",
                yaxis_title="Average Days"
            )

            st.plotly_chart(
                plot_layout(fig, 400),
                use_container_width=True
            )

    with st.expander("View Logistics Data"):
        if not handoff.empty:
            st.dataframe(
                handoff.head(100),
                use_container_width=True
            )


# ==================================================
# PAGE 6: BUSINESS INSIGHTS
# ==================================================
elif page == "Business Insights":

    st.markdown(
        '<div class="section-title">Business Insights & Recommendations</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 📌 Key Findings")

    st.markdown(f"""
    <div class="insight-card">
        <b>1. On-time delivery:</b>
        Current on-time delivery performance is
        {kpi['on_time_rate']:.2f}%.
    </div>

    <div class="insight-card">
        <b>2. Delayed orders:</b>
        {kpi['delayed']:,} orders were delayed in the selected period.
    </div>

    <div class="insight-card">
        <b>3. Delivery duration:</b>
        Average delivery takes
        {kpi['average_days']:.2f} days.
    </div>
    """, unsafe_allow_html=True)

    # STATE INSIGHTS
    if not states.empty and "on_time_rate" in states.columns:

        state_data = states.copy()

        state_data["on_time_rate"] = pd.to_numeric(
            state_data["on_time_rate"],
            errors="coerce"
        )

        state_data = state_data.dropna(
            subset=["on_time_rate"]
        )

        if not state_data.empty:

            best_state = state_data.loc[
                state_data["on_time_rate"].idxmax()
            ]

            worst_state = state_data.loc[
                state_data["on_time_rate"].idxmin()
            ]

            state_name_col = find_column(
                state_data, ["customer_state", "state"]
            )

            if state_name_col:

                st.markdown("### 🗺️ State-Level Insights")

                st.success(
                    f"Strongest state performance: "
                    f"{best_state[state_name_col]} "
                    f"({best_state['on_time_rate']:.2f}%)."
                )

                st.warning(
                    f"State needing attention: "
                    f"{worst_state[state_name_col]} "
                    f"({worst_state['on_time_rate']:.2f}%). "
                    "Investigate regional delivery challenges "
                    "and consider the number of orders."
                )

    # MONTHLY INSIGHTS
    if not monthly_report.empty:

        st.markdown("### 📈 Monthly Trend Insights")

        if "On-Time Rate" in monthly_report.columns:

            best_month = monthly_report.loc[
                monthly_report["On-Time Rate"].idxmax()
            ]

            worst_month = monthly_report.loc[
                monthly_report["On-Time Rate"].idxmin()
            ]

            st.markdown(f"""
            <div class="insight-card">
                <b>Best month:</b> {best_month['Month']}
                with an on-time rate of
                {best_month['On-Time Rate']:.2f}%.
            </div>

            <div class="insight-card">
                <b>Month needing attention:</b> {worst_month['Month']}
                with an on-time rate of
                {worst_month['On-Time Rate']:.2f}%.
            </div>
            """, unsafe_allow_html=True)

    # RECOMMENDATIONS
    st.markdown("### 🎯 Recommended Business Actions")

    recommendations = [
        "Investigate delayed orders and identify their root causes.",
        "Improve coordination between sellers and logistics operations.",
        "Monitor states with lower on-time delivery performance.",
        "Track handoff time separately from carrier transit time.",
        "Review seller performance using both delivery rate and order volume.",
        "Monitor monthly KPIs to identify improving or declining trends."
    ]

    for item in recommendations:
        st.markdown(f"- {item}")


# ==================================================
# FOOTER
# ==================================================
st.markdown("""
<div class="footer">
    E-Commerce Shipping & Delivery Intelligence Dashboard
    <br>
    Built with Python • Streamlit • Pandas • Plotly
    <br>
    Advanced Analytics Edition
</div>
""", unsafe_allow_html=True)
