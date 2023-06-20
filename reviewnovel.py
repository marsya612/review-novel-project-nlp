import subprocess
import sys

# Fungsi untuk menginstal library menggunakan pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Menginstal library transformers
try:
    import transformers
except ImportError:
    print("Library transformers tidak ditemukan. Menginstal...")
    install_package("transformers")

# Setelah instalasi selesai, import library transformers
import transformers

import subprocess
import sys

# Fungsi untuk menginstal library menggunakan pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Menginstal library streamlit
try:
    import streamlit
except ImportError:
    print("Library streamlit tidak ditemukan. Menginstal...")
    install_package("streamlit")

# Setelah instalasi selesai, import library streamlit
import streamlit as st

import pandas as pd
import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
model = pipeline('sentiment-analysis')

# Baca dataset
df = pd.read_csv('reviewnovel.csv')

# Fungsi untuk menganalisis sentimen pada teks
def analyze_sentiment(text):
    result = model(text)[0]
    return result['label'], result['score']

# Menampilkan hasil analisis sentimen dan penghighlightan
st.title('Sentiment Analysis on Book Reviews')
input_text = st.text_input('Masukkan kalimat:')
if input_text:
    sentiment, score = analyze_sentiment(input_text)
    highlighted_text = ' '.join([f'<mark>{word}</mark>' if word.lower() in input_text.lower() else word for word in input_text.split()])
    st.markdown(f'Hasil Sentimen: {sentiment} ({score:.2f})')
    st.markdown(f'Kalimat dengan Highlight: {highlighted_text}')
