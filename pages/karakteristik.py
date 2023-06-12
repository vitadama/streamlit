import streamlit as st
import pandas as pd
import numpy as np


with st.expander('pilih ukuran'):
    with st.form('pilih ukuran'):
        row1 = st.number_input('ukuran baris dari matrix pertama', min_value=2)
        col1 = st.number_input('ukuran kolom dari matrix pertama', min_value=2)
        st.form_submit_button('kirim ukuran')


if col1==row1:
    st.write('Input matrix')
    df_1 = pd.DataFrame(columns=range(1, col1+1), index=range(1, row1+1), dtype=float)
    df_1_input = st.experimental_data_editor( df_1, use_container_width=True, key=1)
    matrix1 = df_1_input.fillna(0).to_numpy()
    eigenvalue, eigenvector = np.linalg.eig(matrix1)
    eigenvalue = np.round(eigenvalue).astype(int)
    eigenvector = np.round(eigenvector).astype(int)
    karak = np.poly(matrix1)
    operasi = st.radio('pilih operasi', ['karakteristik', 'eigenvalue', 'eigenvector'])
    if operasi == 'eigenvalue':
     st.write(eigenvalue)
    if operasi == 'karakteristik':
        st.write(karak)
    if operasi == 'eigenvector':
        st.write(eigenvector)
else:
    st.markdown("<h3 style='text-align: center;'>Mohon maaf masukkan ukuran matriks persegi</h3>", unsafe_allow_html=True)
