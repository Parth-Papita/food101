import numpy as np

def dot(arr1, arr2):
    n1  = arr1.shape
    n2 = arr2.shape
    if(n1!=n2):
        print("The shape of both matrices is different and hence there dot product does not exists")
    else:
        arr = np.empty(n1)
        for i in range (0,n1[0]):
            for j in range (0,n1[1]):
                arr[i,j] = arr1[i,j] * arr2[i,j]
        
        print("The resultant matrix after dot product is : \n" , arr)


def multiplication(arr1 , arr2):
    n1 = arr1.shape
    n2 = arr2.shape
    if(n1[1]!=n2[0]):
        print("The number of columns in first matrix and number of rows in second matrix are not the same and hence matrix multiplication is not possible here")
    
    else:
        arr = np.empty((n1[0] , n2[1]))
        for i in range (0,n1[0]):
            for j in range (0,n2[1]):
                for k in range (0,n1[1]):
                    arr[i,j] += arr1[i,k] * arr2[k,j]
        print("The resultant matrix after matrix multiplication is : \n",arr)

