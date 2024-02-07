import streamlit as st
from PIL import Image

def centre_image(path, title=None):
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        if title is not None:
            st.write('**' + title + '**')
        image = Image.open(path)
        st.image(image)
        st.caption(path)

    with col3:
        st.write("")

def write_paragraphs(paras):
    for para in paras:
        st.write(para)