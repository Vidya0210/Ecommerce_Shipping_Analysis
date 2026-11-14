
import pandas as pd
import plotly.express as px
import requests
from pathlib import Path

# Load state-wise delivery report
df = pd.read_csv("data/processed/state_delivery_report.csv")

# Download Brazil states GeoJSON
geojson_url = (
    "https://raw.githubusercontent.com/"
    "giuliano-macedo/geodata-br-states/"
    "master/geojson/br_states.json"
)

response = requests.get(geojson_url, timeout=30)
response.raise_for_status()
brazil_geojson = response.json()

# Create interactive map
fig = px.choropleth(
    df,
    geojson=brazil_geojson,
    locations="customer_state",
    featureidkey="properties.sigla",
    color="on_time_rate",
    hover_name="customer_state",
    hover_data={
        "total_orders": True,
        "on_time_orders": True,
        "average_delivery_days": True,
        "on_time_rate": ":.2f"
    },
    color_continuous_scale="RdYlGn",
    range_color=(70, 100),
    title="Brazil State-wise On-Time Delivery Performance"
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

fig.update_layout(
    title_x=0.5,
    coloraxis_colorbar_title="On-Time Rate (%)"
)

# Save interactive map
Path("outputs/charts").mkdir(parents=True, exist_ok=True)

fig.write_html("outputs/charts/brazil_delivery_map.html")

print("Brazil delivery map created successfully!")
print("Open: outputs/charts/brazil_delivery_map.html")
