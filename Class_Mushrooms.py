#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el dataset como un DataFrame de Pandas
df = pd.read_csv("mushrooms.csv")

# Convertir las columnas categóricas en números utilizando get_dummies
df = pd.get_dummies(df, columns=df.columns[df.dtypes == "object"], prefix=df.columns[df.dtypes == "object"])

# Separar el dataset en datos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop("class_p", axis=1), df["class_p"], test_size=0.2)

# Entrenar un clasificador Random Forest
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Hacer predicciones en los datos de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión de las predicciones
acc = accuracy_score(y_test, y_pred)
print("Precisión:", acc)

# Calcular y visualizar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)
plt.matshow(conf_matrix, cmap=plt.cm.gray)
plt.title("Matriz de Confusión")
plt.xlabel("Predicho")
plt.ylabel("Real")
plt.show()

