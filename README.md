# Web-Based Transportation Problem Solver
Website ini dikembangkan untuk menyelesaikan permasalahan transportasi seimbang menggunakan dua metode terbaru, yaitu Supply Slection Method (SSM) dan Karagul-Sahin Approximation Method (KSAM). Permasalahan transportasi adalah cabang riset operasi yang berutujuan untuk meminimalkan total biaya distribusi barang daru supply ke demand.

Proyek ini bertujuan untuk memberikan solusi yang efisien melalui antarmuka web berbasis Python. Dalam pengujian, metode SSM terbukti lebih optimal dibandingkan KSAM, menghasilkan Initial Basic Feasible Solution (IBFS) dengan biaya distribusi yang lebih rendah.

## ✨ Fitur Utama
* Solusi Permasalahan Transportasi Seimbang: Mengoptimalkan alokasi barang dari sumber ke tujuan.
* Dukungan Dua Metode: Implementasi SSM dan KSAM untuk perbandingan hasil.
* Validasi Data: Sistem secara otomatis memvalidasi kesimbangan antara supply dan demand.
* Antarmuka Modern: Mudah digunakan melalui antarmuka web yang responsif dan menyediakan hasil visualisasi tabel solusi.

## 💻 Persyaratan Sistem
Untuk menjalankan aplikasi ini, ada memerlukan:
- **Python**: Versi 3.8 atau lebih baru
- **Django**: Versi 4.2.16

## 🚀 Tampilan & Cara Kerja Website
1. **Halaman Utama Website**
   Pengguna dapat memilih metode yang ingin digunakan.
![Halaman Utama Website](https://github.com/MaudyDhiya/Transportation_Problem/blob/main/Images/Menu%20Program/Login%20Page.png?raw=true)

3. **Halaman Pengisian Informasi Permasalahan transportasi**

   Pengguna dapat mengisi **Title**, **Number of Source**, **Number of Destination** serta memilih **Row Names**, dan **Column Names** kemudian klik **Submit**

4. **Halaman Pengisian Data Permasalahan Transportasi**

   Pengguna dapat mengisi data permasalahan transportasi yang ingin diselesaikan. Lalu klik *Validate untuk memeriksa apakah permasalahan transportasi yang diinput sudah seimbang. Jika seimbang, akan muncul pop-up seperti ini:



   Namun, jika data yang diisi tidak seimbang, maka akan muncul pop-up seperti ini:

5. **Tampilan Data Siap untuk Di Solve**

6. **Tampilan Hasil IBFS dari Permasalahan Transportasi atau Final Solution Table**



