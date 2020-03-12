from dissonance_project.data import without_dissonance, with_dissonance
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Box(x=with_dissonance, boxpoints="all", name="Dissonance"))
fig.add_trace(go.Box(x=without_dissonance, boxpoints="all", name="Control"))
fig.update_traces(
                  jitter=0.1,
                  fillcolor='#31394d',
                  line_color='#626b73',
                  opacity=0.95
                  )

fig.update_layout(
    title="Effects of Dissonance on Solving a Multiplication Problem",
    xaxis_title="Seconds to Complete Problem",
    yaxis_title="Treatment",
    showlegend=False
)

# fig.show()
fig.write_html(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\dissonance_project\box_plot\box_plot_two.html")
