# -*- coding: utf-8 -*-
"""BREAST CANCER PREDICTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/burikyali/Project--Breast-Cancer-Detection-Using-ML/blob/main/BREAST_CANCER_PREDICTION.ipynb
"""

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(cancer['DESCR'])

cancer.target_names

cancer.feature_names

from sklearn.model_selection import train_test_split

X=cancer.data
y=cancer.target
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

np.shape(X_train)

np.shape(X_test)

from sklearn.linear_model import LogisticRegression

from sklearn.linear_model import LogisticRegression
Lgr=LogisticRegression().fit(X_train,y_train)

Lgr.score(X_train,y_train)*100

Lgr.score(X_test,y_test)*100