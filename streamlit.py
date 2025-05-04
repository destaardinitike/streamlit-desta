import streamlit as st
import numpy as np
import pandas as pd
import requests

#Menambahkan judul
st.title("Aplikasi Dasar dengan Streamlit")
st.title("Aplikasi Dasar dengan Streamlit")

#Menambahkan Penjelasan
st.write("Ini adalah aplikasi pertama yang menggunakan Streamlit")

data = {
    'Nama': ['Desta', 'Dika', 'Dilla', 'Pinkan', 'Citra'],
    'Usia': [19, 23, 24, 17, 19],
    'KOta': ['Malili', 'Balantang', 'Wotu', 'Toraja', 'Morowali']
}
df = pd.DataFrame(data)
st.write(df)

#3.1 Elemen Text
st.title("Halo, Selamat Datang di Streamlit!")
st.header("Bagian 2: Daftar Isi")
st.subheader("Subbagian 1: Data Pengguna")
st.caption("Bersyukur atas apa yang ada")
st.code("import pandas as pd")
st.text("Ini adalah teks biasa tanpa format atau penekanan")
st.latex("l = s x s")
st.markdown('**Teks Tebal** dan _Teks Miring_ serta [Tautan](https://streamlit.io)')
st.divider()

#Menampilkan Data dengan API
import streamlit as st
import requests
import pandas as pd

st.title('Data dari API')

url = 'https://jsonplaceholder.typicode.com/users' # API contoh
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
    print(data)
else:
    st.error('Gagal mengambil data dari API')

uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.write("Tidak ada file yang diunggah.")

# Data sederhana
data = {
    'Nama': ['Mustia', 'Tike', 'Delfi'],
    'Umur': [40, 50, 15],
    'Kota': ['Malili', 'Maros', 'Lampia']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write("Tabel Data:")
st.write(df)

# Membuat DataFrame random
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=(f'col {i+1}' for i in range(5))
)

# Menampilkan DataFrame di Streamlit
st.dataframe(df)

#File Metric
import streamlit as st

colom1, colom2, colom3 = st.columns(3)

with colom1:
    st.metric(label="Omset", value="Rp 200 Juta", delta="+5%")

with colom2:
    st.metric(label="User Aktif", value="1.250", delta="+2%")

with colom3:
    st.metric(label="Refund", value="15", delta="-1%")

colom1, colom2 = st.columns(2)

#Line Chart
import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)
st.bar_chart(data)

#Altair Chart
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)
st.map()

#Contoh Mini Semua Input
import streamlit as st

with st.form("form_input"):
    nama = st.text_input("Nama")
    alamat = st.text_area("Alamat")
    usia = st.number_input("Usia", min_value=0)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_janji = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Membaca", "Olahraga", "Musik", "Traveling"])
    warna_favorit = st.color_picker("Pilih warna favorit")
    file_foto = st.file_uploader("Upload Foto")
    foto_kamera = st.camera_input("Ambil Foto dari Kamera")
    rating = st.slider("Rating Kepuasan", 1, 10)

    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data {nama} berhasil dikirim! 🎉")

import streamlit as st
from PIL import Image

import streamlit as st

# Menampilkan video dari file lokal
#st.video()

# Menampilkan video dari URL (misalnya YouTube)
st.video('https://youtu.be/WQ93gQCkQ48?si=3KrGZ4vEcoDja6ED')

import streamlit as st

# Menampilkan audio dari URL
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

import streamlit as st

# Upload file
uploaded_file = st.file_uploader("Pilih file PDF atau CSV", type=['pdf', 'csv'])

if uploaded_file is not None:
    st.write("File berhasil di-upload:")
    st.write(uploaded_file.name)
    st.download_button("Unduh file", uploaded_file)

import streamlit as st

# Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom 1")
    st.write("Ini adalah konten di kolom pertama.")
    st.button("Tombol Kolom 1")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom 2")
    st.write("Ini adalah konten di kolom kedua.")
    st.button("Tombol Kolom 2")

import streamlit as st

with st.expander("Klik untuk melihat lebih banyak"):
    st.write("Ini adalah konten tersembunyi yang bisa dilihat saat pengguna klik expander.")
    st.image("https://via.placeholder.com/150", caption="Contoh Gambar")

import streamlit as st

# Menambahkan elemen ke Sidebar
st.sidebar.header("Ini Sidebar")
st.sidebar.radio("Pilih Opsi", ["Opsi 1", "Opsi 2", "Opsi 3"])

# Konten utama
st.title("Konten Utama")
st.write("Ini adalah konten utama yang ditampilkan di layar.")