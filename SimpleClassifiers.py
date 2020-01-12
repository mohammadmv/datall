import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split

def KNN_Clssify(data_):
    test_percent=input("KNN Classify Tool>>> Test Percent:")
    read_n_neighbors=input("KNN Classify Tool>>> Number of neighbors to use:")

    vector_len=len(data_[0])-1

    X = data_[:, 0:vector_len]  # select columns 1 through end
    y = data_[:, vector_len]  # select column 0, the stock price

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = float(test_percent)/100.0, random_state = 42)
    clf=KNeighborsClassifier(n_neighbors=int(read_n_neighbors), weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=None)
    clf.fit(X_train,y_train)

    