from scipy.stats import binom
import plotly.graph_objects as go
import plotly.figure_factory as ff


more = [binom.pmf(x, 100, 0.7186) for x in range(100)]
less = [binom.pmf(x, 100, 0.2814) for x in range(100)]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name=">35k",
        x=list(range(100)),
        y=[x*100 for x in more]
    )
)
fig.add_trace(
    go.Bar(
        name="<35k",
        x=list(range(100)),
        y=[x*100 for x in less]
    )
)

fig.update_layout(
    title="Ford F150 Binomial PDF out of 100",
    xaxis_title="N (Number of F150s)",
    yaxis_title="Probability",
    yaxis=dict(
        ticksuffix="%"
    )
)
fig.show()
fig.write_html("ford_binomial_prob.html")


