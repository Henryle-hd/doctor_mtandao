import streamlit as st
from dM import llm_response
st.write("# Doctor Mtandao!")
symptoms=st.text_input(label="Enter symptom...")

if st.button("Submit"):
    if symptoms:
        result=llm_response(symptoms)
        st.write("# Doctor")
        st.write(result)


