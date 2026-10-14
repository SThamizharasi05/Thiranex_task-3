# 🎣 Phishing Email Detection Model

A machine learning model built with **Scikit-learn** that classifies emails as **Phishing** or **Safe** using text content and URL-based features.

## ✨ Features

- Trains on a dataset of phishing and legitimate emails
- Extracts and analyzes email features:
  - **Text:** TF-IDF on email content
  - **URLs:** number of links, IP-address links, URL shorteners (bit.ly, etc.), suspicious domains
  - **Keywords:** words like *urgent*, *verify*, *password*, *suspend*, *bank*
- Classifies emails as `Phishing` or `Safe`
- Displays **accuracy** and a **confusion matrix**

## 🛠️ Tech Stack

- Python 3.8+
- Scikit-learn
- Pandas
- SciPy
- Matplotlib

## 📦 Installation

```bash
git clone https://github.com/<your-username>/phishing-email-detection.git
cd phishing-email-detection
pip install scikit-learn pandas scipy matplotlib
```

## 🚀 Usage

**Run with your own dataset:**

```bash
python phishing_short.py your_dataset.csv
```

**Run with built-in demo data:**

```bash
python phishing_short.py
```

### Dataset format

A CSV file with two columns:

| text                                   | label    |
|----------------------------------------|----------|
| Verify your password now: http://...   | phishing |
| Meeting moved to 3pm tomorrow          | safe     |

Labels can be `phishing` / `safe` or `1` / `0`.

> Public datasets you can use: Kaggle *Phishing Email Dataset*, SpamAssassin, Enron, Nazario.

## 📊 Output

The program prints:

- **Accuracy** score
- **Confusion matrix**

and saves the confusion matrix plot as `cm.png`.

```
Accuracy: 0.97
Confusion matrix:
 [[118   3]
 [  4 115]]
```



## 🧠 How It Works

1. Load the dataset and convert labels to 0 (Safe) / 1 (Phishing)
2. Extract TF-IDF text features and handcrafted URL/keyword features
3. Split data 80% train / 20% test
4. Train a Logistic Regression classifier
5. Evaluate with accuracy and a confusion matrix


```

## 🔮 Future Improvements

- Try Random Forest / XGBoost and compare accuracy
- Add email header analysis (sender domain, SPF/DKIM)
- Build a simple web app for live email checking

## ⚠️ Note

The built-in demo data is tiny and only for testing. Use a real dataset for meaningful results.# Thiranex_task-3
