from sklearn.cluster import KMeans
import numpy as np
X=np.array([[1.713,1.586],[0.180,1.786],[0.353,1.240],[0.940,1.566],[1.486,0.786]])
y=np.array([0,1,1,0,1,0,1,1,1])
Kmeans=KMeans(n_clusters=3,random_state=0).fit(X,y)
print("the input data is")
print("VAR1\tVAR2\tCLASS")
i=0
for val in X:
	print(val[0],"\t",val[1],"\t",y[i])
	i+=1
print("="*20)
print("the test data to predict")
test_data=[]
VAR1=float(input("Enter value for VAR1:"))
VAR2=float(input("Enter value for VAR2:"))
test_data.append(VAR1)
test_data.append(VAR2)
print("="*20)
print("the predicted class is :",Kmeans.predict([test_data]))
