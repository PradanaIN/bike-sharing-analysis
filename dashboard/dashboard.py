import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Konversi kategori
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df_day['season'] = df_day['season'].map(season_mapping)

def main():
    st.title("Dashboard Analisis Peminjaman Sepeda")
    st.sidebar.title("Navigasi")
    menu = st.sidebar.radio("Pilih Analisis:", [
        "Distribusi Peminjaman", "Tren Peminjaman", "Pengaruh Musim & Cuaca",
        "Peminjaman pada Hari Kerja vs Akhir Pekan", "Pola Peminjaman per Jam", "Clustering Kategori Permintaan"])
    
    if menu == "Distribusi Peminjaman":
        st.subheader("Distribusi Jumlah Peminjaman Sepeda")
        fig, ax = plt.subplots()
        sns.histplot(df_day['cnt'], bins=30, kde=True, ax=ax)
        st.pyplot(fig)
        st.write("Jumlah peminjaman sepeda memiliki distribusi miring ke kanan, menunjukkan ada beberapa hari dengan jumlah peminjaman sangat tinggi.")
    
    elif menu == "Tren Peminjaman":
        st.subheader("Tren Peminjaman Sepeda Berdasarkan Bulan")
        fig, ax = plt.subplots()
        sns.lineplot(x='mnth', y='cnt', data=df_day, estimator='mean', marker='o', color='green', ax=ax)
        st.pyplot(fig)
        st.write("Tren peminjaman meningkat dari awal tahun, mencapai puncaknya di musim panas, dan menurun saat musim dingin.")
    
    elif menu == "Pengaruh Musim & Cuaca":
        st.subheader("Pengaruh Musim dan Cuaca terhadap Peminjaman")
        fig, ax = plt.subplots()
        sns.boxplot(x=df_day['season'], y=df_day['cnt'], ax=ax)
        st.pyplot(fig)
        st.write("Musim panas dan gugur memiliki jumlah peminjaman tertinggi, sedangkan musim dingin menunjukkan peminjaman terendah.")
    
    elif menu == "Peminjaman pada Hari Kerja vs Akhir Pekan":
        st.subheader("Perbandingan Peminjaman antara Hari Kerja dan Akhir Pekan")
        fig, ax = plt.subplots()
        sns.barplot(x=df_day['workingday'], y=df_day['cnt'], ax=ax)
        st.pyplot(fig)
        st.write("Peminjaman lebih tinggi pada hari kerja, menunjukkan banyak pengguna memanfaatkan sepeda untuk keperluan transportasi.")
    
    elif menu == "Pola Peminjaman per Jam":
        st.subheader("Pola Peminjaman Berdasarkan Jam")
        fig, ax = plt.subplots()
        sns.lineplot(x='hr', y='cnt', data=df_hour, estimator='mean', marker='o', color='red', ax=ax)
        st.pyplot(fig)
        st.write("Peminjaman sepeda memuncak di pagi dan sore hari, sejalan dengan jam kerja dan perjalanan pulang pergi kantor.")
    
    elif menu == "Clustering Kategori Permintaan":
        st.subheader("Kategori Permintaan Peminjaman Sepeda")
        df_day['demand_category'] = pd.cut(df_day['cnt'], bins=[0, 2000, 4000, df_day['cnt'].max()], labels=['Low Demand', 'Medium Demand', 'High Demand'])
        fig, ax = plt.subplots()
        sns.countplot(x=df_day['demand_category'], order=['Low Demand', 'Medium Demand', 'High Demand'], ax=ax)
        st.pyplot(fig)
        st.write("Sebagian besar hari memiliki permintaan sepeda dalam kategori Medium Demand, sedangkan High Demand terjadi lebih jarang.")
    
if __name__ == "__main__":
    main()