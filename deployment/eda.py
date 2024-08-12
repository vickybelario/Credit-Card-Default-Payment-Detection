import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def fetch_data():
    df = pd.read_csv("P1G5_Set_1_vicky_belario.csv")
    return df

df = fetch_data()
st.write(df)

# Judul aplikasi
st.title('Exploratory Data Analysis')

# Plot histogram distribusi harga menggunakan seaborn
st.subheader('Distribusi Default Payment Next Month')
fig, ax = plt.subplots()
sns.histplot(df['default_payment_next_month'], bins=20, kde=True, ax=ax)
ax.set_title('Distribusi Default Payment Next Month')
ax.set_xlabel('Default Payment Next Month')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Membuat subplot dengan satu kolom dan ukuran gambar
st.subheader('Boxplot Default Payment Next Month')
fig, ax = plt.subplots(ncols=1, figsize=(6, 4))

# Membuat boxplot untuk harga
sns.boxplot(y=df['default_payment_next_month'], ax=ax)
ax.set_title('Boxplot Default Payment Next Month')
ax.set_ylabel('Default Payment Next Month')

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Hitung harga rata-rata untuk setiap nama berdasarkan age
average_price_by_age = df.groupby('age')['default_payment_next_month'].mean().sort_values()

# Plotting
st.subheader('Rata-rata Default Payment Next Month berdasarkan Age')
fig, ax = plt.subplots(figsize=(12, 6))
average_price_by_age.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Rata-rata Default Payment by Age')
ax.set_xlabel('Age')
ax.set_ylabel('Rata-rata Default Payment Next Month')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Putar label x untuk keterbacaan yang lebih baik
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Hitung harga rata-rata untuk setiap nama berdasarkan education_level
average_price_by_education = df.groupby('education_level')['default_payment_next_month'].mean().sort_values()

# Plotting
st.subheader('Rata-rata Default Payment Next Month berdasarkan Education Level')
fig, ax = plt.subplots(figsize=(12, 6))
average_price_by_education.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Rata-rata Default Payment by Education Level')
ax.set_xlabel('Education Level')
ax.set_ylabel('Rata-rata Default Payment Next Month')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Putar label x untuk keterbacaan yang lebih baik
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Hitung harga rata-rata untuk setiap nama berdasarkan marital_status
average_price_by_marital_status = df.groupby('marital_status')['default_payment_next_month'].mean().sort_values()

# Plotting
st.subheader('Rata-rata Default Payment Next Month berdasarkan Marital Status')
fig, ax = plt.subplots(figsize=(12, 6))
average_price_by_marital_status.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Rata-rata Default Payment by Marital Status')
ax.set_xlabel('Marital Status')
ax.set_ylabel('Rata-rata Default Payment Next Month')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Putar label x untuk keterbacaan yang lebih baik
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Hitung harga rata-rata untuk setiap nama berdasarkan sex
average_price_by_pay_0 = df.groupby('sex')['default_payment_next_month'].mean().sort_values()

# Plotting
st.subheader('Rata-rata Payment Next Month berdasarkan sex')
fig, ax = plt.subplots(figsize=(12, 6))
average_price_by_pay_0.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Rata-rata Default Payment by sex')
ax.set_xlabel('sex')
ax.set_ylabel('Default Rata-rata Payment Next Month')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Putar label x untuk keterbacaan yang lebih baik
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)