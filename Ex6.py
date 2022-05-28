import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Salary_Data.csv")

print(data.head(10))

x = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

plt.scatter(x,y, color="green")
plt.xlabel("Exp")
plt.ylabel("Salary")
plt.title("Exp. vs Salary")

plt.show()

