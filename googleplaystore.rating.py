import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("E:\\python  learning\\udemy\\GoogleAppRating-DataAnalysis-master\\googleplaystore.csv")
print(dataset.head)

dataset.info()
# type of data it is.
print(type(dataset))

print(dataset.shape)
  #summary stats.      
print(dataset.describe())

print(dataset.boxplot())

print(dataset.hist())


print(dataset.isnull().sum())
 # checking the rating is greater than 2 in the perticular column.
print(dataset[dataset.Rating >5])

# droping the perticular row contain outlier value.
print(dataset.drop([10472], inplace = True))
print(dataset[10470:10478])

print(dataset.boxplot())
print(dataset.hist())


# remove column which are 90% empty.(not necessory for this type of data.)
threshold = len(dataset)*0.1
print(threshold)

# droping the column having 90% of empty data.

dataset.dropna(thresh = threshold, axis = 1, inplace = True)
print(dataset.isnull().sum())

dataset['Rating'].fillna(dataset['Rating'].median(), inplace=True)

# checking mode value jor the perticular columns. some columns have more than 1 mode
print(dataset["Type"].mode())
print(dataset["Current Ver"].mode())
print(dataset["Android Ver"].mode())

dataset['Type'].fillna(dataset['Type'].mode()[0], inplace=True)

dataset['Current Ver'].fillna(dataset['Current Ver'].mode()[0], inplace=True)

dataset['Android Ver'].fillna(dataset['Android Ver'].mode()[0], inplace=True)

print(dataset.isnull().sum())


# lets convert price, review and install to numeric 
# removin the $ sign from the price column. here the values are converted into strings.
dataset["Price"] = dataset["Price"].apply(lambda x : str(x).replace("$"," ")if "$" in str(x) else str(x))

# now we have to convert these values into flot.
dataset["Price"] = dataset["Price"].apply(lambda x : float(x))   

# converting the reviews column to numeric, if error = ignore. 
dataset["Reviews"] = pd.to_numeric(dataset["Reviews"], errors = "coerce")

# removin the + sign from the installs column. here the values are converted into strings.
dataset["Installs"] = dataset["Installs"].apply(lambda x : str(x).replace("+"," ")if "+" in str(x) else str(x))

# removin the , sign from the installs column. here the values are converted into strings.
dataset["Installs"] = dataset["Installs"].apply(lambda x : str(x).replace(","," ")if "," in str(x) else str(x))

# converting the reviews column to numeric, if error = ignore. 
dataset["Installs"] = pd.to_numeric(dataset["Installs"], errors = "coerce")

dataset.info()
dataset["Price"].head(5)
dataset.describe()

# grouping the data on the basis of catogary
grp = dataset.groupby("Category")

x = grp["Rating"].agg(np.mean) 
y = grp["Price"].agg(np.sum)
z = grp["Reviews"].agg(np.mean)

print(x,y,z)

# ploting for x
plt.figure(figsize = (7,5))
plt.plot(x, "ro")
plt.xticks(rotation = 90)
plt.title("category wise ratings")
plt.xlabel("categories")
plt.ylabel("Ratings")
plt.show()

# ploting for y
plt.figure(figsize = (7,5))
plt.plot(y, "r--")
plt.xticks(rotation = 90)
plt.title("category wise ratings")
plt.xlabel("categories")
plt.ylabel("Ratings")
plt.show()

# ploting for z
plt.figure(figsize = (7,5))
plt.plot(z, "r^",color = "blue")
plt.xticks(rotation = 90)
plt.title("category wise ratings")
plt.xlabel("categories")
plt.ylabel("Ratings")
plt.show()


