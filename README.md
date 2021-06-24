# Matplotlib
In this repository you can find code and snippets related to matplotlib. 

# What is matplotlib in python?
Matplotlib is the primary library for generating graphs in Python. Most other graphing libraries are wrappers around matplotlib. The matplotlib library is not part of the standard Python library, but it is installed automatically when you install a scientific Python platform such as Anaconda. 
Data visualization is one of the key ingredients of data science or data analysis.

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


# Bar Charts

* Bar plots are used to visualize a continuous variable versus a categorical variable. They provide a great way to visualize the magnitudes of a quantitative variable in terms of a qualitative variable.Depending on the software we used to create a bar plot, the height of the bars can show either the maximum value or the average value of the quantitative variable.

**ADVANTAGES:**
1. Summarize a large amount of data in a very interpretable way.
2. Easily readable by a large amount of audience.
3. Easy to display the contribution for multiple categories

**DISADVANTAGES:**
1. Sometimes need some extra explanation.
2. Fails to show the assumptions behind the data.


# Scatter Plots

Another way of converting your continuous variables to charts is to scatter plots. Scatter plots require two continuous variables in order to plot them and hence they are bivariate.

Scatter plots are also very common in practice when it comes to identifying if there exists a relationship between variables or not. They can also depict if two continuous variables have a positive correlation, negative correlation, or no correlation.

**ADVANTAGES:**
1. Highlights correlation
2. Often depicts minimum, maximum, and outliers in the data.
3. Shows if there is a trend in the data.

**DISADVANTAGES :**
1. Only applicable to continuous variables.
2. Sometimes the results are inconclusive.


# Pie Charts & Doughnut Charts

Pie charts are nothing but a big circle. They are really easy to interpret and represent a circle that is sliced into pieces (like a pizza) based on some categories. The pie chart as a whole shows 100% data but individual slices show their own contribution to the data.


Doughnut Charts are basically the same as Pie Charts, with just a hole in the middle. It is often viewed as a modification to pie charts. Doughnut charts, on the other hand, eliminates the need to compare the size or area of the slice and shifts the focus on the length of the arc, which in turn is easy to measure.

Both Doughnut Charts and Pie charts share the same advantages and disadvantages. 

ADVANTAGES :
1. Easy to interpret and widely used.
2. It visualizes data as a fractional part of the whole and which leads to effective communication.
3. Data comparison is very easily done at a glance.

DISADVANTAGES:
1. Becomes hard to interpret and read if data contains too many slices or categories.
2. Pie charts only represent one series of data and hence we need to draw more than one in order to compare two or more series of data.


# Stack Plots

The idea of stack plots is to show “parts to a whole” over time; basically, it's like a pie-chart, only over time. Stack plots are mainly used to see various trends in variables over a specific period of time. Matplotlib has a built-in function to create stack plots called stackplot().
