# -*- coding: utf-8 -*-
"""mainproject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aqLj4BgNNYpJXzrnHbvZ_slPp6RDo3eI

PROJECT INTRODUCTION
In this project we are analysing the data of california data set,by analysing the data will determine approximate prices for houses
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#importing file from a local folder
#from google.colab import files
#uploaded=files.upload()
housing_data = pd.read_excel("/content/2198208-housing_(1).xlsx")  #To read the file
print(housing_data)
housing_data.head()  #it gives first five

"""In the above step we are importing library required for analysis purpose and loading data to data set with method in pandas pd.read_excel and printing the first five records of dataset"""

housing_data.shape

housing_data.dtypes

"""1. What is the average median income of the data set and check the distribution of data using appropriate plots. Please explain the distribution of the plot.


"""

housing_data['median_income'].mean() #mean is for calculating average

"""from above result the avg median income of data set is 3.8706"""

housing_data.hist(bins=50,figsize=(15,15))##histogram is used for univariate analysis and distribution of a neumerical value
plt.show()

"""In the above graph outliers are present in housing_median_age and median_house_value

2. Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.
"""

plt.hist(housing_data["housing_median_age"],color='#FF2331')#histogram is used to see the distribution of a numerical value.
plt.title("Housing_median_age Histogram plot")
plt.xlabel("Housing_median_age")
plt.ylabel("Frequencies")
plt.grid(True)
plt.show()

"""from the above histogram graph data is distributed symmetrically

3. Show with the help of visualization, how median_income and median_house_values are related?
"""

sns.scatterplot(x="median_house_value",y="median_income",data=housing_data) #scatter plot gives relation ship between two numeric values

"""from above scatter plot median_house_value and median_income values are directly propotional

4. Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.
"""

housing_data[housing_data.isnull().any(axis=1)]

"""above missing values are identified using isnull method and identified in total_bedrooms"""

new_data=housing_data.dropna(subset=["total_bedrooms"])#dropna() method allows the user to analyze and drop Rows/Columns with Null values in different ways.
new_data

"""5. Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.


"""

housing_data["total_bedrooms"]=housing_data["total_bedrooms"].fillna(housing_data["total_bedrooms"].mean())
housing_data

"""In the above code,a new dataset had been created where the missing values in the 'total_bedrooms'which are denoted by NaN are replaced with the mean value of the 'total_bedrooms'.

6. Write a programming construct (create a user defined function) to calculate the median value of the data set wherever required.
"""

housing_data.head()  #to get first five of housing_data

"""MEDIAN():

Basically it is defined as the 50th percentile of the set of measurements,when observed measurements are ranked from smallest to highest.
median() can be calculated for Discrete and Continuous data.


"""

housing_data['longitude'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of longitude is -118.49"""

housing_data['latitude'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of latitude is 34.26"""

housing_data['housing_median_age'].median() #median function() gives the median value that is 50th percentile of the set of all observations

"""median value of housing_median_age is 29.0"""

housing_data['total_rooms'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of total_rooms is 2127.0"""

housing_data['total_bedrooms'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of total_bedrooms in 438.0"""

housing_data['population'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of population is 1166.0"""

housing_data['households'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of households is 409.0"""

housing_data['median_income'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""median value of median_income is 3.534"""

housing_data['median_house_value'].median() #median function() gives the median value that is 50th percentile of the set of all observations.

"""above results median is calculated for every data
median value of median_house_value is 179700.0

7. Plot latitude versus longitude and explain your observations.
"""

sns.scatterplot(x='latitude',y='longitude',data=housing_data)  #Scatter plot gives a relationship between two numerical values.

"""from the above graph latitude and longitude are inversly propotional to each other

8. Create a data set for which the ocean_proximity is ‘Near ocean’.
"""

new_data=housing_data.loc[housing_data["ocean_proximity"]=="NEAR OCEAN"]
# loc is an label based method which is used to select rows and columns by Names/Labels.
new_data                                             #loc is an essential pandas methods used for filtering ,selecting and manipulating the data.

"""9. Find the mean and median of the median income for the data set created in question 8.


"""

new_data['median_income'].mean() #mean() gives the averages of the data
                                #mean()is applicable for discrete and continuous data but not for categorical data.

new_data['median_income'].median() #median()value gives the 50th percentile of the set of all observations.

"""The mean and median value of the 'median_income'in the created new dataset are:4.005784 and 3.64705 respectively.

10. Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less, it should be quoted as small. If the total bedrooms is 11 or more but less than 1000, it should be medium, otherwise it should be considered large.
"""

import numpy as np
conditions = [
              (housing_data['total_bedrooms'] <=10),
              (housing_data['total_bedrooms'] >=11)&(housing_data['total_bedrooms'] <=1000),
              (housing_data['total_bedrooms'] > 1000)
             ]
values = ['small','medium','large']

housing_data['total_bedroom_size']=np.select(conditions,values)

housing_data

"""In the above data set a new column named total_bedroom_size had been added.Where the total_bedroom_size had been compared to the total_bedrooms while mentioning about the sizes of the total_bedroom_size,where:

If the total_bedroom_size <=10 it is indicated as "small" If the total_bedroom_size >=11 or <=1000 it is indicated as "medium" If the total_bedroom_size >1000 it is indicated as "large"
"""