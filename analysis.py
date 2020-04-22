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
petal_length.describe().to_string("Summary_petal_length.txt", index = True, header = True)

plt.clf()

# Specifications for petal_width variable:

plt.hist(df["petal_width"]) # creating histogram
plt.title("Petal_width") # adding title 
plt.savefig("Petal_width.png") # saving the graph

# creating a text file and saving a summary  of petal_width variable using
#  describe() command to the same text file.

petal_width = df["petal_width"]
petal_length.describe().to_string("Summary_petal_width.txt", index = True, header = True)

plt.clf()

# Specifications for sepal_length variable:

plt.hist(df["sepal_length"]) # creating histogram
plt.title("Sepal_length") # adding title 
plt.savefig("Sepal_length.png") # saving the graph


# creating a text file and saving a summary  of sepal_length variable using
#  describe() command to the same text file.

sepal_length = df["sepal_length"]
sepal_length.describe().to_string("Summary_sepal_length.txt", index = True, header = True)

plt.clf()

# Specifications for sepal_width variable:

plt.hist(df["sepal_width"]) # creating histogram
plt.title("Sepal_width") # adding title 
plt.savefig("Sepal_width.png") # saving the graph


# creating a text file and saving a summary  of sepal_width variable using
#  describe() command to the same text file.

sepal_width = df["sepal_width"]
sepal_width.describe().to_string("Summary_sepal_width.txt", index = True, header = True)

plt.clf()


# Specifications for type variable:

plt.hist(df["type"]) # creating histogram
plt.title("type") # adding title 
plt.savefig("type.png") # saving the graph


# creating a text file and saving a summary  of type variable using
#  describe() command to the same text file.

type = df["type"]
type.describe().to_string("Summary_type.txt", index = True, header = True)

plt.clf()

# creating a scatter plot for each pair of variables by using pairplot function from seaborn library
# In order to investigate in pairs I have refereed to following analysis: https://github.com/RitRa/Project2018-iris/blob/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.ipynb
import seaborn as sns

sns.pairplot(df, hue = "Type", palette = "cubehelix",  markers = ["+", "s", "H"])

# how to save to file in seaborn https://stackoverflow.com/questions/32244753/how-to-save-a-seaborn-plot-into-a-file
plt.savefig("Comparison.png")
plt.clf()
