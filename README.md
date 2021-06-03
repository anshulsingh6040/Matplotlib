# Matplotlib
In this repository you can find code and snippets related to matplotlib. 

# What is matplotlib in python?
Matplotlib is a data visualization library/package in python and we can create and customise graphs like line charts, bar grapgs, scatter plots, pie charts, area plots, bubble plots etc. Matplotlib also provides functionalities to save those graphs as png or jpeg format.

# How to install matplotlib ?
If you are using anaconda, chances are that matplotlib is already installed in your environment. If not, we can install matplotlib with pip install matplotlib

# Line Charts
* Line charts are pretty much useful and very common in practice. Line charts are the way to depict relations b/w two continuous variables and hence they are bivariate i.e you need at least 2 variables to plot a line chart.

**Advantages :**
1. Easy to interpret the trends over time and also helps to extrapolate the data.
2. A-line break can also depict the presence of missing data.
3. We can also estimate the correlation value by seeing the steepness in the line.


**Disadvantages :**
1. Though line charts are easy to interpret but plotting two line charts over the same figure can make it difficult to compare the results.


# Histograms

To create a histogram, you need a continuous variable. Seldom histograms are used for discrete variables as well. Histograms are univariate i.e one requires only one variable to plot a histogram.

A histogram is a bar plot where the axis representing the data variable is divided into a set of discrete bins and the count of observations falling within each bin is shown using the height of the corresponding bar. Histograms are also known as frequency distribution plots and it is a very common practice to use histograms to check the distribution of the feature or if the data is positively skewed or negatively skewed.

**DRAWBACKS:**
* Histograms are bin biased. You can change the number of bins in a histogram, but there is no optimal number of bins. Sometimes we use fewer bins and sometimes more, we cannot simply rely on the default bins on whichever software we wish to use to create a histogram.
