import matplotlib.pyplot as plt
import csv
index1 = []
total_amt = []
average_weight = []
average_price = []
with open('2017pig.csv','r',encoding = 'utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    i=0
    for row in plots:
        if i>0:
            index1.append(i)
            total_amt.append(row[0])
            average_weight.append(float(row[1]))
            average_price.append(float(row[2]))
        i+=1
plt.plot(index1,total_amt, label='banana')
plt.xlabel('date')
plt.ylabel('NT$')
plt.ylim([15, 25])
plt.title('Market Average Price')
plt.legend()
plt.show()

