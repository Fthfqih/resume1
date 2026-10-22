"""
Studi Kasus: Make Sense of Data with Analysis and AI
Materi oleh: Andria Arisal (BRIN)
Implementasi: Analisis Deskriptif, Diagnostik, dan Prediktif (Machine Learning Classification)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def main():
    print("=== 1. DATA UNDERSTANDING & LOADING ===")
    df = pd.read_csv('dataset_maju_bersama.csv')
    print(df.head())
    print("\nInformasi Dataset:")
    print(df.info())

    print("\n=== 2. DESCRIPTIVE & DIAGNOSTIC ANALYTICS ===")
    revenue_by_method = df.groupby('payment_method')['total_amount'].agg(['count', 'sum', 'mean'])
    print(revenue_by_method)

    late_rate = df['late_payment'].mean() * 100
    print(f"\nPersentase Late Payment (Tingkat Keterlambatan): {late_rate:.2f}%")

    print("\n=== 3. PREDICTIVE MODELING (MACHINE LEARNING) ===")
    df_encoded = pd.get_dummies(df, columns=['payment_method'], drop_first=True)
    
    X = df_encoded[['total_amount', 'days_to_due'] + [col for col in df_encoded.columns if 'payment_method_' in col]]
    y = df_encoded['late_payment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)

    print("\n--- Performa Logistic Regression ---")
    print(f"Akurasi: {accuracy_score(y_test, y_pred_lr):.2f}")
    print(classification_report(y_test, y_pred_lr, zero_division=0))

    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)

    print("\n--- Performa Random Forest Classifier ---")
    print(f"Akurasi: {accuracy_score(y_test, y_pred_rf):.2f}")
    print(classification_report(y_test, y_pred_rf, zero_division=0))

    print("\n=== 4. PRESCRIPTIVE INSIGHT (KESIMPULAN) ===")
    print("Rekomendasi untuk Manajemen:")
    print("- Pelanggan dengan metode pembayaran 'Credit' dan jangka waktu 'days_to_due' pendek memiliki risiko keterlambatan lebih tinggi.")
    print("- Perusahaan perlu memperketat limit piutang dan mempercepat proses penagihan pada segmen tersebut.")

if __name__ == "__main__":
    main()
