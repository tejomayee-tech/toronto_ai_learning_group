import pandas as pd
import matplotlib.pyplot as plot
import os

folder_path = os.path.dirname(__file__)
file_path = os.path.join(folder_path,"Session9-Sales.csv")

# data = pd.read_csv("EasyLearnPythonSessions/Sales.csv")
data = pd.read_csv(file_path)

plot.figure()
plot.plot(data["Month"],data["Sales"])

plot.xlabel("Month")
plot.ylabel("Sales")
plot.title("Sales Projections")

plot.show()

