"""
SpaceX Falcon 9 Launch Records Dashboard (Plotly Dash)

Run locally:
    pip install dash pandas plotly
    python spacex_dash_app.py
Then open http://127.0.0.1:8050 in a browser.
"""

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)
spacex_df = pd.read_csv(DATA_URL)
max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

app = Dash(__name__)

site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": site, "value": site} for site in sorted(spacex_df["Launch Site"].unique())
]

app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "padding": "20px", "maxWidth": "1100px", "margin": "0 auto"},
    children=[
        html.H1("SpaceX Launch Records Dashboard", style={"textAlign": "center", "color": "#0F62FE"}),
        dcc.Dropdown(
            id="site-dropdown",
            options=site_options,
            value="ALL",
            placeholder="Select a Launch Site here",
            searchable=True,
        ),
        html.Br(),
        dcc.Graph(id="success-pie-chart"),
        html.Br(),
        html.P("Payload range (kg):"),
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            value=[min_payload, max_payload],
            marks={0: "0", 2500: "2500", 5000: "5000", 7500: "7500", 10000: "10000"},
        ),
        dcc.Graph(id="success-payload-scatter-chart"),
    ],
)


@app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
def update_pie_chart(selected_site):
    if selected_site == "ALL":
        counts = spacex_df[spacex_df["class"] == 1]["Launch Site"].value_counts().reset_index()
        counts.columns = ["Launch Site", "Success Count"]
        fig = px.pie(counts, values="Success Count", names="Launch Site",
                     title="Total Successful Launches by Site")
    else:
        site_df = spacex_df[spacex_df["Launch Site"] == selected_site]
        counts = site_df["class"].value_counts().rename({1: "Success", 0: "Failure"}).reset_index()
        counts.columns = ["Outcome", "Count"]
        fig = px.pie(counts, values="Count", names="Outcome",
                     title=f"Launch Outcomes for site {selected_site}",
                     color="Outcome", color_discrete_map={"Success": "#24A148", "Failure": "#DA1E28"})
    return fig


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"), Input("payload-slider", "value")],
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    mask = spacex_df["Payload Mass (kg)"].between(low, high)
    filtered_df = spacex_df[mask]
    if selected_site != "ALL":
        filtered_df = filtered_df[filtered_df["Launch Site"] == selected_site]
    fig = px.scatter(
        filtered_df, x="Payload Mass (kg)", y="class", color="Booster Version Category",
        title="Correlation between Payload and Success for " + (
            "all Sites" if selected_site == "ALL" else selected_site
        ),
        labels={"class": "Launch Outcome (0 = Failure, 1 = Success)"},
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
