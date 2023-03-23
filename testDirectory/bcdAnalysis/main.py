import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv('finalBootCampData.csv')
interestedIn = dataSet['Which bootcamps are you interested in attending?']
modeOfAttendance = dataSet['Mode of attendance (Please note: Entrepreneurship bootcamp can only be attended offline)']

courses = {
    'Entrepreneurship': 0,
    'Blockchain': 0,
    'Internet of Things (IoT)': 0,
    'Machine Learning': 0,
    'Coding (Python)': 0,
    'Computer Graphics': 0,
}

moA = {
    'online': 0,
    'offline': 0,
}
# Count how many attend Online and Offline
for i in modeOfAttendance:
    if i == 'Online':
        moA['online'] += 1
    elif i == 'Offline':
        moA['offline'] += 1




# Count how many are interested in Machine Learning
for i in interestedIn:
    if 'Machine Learning' in i:
        courses['Machine Learning'] += 1
    if 'Coding (Python)' in i:
        courses['Coding (Python)'] += 1
    if 'Computer Graphics' in i:
        courses['Computer Graphics'] += 1
    if 'Entrepreneurship' in i:
        courses['Entrepreneurship'] += 1
    if 'Blockchain' in i:
        courses['Blockchain'] += 1
    if 'Internet of Things (IoT)' in i:
        courses['Internet of Things (IoT)'] += 1

# Plot the data in a Pie chart
plt.pie(courses.values(), labels=courses.keys(), autopct='%1.1f%%')
plt.show()

