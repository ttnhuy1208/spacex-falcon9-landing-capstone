# SpaceX Falcon 9 First-Stage Landing Prediction — IBM Data Science Capstone

Predicting whether the Falcon 9 first stage will land successfully, using data
collected from the SpaceX REST API and Wikipedia, SQL-based exploratory
analysis, interactive visual analytics, and a set of tuned classification
models.

## Contents

| Notebook | Description |
|---|---|
| [`01_data_collection_api.ipynb`](01_data_collection_api.ipynb) | Collects launch records from the SpaceX REST API (`api.spacexdata.com`) |
| [`02_data_collection_webscraping.ipynb`](02_data_collection_webscraping.ipynb) | Scrapes the Wikipedia "List of Falcon 9 and Falcon Heavy launches" page with BeautifulSoup |
| [`03_data_wrangling.ipynb`](03_data_wrangling.ipynb) | Cleans the data and derives the landing-success class label |
| [`04_eda_sql.ipynb`](04_eda_sql.ipynb) | Exploratory data analysis with SQL (SQLite) |
| [`05_eda_visualization.ipynb`](05_eda_visualization.ipynb) | Exploratory data analysis with Matplotlib / Seaborn |
| [`06_interactive_map_folium.ipynb`](06_interactive_map_folium.ipynb) | Interactive launch-site maps with Folium |
| [`07_dashboard_plotly_dash.ipynb`](07_dashboard_plotly_dash.ipynb) | Dashboard figures (see also [`dashboard/spacex_dash_app.py`](dashboard/spacex_dash_app.py) for the live Dash app) |
| [`08_predictive_analysis_classification.ipynb`](08_predictive_analysis_classification.ipynb) | Logistic Regression / SVM / Decision Tree / KNN model comparison |

## Data

All notebooks load data from the public datasets published for this course on
IBM Cloud Object Storage, so every notebook can be re-run end to end.

## Running the dashboard locally

```bash
pip install dash pandas plotly
python dashboard/spacex_dash_app.py
```

Then open `http://127.0.0.1:8050`.
