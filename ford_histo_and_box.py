import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

national = pd.read_csv("all_F150s.csv")
national_prices = national["Price"].to_numpy()

local = pd.read_csv("all_local.csv")
local_prices = local["0"].to_numpy()

longmont = pd.read_csv("all_longmont.csv")
longmont_prices = longmont["0"].to_numpy()


fig = ff.create_distplot([national_prices, local_prices, longmont_prices], ["National (TrueCar.com)", "Brighton Ford", "Longmont Ford"], curve_type="normal")
fig.update_layout(
    title="F150-4WD Price Distribution"
)
fig.show()
