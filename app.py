import streamlit as st
import pandas as pd

# Create a DataFrame from the data
df = pd.read_csv('TABEL-JABATAN.csv')

# # Display the original DataFrame
# st.write("Original Data:")
# st.dataframe(df)

# Input box to search by NAMA
search_term = st.text_input("Search by NAMA:")

# If the user inputs a search term, filter the DataFrame
if search_term:
    filtered_df = df[df['NAMA'].str.contains(search_term, case=False, na=False)]
    
    # Display the filtered DataFrame
    st.write("Search Results:")
    st.dataframe(filtered_df)
