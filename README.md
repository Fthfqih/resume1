# Studi Kasus: Make Sense of Data with Analysis and AI

Repositori ini berisi studi kasus dan implementasi praktis berdasarkan materi **"Make Sense of Data with Analysis and AI"** yang disampaikan oleh **Bapak Andria Arisal, S.T., M.N.** (Peneliti Pusat Riset Sains Data dan Informasi - BRIN) dalam kegiatan *Informatics Practitioner Lecture Series* Universitas Bengkulu.

---

## 📌 Ringkasan Materi & Teori
Dalam dunia nyata, data mentah dari sistem perusahaan (seperti ERP atau basis data transaksional) sering kali berantakan (*messy*), tidak seimbang (*imbalanced*), dan memiliki berbagai anomali bisnis. Proses pengolahan data harus melalui tahapan terstruktur menggunakan kerangka **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*):
1. **Business Understanding**: Menerjemahkan pertanyaan bisnis pimpinan perusahaan menjadi pertanyaan analitik.
2. **Data Understanding & Preparation**: Memahami granularitas data (tingkat detail per baris, misal per item produk, per invoice, per customer), menangani *missing value*, dan membersihkan anomali.
3. **Modeling & Analysis**: Menerapkan 4 level analitik:
   - *Descriptive*: Apa yang terjadi? (Contoh: Total *sales revenue* naik, tapi *net profit* turun).
   - *Diagnostic*: Mengapa hal itu terjadi? (Contoh: Lonjakan piutang/*receivables* dan kenaikan *operating expense*).
   - *Predictive*: Apa yang akan terjadi? (Contoh: Memprediksi invoice mana yang berpotensi *late payment*).
   - *Prescriptive*: Apa tindakan terbaik yang harus diambil? (Rekomendasi kebijakan bisnis).
4. **Evaluation & AI Integration**: Mengevaluasi performa model machine learning dan memanfaatkan Generative AI sebagai *assistant* dengan tetap menjunjung prinsip *Human-in-the-Loop* (keputusan akhir tetap di tangan manusia).

---

## 🛠️ Studi Kasus: Prediksi Keterlambatan Pembayaran (*Late Payment*) PT Maju Bersama

Studi kasus ini mensimulasikan data distribusi penjualan dan status pembayaran tagihan (*invoice*) dari PT Maju Bersama untuk menganalisis risiko keterlambatan pembayaran oleh pelanggan.

### Dataset (`dataset_maju_bersama.csv`)
Berisi data transaksi dengan fitur-fitur utama:
- `invoice_id`: ID unik tagihan.
- `customer_id`: ID pelanggan.
- `total_amount`: Nilai nominal transaksi.
- `payment_method`: Metode pembayaran yang digunakan.
- `days_to_due`: Batas waktu jatuh tempo.
- `late_payment`: Target variabel (0 = Tepat Waktu, 1 = Terlambat / *Late*).

---

## 🚀 Cara Menjalankan Implementasi (Python)

1. **Clone repository ini atau ekstrak file ZIP.**
2. Pastikan Python sudah terinstal di komputer Anda.
3. Install dependencies yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan script analisis dan pemodelan machine learning:
   ```bash
   python analysis_script.py
   ```

---

## 📂 Penjelasan Script (`analysis_script.py`)
Script ini melakukan simulasi:
- **Data Loading & Cleaning**: Memuat dataset dan membersihkan inkonsistensi data.
- **Descriptive & Diagnostic Check**: Menghitung ringkasan statistik pendapatan dan rasio piutang.
- **Predictive Modeling**: Melatih model *Logistic Regression* & *Random Forest* untuk memprediksi potensi *late payment* dengan menghindari *data leakage* (kebocoran fitur masa depan).
- **Evaluation**: Menampilkan metrik akurasi dan *classification report*.
