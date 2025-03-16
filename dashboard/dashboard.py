import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Konversi tanggal ke format datetime
df_day["dteday"] = pd.to_datetime(df_day["dteday"])

# Mapping musim dan cuaca
musim_map = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
df_day["season"] = df_day["season"].map(musim_map)

cuaca_map = {1: "Cerah", 2: "Berawan", 3: "Hujan Ringan/Salju", 4: "Hujan Lebat/Salju"}
df_day["weathersit"] = df_day["weathersit"].map(cuaca_map)

# Sidebar untuk navigasi
st.sidebar.title("📊 Dashboard Bike Sharing")
menu = st.sidebar.radio("Navigasi", ["🏠 Home", "📊 Analisis & Visualisasi", "📌 Kesimpulan"])

# Filter data interaktif
st.sidebar.header("🔎 Filter Data")

# Rentang tanggal
start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal", 
    [df_day["dteday"].min().date(), df_day["dteday"].max().date()]
)
df_filtered = df_day[
    (df_day["dteday"] >= pd.to_datetime(start_date)) & 
    (df_day["dteday"] <= pd.to_datetime(end_date))
]

# Filter musim
selected_season = st.sidebar.selectbox("Pilih Musim", ["Semua"] + list(df_day["season"].unique()))
if selected_season != "Semua":
    df_filtered = df_filtered[df_filtered["season"] == selected_season]

# Filter kondisi cuaca
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca", ["Semua"] + list(df_day["weathersit"].unique()))
if selected_weather != "Semua":
    df_filtered = df_filtered[df_filtered["weathersit"] == selected_weather]

# === HALAMAN HOME ===
if menu == "🏠 Home":
    st.title("🚲 Bike Sharing Dashboard")
    st.write("Selamat datang di dashboard interaktif Bike Sharing! Gunakan menu di sidebar untuk menjelajahi data peminjaman sepeda.")

    st.subheader("🔹 Data Awal")
    st.dataframe(df_filtered.head())

    st.subheader("📊 Statistik Singkat")
    col1, col2, col3 = st.columns(3)
    if not df_filtered.empty:
        max_day = str(df_filtered.loc[df_filtered["cnt"].idxmax(), "dteday"].date())
        total_rental = df_filtered["cnt"].sum()
        avg_rental = df_filtered["cnt"].mean()
    else:
        max_day = "Tidak ada data"
        total_rental = 0
        avg_rental = 0

    col1.metric("Total Peminjaman", total_rental)
    col2.metric("Rata-rata Peminjaman", avg_rental)
    col3.metric("Hari dengan Peminjaman Tertinggi", max_day)

# === HALAMAN ANALISIS & VISUALISASI ===
elif menu == "📊 Analisis & Visualisasi":
    st.title("📊 Analisis dan Visualisasi Data Bike Sharing")
    
    st.subheader("1️⃣ Distribusi Jumlah Peminjaman")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df_filtered["cnt"], bins=30, kde=True, color="blue", ax=ax)
    plt.xlabel("Jumlah Peminjaman")
    plt.ylabel("Frekuensi")
    plt.title("Distribusi Peminjaman Sepeda")
    st.pyplot(fig)
    st.write("📌 Mayoritas peminjaman sepeda berkisar antara **500 hingga 5000 per hari**.")
    
    st.subheader("2️⃣ Tren Peminjaman Berdasarkan Musim & Bulan")
    df_season = df_filtered.groupby(["season"])["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df_season, x="season", y="cnt", palette="coolwarm", ax=ax)
    plt.xlabel("Musim")
    plt.ylabel("Rata-rata Peminjaman")
    plt.title("Tren Peminjaman Sepeda Berdasarkan Musim")
    st.pyplot(fig)
    st.write("📌 **Musim panas** memiliki peminjaman tertinggi, sementara **musim dingin** memiliki peminjaman terendah.")
    
    st.subheader("3️⃣ Pola Peminjaman Berdasarkan Cuaca")
    df_weather = df_filtered.groupby(["weathersit"])["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df_weather, x="weathersit", y="cnt", palette="viridis", ax=ax)
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Rata-rata Peminjaman")
    plt.title("Peminjaman Sepeda Berdasarkan Cuaca")
    st.pyplot(fig)
    st.write("📌 Peminjaman sepeda lebih banyak saat **cuaca cerah**, dan menurun saat hujan atau salju.")

    st.subheader("4️⃣ Pola Peminjaman Berdasarkan Jam")
    df_hour_grouped = df_hour.groupby("hr")["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=df_hour_grouped, x="hr", y="cnt", marker="o", ax=ax)
    plt.xlabel("Jam")
    plt.ylabel("Rata-rata Peminjaman")
    plt.title("Pola Peminjaman Sepeda Berdasarkan Jam")
    st.pyplot(fig)
    st.write("📌 **Puncak peminjaman terjadi pada pagi (07:00 - 09:00) dan sore (17:00 - 19:00).**")

# === HALAMAN KESIMPULAN ===
elif menu == "📌 Kesimpulan":
    st.title("📌 Kesimpulan")
    st.write("- **Peminjaman lebih tinggi saat cuaca cerah dan musim panas.**")
    st.write("- **Hari kerja memiliki peminjaman lebih tinggi dibanding akhir pekan.**")
    st.write("- **Jam sibuk terjadi pada pagi dan sore hari.**")
    st.title("📌 Rekomendasi")
    st.write("📌 Tambahkan sepeda pada jam sibuk dan perbaiki layanan di musim dingin.")
