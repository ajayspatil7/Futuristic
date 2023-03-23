# Key steps involved
# ------------------------------------------------------------------
# Importing the libraries needed
# Exploring the dataset and creating a model out of it
# Compile the model built using the dataset
# Fitting the model
# Predicting and Evaluating the model
# Saving the model in memory for future use
# Loading the model
# ------------------------------------------------------------------

# Project specific library import
from keras.models import Sequential, load_model
from keras.layers import Dense
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

# Dataset path
csvPath = pd.read_csv('Churn.csv')

# Exploring the dataset
# Specifying the data
x = pd.get_dummies(csvPath.drop(['Churn', 'Customer ID'], axis=1))
y = csvPath['Churn'].apply(lambda x: 1 if x == "Yes" else 0)

# Splitting the dataset for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.4)
x_train.head()
y_train.head()

# Building the model
model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=len(x_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# Compiling the built model
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

# Training the compiled model
model.fit(x_train, y_train, epochs=200, batch_size=32)

# Predicting from the trained model
predictions = model.predict(x_test)
predictions = [0 if val < 0.5 else 1 for val in predictions]

print("Predicted values \n")
print(predictions)

# Calculating the accuracy score
model_accuracy_score = accuracy_score(y_test, predictions)
print(f"Accuracy score : {model_accuracy_score}")

# Saving the trained model
model.save('churnTrained')

# Loading the model
load_model('churnTrained')
