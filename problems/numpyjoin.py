import numpy as np
np1=np.array([[1,2,3],[4,5,6]])
np2=np.array([[7,8,9],[10,11,12]])
num=np.hstack([np1,np2])
numa=np.vstack([np1,np2])
numb=np.dstack([np1,np2])
print(numb)