
## Fisher’s Iris data set
![Iris Flower, source: https://thegoodpython.com/iris-dataset/](https://github.com/G00387867/pands-project/blob/master/iris_snipp_it.PNG "Iris Flower, source: https://thegoodpython.com/iris-dataset/")

### _Introduction_

The data set contains a set of 150 records under five attributes - petal length, petal width, sepal length, sepal width and species.
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: **_the length and the width of the sepals and petals_**, in **centimeters**. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other[1].

The aim for this project is to analyse the Fisher's Iris flower data set using python as a coding and scripting language.

### _Methodology_

* Downloading iris data set from (http://archive.ics.uci.edu/ml/datasets/iris) and saving it to this repository [2]
* Assigning columns to raw data with each variable attribute: petal length, petal width, sepal length, sepal width and type
* showing a summary of the dataset by highlighting main data points
* Analysing the data by creating a histogram of each variable and text file summary of the statistical specification of the variable
* Creating a pair plot(s) showing the correlation between the different variable categories
* Configuration and tooling to run the code in README file
* A README file containing information and documentaion of the project including References.


### _Analysis_

>#### Summary of the data set
`summary = df.describe()`

`summary = summary.transpose()`

`summary = summary.head()`


 |    Type      |count | mean      |      std|  min | 25%   |50% | 75%   |max|
 |------------| --------| --------| -----------|-----|------|----|-----|-----|
| sepal_length |  150.0|  5.843333 | 0.828066 | 4.3|  5.1 | 5.80 | 6.4|  7.9|
| sepal_width |   150.0 | 3.054000 | 0.433594 | 2.0 | 2.8 | 3.00 | 3.3 | 4.4|
| petal_length |  150.0 | 3.758667 | 1.764420 | 1.0|  1.6 | 4.35 | 5.1 | 6.9|
|petal_width |   150.0 | 1.198667 | 0.763161 | 0.1 | 0.3 | 1.30 | 1.8 | 2.5|
--------------------------------

>#### _Pairplot_ using SEABORN

![Pairplot](https://github.com/G00387867/pands-project/blob/master/Pairplot.png "Pairplot")

>#### Petal Length vs Petal Width

![Petal Length vs Petal Width](https://github.com/G00387867/pands-project/blob/master/Petal_Length_vs_Petal_width.png "Petal length vs Petal width")

>#### Sepal Length vs Sepal Width

![Sepal Length vs Sepal Width](https://github.com/G00387867/pands-project/blob/master/Sepal_Length_vs_Sepal_width.png "Sepal Length vs Sepal Width")

### Configuration and tooling

The code **`analysis.py`** is written using *python* version 3.8, as a higher level scripting language, the code is supposed to do the following:
>* Outputs and saves a summary of each variable of iris flower to a single text file;
>* Creates and saves a histogram of each variable as png file;
>* Creates and saves a scatter plot of each pair of variables;
>* Creates and saves a scatter plot of the variables that determine the type of the flower, ie; sepal length vs sepalwidth, and petal length vs petal width.

**Libraries** used in writing the code are:

_Numpy_

_Pandas_

_Matplotlib_

_Seaborn_


#### **How to run the code**


**Install:**

_Python 3.8_

_Anaconda_

**Then:**


1. Navigate to the code [analysis.py](https://github.com/G00387867/pands-project/blob/master/analysis.py) in the repository

2. Choose to clone/download the repository and copy the link (make sure you copy the link statrts with https and not the SSH)

3. In the start menu search for `cmd`

4. initiate terminal where the code can be executed 

5. Navigate to the folder where the code needs to be executed

6. Insert `$ git clone (link of the repository)`

7. Insert `$ python analysis.py` 

8. YAY!

9. If you face any issues please contact me and I'd be happy to help!



----------------------------------------------------------------------------------------------




### _[References]_
 
[1] Wikipedia: https://en.wikipedia.org/wiki/Iris_flower_data_set

[2] The data set: http://archive.ics.uci.edu/ml/datasets/iris

[3] Learnbay: https://www.learnbay.co/data-science-course/blog-post/exploratory-data-analysis-on-iris-dataset/

[4] Pythonbasics: https://pythonbasics.org/seaborn-pairplot/

[5] Pandas: https://pandas.pydata.org/docs/

[6] Numpy: https://numpy.org/

[7] Matplotlib: https://matplotlib.org/tutorials/introductory/pyplot.html

[8] Real Python: https://realpython.com/python-matplotlib-guide/

[9] Seaborn: https://python-graph-gallery.com/seaborn/

[10] Kaggle: https://www.kaggle.com/noelano/seaborn-visualization-on-iris-data-set

[11] Scikit-learn: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

[12] Other Reference: https://github.com/mwaskom/seaborn/issues/1114

[13] other reference: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

[14] other reference: https://thegoodpython.com/iris-dataset/

[15] other reference: https://github.com/RitRa/Project2018-iris

[16] Github: https://guides.github.com/features/mastering-markdown/

