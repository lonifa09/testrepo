import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# First 100 records from the dataset
data = {
    'Wh id': [233, 2540, 2524, 3145, 404, 3119, 1010, 3093, 127, 358, 242, 549, 566, 395, 378, 1055, 2541, 3065, 452, 1020, 350, 554, 543, 413, 3105, 473, 575, 573, 437, 355, 254, 124, 346, 248, 265, 3039, 223, 429, 533, 2001, 123, 231, 436, 3138, 471, 257, 3132, 340, 1042, 1045, 3143, 3103, 2513, 411, 168, 568, 239, 3167, 3090, 3008, 361, 354, 529, 337, 569, 3035, 430, 3168, 431, 502, 253, 3174, 3701, 256, 271, 396, 250, 258, 1004, 243, 558, 2509, 415, 489, 3151, 475, 324, 339, 1049, 126, 1019, 252, 420, 1040, 1044, 412, 464, 383, 119, 3057],
    'Store Name': ['Access Park Food', 'Ballito Junction', 'Ballito Lifestyle', 'Bassonia Food', 'Bedfordview', 'Blackheath', 'Blue Route Food', 'Broadacres', 'Canal Walk Food', 'Cascades Centre Food', 'Cavendish Square Food', 'Cedar Square', 'Centurion Mall Food', 'Chilli Lane', 'Columbine Square', 'Constantia Emporium', 'Cornubia', 'Cradlestone Mall', 'Cresta Food', 'DURBANVILLE VILLAGE SQ', 'Delcairn', 'Diamond Mall', 'Doringkloof', 'Douglasdale', 'East Rand Retail Foods', 'Eastgate Food', 'Eden Meadow', 'Farrarmere', 'Fourways Food', 'Galleria', 'Garden Route Mall Food', 'Gardens', 'Gateway Food', 'Glen Garry', 'Grassy Park', 'Graystone Drive', 'Greenacres Food', 'Greenside', 'Hazeldene', 'Hemingways', 'Hout Bay', 'Howick', 'Ilanga Mall', 'Jean Crossing', 'Killarney', 'Knysna', 'Kyalami', 'La Lucia', 'Laborie', 'Laguna Mall', 'Lemontree', 'Lifestyle Food', 'Lillies Quarter Food', 'Linksfield', 'Longbeach Mall', 'Lynnwood Road', 'Magalies View', 'Makhado', 'Mall Of Africa Food', 'Mall Of The North Food', 'Meyersdal', 'Midlands Mall', 'Mooirivier', 'Musgrave Food', 'Nelspruit Crossing Foods', 'Nicolway', 'Northcliff', 'Northridge Mall', 'Northwold', 'Norwood', 'OLD BAKERY CT', 'Olympus', 'Online Dark Store Food', 'Paarl Mall Food', 'Palmyra Road', 'Parkview Shell Food', 'Piazza St Johns', 'Pinelands', 'Plattekloof', 'Plettenberg Bay', 'Preller Square Food', 'Richards Bay', 'River Square', 'Rivonia', 'Rynfield Square', 'Sandton Food', 'Scottburgh', 'Shelley Beach Foods', 'Simonstown', 'Somerset Mall Food', 'Station Square Food', 'Stellenbosch Squaree', 'Sunward Park', 'Table Bay Mall', 'The Sanctuary', 'The Wedge', 'Town Square', 'Trade Route Mall', 'Tygervalley Foods', 'Tzaneen'],
    'Orders': [0, 10, 1, 25, 3, 0, 33, 0, 0, 14, 64, 31, 52, 0, 0, 0, 1, 0, 60, 0, 0, 0, 0, 2, 37, 37, 0, 0, 6, 0, 45, 1, 43, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 20, 0, 0, 0, 0, 0, 0, 49, 1, 1, 1, 0, 0, 16, 25, 0, 2, 0, 0, 0, 0, 130, 9, 0, 84, 1, 0, 0, 1, 21, 3, 0, 0, 0, 58, 0, 9, 0, 45, 32, 1, 0, 51, 0, 1, 0, 0, 0, 0],
    'Pending Picks': [0, 1, 0, 4, 0, 0, 9, 0, 0, 0, 12, 4, 10, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 2, 9, 3, 0, 0, 0, 0, 18, 0, 8, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 9, 0, 1, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 42, 0, 0, 28, 0, 0, 0, 0, 3, 3, 0, 0, 0, 1, 0, 0, 0, 2, 14, 0, 0, 14, 0, 0, 0, 0, 0, 0],
    'Cancelled Orders': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Orders Completed': [0, 9, 1, 21, 3, 0, 24, 0, 0, 13, 52, 27, 41, 0, 0, 0, 1, 0, 47, 0, 0, 0, 0, 0, 28, 34, 0, 0, 6, 0, 26, 1, 33, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 19, 0, 0, 0, 0, 0, 0, 40, 1, 0, 1, 0, 0, 13, 24, 0, 1, 0, 0, 0, 0, 84, 9, 0, 55, 0, 0, 0, 1, 17, 0, 0, 0, 0, 56, 0, 9, 0, 43, 18, 1, 0, 37, 0, 1, 0, 0, 0, 0],
    'Pending Loads': [0, 1, 1, 4, 0, 0, 13, 0, 0, 1, 21, 5, 11, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 23, 4, 0, 0, 0, 0, 18, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 28, 0, 0, 0, 0, 13, 0, 0, 0, 0, 12, 0, 4, 0, 6, 16, 0, 0, 16, 0, 0, 0, 0, 0, 0],
    'Completed Loads': [0, 9, 0, 21, 0, 0, 20, 0, 0, 12, 43, 26, 40, 0, 0, 0, 0, 0, 46, 0, 0, 0, 0, 0, 14, 33, 0, 0, 0, 0, 26, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 2, 24, 0, 0, 0, 0, 0, 0, 81, 9, 0, 55, 0, 0, 0, 0, 7, 0, 0, 0, 0, 45, 0, 5, 0, 39, 16, 0, 0, 35, 0, 0, 0, 0, 0, 0],
    'Historical Open Orders': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Print record counts for each column before validation
print("Record counts before validation:")
for key in data:
    print(f"{key}: {len(data[key])} records")

# Validate all arrays have same length
assert all(len(data['Wh id']) == len(data[key]) for key in data), \
    f"Arrays have different lengths. Expected {len(data['Wh id'])} records, but found varying lengths"

df = pd.DataFrame(data)
print(f"\nSuccessfully created DataFrame with {len(df)} records")

# Create summary cards
def create_summary_card(title, value):
    return html.Div([
        html.H6(title, style={'textAlign': 'center', 'marginBottom': '5px'}),
        html.H3(f"{value:,}", style={'textAlign': 'center', 'marginTop': '5px'})
    ], style={
        'border': '1px solid #ddd',
        'borderRadius': '5px',
        'padding': '10px',
        'margin': '10px',
        'backgroundColor': '#f9f9f9',
        'width': '150px'
    })

# Calculate summary values
metrics = {
    'Total Orders': df['Orders'].sum(),
    'Pending Loads': df['Pending Loads'].sum(),
    'Orders Completed': df['Orders Completed'].sum(),
    'Pending Picks': df['Pending Picks'].sum()
}

# Create visualizations
order_status_fig = px.bar(
    df.nlargest(20, 'Orders'),
    x='Store Name',
    y=['Pending Picks', 'Cancelled Orders', 'Orders Completed'],
    title='Top 20 Stores by Order Status',
    barmode='stack',
    height=400
)

scatter_fig = px.scatter(
    df,
    x='Orders Completed',
    y='Pending Picks',
    size='Orders',
    color='Store Name',
    hover_name='Store Name',
    title='Order Completion Efficiency',
    height=400
)

# NEW: Third graph - Grouped bar chart for Orders, Orders Completed, and Pending Loads
metrics_comparison = px.bar(
    df.nlargest(20, 'Orders'),
    x='Store Name',
    y=['Orders', 'Orders Completed', 'Pending Loads'],
    title='Order Metrics Comparison (Top 20 Stores)',
    barmode='group',
    height=500,
    color_discrete_map={
        'Orders': '#1f77b4',
        'Orders Completed': '#2ca02c',
        'Pending Loads': '#ff0000'
    }
)

metrics_comparison.update_layout(
    xaxis_title="Store Name",
    yaxis_title="Count",
    legend_title="Metrics",
    hovermode='x unified'
)

metrics_comparison.update_traces(
    hovertemplate="<b>%{x}</b><br>%{y:.0f} %{fullData.name}"
)

# App layout
app.layout = html.Div([
    html.H1("Order Status Dashboard", style={
        'textAlign': 'center', 
        'marginBottom': '20px',
        'color': '#2c3e50'
    }),
    
    # Summary Cards
    html.Div([
        create_summary_card(title, value) 
        for title, value in metrics.items()
    ], style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'justifyContent': 'center',
        'marginBottom': '20px'
    }),
    
    # Filters
    html.Div([
        html.Div([
            html.Label("Select Stores:", style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='store-filter',
                options=[{'label': store, 'value': store} for store in df['Store Name'].unique()],
                multi=True,
                placeholder="All Stores",
                style={'width': '100%'}
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
        
        html.Div([
            html.Label("Metrics to Display:", style={'fontWeight': 'bold'}),
            dcc.Checklist(
                id='metrics-toggle',
                options=[
                    {'label': ' Orders', 'value': 'Orders'},
                    {'label': ' Orders Completed', 'value': 'Orders Completed'},
                    {'label': ' Pending Loads', 'value': 'Pending Loads'}
                ],
                value=['Orders', 'Orders Completed', 'Pending Loads'],
                inline=True,
                style={'marginTop': '10px'}
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'})
    ], style={
        'margin': '20px 0',
        'backgroundColor': '#f0f0f0',
        'padding': '10px',
        'borderRadius': '5px'
    }),
    
    # Visualizations - Now 3 graphs in 2 rows
    html.Div([
        # First row with two graphs
        html.Div([
            dcc.Graph(
                id='order-status-chart', 
                figure=order_status_fig, 
                style={'width': '48%', 'display': 'inline-block'}
            ),
            dcc.Graph(
                id='scatter-plot', 
                figure=scatter_fig,
                style={'width': '48%', 'display': 'inline-block', 'float': 'right'}
            )
        ], style={'marginBottom': '20px'}),
        
        # Second row with the new metrics comparison graph (full width)
        html.Div([
            dcc.Graph(
                id='metrics-comparison',
                figure=metrics_comparison,
                style={'width': '100%'}
            )
        ])
    ]),
    
    # Data Table
    dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10,
        style_table={
            'overflowX': 'auto', 
            'margin': '20px',
            'border': '1px solid #ddd',
            'borderRadius': '5px'
        },
        style_header={
            'backgroundColor': '#2c3e50',
            'color': 'white',
            'fontWeight': 'bold'
        },
        style_cell={
            'minWidth': '100px', 
            'width': '150px', 
            'maxWidth': '180px',
            'whiteSpace': 'normal',
            'textAlign': 'left',
            'padding': '10px'
        },
        filter_action="native",
        sort_action="native",
        filter_options={"placeholder_text": "Filter..."}
    )
], style={
    'fontFamily': 'Arial, sans-serif',
    'padding': '20px',
    'maxWidth': '1200px',
    'margin': '0 auto'
})

# Callbacks for interactivity
@app.callback(
    Output('order-status-chart', 'figure'),
    [Input('store-filter', 'value'),
     Input('metrics-toggle', 'value')]  # Updated to match layout
)
def update_order_chart(selected_stores, selected_statuses):
    if not selected_stores:
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Store Name'].isin(selected_stores)]
    
    filtered_df = filtered_df.nlargest(20, 'Orders')
    
    fig = px.bar(
        filtered_df,
        x='Store Name',
        y=selected_statuses,
        title='Store Order Status Breakdown',
        barmode='stack',
        height=400
    )
    
    return fig

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('store-filter', 'value')]
)
def update_scatter_plot(selected_stores):
    if not selected_stores:
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Store Name'].isin(selected_stores)]
    
    fig = px.scatter(
        filtered_df,
        x='Orders Completed',
        y='Pending Picks',
        size='Orders',
        color='Store Name',
        hover_name='Store Name',
        title='Order Completion Efficiency',
        height=400
    )
    
    return fig

@app.callback(
    Output('metrics-comparison', 'figure'),
    [Input('store-filter', 'value'),
     Input('metrics-toggle', 'value')]
)
def update_metrics_comparison(selected_stores, selected_metrics):
    if not selected_stores:
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Store Name'].isin(selected_stores)]
    
    filtered_df = filtered_df.nlargest(20, 'Orders')
    
    fig = px.bar(
        filtered_df,
        x='Store Name',
        y=selected_metrics,
        title='Order Metrics Comparison',
        barmode='group',
        height=500,
        color_discrete_map={
            'Orders': '#1f77b4',
            'Orders Completed': '#2ca02c',
            'Pending Loads': '#ff7f0e'
        }
    )
    
    fig.update_layout(
        xaxis_title="Store Name",
        yaxis_title="Count",
        legend_title="Metrics",
        hovermode='x unified'
    )
    
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>%{y:.0f} %{fullData.name}"
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)