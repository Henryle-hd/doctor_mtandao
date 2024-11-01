import streamlit as st
from dM import llm_response
st.write("# Doctor Mtandao🧑‍⚕️!")
# st.markdown("###### What to test?")
st.sidebar.markdown("What to test?")
st.sidebar.markdown("Upload test results")

symptoms=st.text_input(label="Enter symptom...")

if st.button("Submit"):
    if symptoms:
        result=llm_response(symptoms)
        st.write("# Doctor🩺")
        st.write(result)
        st.error("Response may be incorrect as the app is still under development and undergoing testing.")
    else:
        st.write("Please enter your symptom...")


