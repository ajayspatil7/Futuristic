import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'bootcampResponses.csv'
pandaDFrame = pd.read_csv(file)

interestedIn = pandaDFrame['w']
interestedIn = interestedIn.dropna()
#print(interestedIn)

# Count number of 'Machine Learning' in the column
#print("Machine Learning :", interestedIn.str.count('Machine Learning').sum())

# Count number of 'Blockchain' in the column
#print("Blockchain :", interestedIn.str.count('Blockchain').sum())

# Count number of 'Computer Graphics' in the column
#print("Computer graphics :", interestedIn.str.count('Computer Graphics').sum())

# Count number of 'Entrepreneurship' in the column
#print("Entrepreneurship :", interestedIn.str.count('Entrepreneurship').sum())

# Count number of 'Internet of things' in the column
#print("IOT :", interestedIn.str.count('Internet of Things (IoT)').sum())

# Count number of 'Coding (Python)' in the column
#print("Coding (Python) :", interestedIn.str.count('Coding (Python)').sum())
# Name: Madan gowda
print(interestedIn[10])
# Python (Coding)
