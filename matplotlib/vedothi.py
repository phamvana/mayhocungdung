from matplotlib import pyplot
import numpy as np
X = [1,2,4]
Y = [2,3,6]
#pyplot.plot(X, Y,"ro", color='red')
#pyplot.grid(True)
#pyplot.legend("Ve bieu do")
#pyplot.show()

# Ham LR1
def LR1(X,Y,eta,lanlap,theta0,theta1):
    m = len(X) # So luong phan tu cua X
    for k in range(0,lanlap):
        print("Lan lap: ",k)
        for i in range(0,m):
            h_i = theta0 + theta1 * X[i]
            #theta0
            theta0 = theta0 + eta*(Y[i]-h_i)*1
            print("Phan tu ", i, "y = ", Y[i], "h = ", round(h_i,3), "gia tro theta0", round(theta0,3))
            # theta1
            theta1 = theta1 + eta*(Y[i]-h_i)*X[i]
            print("Phan tu ", i, "gia tri theta1 = ", round(theta1,3))
    return [round(theta0,3), round(theta1,3)]

theta = LR1(X,Y, 0.1,1,0,1)     

X1 = np.array([1,6])
Y1 = theta[0] + theta[1]*X1

theta2 = LR1(X,Y,0.1,2,0,1) 
X2 = np.array([1,6])
Y2 = theta2[0]+ theta2[1]*X2

pyplot.axis([0,7,0,10])
pyplot.plot(X,Y,"ro","blue")

pyplot.plot(X1,Y1,"violet")
pyplot.plot(X2, Y2,"green")

pyplot.xlabel("Gia tri thuoc tinh X")
pyplot.ylabel("Gia tri du doan Y")
pyplot.show()

XX = [0,3,5]
for i in range(0,3):
    YY=theta[0]+theta[1]*XX[i]
    print(round(YY,3))