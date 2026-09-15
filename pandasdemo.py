import pandas as pd

#to check the version
print(pd.__version__)

#create a dataset
dataset = {
            "cars":["BMW", "Volvo", "Ford"],
            "price": [1000,2000,1500]
}

#to view the dataset in a row column manner
myvar = pd.DataFrame(dataset)
print(myvar)

print("****************************")
#series create a one dimentional array of the given dataset
print("Series")

myvar1 = pd.Series(dataset)

myvar2 = pd.Series(dataset, index=["price"])

print(myvar1)
print("Limited Series")
print(myvar2)

print("*****************************")
#to create a visual data with index of our own
print("INDEXING")
myind = pd.DataFrame(dataset, index = ["a", "b",  "c"])
print(myind)


print("*****************************")
#calling values with labels
print("Value called with the index number")
print(myind.iloc[0])

print("Value called with label")
print(myind.loc["a"])





print("-------------------------xxxxxx-------------------------------")

print("Read File")

myfile = pd.read_csv(r"C:\Users\KiTE\Downloads\datass\cities.csv")
print(myfile)
pd.options.display.max_rows = 9999
print(myfile.to_string)
print(pd.options.display.max_rows)

print("*************************")
#Read specific columns using read_csv
myfile1 = pd.read_csv(r"C:\Users\KiTE\Downloads\datass\cities.csv", usecols = ["City", "Country"])
print(myfile1)

print("***************************************")
myfile2 = pd.read_csv(r"C:\Users\KiTE\Downloads\datass\cities.csv", index_col="City")
print(myfile2)


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(myfile2.loc["Tokyo"])

print("########################3333")
print(myvar.iloc[1])

print("###############################################")

myfile3 = pd.read_csv(r"C:\Users\KiTE\Downloads\datass\cities.csv", nrows = 3)
print(myfile3)

print("#######################################333")
myfile4 = pd.read_csv(r"C:\Users\KiTE\Downloads\datass\cities.csv", usecols = [ "Country", "City"], nrows = 3)
print(myfile4)


print("**********************************************")
print("WRITING INTO AN CSV FILE")
#to create a new dataset

df = {
        "animals" :["parrot", "dog", "cat"],
        "colours" : ["green", "orange", "white"]
}

df2 = pd.DataFrame(df)
print(df2)

df2.to_csv("D:\pylibs\datademo", header = False, index = False)

df1 = pd.read_csv(r"D:\pylibs\datademo", header = None)
print(df1)


df3 = {
        "animals" :["p", "d", "c"],
        "colours" : ["gren", "orang", "whit"]
}

df4 = pd.DataFrame(df3)
print(df4)

df4.to_csv("D:\pylibs\datasdemo", sep = "\t", index = False)

df5 = pd.read_csv(r"D:\pylibs\datasdemo", sep = "\t")
print(df5)


print("*********************************************")
da = pd.read_csv()