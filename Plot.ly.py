# import plotly express after installing
# import pandas after installing
import plotly.express as px
import pandas as pd

# read excel dataset
# and print to show accuracy
new_df = pd.read_excel("Module5.xlsx")
print(new_df)

# plot a line chart using px.line() function
# use fig.show() to see final visualization
fig = px.line(new_df, x = "Time", y = "Average Position", markers = True)
fig.show()