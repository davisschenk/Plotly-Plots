import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

z = [(x - .7186)/0.0038 for x in np.arange(0, 1, 0.01)]
data = pd.DataFrame()
data["Z"] = z

fig = go.Figure()
fig.add_trace(
    go.Bar(
        y=data["Z"],
        x=list(range(0, 100))
    )
)
fig.update_layout(
    xaxis=dict(
        ticksuffix="%"
    ),
    yaxis_title="Z Value",
    xaxis_title="Probability",
    title="Normal Model Probability",
    annotations=[
        go.layout.Annotation(
            x=75,
            y=8.263,
            text="75%",
            hovertext="Probability: 75%<br>"
                      "Z-Score: 8.263",
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,

        )
    ]
)
fig.show()
fig.write_html("ford_normal_model_prob.html")