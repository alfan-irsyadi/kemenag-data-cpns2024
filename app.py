import streamlit as st
import pandas as pd

# Create a DataFrame from the data
df = pd.read_csv('TABEL-JABATAN.csv')

# # Display the original DataFrame
# st.write("Original Data:")
# st.dataframe(df)

search_nama = st.text_input("Search by NAMA:")
search_jabatan = st.text_input("Search by JABATAN:")

# If user inputs a search term, filter the DataFrame
filtered_df = df.copy()  # Start with the original DataFrame

if search_nama:
    filtered_df = filtered_df[filtered_df['NAMA'].str.contains(search_nama, case=False, na=False)]

if search_jabatan:
    filtered_df = filtered_df[filtered_df['JABATAN'].str.contains(search_jabatan, case=False, na=False)]

# Display the filtered DataFrame
st.write("Search Results:")
st.dataframe(filtered_df)