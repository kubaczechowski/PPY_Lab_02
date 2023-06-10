import ssl
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Wyłączenie weryfikacji certyfikatu SSL -problem z ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Nagłówki kolumn:
headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

# Pobieraniei przypisanie nagłówków:
df = pd.read_csv(url, names=headers)

print(df)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023)

gnb = GaussianNB()

gnb.fit(X_train, y_train)

kfold = KFold(n_splits=5, random_state=2023, shuffle=True)
scores = cross_val_score(gnb, X_train, y_train, cv=kfold, scoring="accuracy")

print("Wyniki sprawdzianu krzyżowego:")
print(scores)
print(f"Średnia dokładność: {scores.mean()}")

# No need for parameter grid or grid search in Naive Bayes

results = pd.DataFrame({'mean_test_score': scores})
print(results)
results.to_csv("results.csv")

print("Best model parameters: ", gnb.get_params())

best_predict = gnb.predict(X_test)
print("Accuracy on the test set: ", accuracy_score(y_test, best_predict))

best_predict_train = gnb.predict(X_train)
print("Accuracy on the training set: ", accuracy_score(y_train, best_predict_train))

cm_train = confusion_matrix(y_train, best_predict_train)
print("Confusion matrix for the training set:")
print(cm_train)

report = classification_report(y_train, best_predict_train)
print(report)
