import pandas
import plotly.express as px
import datetime

data = pandas.read_csv(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\visually_thinking\data\avocado.csv")
data.sort_values(by=["Date"], inplace=True)
data.query("region == 'Denver'", inplace=True)
data["Date"].apply(datetime.datetime.fromisoformat)
fig = px.line(data, y="AveragePrice", x="Date", color="region", line_shape="linear")
fig.show()