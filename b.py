import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
n = np.arange(-20, 20)
l = np.size(n)
imp = np.zeros(l)


arrx = []
arry = []
num = int(input("how many points do you want to add ? : "))
for i in range(0, num):
    x = float(input("x : "))
    arrx.append(x)
    y = float(input("y : "))
    arry.append(y)


while(True):
    method = int(input("what do  you want to do :\n1- reverse \n2- shift \n3- scale\n: "))
    if method == 1:
        for i in range(0, num):
            arrx[i] = arrx[i] * -1
    elif method == 2:
        shift = int(input("Enter the number you want to shift by : "))
        for i in range(0, num):
            arrx[i] = arrx[i] - shift
    elif method == 3:
        arrxNew = sorted(arrx)
        arryFinal = []
        scale = float(input("Enter the number you want to scale by : "))
        if scale >= 1:
            scale = int(scale)
            for i in range(0, num):
                if arrx[i] < 0:

                    if arrx[i]*scale >= arrxNew[0]:
                        for k in range(0, num):
                            if arrx[k] == arrx[i]*scale:
                                loc = k
                        arryFinal.append(arry[loc])

                    else:
                        arryFinal.append(0)
                elif arrx[i] > 0:
                    if arrx[i]*scale <= arrxNew[num - 1]:
                        for k in range(0, num):
                            if arrx[k] == arrx[i]*scale:
                                loc = k
                        arryFinal.append(arry[loc])

                    else:
                        arryFinal.append(0)
                else:
                    for k in range(0, num):
                        if arrx[k] == 0:
                            loc = k
                    arryFinal.append(arry[loc])
        elif scale < 1:
            for i in range(0, num):
                if arrx[i] < 0:

                    if arrx[i]*scale >= arrxNew[0]:
                        if (arrx[i] * scale - int(arrx[i] * scale)) == 0:

                            for k in range(0, num):
                                if arrx[k] == arrx[i]*scale and (arrx[i]*scale - int(arrx[i]*scale)) == 0:
                                    loc = k
                            arryFinal.append(arry[loc])
                        else:
                            arryFinal.append(0)
                    else:
                        arryFinal.append(0)
                elif arrx[i] > 0:
                    if arrx[i]*scale <= arrxNew[num - 1]:
                        if (arrx[i] * scale - int(arrx[i] * scale)) == 0:
                            for k in range(0, num):
                                if arrx[k] == arrx[i]*scale and (arrx[i]*scale - int(arrx[i]*scale)) == 0:
                                    loc = k
                            arryFinal.append(arry[loc])
                        else:
                            arryFinal.append(0)
                    else:
                        arryFinal.append(0)
                else:
                    for k in range(0, num):
                        if arrx[k] == 0:
                            loc = k
                    arryFinal.append(arry[loc])
    else:
        False
        break
if method == 3:
    for j in range(0, num):
        ind = np.where(n == arrx[j])
        imp[ind] = arryFinal[j]
else:
    for j in range(0,num):
        ind = np.where(n == arrx[j])
        imp[ind] = arry[j]

plt.stem(n, imp)
plt.xlabel('sample Number')
plt.ylabel('Amplitude')
plt.show()
