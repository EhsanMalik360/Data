import streamlit as st
import pandas as pd
from dataprep.datasets import load_dataset
from dataprep.eda import create_report


# Load the dataset
df = pd.read_csv('mydata.csv')

# Generate the report
report = create_report(df)


# Show the Streamlit app in the browser
st.set_page_config(layout="wide")

# Create a Streamlit app
st.title("Titanic Dataset Report")

# Display the report in Streamlit
st.write("### EDA Report")
st.components.v1.html(report.show_browser(), height=600, scrolling=True)
