# Adam Shaat
# A program to analyse the Fisher's Iris flower datasets.

import numpy as np # importing numpy
import pandas as pd # importing pandas library
import matplotlib.pyplot as plt  # importing matplotlib library
import seaborn as sns


pd.read_csv("https://raw.githubusercontent.com/G00387867/pands-project/master/iris.data") # recalling the iris file from own repository

# setting variable to data is taken from the following web refernce:
# https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
variables =['sepal_length','sepal_width','petal_length','petal_width','Type'] 
df = pd.read_csv("https://raw.githubusercontent.com/G00387867/pands-project/master/iris.data", names = variables)

# analysing the dataset
# https://github.com/RitRa/Project2018-iris
# https://stackoverflow.com/questions/48158688/save-pandas-describe-for-human-readibility/48158748

from pandas.plotting import table
summary = df.describe()
summary = summary.transpose()
summary = summary.head()
# creating a subplot without frame
ax = plt.subplot(111, frame_on = False)
# remove axis
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False) 
# creating the table and positioning
table(ax, summary, loc = "upper right")
plt.savefig("Summary_Iris.png")
# change image resolution
# https://stackoverflow.com/questions/9174338/programmatically-change-image-resolution
from PIL import Image
im = Image.open("Summary_Iris.png")
im.save("Summary_Iris.png", dpi=(600,600)
plt.show()


# Specifications for petal_length variable:

plt.hist(df["petal_length"]) # creating histogram
plt.title("Petal_length") # adding title 
plt.savefig("Petal_length.png") # saving the graphs

# creating a text file and saving a summary  of petal_length variable using
#  describe() command to the same text file.

petal_length = df["petal_length"]
petal_length.describe().to_string("Summary_petal_length.txt", index = True, header = True)
plt.clf()

# Specifications for petal_width variable:

plt.hist(df["petal_width"]) # creating histogram
plt.title("Petal_width") # adding title 
plt.savefig("Petal_width.png") # saving the graph
plt.show()

# creating a text file and saving a summary  of petal_width variable using
#  describe() command to the same text file.

petal_width = df["petal_width"]
petal_width.describe().to_string("Summary_petal_width.txt", index = True, header = True)
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


# Specifications for Type variable:

plt.hist(df["Type"]) # creating histogram
plt.title("Type") # adding title 
plt.savefig("Type.png") # saving the graph


# creating a text file and saving a summary  of Type variable using
#  describe() command to the same text file.

Type = df["Type"]
Type.describe().to_string("Summary_type.txt", index = True, header = True)
plt.clf()

# creating a scatter plot for each pair of variables by using pairplot function from seaborn library
# In order to investigate in pairs I have refereed to following analysis: https://github.com/RitRa/Project2018-iris/blob/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.ipynb

sns.pairplot(df, hue = "Type", palette = "cubehelix",  markers = ["+", "s", "H"])
plt.savefig("Pair_Scatter.png")
plt.clf()


# investigating in pairs
# 

sns.set_style("whitegrid")
sns.FacetGrid(df,hue="Type",height=4).map(plt.scatter,"petal_length","petal_width").add_legend()
plt.savefig("Petal_Length_vs_Petal_width.png")
plt.clf()
plt.show()

