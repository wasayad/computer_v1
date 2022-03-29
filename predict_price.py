import csv
import matplotlib.pyplot as plt
import sys

data = ""
try:
    with open('theta.txt', 'r') as f:
        data = f.read()
except:
    sys.exit("Train your model before trying to predict a price.")

theta = data.split(" ")

def estimate_price(km):
    return float(theta[0]) + float(theta[1]) * float(km)
try:
    print(estimate_price(sys.argv[1]))
except: 
    sys.exit("An error has occred with exec arg.")