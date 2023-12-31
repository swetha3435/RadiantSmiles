# -*- coding: utf-8 -*-
"""Advanced House Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VjwreVnYJAShLqypkJ3UYk1UFMd_zdVS

Advanced House Price Prediction
"""

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("/train.csv")

df.head()

df.tail()

df.shape

df.columns

df.duplicated().sum()

df.isnull().sum()

null_counts=df.isnull().sum()

null_counts=df[['LotFrontage', 'Alley', 'MasVnrType', 'MasVnrArea', 'BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
       'Electrical', 'FireplaceQu', 'GarageType', 'GarageYrBlt',
       'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence',
       'MiscFeature']].isnull().sum()
print(null_counts)

df=df.drop(['Alley', 'PoolQC', 'Fence', 'MiscFeature'],axis=1)

numeric_features=['LotFrontage','MasVnrArea','GarageYrBlt']
for feature in numeric_features:
    df[feature].fillna(df[feature].mean(),inplace=True)
categorical_features=['BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2','FireplaceQu',
         'GarageType','Electrical','GarageFinish', 'GarageQual', 'GarageCond']
for feature in categorical_features:
    df[feature].fillna(df[feature].mode(),inplace=True)

df.isnull().sum()

df.info()

df.describe()

df=df.drop(['Id'],axis=1)

"""#dividing object and numerical columns and making a list"""

object_columns=df.select_dtypes(include='object').columns.tolist()
numerical_columns=df.select_dtypes(include=['int','float']).columns.tolist()
print("object columns:",object_columns)

print("Numerical columns:",numerical_columns)

df.nunique()  #to print unique  values present in each and every columns

#to show the unique values in object columns
for i in object_columns:
    print(i)
    print(df[i].unique())
    print('\n')

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have already defined 'object_columns' and 'df'

for i in object_columns:
    print('Countplot for:', i)

    # Create a new figure and axis for each countplot
    plt.figure(figsize=(15, 6))

    # Use seaborn's countplot to create the plot
    sns.countplot(x=i, data=df, palette='hls')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=-45)

    # Add a title if desired
    plt.title(f'Countplot for {i}')

    # Display the plot
    plt.show()

    print('\n')

for i in object_columns:
    print("pie plot for:",i)
    plt.figure(figsize=(20,10))
    df[i].value_counts().plot(kind='pie',autopct='%1.1f%%')
    plt.title('Distribution of '+i)
    plt.ylabel('')
    plt.show()

#graphical object
#plotly is used for better visualization that matplot or seaborn
for i  in object_columns:
    fig = go.Figure(data=[go.Bar(x=df[i].value_counts().index,y=df[i].value_counts())])
    fig.update_layout(
    title=i,
    xaxis_title=i,
    yaxis_title="count")
    fig.show()

# px is used or high level interface
for i in object_columns:
    print('Pie plot for:',i)
    fig=px.pie(df,names=i,title='Distribution of'+i)
    fig.show()
("   print('\n')")

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.histplot(df[i],kde=True,bins=20,palette='hls')
    plt.xticks(rotation=0)
    plt.show()

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.distplot(df[i],kde=True,bins=20)
    plt.xticks(rotation=0)
    plt.show()

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.boxplot(x=df[i],data=df,palette='hls')
    plt.xticks(rotation=0)
    plt.show()

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.violinplot(x=df[i],data=df,palette='hls')
    plt.xticks(rotation=0)
    plt.show()

for i in numerical_columns:
    fig =go.Figure(data=[go.Histogram(x=df[i],nbinsx=20)])
    fig.update_layout(
    title=i,
    xaxis_title=i,
    yaxis_title="count")
    fig.show()

for i in numerical_columns:
  if i!='SalePrice':
    plt.figure(figsize=(15,6))
    sns.barplot(x=df[i],y=df['SalePrice'],data=df,ci=None,palette='hls')
    plt.show()

for i in numerical_columns:
    plt.figure(figsize=(15,6))
    sns.scatterplot(x=df[i],y=df['SalePrice'],data=df,palette='hls')
    plt.show()

for i in numerical_columns:
    for j in object_columns:
        plt.figure(figsize=(15,6))
        sns.barplot(x=df[j],y=df[i],data=df,ci=None,palette='hls')
        plt.show()

corr = df.corr()

plt.figure(figsize=(30,20))
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt=" .2f")
plt.title("correlation plot")
plt.show()

df1 =df.copy()

plt.figure(figsize=(15,6))
sns.histplot(df1['SalePrice'],kde=True,bins=20,palette='hls')
plt.xticks(rotation=0)
plt.show()
#target feature and other features should be normally distributed then only we can apply linear regression

#if features are not normally distributed make it normal distribution
df1['SalepPrice'] =np.log(df1['SalePrice'])

numerical_columns

numerical_columns=['MSSubClass','LotFrontage','LotArea','OverallQual','OverallCond','YearBuilt','YearRemodAdd', 'MasVnrArea','BsmtFinSF1','BsmtFinSF2',
 'BsmtUnfSF','TotalBsmtSF','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd',
 'Fireplaces','GarageYrBlt','GarageCars','GarageArea','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','MoSold',
 'YrSold',]

# Calculate skewness for each numeric column
skewed_columns = df.select_dtypes(include=[np.number]).apply(lambda x: x.skew())

# Extract the names of columns with skewness greater than a threshold (e.g., 0.5)
skew_threshold = 0.5
skew_features = skewed_columns[skewed_columns > skew_threshold].index.tolist()

# Now, 'skew_features' contains the names of columns with skewness greater than the threshold
print(skew_features)

for feature in skew_features:
    plt.figure(figsize=(15,6))
    sns.histplot(df1[feature],kde=True)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Density')
    plt.show()

df1=pd.get_dummies(df1,columns=object_columns,drop_first=True)

df1

corr1 = df1.corr()

correlation_threshold = 0.5

good_features=corr1[corr1['SalePrice'].abs() > correlation_threshold]['SalePrice'].index.tolist()

good_features.append('SalePrice')

df2 = corr1[good_features]

df2

X =df2.drop(['SalePrice'],axis=1)
y=df2['SalePrice']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
regression_model = LinearRegression()

regression_model.fit(X_train,y_train)

y_pred =regression_model.predict(X_test)

from sklearn.metrics import mean_squared_error,r2_score

mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
r2_linear = r2_score(y_test,y_pred)
print("Mean Squared Error:",mse)
print("Root Mean Squared Error:",rmse)
print("R-squared Score:",r2_linear)