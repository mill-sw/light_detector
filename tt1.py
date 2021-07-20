import csv
import os
import matplotlib.pyplot as plt
import numpy as np


f = open("test2.csv", 'r', encoding='utf-8')
rdr = csv.reader(f)
for line1 in rdr:
    # print(line1)
    break

data = []
date = None
for line1 in rdr:
    if date == None:
        date = line1[10][:10]
        data.append([line1[10][11:], line1[4]])
        continue
    if date != line1[10][:10]:

        # for k in range(len(data)):
        #
        #     data[k].append(int(data[k][0][:2]) + int(data[k][0][3:5])/60.0)
        #
        #
        # for k in range(len(data)):
        #     if k == 0:
        #         data[k].append(0)
        #     else:
        #         dif = int(data[k][1]) - int(data[k-1][1])
        #         if dif != 0:
        #             data[k].append(dif/5)#threshold
        #         else:
        #             data[k].append(0)
        #
        # fig = plt.figure()
        # plt.plot([i[2] for i in data],[int(i[1]) for i in data])
        # plt.plot([i[2] for i in data],[int(i[3])-10 for i in data])
        # # plt.xticks([i for i in range(len(data)) if i % 6 == 0], [i for i in range(24)])
        # plt.show()
        #
        #
        # k = 10
        # plt.close()
        f1 = open("data/" + date + ".csv", 'w', encoding='euc-kr')
        f1.write(
            '"등록일시","조도"\n')
        for a in data:
            f1.writelines(",".join(a))
            f1.write("\n")
        f1.close()
        date = line1[10][:10]
        data = []
    else:
        data.append([line1[10][11:], line1[4]])

    # print("시간 " + line1[9] + "\t조도 " + line1[4])