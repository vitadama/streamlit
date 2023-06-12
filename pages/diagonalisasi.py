import streamlit as st
import pandas as pd
import numpy as np


with st.expander('pilih ukuran'):
    with st.form('Ukuran matriks A'):
        row1 = st.number_input('ukuran baris dari matrix pertama', min_value=2)
        col1 = st.number_input('ukuran kolom dari matrix pertama', min_value=2)
        st.form_submit_button('kirim ukuran')

if col1 == row1 :
    st.write('input matrix')
    df_1 = pd.DataFrame(columns=range(1, col1+1), index=range(1, row1+1), dtype=float)
    df_1_input = st.experimental_data_editor( df_1, use_container_width=True, key=1)
    matrix1 = df_1_input.fillna(0).to_numpy()
    eigenvalue, eigenvector = np.linalg.eig(matrix1)
    diag = np.diag(eigenvalue)
    normalisasi = np.linalg.norm(eigenvector)
    Normavect = eigenvector/normalisasi
    inv_eigen = np.linalg.inv(eigenvector)
    diagonalisasi = np.matmul(np.matmul(eigenvector, diag), inv_eigen)
    operasi = st.radio('pilih operasi', ['diagonalisasi', 'P'])
    if operasi == 'P':
        st.write(eigenvector)
    if operasi == 'diagonalisasi':
        st.write(diag)
else:
    st.markdown("<h3 style='text-align: center;'>Mohon maaf masukkan ukuran matriks persegi</h3>", unsafe_allow_html=True)
           


    
