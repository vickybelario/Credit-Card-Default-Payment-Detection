<center>

<img width="782" alt="Screenshot 2024-10-17 at 20 58 39" src="https://github.com/user-attachments/assets/bd3742d0-4727-44c2-b79d-825e85fe20c6">

</center>

# Work In Progress
# Credit Card Default Payment Detection 


---
## 1. Introduction
 Nama  : Vicky Belario

project ini dilakukan untuk mengaplikasikan model classification pada dataset credit_card_default

## Goal
memprediksi default_payment_next_month menggunakan model Classification terutama Logistic Regression, SVM, dan KNN dari dataset credit_card_default

---

## Dataset

| **Nama Kolom**                  | **Tipe Data** | **Deskripsi**                                                                                                                        |
| -------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| id                               | Float         | ID anonim dari setiap klien                                                                                                           |
| limit_balance                    | Float         | Jumlah kredit yang diberikan dalam dolar NT (termasuk kredit individu dan keluarga/suplemen)                                         |
| sex                              | String        | Jenis kelamin (1=pria, 2=wanita)                                                                                                      |
| education_level                  | String        | Tingkat pendidikan (1=pasca sarjana, 2=universitas, 3=sekolah menengah, 4=lainnya, 5=tidak diketahui, 6=tidak diketahui)             |
| marital_status                   | String        | Status pernikahan (1=menikah, 2=belum menikah, 3=lainnya)                                                                           |
| age                              | Float         | Usia dalam tahun                                                                                                                     |
| pay_0                            | Float         | Status pembayaran pada September 2005 (-1=pembayaran tepat waktu, 1=terlambat satu bulan, 2=terlambat dua bulan, ... 8=terlambat delapan bulan, 9=terlambat sembilan bulan atau lebih) |
| pay_2                            | Float         | Status pembayaran pada Agustus 2005 (skala sama seperti di atas)                                                                      |
| pay_3                            | Float         | Status pembayaran pada Juli 2005 (skala sama seperti di atas)                                                                        |
| pay_4                            | Float         | Status pembayaran pada Juni 2005 (skala sama seperti di atas)                                                                        |
| pay_5                            | String        | Status pembayaran pada Mei 2005 (skala sama seperti di atas)                                                                         |
| pay_6                            | String        | Status pembayaran pada April 2005 (skala sama seperti di atas)                                                                       |
| bill_amt_1                       | Float         | Jumlah tagihan pada September 2005 (dolar NT)                                                                                       |
| bill_amt_2                       | Float         | Jumlah tagihan pada Agustus 2005 (dolar NT)                                                                                         |
| bill_amt_3                       | Float         | Jumlah tagihan pada Juli 2005 (dolar NT)                                                                                            |
| bill_amt_4                       | Float         | Jumlah tagihan pada Juni 2005 (dolar NT)                                                                                           |
| bill_amt_5                       | Float         | Jumlah tagihan pada Mei 2005 (dolar NT)                                                                                             |
| bill_amt_6                       | Float         | Jumlah tagihan pada April 2005 (dolar NT)                                                                                           |
| pay_amt_1                        | Float         | Jumlah pembayaran sebelumnya pada September 2005 (dolar NT)                                                                          |
| pay_amt_2                        | Float         | Jumlah pembayaran sebelumnya pada Agustus 2005 (dolar NT)                                                                           |
| pay_amt_3                        | Float         | Jumlah pembayaran sebelumnya pada Juli 2005 (dolar NT)                                                                             |
| pay_amt_4                        | Float         | Jumlah pembayaran sebelumnya pada Juni 2005 (dolar NT)                                                                             |
| pay_amt_5                        | Float         | Jumlah pembayaran sebelumnya pada Mei 2005 (dolar NT)                                                                              |
| pay_amt_6                        | Float         | Jumlah pembayaran sebelumnya pada April 2005 (dolar NT)                                                                            |
| default_payment_next_month       | String        | Pembayaran macet (1=ya, 0=tidak)                                                                                                    |
| predicted_default_payment_next_month | Record   | Prediksi pembayaran macet bulan depan                                                                                                 |

## penjelasan isi konten sebagai berikut :

   1. Import Libraries
      > _Cell_ pertama pada _notebook_ **harus berisi dan hanya berisi** semua _library_ yang digunakan dalam _project_.

   2. Query SQL
      > Tulis query yang telah dibuat untuk mengambil data dari Google Cloud Platform di bagian ini.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

   9. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   10. Model Saving
       > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. **Dengan melihat hasil Model Evaluation, pilihlah satu model terbaik untuk disimpan. Model terbaik ini akan digunakan kembali dalam melakukan Model Inference dan Model Deployment.**
   
   11. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled. Gunakan model terbaik berdasarkan hasil Model Evaluation.


# Kesimpulan 

Berdasarkan analisis dari ketiga model yang telah dilakukan (Logistic Regression, K-Nearest Neighbors, dan SVM) dengan menggunakan metrik recall sebagai fokus utama untuk evaluasi model pada dataset yang tidak seimbang (imbalanced dataset),

dari 3 model model logistic yang paling rendah recall nya dengan svm dan knn memiliki recall yang sama
fokus utama untuk evaluasi menggunakan model svm karena dataset memiliki distribusi skew dengan outlier yang banyak dan tinggi

Tuning hyperparameter telah terbukti efektif dalam meningkatkan kinerja model svm dalam  memprediksi default pembayaran bulan depan.
hasil terutama terlihat dalam recall untuk kelas positif 1,  dalam mengidentifikasi pelanggan yang berisiko gagal bayar.
