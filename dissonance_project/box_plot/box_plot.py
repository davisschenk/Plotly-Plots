import pandas as pd
from dissonance_project.data import without_dissonance, with_dissonance
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Violin(y=with_dissonance, name="Dissonance", box_visible=True))
fig.add_trace(go.Violin(y=without_dissonance, name="Control", box_visible=True))
fig.update_traces(meanline_visible=True,
                  points='all',
                  jitter=0.05,
                  scalemode='count',
                  fillcolor='#31394d',
                  line_color='#626b73',
                  opacity=0.95
                  )

fig.update_layout(
    title="Effects of Dissonance on Solving a Multiplication Problem",
    yaxis_title="Seconds to Complete Problem",
    xaxis_title="Treatment",
    showlegend=False
)


fig.write_html(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\dissonance_project\box_plot\box_plot.html")

