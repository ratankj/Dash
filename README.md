# Dash

DCC: We import the dcc module (DCC stands for Dash Core Components). This module includes a Graph component called dcc.Graph, which is used to render interactive graphs.

plotly.express: We also import the plotly.express library to build the interactive graphs.

---------------------------------------------------------------------------------------------------

# Initialize the app
app = Dash(__name__)

This line is known as the Dash constructor and is responsible for initializing your app. It is almost always the same for any Dash app you create.

---------------------------------------------------------------------------------------------------


# App layout
app.layout = html.Div([
    html.Div(children='Hello World')
])


 children:   we use to add text content to the page

 ---------------------------------------------------------------------------------------------------


 # Run the app
if __name__ == '__main__':
    app.run(debug=True)



These lines are for running your app, and they are almost always the same for any Dash app you create.

 ---------------------------------------------------------------------------------------------------