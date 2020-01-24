import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

data = pd.read_csv("data/data/all.csv")
national_prices = data[data["Where"] == "National"]["Price"].to_numpy()
local_prices = data[data["Where"] == "Local"]["Price"].to_numpy()
longmont_prices = data[data["Where"] == "Longmont"]["Price"].to_numpy()

fig = ff.create_distplot([national_prices, local_prices, longmont_prices],
                         ["National Price", "Brighton data", "Longmont data"], curve_type="normal", show_hist=False)
fig.update_layout(
    title="F150-4WD Normal Curves"
)
fig.show()
fig.write_html("plot.html")
