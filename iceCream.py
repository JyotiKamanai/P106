import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature", y="Ice-cream Sales")
        fig.show()
def getDataSource(data_Path):
    iceCream_sales=[]
    coldDrink_sales=[]
    with open("IceCream.csv") as f:
        df = csv.DictReader(f)
        for row in df:
            iceCream_sales.append(float(row['Temperature']))
            coldDrink_sales.append(float(row['Ice-cream Sales']))
    return{"x": iceCream_sales, "y": coldDrink_sales}

def findCorrelation(datasource):
    correlation= np.corrcoef(datasource["x"],datasource["y"])
    print("Corelation between Ice-Cream and Cold Drink", correlation[0,1])

def setup():
    data_Path="IceCream.csv"
    data_source=getDataSource(data_Path)
    findCorrelation(data_source)
    plotFigure(data_Path)
setup()
