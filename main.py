import streamlit as st
from dM import llm_response

st.set_page_config(
    page_title="Doctor Mtandao",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

logo_url = "./home_health_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png"
st.image(logo_url, width=100)
st.title("Doctor Mtandao🧑‍⚕️")

# st.sidebar.markdown("What to test?")
# st.sidebar.markdown("Upload test results")

symptoms=st.text_area(label="🏥🏠🩺",placeholder="Enter symptom (e.g. I feel tired, and I have a slight fever and congestion., etc.)")

if st.button("Send to doctor"):
    if symptoms:
        result=llm_response(symptoms)
        st.write("# Doctor🩺")
        st.write(result.strip())
        st.error("Response may be incorrect as the app is still under development and undergoing testing.")
    else:
        st.write("Please enter your symptom...")



