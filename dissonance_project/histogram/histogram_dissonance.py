import plotly.graph_objects as go
from dissonance_project.data import with_dissonance

fig = go.Figure()
fig.add_trace(go.Histogram(x=with_dissonance, marker_color='#31394d', nbinsy=10, nbinsx=10))

fig.update_layout(
    title="Distribution without Dissonance",
    yaxis_title="Seconds to Complete Problem",
    showlegend=False
)

# fig.show()
fig.write_html(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\dissonance_project\box_plot\histogram_dissonance.html")
