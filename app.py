
import streamlit as st

def main():
    st.title("🔮 DataDazzler: Your Automated EDA and Model Builder 🔮")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Upload Data", "Preprocessing", "Modeling", "Download Model"))

    if page == "Upload Data":
        upload_data_page()
    elif page == "Preprocessing":
        preprocessing_page()
    elif page == "Modeling":
        modeling_page()
    elif page == "Download Model":
        download_model_page()

def upload_data_page():
    st.header("Upload Data")
    st.write("This is the page where users can upload their dataset.")

def preprocessing_page():
    st.header("Preprocessing")
    st.write("This is the page where users can preprocess their data.")

def modeling_page():
    st.header("Modeling")
    st.write("This is the page where users can select their target variable and input features, and train multiple models.")

def download_model_page():
    st.header("Download Model")
    st.write("This is the page where users can download the best model.")

if __name__ == "__main__":
    main()
