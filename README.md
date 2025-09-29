# 🧬 DNA Classifier App (React + Flask + ML)

Bu proje, **DNA dizilerini sınıflandıran** basit bir makine öğrenmesi uygulamasıdır.  
Amaç, biyoinformatik veriler üzerinde çalışan bir ML modelini **web arayüzü** üzerinden erişilebilir hale getirmektir.  

- **Frontend:** React (Vite ile)  
- **Backend:** Flask (Python)  
- **ML Modeli:** Logistic Regression (Scikit-learn)  
- **Amaç:** DNA sekansını gir → model tahmin etsin (Healthy / Mutant)  

## 🚀 Özellikler
- Kullanıcı DNA dizisini web arayüzünden girebilir  
- Flask API diziyi alıp **önceden eğitilmiş ML modeli** ile sınıflandırır  
- Sonuç JSON olarak dönüp ekranda gösterilir  
- Eğitim ve tahmin süreci birbirinden ayrılmıştır (profesyonel yaklaşım)  

## 📂 Proje Yapısı
```
dna-classifier-app/
│
├── vite-project/ # React (Vite) projesi
│ └── src/App.jsx
│
├
│ ├── app.py # Flask API
│ ├── train_model.py # Model eğitimi
│ ├── model.pkl # Eğitilmiş model
│ └── vectorizer.pkl
│
└── README.md
```
## ⚙️ Kurulum ve Çalıştırma

### 1. Backend (Flask)
```bash
cd vite-project
python train_model.py
python app.py
```     
### 2. Frontend (React)
```bash
npm install
npm run dev
```
### 3. Tarayıcıdan açın.
```bash
http://localhost:5173
```
### 4. DNA Sekansını girin.
DNA sekansı girin (ör. ATCGATCGATCGA) → model sonucu tahmin edecek: Healthy veya Mutant

## 🔮 Gelecek Geliştirmeler

- Daha büyük DNA datasetleri ile model eğitimi

- Derin öğrenme modelleri (RNN / Transformer)

- Arayüze grafiksel DNA baz dağılımı ekleme

- Kullanıcı dostu hata kontrolleri

## Kullanılan Teknolojiler

-React (Vite)

- Python (Flask)

- Scikit-learn

- Joblib

- Numpy
## Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

