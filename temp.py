import csv
import matplotlib.pyplot as plt
data = []
teta0 = 0
teta1 = 0
tmp0 = 1
tmp1 = 1

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if (row[0] != "km"):
            data.append([float(row[0]) / 100000, float(row[1]) / 100000])
km = []
price = []
for row in data:
    km.append(row[0] * 100000)
    price.append(row[1] * 100000)


    
def estimate_price(km, teta0, teta1):
    return teta0 + teta1 * km

def sum_theta0(teta0, teta1):
    sum = 0
    for row in data:
        sum += estimate_price(row[0], teta0, teta1) - row[1]
    return sum

def sum_theta1(teta0, teta1):
    sum = 0
    for row in data:
        sum += (estimate_price(row[0], teta0, teta1) - row[1]) * row[0]
    return sum


for i in range(1000):
    tmp0 -=  0.1 * (1 / len(data)) * sum_theta0(teta0, teta1)
    tmp1 -=  0.1 * (1 / len(data)) * sum_theta1(teta0, teta1)
    teta0 = tmp0
    teta1 = tmp1

teta0 *= 100000
to_write = str(teta0) + " "+ str(teta1)
with open('theta.txt', 'w') as f:
    f.write(to_write)
plt.plot(km, price, ".", [km[22], km[0]], [estimate_price(km[22], teta0, teta1), estimate_price(km[0], teta0, teta1)])
plt.show() 