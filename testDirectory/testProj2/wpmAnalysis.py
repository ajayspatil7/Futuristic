import pandas as pd

resultsFile = pd.read_csv('results.csv')
heads = resultsFile.head()
print(heads)

modes = resultsFile['mode']
print(modes)

