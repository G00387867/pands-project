# Adam Shaat
# A program to analyse the Fisher's Iris flower datasets


import numpy as np # importing numpy
import pandas as pd # importing pandas library
import matplotlib.pyplot as plt  # importing matplotlib library
import seaborn as sns # importing seaborn library


pd.read_csv("https://raw.githubusercontent.com/G00387867/pands-project/master/iris.data") # recalling the iris file from own repository

# setting variable to data is taken from the following web refernce:
# https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
variables =['sepal_length','sepal_width','petal_length','petal_width','Type'] 
df = pd.read_csv("https://raw.githubusercontent.com/G00387867/pands-project/master/iris.data", names = variables)


# https://github.com/RitRa/Project2018-iris
# analysing the dataset's main datapoints

summary = df.describe() #showing summary of the data set
summary = summary.transpose()
summary = summary.head()

# Specifications for petal_length variable:

plt.hist(df["petal_length"], label = "iris setosa, iris versicolor and iris virginica, count = 150", color ='r') # creating histogram
plt.legend() # adding legend
plt.xlabel("size in cm") # defining x-axis
plt.ylabel("count") # defining y-axis
plt.title("Petal_length") # adding title 
plt.savefig("Petal_length.png") # saving the graphs
plt.clf()

# creating a text file and saving a summary  of petal_length variable using
#  describe() command to the same text file.

petal_length = df["petal_length"]
petal_length.describe().to_string("Summary_petal_length.txt", index = True, header = True)


# Specifications for petal_width variable:


plt.hist(df["petal_width"], label = "iris setosa, iris versicolor and iris virginica, count = 150", color ='g') # creating histogram
plt.legend() # adding legend
plt.xlabel("size in cm") # defining x-axis
plt.ylabel("count") # defining y-axis
plt.title("Petal_width") # adding title 
plt.savefig("Petal_width.png") # saving the graph
plt.clf()

# creating a text file and saving a summary  of petal_width variable using
#  describe() command to the same text file.

petal_width = df["petal_width"]
petal_width.describe().to_string("Summary_petal_width.txt", index = True, header = True)


# Specifications for sepal_length variable:


plt.hist(df["sepal_length"], label = "iris setosa, iris versicolor and iris virginica, count = 150", color ='b') # creating histogram
plt.legend() # adding legend
plt.xlabel("size in cm") # defining x-axis
plt.ylabel("count") # defining y-axis
plt.title("Sepal_length") # adding title 
plt.savefig("Sepal_length.png") # saving the graph
plt.clf()

# creating a text file and saving a summary  of sepal_length variable using
#  describe() command to the same text file.

sepal_length = df["sepal_length"]
sepal_length.describe().to_string("Summary_sepal_length.txt", index = True, header = True)


# Specifications for sepal_width variable:


plt.hist(df["sepal_width"], label = "iris setosa, iris versicolor and iris virginica, count = 150", color ='m') # creating histogram
plt.legend() # adding legend
plt.xlabel("size in cm") # defining x-axis
plt.ylabel("count") # defining y-axis
plt.title("Sepal_width") # adding title 
plt.savefig("Sepal_width.png") # saving the graph
plt.clf()

# creating a text file and saving a summary  of sepal_width variable using
#  describe() command to the same text file.

sepal_width = df["sepal_width"]
sepal_width.describe().to_string("Summary_sepal_width.txt", index = True, header = True)


# Specifications for Type variable:

plt.hist(df["Type"], label = "iris setosa, iris versicolor and iris virginica, count = 150", color ='y') # creating histogram
plt.legend() # adding legend
plt.xlabel("size in cm") # defining x-axis
plt.ylabel("count") # defining y-axis
plt.title("Type") # adding title 
plt.savefig("Type.png") # saving the graph
plt.clf()

# creating a text file and saving a summary  of Type variable using
#  describe() command to the same text file.

Type = df["Type"]
Type.describe().to_string("Summary_type.txt", index = True, header = True)


# creating a pairplot for each pair of variables by using pairplot function from seaborn library
# In order to investigate in pairs I have refereed to following analysis: https://github.com/RitRa/Project2018-iris/blob/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.ipynb

sns.pairplot(df, hue = "Type", palette = "cubehelix",  markers = ["+", "s", "H"])
plt.savefig("Pairplot.png")
plt.clf()


# investigating in pairs

# scatter Petal_Length_vs_Petal_width
# code refernced from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
# There was an issue with inserting the title as the letters were cut, researched solution from 
# https://github.com/mwaskom/seaborn/issues/1114

sns.set_style("white")
sns.FacetGrid(df,hue="Type",height=5).map(plt.scatter,"petal_length","petal_width").add_legend()
plt.suptitle("Petal_Length vs Petal_Width")
plt.savefig("Petal_Length_vs_Petal_width.png")
plt.clf()


# scatter Sepal_length_vs_Sepal_Width
# code refernced from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
# There was an issue with inserting the title as the letters were cut, researched solution from 
# https://github.com/mwaskom/seaborn/issues/1114

sns.set_style("white")
sns.FacetGrid(df,hue="Type",height=5).map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.suptitle("Sepal_Length vs Sepal_Width")
plt.savefig("Sepal_Length_vs_Sepal_width.png")
plt.clf()
