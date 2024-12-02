#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset with the correct encoding
file_path = r"C:\Users\Admin\Downloads\archive (4)\DataCoSupplyChainDataset.csv"
df = pd.read_csv(file_path, encoding='latin-1')  # Use 'latin-1' or 'ISO-8859-1' for non-UTF-8 files

# Display the first few rows of the dataset
print(df.head())


# In[2]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected = True)


# In[3]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df.head()


# In[4]:


df.columns


# In[5]:


data=df.copy()
FeatureList=['Type', 'Benefit per order', 'Sales per customer', 
          'Delivery Status', 'Late_delivery_risk', 'Category Name', 'Customer City', 'Customer Country', 
           'Customer Id', 'Customer Segment', 
          'Customer State', 'Customer Zipcode', 'Department Name', 'Latitude', 'Longitude',
          'Market', 'Order City', 'Order Country', 'Order Customer Id', 'order date (DateOrders)', 'Order Id', 
          'Order Item Cardprod Id', 'Order Item Discount', 'Order Item Discount Rate', 'Order Item Id', 
          'Order Item Product Price', 'Order Item Profit Ratio', 'Order Item Quantity', 'Sales', 'Order Item Total', 
          'Order Profit Per Order', 'Order Region', 'Order State', 'Order Status', 'Order Zipcode','Product Card Id',
          'Product Category Id', 'Product Description', 'Product Image', 'Product Name', 'Product Price', 'Product Status',
       'shipping date (DateOrders)', 'Shipping Mode']

df1=df[FeatureList]
df1.head()


# In[6]:


import plotly.express as px

# Group and prepare the data
data_delivery_status = df1.groupby(['Delivery Status'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=False)

# Create the bar plot with customized colors and layout
fig = px.bar(
    data_delivery_status,
    x='Delivery Status',
    y='Number of Orders',
    color='Number of Orders',
    labels={'Delivery Status': 'Delivery Status', 'Number of Orders': 'Number of Orders'},
    color_continuous_scale='reds'  # Use a red gradient for the bars
)

# Update layout for better aesthetics
fig.update_layout(
    title={
        'text': "Number of Orders by Delivery Status",  # Add a descriptive title
        'y': 0.9,  # Position title closer to the top
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 24  # Increase title font size
    },
    xaxis_title="Delivery Status",  # Label for x-axis
    yaxis_title="Number of Orders",  # Label for y-axis
    coloraxis_colorbar={
        'title': "Number of Orders"  # Label for color bar
    },
    plot_bgcolor='white'  # Set background color to white for clarity
)

# Update x-axis and y-axis for better readability
fig.update_xaxes(tickangle=45)  # Rotate x-axis labels for readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray')  # Add gridlines for better reference

# Show the plot
fig.show()


# In[7]:


import plotly.express as px

# Group and prepare the data
data_delivery_status_region = df1.groupby(['Delivery Status', 'Order Region'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']

# Create the bar chart
fig = px.bar(
    data_delivery_status_region,
    x='Delivery Status',
    y='Number of Orders',
    color='Order Region',
    color_discrete_sequence=custom_colors,  # Apply the custom color palette
    labels={
        'Delivery Status': 'Delivery Status',
        'Number of Orders': 'Number of Orders',
        'Order Region': 'Order Region'
    },
    title="Number of Orders by Delivery Status and Region"
)

# Update the layout for better aesthetics
fig.update_layout(
    title={
        'text': "Number of Orders by Delivery Status and Region",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#333333'  # Neutral color for the title
    },
    xaxis_title="Delivery Status",
    yaxis_title="Number of Orders",
    legend_title="Order Region",
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral font color
    )
)

# Improve x-axis readability
fig.update_xaxes(tickangle=45, title_font=dict(size=14), tickfont=dict(size=10))

# Add subtle gridlines for the y-axis
fig.update_yaxes(showgrid=True, gridcolor='lightgray', zerolinecolor='black', title_font=dict(size=14), tickfont=dict(size=10))

# Show the plot
fig.show()


# In[8]:


# Ensure 'Customer Id' is converted to a string
df1['Customer_ID_STR'] = df1['Customer Id'].astype(str)

# Group by 'Customer_ID_STR' to count the number of orders
data_customers = df1.groupby(['Customer_ID_STR'])['Order Id'].count().reset_index(name='Number of Orders')

# Sort by 'Number of Orders' in descending order
data_customers = data_customers.sort_values(by='Number of Orders', ascending=False)

# Create a bar chart for the top 20 customers with better colors and layout
fig = px.bar(
    data_customers.head(20),
    x='Number of Orders',
    y='Customer_ID_STR',
    color='Number of Orders',
    color_continuous_scale='Viridis',  # Use a visually appealing color scale
    title='Top 20 Customers by Number of Orders',
    labels={
        'Number of Orders': 'Number of Orders',
        'Customer_ID_STR': 'Customer ID'
    }
)

# Customize layout for better presentation
fig.update_layout(
    title={
        'text': "Top 20 Customers by Number of Orders",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22  # Adjust the title font size
    },
    xaxis_title="Number of Orders",  # Add x-axis title
    yaxis_title="Customer ID",  # Add y-axis title
    plot_bgcolor='white',  # Set background color to white
    font=dict(
        family="Arial",  # Set font family for professionalism
        size=12  # Set default font size
    )
)

# Update y-axis to improve readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray')  # Add subtle gridlines to y-axis
fig.update_xaxes(showgrid=False)  # Remove gridlines from x-axis

# Show the chart
fig.show()


# In[9]:


import plotly.express as px

# Convert 'Customer Id' to string explicitly using .loc
df1.loc[:, 'Customer_ID_STR'] = df1['Customer Id'].astype(str)

# Group by 'Customer_ID_STR' to calculate the total profit per customer
data_customers_profit = df1.groupby(['Customer_ID_STR'])['Order Profit Per Order'].sum().reset_index(name='Profit of Orders')

# Sort by 'Profit of Orders' in descending order
data_customers_profit = data_customers_profit.sort_values(by='Profit of Orders', ascending=False)

# Define a darker color palette for a bolder look
custom_colors = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600']

# Create a bar chart for the top 20 customers by profit
fig = px.bar(
    data_customers_profit.head(20),
    x='Profit of Orders',
    y='Customer_ID_STR',
    color='Profit of Orders',
    color_continuous_scale=custom_colors,  # Apply the darker color palette
    title='Top 20 Customers by Profit of Orders',
    labels={
        'Profit of Orders': 'Profit ($)',
        'Customer_ID_STR': 'Customer ID'
    }
)

# Update layout for better presentation
fig.update_layout(
    title={
        'text': "Top 20 Customers by Profit of Orders",
        'y': 0.95,  # Position title closer to the top
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Darker color for the title
    },
    xaxis_title="Profit ($)",
    yaxis_title="Customer ID",
    legend_title="Profit ($)",
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#111111"  # Darker font color for contrast
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(tickangle=0, showgrid=True, gridcolor='gray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for a cleaner look
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the plot
fig.show()


# In[10]:


import plotly.express as px

# Group and prepare the data
data_Customer_Segment = df1.groupby(['Customer Segment'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=False)

# Define a custom 3-color palette
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green - complementary colors

# Create a pie chart with custom colors
fig = px.pie(
    data_Customer_Segment,
    values='Number of Orders',
    names='Customer Segment',
    title='Number of Orders by Customer Segments',
    width=700,
    height=700,
    color_discrete_sequence=custom_colors  # Apply the 3 matching colors
)

# Update layout for a polished presentation
fig.update_layout(
    title={
        'text': 'Number of Orders by Customer Segments',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'
    },
    font=dict(
        family="Arial",
        size=14,
        color="#111111"
    )
)

# Add labels and percentages
fig.update_traces(
    textposition='inside',
    textinfo='percent+label'  # Show both percentages and segment labels
)

# Show the plot
fig.show()


# In[11]:


import plotly.express as px

# Group and prepare the data
data_Category_Name = df1.groupby(['Category Name'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=True)

# Define a custom 3-color palette for presentation
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green

# Create the bar chart
fig = px.bar(
    data_Category_Name,
    x='Number of Orders',
    y='Category Name',
    color='Number of Orders',
    color_continuous_scale=custom_colors,  # Apply the custom colors
    title='Number of Orders by Category Name',
    labels={
        'Number of Orders': 'Number of Orders',
        'Category Name': 'Category Name'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Number of Orders by Category Name",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral title color
    },
    xaxis_title="Number of Orders",  # Label for x-axis
    yaxis_title="Category Name",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#111111"  # Darker font for readability
    )
)

# Improve axis and gridline readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=10))
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=10))

# Show the chart
fig.show()


# In[12]:


import plotly.express as px

# Group and prepare the data
data_Region = df1.groupby(['Order Region'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=True)

# Define a visually appealing color palette
custom_colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

# Create the bar chart
fig = px.bar(
    data_Region,
    x='Number of Orders',
    y='Order Region',
    color='Number of Orders',
    color_continuous_scale=custom_colors,  # Apply the custom color palette
    title='Number of Orders by Region',
    labels={
        'Number of Orders': 'Number of Orders',
        'Order Region': 'Order Region'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Number of Orders by Region",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral title color
    },
    xaxis_title="Number of Orders",  # Label for x-axis
    yaxis_title="Order Region",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#111111"  # Darker font for readability
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=10))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=10))

# Show the chart
fig.show()


# In[13]:


import plotly.express as px

# Group and prepare the data
data_countries = df1.groupby(['Order Country'])['Order Id'].count().reset_index(name='Number of Orders').sort_values(by='Number of Orders', ascending=True)

# Define a green color palette
custom_colors = ['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#2E7D32']  # Shades of green

# Create the bar chart
fig = px.bar(
    data_countries.head(20),
    x='Number of Orders',
    y='Order Country',
    color='Number of Orders',
    color_continuous_scale=custom_colors,  # Apply green color palette
    title='Top 20 Countries by Number of Orders',
    labels={
        'Number of Orders': 'Number of Orders',
        'Order Country': 'Country'
    }
)

# Update layout for a polished look
fig.update_layout(
    title={
        'text': "Top 20 Countries by Number of Orders",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#333333'  # Neutral title color
    },
    xaxis_title="Number of Orders",
    yaxis_title="Country",
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Darker font for better readability
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[14]:


df_geo=df1.groupby([ 'Order Country', 'Order City'])['Order Profit Per Order'].sum().reset_index(name='Profit of Orders').sort_values(by= 'Profit of Orders', ascending= False)

df_geo


# In[15]:


import plotly.express as px

# Create the choropleth map
fig = px.choropleth(
    df_geo,
    locationmode='country names',
    locations='Order Country',
    color='Profit of Orders',  # Column representing the profit
    hover_name='Order Country',  # Display country name on hover
    hover_data={'Profit of Orders': True, 'Order City': False},  # Include 'Profit of Orders' on hover but exclude 'Order City'
    color_continuous_scale=px.colors.sequential.Plasma,  # Use the Plasma color scale for a vibrant look
    title="Global Distribution of Profit by Country"  # Add a descriptive title
)

# Update layout for better aesthetics
fig.update_layout(
    title={
        'text': "Global Distribution of Profit by Country",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 20,
        'color': '#111111'  # Neutral dark title color
    },
    geo=dict(
        showframe=False,  # Remove frame around the map
        showcoastlines=True,  # Highlight coastlines for better reference
        coastlinecolor="gray",  # Color for coastlines
        projection_type='equirectangular'  # Use a standard map projection
    ),
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Show the plot
fig.show()


# In[16]:


import plotly.express as px

# Group and prepare the data
df_sales_country = df1.groupby(['Order Country'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing blue-to-orange color palette
custom_colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#d62728']

# Create the bar chart
fig = px.bar(
    df_sales_country.head(10),
    x='Sales of Orders',
    y='Order Country',
    color='Sales of Orders',
    color_continuous_scale=custom_colors,  # Apply custom color scale
    title='Top 10 Countries by Sales of Orders',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Order Country': 'Country'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top 10 Countries by Sales of Orders",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Country",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Adjust axes for readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[17]:


import plotly.express as px

# Group and prepare the data
df_sales_country = df1.groupby(['Order Country'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#006d2c', '#31a354', '#74c476', '#bae4b3', '#edf8e9']  # Shades of green for a cohesive look

# Create the bar chart
fig = px.bar(
    df_sales_country.head(10),
    x='Sales of Orders',
    y='Order Country',
    color='Sales of Orders',
    color_continuous_scale=custom_colors,  # Apply custom green shades
    title='Top 10 Countries by Sales of Orders',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Order Country': 'Country'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top 10 Countries by Sales of Orders",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Country",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Adjust axes for readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[18]:


import plotly.express as px

# Group and prepare the data
df_sales_product = df1.groupby(['Product Name'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#FFA07A', '#FF6347', '#FF4500', '#FF7F50', '#FF8C00']  # Warm shades of red-orange

# Create the bar chart
fig = px.bar(
    df_sales_product.head(10),
    x='Sales of Orders',
    y='Product Name',
    color='Sales of Orders',
    color_continuous_scale=custom_colors,  # Apply the custom warm palette
    title='Top 10 Products by Sales of Orders',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Product Name': 'Product Name'
    }
)

# Update layout for polished visuals
fig.update_layout(
    title={
        'text': "Top 10 Products by Sales of Orders",
        'y': 0.95,  # Position title closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Product Name",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[19]:


import plotly.express as px

# Group and prepare the data
df_sales_pd = df1.groupby(['Product Name', 'Delivery Status'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette for delivery statuses
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']  # Matching and distinct colors

# Create the bar chart
fig = px.bar(
    df_sales_pd.head(10),
    x='Sales of Orders',
    y='Product Name',
    color='Delivery Status',
    color_discrete_sequence=custom_colors,  # Apply custom colors for delivery statuses
    title='Top 10 Products by Sales and Delivery Status',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Product Name': 'Product Name',
        'Delivery Status': 'Delivery Status'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top 10 Products by Sales and Delivery Status",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Product Name",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    ),
    legend_title="Delivery Status"  # Set a clear legend title
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[20]:


import plotly.express as px

# Group and prepare the data
df_sales_pr = df1.groupby(['Product Name', 'Order Region'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette for order regions
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']

# Create the bar chart
fig = px.bar(
    df_sales_pr.head(10),
    x='Sales of Orders',
    y='Product Name',
    color='Order Region',
    color_discrete_sequence=custom_colors,  # Apply custom colors for order regions
    title='Top 10 Products by Sales and Order Region',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Product Name': 'Product Name',
        'Order Region': 'Order Region'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top 10 Products by Sales and Order Region",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Product Name",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    ),
    legend_title="Order Region"  # Set a clear legend title
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[21]:


import plotly.express as px

# Group and prepare the data
df_sales_pr = df1.groupby(['Category Name'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#FFA07A', '#FF6347', '#FF4500', '#FF7F50', '#FF8C00']  # Warm tones for better visual appeal

# Create the bar chart
fig = px.bar(
    df_sales_pr.head(10),
    x='Sales of Orders',
    y='Category Name',
    color='Sales of Orders',
    color_continuous_scale=custom_colors,  # Apply custom warm tones
    title='Top 10 Categories by Sales of Orders',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Category Name': 'Category Name'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top 10 Categories by Sales of Orders",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Category Name",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[22]:


import plotly.express as px

# Group and prepare the data
df_sales_pr = df1.groupby(['Type'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#FF6F61', '#FFB400', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

# Create the bar chart
fig = px.bar(
    df_sales_pr.head(10),
    x='Sales of Orders',
    y='Type',
    color='Sales of Orders',
    color_continuous_scale=custom_colors,  # Apply custom colors
    title='Top Payment Types by Sales of Orders',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Type': 'Type of Payment'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top Payment Types by Sales of Orders",
        'y': 0.95,  # Position title closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Type of Payment",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[23]:


import plotly.express as px

# Group and prepare the data
df_sales_tp = df1.groupby(['Type', 'Product Name'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#FF5733', '#33FF57', '#3357FF', '#FFC300', '#DAF7A6', '#FF33A1', '#33FFF6', '#C70039', '#900C3F', '#581845']

# Create the bar chart
fig = px.bar(
    df_sales_tp.head(10),
    x='Sales of Orders',
    y='Type',
    color='Product Name',
    color_discrete_sequence=custom_colors,  # Apply custom color palette
    title='Top 10 Sales by Type and Product Name',
    labels={
        'Sales of Orders': 'Sales ($)',
        'Type': 'Type',
        'Product Name': 'Product Name'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Top 10 Sales by Type and Product Name",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Type",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    ),
    legend_title="Product Name"  # Set a clear legend title
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[24]:


import pandas as pd
import datetime as dt

# Select relevant columns and create a copy
data_orderdate = df[['order date (DateOrders)', 'Sales']].copy()

# Convert 'order date (DateOrders)' to datetime format
data_orderdate['order_date'] = pd.to_datetime(data_orderdate['order date (DateOrders)'])


# In[25]:


data_orderdate["Quarter"] = data_orderdate['order_date'].dt.quarter
data_orderdate["Month"] = data_orderdate['order_date'].dt.month
data_orderdate["year"] = data_orderdate['order_date'].dt.year


# In[26]:


import plotly.express as px

# Create a string representation of the year
data_orderdate['YearStr'] = data_orderdate['year'].astype(str)

# Group and prepare the data
df_sales_year = data_orderdate.groupby(['YearStr'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a visually appealing color palette
custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']  # A vibrant and diverse palette

# Create the bar chart
fig = px.bar(
    df_sales_year,
    x='Sales of Orders',
    y='YearStr',
    color='Sales of Orders',
    color_continuous_scale=custom_colors,  # Apply custom color palette
    title='Yearly Sales',
    labels={
        'Sales of Orders': 'Sales ($)',
        'YearStr': 'Year'
    }
)

# Update layout for a polished look
fig.update_layout(
    title={
        'text': "Yearly Sales",
        'y': 0.95,  # Position title closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Year",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    )
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[29]:


# Group and prepare the data
df_sales_quarter = data_orderdate.groupby(['YearStr', 'QuarterStr'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Create the bar chart
fig = px.bar(
    df_sales_quarter,
    x='Sales of Orders',
    y='QuarterStr',
    color='YearStr',
    color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'],
    title='Quarterly Sales by Year',
    labels={
        'Sales of Orders': 'Sales ($)',
        'QuarterStr': 'Quarter',
        'YearStr': 'Year'
    }
)

fig.show()


# In[28]:


import plotly.express as px

# Ensure 'MonthStr' and 'QuarterStr' columns exist
data_orderdate['MonthStr'] = data_orderdate['Month'].astype(str)
data_orderdate['QuarterStr'] = data_orderdate['Quarter'].astype(str)

# Group and prepare the data
df_sales_m = data_orderdate.groupby(['QuarterStr', 'MonthStr'])['Sales'].sum().reset_index(name='Sales of Orders').sort_values(by='Sales of Orders', ascending=False)

# Define a color palette for months
custom_colors = ['#FF7F50', '#87CEFA', '#32CD32', '#FFD700', '#6A5ACD', '#FF69B4', '#8B0000', '#00CED1', '#7FFF00', '#FF4500', '#2E8B57', '#9932CC']

# Create the bar chart
fig = px.bar(
    df_sales_m,
    x='Sales of Orders',
    y='QuarterStr',
    color='MonthStr',
    color_discrete_sequence=custom_colors,  # Apply custom colors for months
    title='Sales by Quarter and Month',
    labels={
        'Sales of Orders': 'Sales ($)',
        'QuarterStr': 'Quarter',
        'MonthStr': 'Month'
    }
)

# Update layout for better visuals
fig.update_layout(
    title={
        'text': "Sales by Quarter and Month",
        'y': 0.95,  # Position closer to the top
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'size': 22,
        'color': '#111111'  # Neutral dark title color
    },
    xaxis_title="Sales ($)",  # Label for x-axis
    yaxis_title="Quarter",  # Label for y-axis
    plot_bgcolor='white',  # Clean white background
    font=dict(
        family="Arial",
        size=12,
        color="#333333"  # Neutral dark font for readability
    ),
    legend_title="Month"  # Set a clear legend title
)

# Adjust y-axis for better readability
fig.update_yaxes(showgrid=True, gridcolor='lightgray', title_font=dict(size=14), tickfont=dict(size=12))

# Adjust x-axis for clarity
fig.update_xaxes(showgrid=False, title_font=dict(size=14), tickfont=dict(size=12))

# Show the chart
fig.show()


# In[30]:


data=df1.copy()
data['SUSPECTED_FRAUD'] = np.where(data['Order Status'] == 'SUSPECTED_FRAUD', 1, 0)


# In[31]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
def Labelencoder_feature(x):
    le=LabelEncoder()
    x=le.fit_transform(x)
    return x


# In[32]:


features=data.drop(columns=['SUSPECTED_FRAUD','Order Status' ])
target=data['SUSPECTED_FRAUD']


# In[33]:


features.isnull().sum()


# In[34]:


features=features.apply(Labelencoder_feature)
features.head()


# In[35]:


#deleting features which high-correlated with other features to avoid multicollinarity
data1=pd.concat([features,target],axis=1)


# In[36]:


#deleting features which high-correlated with other features to avoid multicollinarity

corr = data1.corr()
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.8:
            if columns[j]:
                columns[j] = False
selected_columns = data1.columns[columns]
selected_columns


# In[37]:


features1=features[['Type', 'Benefit per order', 'Sales per customer', 'Delivery Status', 'Late_delivery_risk', 
                    'Category Name', 'Customer City', 'Customer Country', 'Customer Id', 'Customer Segment', 
                    'Customer State', 'Customer Zipcode', 'Department Name', 'Latitude', 'Longitude', 'Market', 
                    'Order City', 'Order Country', 'order date (DateOrders)', 'Order Id', 'Order Item Cardprod Id',
                    'Order Item Discount', 'Order Item Discount Rate', 'Order Item Product Price', 'Order Item Quantity',
                    'Order Region', 'Order State', 'Order Zipcode', 'Product Description', 'Product Image', 
                    'Product Status', 'Shipping Mode', 'Customer_ID_STR']]


# In[38]:


from scipy.stats import pearsonr

corre=pd.DataFrame()

for i in features1.columns:
    corre[i]= pearsonr(target, features1[i])
    
    
corre


# In[39]:


corre1=corre.T


# In[40]:


coore2= corre1.iloc[:,0].sort_values(ascending=False)

coore2


# In[41]:


coore2.index


# In[42]:


new_features= ['Type', 'Delivery Status', 'Order Region', 'Customer Country', 'Customer State', 'Order Zipcode',
               'Shipping Mode', 'Order Country', 'Customer Zipcode', 'Order City', 'Customer Segment', 'Order State',
               'Late_delivery_risk', 'Product Description', 'Product Status']


# In[43]:


#Feature Selection

# Feature Selection based on importance
from sklearn.feature_selection import f_regression
F_values, p_values  = f_regression(features, target)


# In[44]:


import itertools
f_reg_results = [(i, v, z) for i, v, z in itertools.zip_longest(features.columns, F_values,  ['%.3f' % p for p in p_values])]
f_reg_results=pd.DataFrame(f_reg_results, columns=['Variable','F_Value', 'P_Value'])


# In[45]:


f_reg_results=pd.DataFrame(f_reg_results, columns=['Variable','F_Value', 'P_Value'])
f_reg_results = f_reg_results.sort_values(by=['P_Value'])
f_reg_results.P_Value= f_reg_results.P_Value.astype(float)
f_reg_results=f_reg_results[f_reg_results.P_Value<0.06]
f_reg_results


# In[46]:


f_reg_list=f_reg_results.Variable.values
f_reg_list


# In[47]:


#final features list is both f_ref_list and new_feature
final_features=features[['Type', 'Order Region', 'Delivery Status', 'Late_delivery_risk',
       'Customer Country', 'Order State', 'Order City',
       'Customer Segment', 'Customer State', 'Customer Zipcode',
       'Order Country', 'Order Zipcode', 'shipping date (DateOrders)',
       'Shipping Mode']]


# In[48]:


final_data=pd.concat([final_features, target], axis=1)


# In[49]:


import matplotlib.pyplot as plt
import seaborn as sns

# Create a heatmap to visualize the correlation matrix
fig = plt.figure(figsize=(20, 10))  # Adjust figure size for better readability
sns.heatmap(
    final_data.corr(),  # Correlation matrix
    annot=True,         # Show correlation coefficients
    fmt='.2f',          # Format the numbers to 2 decimal places
    cmap='magma',       # Color map for the heatmap
    linewidths=0.5,     # Add lines between cells for clarity
    linecolor='gray',   # Set line color
    cbar_kws={'shrink': 0.8, 'aspect': 30}  # Adjust the color bar
)

# Add title and labels
plt.title('Correlation Heatmap of Final Data', fontsize=16, pad=20)  # Title with padding
plt.xticks(rotation=45, fontsize=10)  # Rotate x-axis labels for better readability
plt.yticks(fontsize=10)  # Adjust y-axis label size

# Show the plot
plt.tight_layout()  # Ensure the layout fits well
plt.show()


# In[50]:


final_features2=final_features.drop(columns=['Customer State', 'Customer Zipcode'])


# In[51]:


from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import *
from sklearn import metrics
from sklearn.metrics import classification_report


# In[52]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(final_features2, target, test_size = 0.2, random_state = 42)


# In[53]:


lgr_pipline  = Pipeline([("scaler", StandardScaler()), ("LogisticRegression", LogisticRegression())])
rfc_pipline = Pipeline([("scaler", StandardScaler()), ("RandomForestClassifier", RandomForestClassifier())])
knn_pipline = Pipeline([("scaler", StandardScaler()), ("KNeighborsClassifier", KNeighborsClassifier())])
gnb_pipline = Pipeline([("scaler", StandardScaler()), ("GaussianNB", GaussianNB())])
sgd_pipline = Pipeline([("scaler", StandardScaler()), ("SGDClassifier", SGDClassifier())])
dt_pipline = Pipeline([("scaler", StandardScaler()), ("DecisionTreeClassifier", DecisionTreeClassifier())])


# In[54]:


pip_dict1 ={0:'Logistic Regression' , 1:'RandomForestClassifier' , 2: 'KNeighborsClassifier' ,
            3: 'GaussianNB', 4: 'SGDClassifier', 5: 'DecisionTreeClassifier' }


# In[55]:


piplines1=[lgr_pipline, rfc_pipline , knn_pipline, gnb_pipline  , sgd_pipline , dt_pipline ]


# In[56]:


scores_df = pd.DataFrame(columns = ["Model", "CVScores"])
for i, pipe in enumerate(piplines1):
    score = cross_val_score(pipe, final_features2, target, cv = 10)
    print(pip_dict1[i], ": ", score.mean())


# In[62]:


grid_params = [
    {"classifier": [RandomForestClassifier()],
    "classifier__n_estimators": [50,100,150,200,250,300],
    "classifier__criterion": ["gini", "entropy"],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    },   
]


# In[63]:


pipeline_new = Pipeline([("scaler", StandardScaler()), ("classifier", RandomForestClassifier())])

random_search = RandomizedSearchCV(estimator = pipeline_new, param_distributions = grid_params, scoring = 'neg_mean_absolute_error', n_jobs= -1, cv = 8, verbose = 10, random_state = 42)


# In[65]:


pipeline_rf = Pipeline([('scaler', StandardScaler()), 
                           ('Random Forest Calssifer', RandomForestClassifier(criterion='entropy', max_features='sqrt',
                        n_estimators=150))])


# In[66]:


model = pipeline_rf.fit(X_train, y_train)


# In[67]:


rf_train_predict = pd.DataFrame({'actual' : y_train,
                                 'predicted' : model.predict(X_train)})
rf_train_predict.head()


# In[68]:


rf_test_predict = pd.DataFrame({'actual' : y_test,
                                 'predicted' : model.predict(X_test)})
rf_test_predict.head()


# In[69]:


print('Accuracy Score for train dataset : ' , metrics.accuracy_score(rf_train_predict.actual, rf_train_predict.predicted))
print('Accuracy Score for test dataset : ' , metrics.accuracy_score(rf_test_predict.actual, rf_test_predict.predicted))


# In[70]:


print('ROC-AUC Score for train dataset : ' , metrics.roc_auc_score(rf_train_predict.actual, rf_train_predict.predicted))
print('ROC-AUC Score for validation dataset : ' , metrics.roc_auc_score(rf_test_predict.actual, rf_test_predict.predicted))


# In[71]:


param_distributions = {
    'n_estimators': [100, 200, 300],
    'max_features': ['sqrt', 'log2', None],  # Replace 'auto' with valid options
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}


# In[72]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# Create the Random Forest model
rf = RandomForestClassifier(random_state=42)

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_distributions,
    n_iter=10,
    cv=8,
    random_state=42,
    verbose=2,
    n_jobs=-1
)

# Fit the model
best_model = random_search.fit(X_train, y_train)


# In[73]:


print("Best Parameters:", random_search.best_params_)
print("Best Score:", random_search.best_score_)


# In[74]:


import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

# Generate the confusion matrix
conn_cm_test = metrics.confusion_matrix(rf_test_predict.actual, rf_test_predict.predicted, labels=[1, 0])

# Plot the confusion matrix as a heatmap
plt.figure(figsize=(8, 6))  # Adjust the figure size for better readability
sns.heatmap(
    conn_cm_test,
    annot=True,       # Show the values in each cell
    fmt='d',          # Use integers for confusion matrix values
    cmap='Blues',     # Set a visually appealing colormap
    xticklabels=['Predicted 1', 'Predicted 0'],  # Customize x-axis labels
    yticklabels=['Actual 1', 'Actual 0']         # Customize y-axis labels
)

# Add labels and title
plt.title('Confusion Matrix', fontsize=16)
plt.xlabel('Predicted Labels', fontsize=12)
plt.ylabel('Actual Labels', fontsize=12)

# Display the plot
plt.tight_layout()  # Adjust layout to fit elements properly
plt.show()


# In[75]:


print(metrics.classification_report(rf_test_predict.actual, rf_test_predict.predicted))


# In[76]:


features=data.drop(columns=['Late_delivery_risk'])
target=data['Late_delivery_risk']


# In[77]:


features=features.apply(Labelencoder_feature)
features.head()


# In[81]:


categorical_columns = features.select_dtypes(include=['object', 'category']).columns
for col in categorical_columns:
    print(f"{col}: {features[col].nunique()} unique values")


# In[82]:


from sklearn.preprocessing import LabelEncoder

label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    features[col] = le.fit_transform(features[col].astype(str))
    label_encoders[col] = le  # Save encoders for later decoding


# In[83]:


from sklearn.preprocessing import OneHotEncoder
from scipy.sparse import hstack

encoder = OneHotEncoder(drop='first', sparse_output=True)
sparse_encoded = encoder.fit_transform(features[categorical_columns])

# Combine sparse encoded columns with numerical columns
numerical_columns = features.select_dtypes(exclude=['object', 'category']).columns
sparse_features = hstack([sparse_encoded, features[numerical_columns].to_numpy()])


# In[84]:


import itertools
f_reg_results = [(i, v, z) for i, v, z in itertools.zip_longest(features.columns, F_values,  ['%.3f' % p for p in p_values])]
f_reg_results=pd.DataFrame(f_reg_results, columns=['Variable','F_Value', 'P_Value'])


# In[85]:


f_reg_results=pd.DataFrame(f_reg_results, columns=['Variable','F_Value', 'P_Value'])
f_reg_results = f_reg_results.sort_values(by=['P_Value'])
f_reg_results.P_Value= f_reg_results.P_Value.astype(float)
f_reg_results=f_reg_results[f_reg_results.P_Value<0.06]
f_reg_results


# In[86]:


f_reg_list=f_reg_results.Variable.values
f_reg_list


# In[87]:


df['Delivery Status'].value_counts()


# In[88]:


final_features=features[['Type', 'Shipping Mode', 'Order Region',
       'Customer City', 'shipping date (DateOrders)']]


# In[89]:


final_data=pd.concat([final_features, target], axis=1)


# In[90]:


fig = plt.figure(figsize=(20,10))
sns.heatmap(final_data.corr(), annot = True, fmt = '.2f', cmap = 'magma')


# In[91]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(final_features, target, test_size = 0.2, random_state = 42)


# In[92]:


scores_df = pd.DataFrame(columns = ["Model", "CVScores"])
for i, pipe in enumerate(piplines1):
    score = cross_val_score(pipe, final_features, target, cv = 10)
    print(pip_dict1[i], ": ", score.mean())


# In[93]:


grid_params = [
    {"classifier": [RandomForestClassifier()],
    "classifier__n_estimators": [50,100,150,200,250,300],
    "classifier__criterion": ["gini", "entropy"],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    },
    
    {"classifier": [KNeighborsClassifier()],
     "classifier__n_neighbors": [2,3,4,5,6],
     "classifier__algorithm": ['auto', 'ball_tree', 'kd_tree', 'brute'],
     "classifier__leaf_size": [10,20,30,40,50],
    
    },
    
    {"classifier": [DecisionTreeClassifier()],
    "classifier__splitter" :["best", "random"],
    "classifier__criterion": ["gini", "entropy"],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    },
    
]


# In[94]:


pipeline_new = Pipeline([("scaler", StandardScaler()), ("classifier", RandomForestClassifier())])

random_search = RandomizedSearchCV(estimator = pipeline_new, param_distributions = grid_params, scoring = 'neg_mean_absolute_error', n_jobs= -1, cv = 8, verbose = 10, random_state = 42)


# In[95]:


best_model.best_params_


# In[96]:


pipeline_rfl = Pipeline([('scaler', StandardScaler()), 
                           ('andomForestClassifier', RandomForestClassifier(criterion='entropy'))])


# In[97]:


model_rfl = pipeline_rfl.fit(X_train, y_train)


# In[98]:


rfl_train_predict = pd.DataFrame({'actual' : y_train,
                                 'predicted' : model_rfl.predict(X_train)})
rfl_train_predict.head()


# In[99]:


rfl_test_predict = pd.DataFrame({'actual' : y_test,
                                 'predicted' : model_rfl.predict(X_test)})
rfl_test_predict.head()


# In[100]:


print('Accuracy Score for train dataset : ' , metrics.accuracy_score(rfl_train_predict.actual, rfl_train_predict.predicted))
print('Accuracy Score for test dataset : ' , metrics.accuracy_score(rfl_test_predict.actual, rfl_test_predict.predicted))


# In[101]:


print('ROC-AUC Score for train dataset : ' , metrics.roc_auc_score(rfl_train_predict.actual, rfl_train_predict.predicted))
print('ROC-AUC Score for validation dataset : ' , metrics.roc_auc_score(rfl_test_predict.actual, rfl_test_predict.predicted))


# In[102]:


print(metrics.classification_report(rfl_test_predict.actual, rfl_test_predict.predicted))


# In[103]:


data_sales=df[['Type', 'Benefit per order', 'Sales per customer', 
          'Delivery Status', 'Late_delivery_risk', 'Category Name', 'Customer City', 'Customer Country', 
           'Customer Id', 'Customer Segment', 
          'Customer State', 'Customer Zipcode', 'Department Name', 'Latitude', 'Longitude',
          'Market', 'Order City', 'Order Country', 'Order Customer Id', 'order date (DateOrders)', 'Order Id', 
          'Order Item Cardprod Id', 'Order Item Discount', 'Order Item Discount Rate', 'Order Item Id', 
          'Order Item Product Price', 'Order Item Profit Ratio', 'Order Item Quantity', 'Sales', 'Order Item Total', 
          'Order Profit Per Order', 'Order Region', 'Order State', 'Order Status', 'Order Zipcode', 'Product Card Id',
          'Product Category Id', 'Product Description', 'Product Image', 'Product Name', 'Product Price', 'Product Status',
       'shipping date (DateOrders)', 'Shipping Mode']]


# In[104]:


features=data_sales.drop(columns=['Sales', 'Order Item Quantity', 'Order Item Product Price'])
target=data_sales['Sales']


# In[105]:


features=features.apply(Labelencoder_feature)
features.head()


# In[106]:


#Feature Selection based on importance
from sklearn.feature_selection import f_regression
F_values, p_values  = f_regression(features, target)


# In[107]:


import itertools
f_reg_results = [(i, v, z) for i, v, z in itertools.zip_longest(features.columns, F_values,  ['%.3f' % p for p in p_values])]
f_reg_results=pd.DataFrame(f_reg_results, columns=['Variable','F_Value', 'P_Value'])


# In[108]:


f_reg_results=pd.DataFrame(f_reg_results, columns=['Variable','F_Value', 'P_Value'])
f_reg_results = f_reg_results.sort_values(by=['P_Value'])
f_reg_results.P_Value= f_reg_results.P_Value.astype(float)
f_reg_results=f_reg_results[f_reg_results.P_Value<0.06]
f_reg_results


# In[109]:


f_reg_list=f_reg_results.Variable.values
f_reg_list


# In[110]:


final_features=features[['Order Id', 'Order Item Discount', 'Order Item Cardprod Id',
       'shipping date (DateOrders)', 'order date (DateOrders)',
       'Order Customer Id', 'Order Profit Per Order', 'Market',
       'Order Region', 'Order State', 'Order Item Total',
       'Department Name', 'Product Card Id', 'Customer Id',
       'Product Category Id', 'Product Image', 'Category Name',
       'Product Name', 'Product Price', 'Sales per customer',
       'Benefit per order', 'Order Zipcode', 'Order Item Id',
       'Order City', 'Customer Segment']]


# In[111]:


final_data=pd.concat([final_features, target], axis=1)


# In[112]:


fig = plt.figure(figsize=(20,10))
sns.heatmap(final_data.corr(), annot = True, fmt = '.2f', cmap = 'magma')


# In[113]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

from sklearn.metrics import *
from sklearn.linear_model import LinearRegression, RANSACRegressor, Lasso, Ridge, SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor


# In[114]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(final_features, target, test_size = 0.3, random_state = 42)


# In[115]:


lr_pipeline = Pipeline([("scaler", StandardScaler()), ("linear_regression", LinearRegression())])
ridge_pipeline = Pipeline([("scaler", StandardScaler()), ("ridge_regressor", Ridge(random_state = 42))])
lasso_pipeline = Pipeline([("scaler", StandardScaler()), ("lasso_regressor", Lasso(random_state = 42))])
random_forest_pipeline = Pipeline([("scaler", StandardScaler()), ("randomforest_regression", RandomForestRegressor(random_state = 42))])
xgboost_pipeline = Pipeline([("scaler", StandardScaler()), ("xgboost_regression", XGBRegressor())])
knn_pipeline = Pipeline([("scaler", StandardScaler()), ("knn_regression", KNeighborsRegressor())])


# In[116]:


pipelines = [lr_pipeline, ridge_pipeline, lasso_pipeline,
            random_forest_pipeline, xgboost_pipeline, knn_pipeline]


# In[117]:


pipe_dict = {0: "Linear Regression", 1: "Ridge",
            2: "Lasso", 3: "RandomForest", 4: "XGBoost",
            5: "Decision Tree", 6: "KNN"}


# In[118]:


scores_df = pd.DataFrame(columns = ["Model", "CVScores"])
for i, pipe in enumerate(pipelines):
    score = cross_val_score(pipe, final_features,target, cv = 5)
    print(pipe_dict[i], ": ", score.mean())


# In[119]:


grid_params = [
    
{"classifier": [XGBRegressor()],
     "classifier__n_estimators": [100,150,200,250,300],
     
}
    
]


# In[120]:


pipeline_new = Pipeline([("scaler", StandardScaler()), ("classifier", XGBRegressor())])
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


# In[121]:


random_search = RandomizedSearchCV(estimator = pipeline_new, param_distributions = grid_params, scoring = 'neg_mean_absolute_error', n_jobs= -1, cv = 8, verbose = 10, random_state = 42)


# In[122]:


best_model = random_search.fit(X_train, y_train)


# In[123]:


best_model.best_params_


# In[124]:


pipeline_XGBRegressor = Pipeline([('scaler', StandardScaler()), ('XGBRegressor',  XGBRegressor(importance_type='gain', n_estimators=300, ))])


# In[125]:


model = pipeline_XGBRegressor.fit(X_train, y_train)


# In[126]:


XGB_train_predict = pd.DataFrame({'actual' : y_train,
                                 'predicted' : model.predict(X_train)})
XGB_train_predict.head()


# In[127]:


XGB_test_predict = pd.DataFrame({'actual' : y_test,
                                 'predicted' : model.predict(X_test)})
XGB_test_predict.head()


# In[128]:


predict = model.predict(X_test)


# In[129]:


r2_score(y_test, predict, multioutput='uniform_average')


# In[130]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=y_test, y=predict, mode='markers' ,  name='predicted vs actual'))
fig.add_trace(go.Scatter(x=y_test , y=y_test, mode='lines' , name='actual'))


fig.update_layout(title='actual Sales vs predicted Sales', xaxis_title= 'Actual Score', yaxis_title = 'Predicted Score' , template= 'plotly_dark')


# In[ ]:




