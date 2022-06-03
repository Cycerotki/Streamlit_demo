#importing dependencies
import streamlit as st
import pandas as pd
import numpy as np

#dummy function for documents upload
def doc_upload():
    st.write("Documents uploaded!")

#dummy function for upload
def upload():
    st.write("Uploaded info!")

#dummy function for submit
def submit_func(search_query):
    st.write(search_query)

col1,col2,col3 = st.columns(3)
#solution to centering header: https://stackoverflow.com/questions/70932538/how-to-center-the-title-and-an-image-in-streamlit
with col2:
    st.markdown("<h1 style='text-align: center; color: grey;'>Header</h1>", unsafe_allow_html=True)
#for spacing
st.columns(1)
row2_1,row2_2, row2_3, row2_4, = st.columns(4)
with row2_1:
    if st.button("Upload Documents"):
        doc_upload()
with row2_4:
    if st.button("Upload"):
        upload()
#for more spacing
st.columns(1)
st.columns(1)
st.columns(1)

#Query and submit button section
row3_1,row3_2,row3_3 = st.columns(3)
search_query = ""
with row3_2:
    search_query = st.text_input('Query', placeholder = '')
    if st.button("Submit"):
        submit_func(search_query)