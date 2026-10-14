import re, sys
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load CSV (columns: text, label) or use a tiny demo set
if len(sys.argv) > 1:
    df = pd.read_csv(sys.argv[1])[["text", "label"]].dropna()
else:
    phish = ["URGENT verify your password now http://192.168.1.5/login",
             "Account suspended! Click http://bit.ly/abc to confirm bank details",
             "You won a prize! Claim refund at http://secure-pay.xyz/claim"] * 20
    safe = ["Meeting moved to 3pm, agenda at https://docs.company.com/a",
            "Thanks for your order, invoice at https://www.amazon.com/orders",
            "Lunch on Friday? Let me know."] * 20
    df = pd.DataFrame({"text": phish + safe, "label": ["phishing"] * 60 + ["safe"] * 60})
df["y"] = df["label"].astype(str).str.lower().isin(["phishing", "spam", "1"]).astype(int)

# URL/keyword features
def feats(t):
    urls = re.findall(r"https?://\S+", t)
    return [len(urls), int(bool(re.search(r"https?://\d+\.\d+\.\d+\.\d+", t))),
            int(any(s in t for s in ["bit.ly", "tinyurl", ".xyz", ".top"])),
            sum(w in t.lower() for w in ["urgent", "verify", "password", "suspend", "click", "bank"])]

tfidf = TfidfVectorizer(stop_words="english")
Xtr, Xte, ytr, yte = train_test_split(df.text, df.y, test_size=0.2, stratify=df.y, random_state=42)
vec = lambda X, fit=False: hstack([(tfidf.fit_transform if fit else tfidf.transform)(X),
                                   csr_matrix([feats(t) for t in X])])
model = LogisticRegression(max_iter=1000).fit(vec(Xtr, True), ytr)
pred = model.predict(vec(Xte))

print("Accuracy:", accuracy_score(yte, pred))
print("Confusion matrix:\n", confusion_matrix(yte, pred))
ConfusionMatrixDisplay.from_predictions(yte, pred, display_labels=["Safe", "Phishing"]).figure_.savefig("cm.png")