import os
import streamlit as st


def save_uploaded_file(directory, file):

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 저장 완료!')