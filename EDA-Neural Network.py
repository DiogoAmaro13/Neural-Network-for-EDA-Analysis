# 0. Import and Install Dependencies

%matplotlib inline
import os  
import pandas as pd  
import seaborn as sns   
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
import numpy as np

# 0.1 Install tensorflow
!pip install tensorflow

# 0.2 Check if the dependencies are installed
!pip list


# 1. Load and Study Data 
# 1.1 Load the data

  # 1.1.1 Find path of the dataset 
cwd = os.getcwd()
file_path = os.path.join(cwd, 'emotions.csv')
file_path

  # 1.1.2 Load the file as a dataframe
df = pd.read_csv('C:\\Users\\jmsi\\emotions.csv')

# 1.2 Study the data
""" To study the data, it is recommend to use methods that allow us to find general info about our dataset, such as: """
  #✔ Was the dataset loaded correctly into our environment?
  df
  #✔ General view on the dataframe
  df.head()
  #✔ Number of rows & columns
  df.shape()
  #✔ Statistical values
  df.describe()
  #✔ Are the values in our dataset balanced?
  df['label'].value_counts()  #The 'label' element must be replaced with the name of the last column of the dataset that, in our case, is called 'label'.
  #✔ Are there missing values?
  for col in df.columns:
    if df[col].isnull().sum()>0:
        print(col)
  #✔ How many categorical features are in our dataset?
  for col in df.columns:
    if(df[col].dtype=='object'):
        print(col)
        
""" Take the conclusions: """
  #✔ Was the dataset loaded correctly into our environment?
    # Yes it was, because 'df' displays an actual dataframe, which means the load was done properly
  #✔ General view on the dataframe
    # With 'df.head()' we get the first 5 rows of our dataset
  #✔ Number of rows & columns
    # 'df.shape()' gives us the shape of our dataset -> (2132, 2549)
  #✔ Statistical values
    # 'df.describe()' outputs a dataframe with values such as mean, standard deviation, min, max, etc
  #✔ Are the values in our dataset balanced?
    # The code provided allow us to understant


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
