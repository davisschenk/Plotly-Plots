import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from scipy import stats
data = pd.read_csv(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\ford\data\all.csv")

fig = px.histogram(data, x="Price", color="Where", marginal="box", histnorm="percent")
fig.update_layout(
    title="F150 Price Distribution",
    yaxis_title="Percent",
    yaxis=dict(
        ticksuffix="%"
    )

)
fig.show()
fig.write_html(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\ford\ford_histo_and_plot\ford_histo_and_plot.html")




