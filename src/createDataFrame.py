from pandas import pandas, DataFrame

def createDataFrame(filePath):
  return  pandas.read_csv(filePath)
