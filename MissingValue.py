import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer,SimpleImputer

def Mean_Imputer(data):
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(data)
    return imp.transform(data)

def Most_Frequent(data):
    imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    imp.fit(data)
    return imp.transform(data)

def KNN_Imputer(data):
    imp = KNNImputer()
    return imp.fit_transform(data)