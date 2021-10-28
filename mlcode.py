import pandas
import numpy

dataset = pandas.read_csv("SalaryData.csv")

print(dataset)

x = dataset["YearsExperience"]
y = dataset["Salary"]

X = x.values.reshape(-1,1)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model_fit = model.fit(X,y)

print(model_fit)

print(" Aap apna year of Experience put kare : " )

a = input()
s = model.predict( [[ a ]] )

print(s)
