import streamlit as st
import pandas as pd
import plotly.express as px

# 0. Set the page configuration title and layout
st.set_page_config(page_title='Vehicle Sales Data Analysis', layout='wide')

# --- Load the dataset ---
@st.cache_data
def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{path}' was not found. Please ensure the CSV is in the correct directory.")
        st.stop() # Stop the app if data can't be loaded

vehicles_us = load_data('notebooks/vehicles_us.csv') # This call should be here.

# --- Data Cleaning/Preparation ---
# Create 'manufacturer' column and capitalize it
if 'manufacturer' not in vehicles_us.columns:
    vehicles_us['manufacturer'] = vehicles_us['model'].str.split(' ').str[0]
    vehicles_us['manufacturer'] = vehicles_us['manufacturer'].str.capitalize()

# Create 'type_capitalized' column for box plot
if 'type_capitalized' not in vehicles_us.columns:
    vehicles_us['type_capitalized'] = vehicles_us['type'].str.capitalize()


# --- Streamlit App Layout ---

# 1. Add a header
st.title('Vehicle Sales Data Analysis')
st.markdown('A simple web application to explore vehicle listings data.')

# 2. Create a table with the first 10 non-NaN lines of the dataset
st.header('Dataset Preview (First 10 Rows)')
st.write("Here's a glimpse of the data:")
st.dataframe(vehicles_us.dropna().head(10))


# --- Functions to generate graphs  ---

def plot_fig1():
    st.subheader('Distribution of Vehicle Prices')
    fig1 = px.histogram(vehicles_us,
                        x='price',
                        nbins=100,
                        title='Distribution of Vehicle Prices')

    fig1.update_xaxes(range=[0, 100000])

    fig1.update_layout(
        title={
            'text': '<b>Distribution of Vehicle Prices</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 14} 
        },
        xaxis_title={
            'text': '<b>Price</b>',
            'font': {'size': 12}
        },
        yaxis_title={
            'text': '<b>Vehicle Count</b>',
            'font': {'size': 12}
        }
    )
    st.plotly_chart(fig1)

def plot_fig2():
    st.subheader('Distribution of Odometer Readings')
    fig2 = px.histogram(vehicles_us,
                        x='odometer',
                        nbins=100,
                        title='Distribution of Odometer Readings')

    fig2.update_xaxes(range=[0, 300000]) 

    fig2.update_layout(
        title={
            'text': '<b>Distribution of Odometer Readings</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 14}
        },
        xaxis_title={
            'text': '<b>Odometer</b>',
            'font': {'size': 12}
        },
        yaxis_title={
            'text': '<b>Vehicle Count</b>',
            'font': {'size': 12}
        }
    )
    st.plotly_chart(fig2)

def plot_fig3():
    st.subheader('Number of Vehicles by Manufacturer (Stacked by Model)')

    # Calculate counts by manufacturer and model for the stacked bar chart
    model_manufacturer_counts = vehicles_us.groupby(['manufacturer', 'model']).size().reset_index(name='Count')

    # Order manufacturers by total count for consistent sorting
    manufacturer_total_counts_ordered = vehicles_us['manufacturer'].value_counts().index.tolist()

    model_manufacturer_counts['manufacturer'] = pd.Categorical(
        model_manufacturer_counts['manufacturer'],
        categories=manufacturer_total_counts_ordered,
        ordered=True
    )

    # Sort the DataFrame for visualization
    model_manufacturer_counts = model_manufacturer_counts.sort_values(
        by=['manufacturer', 'Count'],
        ascending=[True, False]
    )

    fig3 = px.bar(model_manufacturer_counts,
                  x='Count',
                  y='manufacturer',
                  color='model',
                  labels={'manufacturer': 'Manufacturer', 'model': 'Model', 'Count': 'Number of Vehicles'},
                  title='Number of Vehicles by Manufacturer (Stacked by Model)')

    fig3.update_layout(
        title={
            'text': '<b>Number of Vehicles by Manufacturer (Stacked by Model)</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 14}
        },
        xaxis_title={
            'text': '<b>Number of Vehicles</b>',
            'font': {'size': 12}
        },
        yaxis_title={
            'text': '<b>Manufacturer</b>',
            'font': {'size': 12}
        },
        barmode='stack',
        showlegend=False, 
        yaxis={'categoryorder': 'total ascending'} 
    )
    st.plotly_chart(fig3)

def plot_fig4():
    st.subheader('Price vs. Model Year Colored by Condition')
    fig4 = px.scatter(vehicles_us,
                      x='model_year',
                      y='price',
                      color='condition',
                      title='Price vs. Model Year Colored by Condition',
                      hover_data=['model'])

    fig4.update_layout(
        title={
            'text': '<b>Price vs. Model Year Colored by Condition</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 14}
        },
        xaxis_title={
            'text': '<b>Model Year</b>',
            'font': {'size': 12}
        },
        yaxis_title={
            'text': '<b>Price</b>',
            'font': {'size': 12}
        }
    )
    st.plotly_chart(fig4)

def plot_fig5():
    st.subheader('Price Distribution by Vehicle Type')
    # Using 'type_capitalized' for the plot
    fig5 = px.box(vehicles_us,
                  x='price',
                  y='type_capitalized',
                  title='Price Distribution by Vehicle Type')

    fig5.update_xaxes(range=[0, 100000]) 

    fig5.update_layout(
        title={
            'text': '<b>Price Distribution by Vehicle Type</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 14}
        },
        xaxis_title={
            'text': '<b>Price</b>',
            'font': {'size': 12}
        },
        yaxis_title={
            'text': '<b>Vehicle Type</b>',
            'font': {'size': 12}
        }
    )
    st.plotly_chart(fig5)


# --- Graph Buttons ---
st.header('Explore Key Distributions')

if st.button('Show Price Distribution'):
    plot_fig1()
if st.button('Show Odometer Distribution'):
    plot_fig2()
if st.button('Show Manufacturer Count'):
    plot_fig3()


# --- Graph Checkboxes ---
st.header('Detailed Vehicle Insights')
# Eliminamos st.columns aquí para que los checkboxes se apilen y los gráficos tomen todo el ancho
if st.checkbox('Show Price vs. Model Year'):
    plot_fig4()
if st.checkbox('Show Price by Vehicle Type'):
    plot_fig5()

st.markdown('---')
st.markdown('App developed with Streamlit and Plotly.')