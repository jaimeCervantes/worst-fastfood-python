from pandas import pandas

def createDataFrame(filePath):
  return pandas.read_csv(filePath)
