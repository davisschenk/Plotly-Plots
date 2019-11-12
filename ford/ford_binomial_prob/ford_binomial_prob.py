from scipy.stats import binom
import plotly.graph_objects as go

more = [binom.pmf(x, 100, 0.7186) for x in range(100)]
print(more)
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=list(range(100)),
        y=[x*100 for x in more]
    )
)

fig.update_layout(
    title="Probability of exactly N F150s being selected out of 100",
    xaxis_title="N (Number of F150s)",
    yaxis_title="Probability",
    yaxis=dict(
        ticksuffix="%"
    )
)
fig.show()
fig.write_html("ford_binomial_prob.html")
