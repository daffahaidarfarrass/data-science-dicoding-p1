import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
import pandas as pd

def daily_rent(df):
    daily_rent_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum"
    })

    daily_rent_df = daily_rent_df.reset_index()

    daily_rent_df.rename(columns={
        "cnt": "total_bike_rentals"
    }, inplace=True)

    return daily_rent_df

# Fungsi untuk menghitung total pengguna terdaftar per hari
def daily_user_register(df):
    daily_users_df = df.resample(rule='D', on='dteday').agg({
        "registered": "sum"  # Menghitung total pengguna terdaftar
    })
    
    daily_users_df = daily_users_df.reset_index()
    
    daily_users_df.rename(columns={
        "registered": "total_user_registered"
    }, inplace=True)
    
    return daily_users_df

# Load dataset
day = pd.read_csv('Bike-sharing-dataset/day.csv')
hour = pd.read_csv('Bike-sharing-dataset/hour.csv')

# Konversi kolom tanggal menjadi datetime
day["dteday"] = pd.to_datetime(day["dteday"])

# Dapatkan tanggal minimum dan maksimum untuk rentang tanggal
min_date = day["dteday"].min()
max_date = day["dteday"].max()

# Menghitung satu bulan ke belakang dari max_date
one_month_ago = max_date - pd.DateOffset(months=1)

# Sidebar input untuk memilih rentang waktu
with st.sidebar:
    st.image("https://www.zarla.com/images/zarla-ngegowes-1x1-2400x2400-20211104-q8cqhby8frtyhtkjtkdq.png?crop=1:1,smart&width=250&dpr=2")

    # Input rentang waktu
    start_date, end_date = st.date_input(
        label='Rentang Waktu', 
        min_value=min_date,
        max_value=max_date,
        value=[one_month_ago, max_date]  # Default ke satu bulan ke belakang
    )
    
    # Filter dataframe berdasarkan rentang tanggal
    main_df = day[(day["dteday"] >= pd.to_datetime(start_date)) & 
                     (day["dteday"] <= pd.to_datetime(end_date))]

    # Menghitung total penyewaan sepeda dan total pengguna terdaftar
    daily_rent_df = daily_rent(main_df)
    daily_users_df = daily_user_register(main_df)

# Tampilkan data
st.subheader("Customer Demographics")

# Layout untuk menampilkan informasi
col1, col2 = st.columns(2)

# Kolom 1 - Total Penyewaan Sepeda
with col1:
    total_rents = daily_rent_df["total_bike_rentals"].sum()
    st.metric("Total Bike Rentals", value=f'{total_rents:,}')
    
    
    # Plot total penyewaan sepeda per hari
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        daily_rent_df["dteday"],
        daily_rent_df["total_bike_rentals"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.set_title('Daily Bike Rentals', fontsize=20)
    ax.set_xlabel('Date', fontsize=15)
    ax.set_ylabel('Total Rentals', fontsize=15)
    ax.tick_params(axis='y', labelsize=12)
    ax.tick_params(axis='x', labelsize=12)
    
    st.pyplot(fig)

# Kolom 2 - Total Pengguna Terdaftar
with col2:
    total_users = daily_users_df["total_user_registered"].sum()
    st.metric("Total User Registered", value=f'{total_users:,}')

    
    
    # Plot total pengguna terdaftar per hari
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        daily_users_df["dteday"],
        daily_users_df["total_user_registered"],
        marker='o',
        linewidth=2,
        color="#FFA726"
    )
    ax.set_title('Daily Registered Users', fontsize=20)
    ax.set_xlabel('Date', fontsize=15)
    ax.set_ylabel('Total Registered Users', fontsize=15)
    ax.tick_params(axis='y', labelsize=12)
    ax.tick_params(axis='x', labelsize=12)
    
    st.pyplot(fig)



st.subheader("Amount Bike Rentals per Season")


# Map angka season ke nama musim
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day['season_label'] = day['season'].map(season_map)

# Konversi kolom 'dteday' ke tipe datetime
day['dteday'] = pd.to_datetime(day['dteday'])

# Hitung rata-rata penyewaan sepeda per musim untuk setiap tahun
season_trend = day.groupby(['season_label', 'yr']).agg({'cnt': 'sum'}).reset_index()

season_trend['yr'] = season_trend['yr'].replace({0: 2011, 1: 2012})

# Plot tren musiman
plt.figure(figsize=(10, 6))
custom_palette = ['#1f77b4', '#ff7f0e']
sns.barplot(x='season_label', y='cnt', hue='yr', data=season_trend, palette=custom_palette)
plt.title('Amount Bike Rentals per Season (2011 vs 2012)')
plt.ylabel('Amount Rental Count')
plt.xlabel('Season')
plt.legend(title='Year')
plt.grid(True)

# Tampilkan grafik di Streamlit
st.pyplot(plt)



st.subheader("Amount Bike Rentals per Hour")
# Hitung jumlah penyewaan sepeda per jam untuk setiap tahun
hour_trend = hour.groupby(['hr', 'yr']).agg({'cnt': 'sum'}).reset_index()

# Mengganti nilai tahun dengan 2011 dan 2012
hour_trend['yr'] = hour_trend['yr'].replace({0: 2011, 1: 2012})

# Plot tren penyewaan sepeda per jam
plt.figure(figsize=(12, 6))
custom_palette = ['#1f77b4', '#ff7f0e']
sns.barplot(x='hr', y='cnt', hue='yr', data=hour_trend, palette=custom_palette)
plt.title('Amount Bike Rentals per Hour (2011 vs 2012)')
plt.ylabel('Amount Rental Count')
plt.xlabel('Hour of the Day')

# sumbu X agar hanya menampilkan jam
plt.xticks(ticks=range(0, 24), labels=[f"{i}:00" for i in range(24)], rotation=45)  # Format jam
plt.xlim(-0.5, 23.5)  # Mengatur batas sumbu x untuk menampung semua jam
plt.legend(title='Year')
plt.grid(True)
st.pyplot(plt)





