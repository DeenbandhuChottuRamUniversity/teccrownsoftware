import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# %matplotlib inline


def PrizePrediction(data):
    USAhousing = pd.read_csv('./USA_Housing.csv') # dataset

    X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
    y = USAhousing['Price']

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
   
    lm = LinearRegression()
    lm.fit(X_train,y_train)

    toPredict = np.array(data)
    toPredict = toPredict.reshape((1, -1))

    return lm.predict(toPredict)[0]


