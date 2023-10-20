import streamlit as st
from PIL import Image

def centre_image(path):
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        image = Image.open(path)
        st.image(image)

    with col3:
        st.write("")