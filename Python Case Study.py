#!/usr/bin/env python
# coding: utf-8

# ### Welcome to the Southern Water Corp Python Case Study!
# 
# While working on the Statistics unit, you used Microsoft Excel's data analytics capabilities to analyze Southern Water Corp's Pump Data.
# 
# Now, Joanna Luez — Southern Water Corp's Lead Scientist — has requested that you convert your earlier analysis in Excel to Python Code. After all, with all the formulas in Excel, it can be tricky for others with less experience in Excel to follow.
# 
# Excel is an excellent tool for adhoc analysis, but Python is an invaluable tool thanks to its advanced data analysis capabilities that only take a few lines of code to complete.
# 
# **Please note that this case study is composed of two parts** — once you have completed part 1, which involves descriptive statistics, please submit your work and discuss it with your mentor before moving on to part 2. 
# 
# ### Let's get started!

# ---

# ## Part I: <span style="color:blue">Descriptive Statistics</span>

# ### Step 1: <span style="color:green">Import Libraries</span> 
# 
# Import the libraries you'll need for your analysis. You will need the following libraries:  
# 
# **Matplotlib** - This is Python's basic plotting library.
# You'll use the pyplot and dates function collections from matplotlib throughout this case study so we encourage you to important these two specific libraries with their own aliases. Also, include the line **'%matplotlib inline'** so that your graphs are easily included in your notebook. 
# 
# Don't forget that to modify the matplotlib plot sizes so they're at a comfortable reading size you should use the following:
# 
# **import matplotlib as mpl**
# 
# **mpl.rcParams['figure.figsize'] = (20,5)**
# 
# **Seaborn** - This library will enable you to create aesthetically pleasing plots.
# 
# **Pandas** - This library will enable you to view and manipulate your data in a tabular format.
# 
# **statsmodels.api** - This library will enable you to create statistical models. You will need this library when performing regession analysis in Part 2 of this case study.

# ## Place your code here

# In[5]:


import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.dates as md
get_ipython().run_line_magic('matplotlib', 'inline')
mpl.rcParams['figure.figsize'] = (20,5)
import seaborn as sns
import pandas as pd
import statsmodels.api as sm


# ---------------------------------------------------------------------------

# 
# ### Step 2: <span style="color:green">Descriptive Statistics</span> 
# The data you've received from Southern Water Corp has been split into two files.
# The first file, titled DF_Raw_Data contains all the 'raw' Pump Data you will need for your analysis.
# The second file, titled DF_Rolling_Stdev contains the Rolling Standard Deviation Data you will need for questions 10 Onwards.
# 
# We have **deliberately** set up the data in this manner so please ensure that when you need to perform the rolling standard deviation calculations, you use the **DF_Rolling_Stdev.csv** file.
# 
# i. Import each of the two data sources and store them into their individual dataframes. 
# Suggested names: **dataframe_raw & dataframe_stdev respectively**. 
# Don't forget to use the **header** argument to ensure your columns have meaningful names! 
# 
# ii. Print descriptive statistics for each of the dataframes using **.describe()** and **.info()**

# In[6]:


raw_data = pd.read_csv(r'C:\Users\cpoll\Downloads\DF_Raw_Data.csv', header=0)
stdev_data = pd.read_csv(r'C:\Users\cpoll\Downloads\DF_Rolling_Stdev.csv', header=0)
print(raw_data.describe())
print(raw_data.info()) 
print(stdev_data.describe()) 
print(stdev_data.info())


# ---------------------------------------------------------------------------

# ### Step 3: <span style="color:green">Create a Boxplot</span> 
# 
# When you look at your dataframe, you should now be able to see the upper and lower quartiles for each row of data from the **.info** command you used previously.
# 
# You should now also have a rough sense of the number of entires in each dataset (~2,452). However, just as you learned when using Excel, creating a visualization of the data using Python is often more informative than viewing the table statistics. Next up — convert the tables you created into a boxplot by following these instructions:
# 
# i) Using the dataframe_raw, create a boxplot visualising this information.
# 
# ii) Using the dataframe_raw, create a lineplot visualising this information.
# 
# Hint: You might want to reference the following .plot function (https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html)

# ### Please put your code here
# 

# #### We've included an example of what your Box Plot *should* look like once you've plotted this using the dataframe_raw dataset

# In[7]:


raw_data.plot(kind='box')


# In[8]:


raw_data.plot()


# In[ ]:





# ### **What have you observed from the boxplot and line plots?**

# In[ ]:


# Box plot shows pump torque as having the greatest variation in values, followed by pump speed. The line plot shows us how
# the performance of the different systems is linked, as well as the huge spike that occured during pump failure.


# ### You would probably note that it might seem that some variables, due to their range and size of values, dwarfs some of the other variables which makes the variation difficult to see. 
# 
# ### More importantly, the dataset we do have contains Pump Failure Data where it has failed (i.e. Pump Failure = 0) as well as when it is operating normally. We should separate this data accordingly to more effectively visualise the information.

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

# ### Step 4: <span style="color:green">Filtered Dataframes with Box Plots</span> 
# 
# i) Using the dataframe_raw dataset, create two boxplots specifically for when the Pump has failed (i.e. Pump Failure = 1)  and 0 (Pump is in normal operations). 
# 
# As part of best practice, don't forget to clearly title your box plots so we can identify which plot is for the failure and which plot is for the normal operations.
# 
# To do this, you'll have to recall how to apply **boolean** filtering to a dataframe.
# 
# 

# ## Please put your code here

# In[9]:


raw_pump_0 = raw_data[raw_data['PUMP FAILURE (1 or 0)'] == 0]

raw_pump_0.plot(kind='box', title='Pump Failure = 0')

raw_pump_1 = raw_data[raw_data['PUMP FAILURE (1 or 0)'] == 1]

raw_pump_1.plot(kind='box', title='Pump Failure = 1')


# **Open-ended Question:**
# ### What have you noticed when you compared the dataset in this manner?

# In[ ]:


# When the pumps are failing, outliers are reduced resulting in more consistent performance for the other systems.


# ### From analysing the boxplots, you might notice that there seem to be a number of outliers. We might want to see if we can actively remove this with Python. 
# When you did this work in Excel, you used the interquartile ranges to remove the outliers from each column. Happily, Python allows you to do this same process more quickly and efficiently, as you'll see when working on  <span style="color:green">Step 5</span>.

# ---------------------------------------------------------------------------

# ### Step 5: <span style="color:green">Create Quartiles</span> 
# 
# i) Create two new variables called Q1 and Q3. 
# 
# Q1 should contain the 25th percentile for all columns in the dataframe while Q3 should contain the 75th percentile for all the columns in the dataframe.
# 
# ii) Calculate the interquartile range **(IQR = Q3 - Q1)** for all columns in the dataframe and print it to the screen.

# ## Please put your code here

# In[10]:


Q1 = raw_data.quantile(0.25)

Q3 = raw_data.quantile(0.75)

IQR = Q3 - Q1

print(IQR)


# ---------------------------------------------------------------------------

# ### Step 6: <span style="color:green">Identify Outliers</span> 
# 
# How many outliers do you have? What will happen to your dataset if you remove them all? Let's find out!
# 
# i) Calculate how many entries you currently have in the original dataframe.
# 
# ii) Using the quartiles and IQR previously calculated, identify the number of entries you'd have if you were to remove the outliers.
# 
# ii) Find the proportion of outliers that exist in the dataset.
# 
# 

# ## Please put your code here

# In[11]:


raw_data_t = raw_data.set_index('TIMEFRAME (DD/MM/YYYY)')

print ("When we have not removed any outliers from the dataset, we have " + str(len(raw_data)) + " entries") 

raw_data_drop = raw_data_t.drop(['Data Source'], axis=1)

raw_data_no_outliers = raw_data_drop[~((raw_data_drop < (Q1 - 1.5 * IQR)) | (raw_data_drop > (Q3 + 1.5 * IQR))).any(axis=1)]

print ("When we have removed all outliers from the dataset, we have " + str(len(raw_data_no_outliers)) + " entries")
print ("The proportion of outliers which exist when compared to the dataframe are: " + str(len(raw_data_no_outliers)/len(raw_data)))


# ### Having removed the outliers from the dataset - do we think this is a good option? Why or why not?

# In[ ]:


# I'm assuming these outliers are related to pump failure, considering we want to analyze that I'd say no.


# In[22]:





# ---------------------------------------------------------------------------

# ### Step 7: <span style="color:green">Create a Boxplot without Outliers</span> 
# 
# With the dataset now stripped of outliers, create the following boxplots:
# 
# i) A boxplot when PUMP FAILURE is 1 (Check what the **length** of the dataframe is before you try and plot this. You may be surprised!)
# 
# ii) A boxplot when PUMP FAILURE is 0 
# 
# #### Note 1: Removing outliers is very situational and specific. Outliers can skew the dataset unfavourably; however, if you are doing a failure analysis, it is likely those outliers actually contain valuable insights you will want to keep as they represent a deviation from the norm that you'll need to understand. If you remove all the outliers - you might discover you have nothing to plot...!
# 

# ## Please put your code here

# In[12]:


raw_pump_0_no_outliers = raw_data_no_outliers[raw_data_no_outliers['PUMP FAILURE (1 or 0)'] == 0]

raw_pump_0_no_outliers.plot(kind='box', title='Pump Failure = 0')

raw_pump_1_no_outliers = raw_data_no_outliers[raw_data_no_outliers['PUMP FAILURE (1 or 0)'] == 1]

raw_pump_1_no_outliers.plot(kind='box', title='Pump Failure = 1')


# In[ ]:


#I assume that by making the 'pump failure = 1' plot I'm supposed to see that it's empty, but all I get is an error saying
#"TypeError: Empty 'DataFrame': no numeric data to plot". This is despite the fact that I had a mentor help me solve Q6,
#ensuring that the setup for Q7 was correct, so I got no idea. This is also why the wording from Q6 is not mine, just fyi


# ### Based on the boxplots you've created, you've likely come to the conclusion that, for this case study, you actually _shouldn't_ remove the outliers, as you are attempting to understand the Pump Failure Behavior and the portion of data you need is actually stored WITHIN the Outliers.
# 
# ### This is exactly why you should never remove Outliers without Subject Matter Expertise input. Otherwise valuable information may be discarded.

# -----

# ### Step 8: <span style="color:green">Plot and Examine Each Column</span> 
# 
# As you might recall from the earlier plot you had made with the line plot; it was hard to see which variables were the most significant with respect to pump failure when all the variables are plotted together. This is why we are going to ITERATE through the dataframe and plot each individual variable out and compare this with the Pump Failure.
# 
# This will require you to make use of the following syntax:
# 
# #### for variable in listOfVariables:
#     #Loop through each variable in the dataframe (i.e. dataframe[___].plot
#     #Specify the dual-axis (i.e. ax.twinx())
#     #Plot the Pump Failure (1 or 0) on the secondary axes
#     #Include Plot Titles for each plot (i.e. print ("This is for the attribute " + i))
#     
# #### Using the syntax provided, loop through the dataframe_raw dataset, plotting every variable individually, against the Pump Failure to better identify trends.
# 
# **Note:** For each plot, ensure that you have a dual axis set up so you can see the Pump Behaviour (0 or 1) on the second Y-axis, and the attribute on the first Y-Axis. It might be helpful to give the failureState it's own color and add a legend to the axis to make it easier to view. 
# 
# Check out this link to learn how to do this: https://matplotlib.org/gallery/api/two_scales.html
# 
# ##### Note: Please ensure that the dataframe you are plotting contains all the outliers and that the Pump Failure Behaviour includes both the 0 and 1 State.

# ## Please put your code here

# In[13]:


raw_data_drop = raw_data.drop(['Data Source','TIMEFRAME (DD/MM/YYYY)','PUMP FAILURE (1 or 0)'], axis=1)

for i in raw_data_drop:
    ax = raw_data_drop[i].plot()
    ax.set_ylabel(i)
    ax2 = ax.twinx()
    ax2.plot(raw_data['PUMP FAILURE (1 or 0)'], 'red', label ='Pump Failure')
    ax2.set_ylabel('Pump Failure')
    plt.tight_layout()
    plt.title(i + " Activity Compared to Pump Failure")
    plt.show()


# ### What do you notice when looking at the data in this way? Do any particular trends emerge?

# In[41]:


#I got stuck on this question for 5 actual hours and am still pretty sure it's not correct so we'll have to fix that before I
#can draw conclusions


# 
# Of course, given that all the attributes have varying units, you might need more than one plot to make sense of all this data. For this next step, let's view the information by comparing the <b>ROLILNG DEVIATIONS</b> over a 30-point period. 
# 
# This is where we will switch to using the dataframe_stdev that you had previously defined in Q1.
# 
# As the deviations will likely be a lot lower, the scale should be much simpler to view on one plot.
# Make sure that you include the 'PUMP FAILURE 1 or 0' attribute on the secondary Y-axis. 
# 
# #### Hint: Remember to make use of the Dual-Axis plot trick you learned in the previous exercise!
# 

# ---

# ### Step 9: <span style="color:green">Create a Plot for Pump Failures Over a Rolling Time Period</span> 
# 
# i) Set the **index** of the dataframe to the TIMEFRAME (DD/MM/YYYY) attribute
# 
# 
# ii) Exactly as you did in Q8, Re-plot all variables, now transformed via a rolling standard deviation in the dataframe_stdev for the time period 10/12/2014 13:30 to 10/12/2014 14:30 against Pump Failure.
# 
# Note: To effectively filter on the time period you will need to make use of the below syntax
#     # dataframe_time_filtered = dataframe[(dataframe.index >= "_____") & (dataframe.index <= "_____")
# 

# ## Please put your code here

# ### The output from your code should display image(s) like the one shown below

# In[14]:


stdev_data_t = stdev_data.set_index('TIMEFRAME (DD/MM/YYYY)')
dataframe_time_filtered = stdev_data_t[(stdev_data_t.index >= "10/12/2014 13:30") & (stdev_data_t.index <= "10/12/2014 14:30")]
stdev_data_trans = dataframe_time_filtered.drop(['Data Source','PUMP FAILURE (1 or 0)'], axis=1)


for i in stdev_data_trans:
    ax = dataframe_time_filtered[i].plot()
    ax.set_ylabel(i)
    ax2 = ax.twinx()
    ax2.plot(dataframe_time_filtered['PUMP FAILURE (1 or 0)'], 'red', label ='Pump Failure')
    ax2.set_ylabel('Pump Failure')
    plt.tight_layout()
    plt.title(i + " Activity Compared to Pump Failure")
    plt.show()


# ---

# ## Part II: <span style="color:blue">Inferential Statistical Analysis</span>

# When you performed inferential statistics for Southern Water Corp using Excel, you made use of the data analysis package to create a heatmap using the correlation function. The heatmap showed the attributes that strongly correlated to Pump Failure. 
# 
# Now, you'll create a heatmap using Seaborn's heatmap function — another testament to the fact that having Matplotlib and Seaborn in your toolbox will allow you to quickly create beautiful graphics that provide key insights. 
# 
# ### Step 10: <span style="color:purple">Create a Heatmap</span> 
# i) Using Seaborn's heatmap function, create a heatmap that clearly shows the correlations (including R Squared) for all variables using the dataframe_raw dataset.
# 
# 
# Link: (https://seaborn.pydata.org/generated/seaborn.heatmap.html)

# ## Please put your code here

# #### We've included an example of what the output *may* look like below

# In[15]:


sns.heatmap(raw_data.corr(), annot=True)


# **Open-ended Question:**
# 
# Which variables seem to correlate with Pump Failure?
# 

# In[ ]:


# Horse power looks to have the strongest correlation by a decent margin.


# 
# ### Step 11: <span style="color:purple">Create a Barplot of Correlated Features</span>
# Create a barplot that shows the correlated features against PUMP FAILURE (1 or 0), in descending order.
# 
# You can do this with the matplotlib library when you specify matplotlib.pyplot(kind='bar')
# 

# ### Please put your code here

# In[18]:


raw_data_corr = raw_data.corr()

raw_data_corr = raw_data_corr.sort_values("PUMP FAILURE (1 or 0)", ascending=False)

raw_data_corr['PUMP FAILURE (1 or 0)'].plot(kind='bar')


# ---

# ### Step 12: <span style="color:purple">Create a Rolling Standard Deviation Heatmap</span> 
# Previously, you created a correlation matrix using 'raw' variables. We saw *some* correlations with the raw data but they weren't necessarily as strong as we would have liked. This time, we'll recreate a Heatmap using the rolling standard deviation dataframe you had imported in Q1.
# 
# ii) Using Seaborn's heatmap function, create a heatmap that clearly shows the correlations (including R Squared) for all variables using the dataframe_stdev dataset.
# 
# Do any variables stand out? If yes, list these out below your heatmap.
# 

# ## Please put your code here

# In[19]:


sns.heatmap(stdev_data.corr(), annot=True)


# ### Creating a Multivariate Regression Model
# 

# When you worked on this case study in Excel, you went through the tricky process of using the rolling standard deviation variables to generate a regression equation. Happily, this process is much simpler in Python.  
# 
# For this step, you'll be using the statsmodel.api library you imported earlier and calling the Ordinary Least Squares Regression to create a multivariate regression model (which is a linear regression model with more than one independent variable).
# 
# ### Step 13: <span style="color:purple">Use OLS Regression</span> 
# i) Using the OLS Regression Model in the statsmodel.api library, create a regression equation that models the Pump Failure (Y-Variable) against all your independent variables, which include every other variable that is not PUMP FAILURE (1 or 0).
# 
# In order to fit a linear regression model with statsmodels.api there are a few steps that need to be taken. We have demonstrated this below:
#     ## Add a constant to follow the equation form: Ab + x (X = sm.add_constant(X))
#     ## Instantiate the Ordinary Least Squares Model with: model = sm.OLS(Y,X) where Y is the dependent variable and X is the independent variable (Make sure you don't include the PUMP FAILURE (1 or 0) in your list of independent variables as this is what you are trying to predict)
#     ## Fit the Model (OLSmodelResult = OLSmodel.fit())
#     ## Print the OLSModel Summary 
# 
# Link: https://www.statsmodels.org/devel/generated/statsmodels.regression.linear_model.OLS.html
# 
# ii) Repeat i) but this time use the dataframe_stdev you imported previously. What is the R Squared for the model and what does this signify?
# 
# 

# ## Please put your code here 

# In[20]:


X = raw_data[['Volumetric Flow Meter 1','Volumetric Flow Meter 2','Pump Speed (RPM)','Pump Torque ','Ambient Temperature','Horse Power','Pump Efficiency']]
X = sm.add_constant(X)
Y = raw_data['PUMP FAILURE (1 or 0)']
OLSmodel = sm.OLS(Y,X)
OLSmodelResult = OLSmodel.fit()
OLSmodelResult.summary()


# In[21]:


X = stdev_data[['Volumetric Flow Meter 1','Volumetric Flow Meter 2','Pump Speed (RPM)','Pump Torque ','Ambient Temperature','Horse Power','Pump Efficiency']]
X = sm.add_constant(X)
Y = stdev_data['PUMP FAILURE (1 or 0)']
OLSmodel = sm.OLS(Y,X)
OLSmodelResult = OLSmodel.fit()
OLSmodelResult.summary()


# **Open-ended Question:**
# 
# ### Which linear regression model seems to be a better fit? Why do you think this is the case?
# 

# In[ ]:


# Stdev_data looks better cause uhhhh the r-squared is higher?


# Great job creating those regressive equations! You've reached the final step of this case study!
# ### Step 14: <span style="color:purple">Validate Predictions</span> 
# i) Use the regression equation you created in the previous step and apply the .predict() function to the dataframe to see whether or not your model 'picks' up the Pump Failure Event.  
# 
# ii) Plot the rolling linear regression equation against the attribute 'PUMP FAILURE (1 or 0)'
# 
# **Note:** Please ensure all axes are clearly labelled and ensure that you use Dual Axes to plot this.

# ## Please put your code here

# In[26]:


Yprediction = OLSmodelResult.predict(X)
plt.plot(Yprediction)
plt.plot(Y, color = 'red')
plt.tight_layout()
plt.xlabel('Multivariate Regression Model')
plt.ylabel('Pump Failure (1 or 0)')
plt.title('Multivariate Regression Model for All Variables vs Pump Failure')
plt.show()


# You've made it to the end of this challenging case study — well done! You've now converted all of the analysis you did for Southern Water Corp using Excel into Python. You created visualizations using Seaborn, manipulated datasets with pandas, and so much more! This case study was designed to give you practice using Python to analyze datasets both large and small — you can now apply these skills to work you do throughout your career as a data analyst.
# 
# ## Great job! Being able to complete this case study means that you're now proficient with the fundamentals of data analysis in Python!

# In[ ]:




