# Adam Shaat
# A program to analyse the Fisher's Iris flower data sets.

import numpy as np # importing numpy
import pandas as pd # importing pandas library
import matplotlib.pyplot as plt  # importing matplotlib library

pd.read_csv("https://raw.githubusercontent.com/G00387867/pands-project/master/iris.data") # recalling the iris file from own repository

# setting variable to data is taken from the following web refernce:
# https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
variables =['sepal_length','sepal_width','petal_length','petal_width','type'] 
df = pd.read_csv("https://raw.githubusercontent.com/G00387867/pands-project/master/iris.data", names = variables)

# Specifications for petal_length variable:

plt.hist(df["petal_length"]) # creating histogram
plt.title("Petal_length") # adding title 
plt.savefig("Petal_length.png") # saving the graph


# creating a text file and saving a summary  of petal_length variable using
#  describe() command to the same text file.

petal_length = df["petal_length"]
petal_length.describe().to_string("Summary_petal_length.txt", index = False, header = False)

plt.clf()

# Specifications for petal_width variable:

plt.hist(df["petal_width"]) # creating histogram
plt.title("Petal_width") # adding title 
plt.savefig("Petal_width.png") # saving the graph

# creating a text file and saving a summary  of petal_width variable using
#  describe() command to the same text file.

petal_length = df["petal_width"]
petal_length.describe().to_string("Summary_petal_width.txt", index = False, header = False)
