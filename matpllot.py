import matplotlib.pyplot as plt

x=[]
y=[]



reading=open("s.txt","r")


data=reading.read().split("\n")


for i in data:
    val=i.split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))
