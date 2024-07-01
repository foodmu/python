"""
  @ClassName 01numpy_base
  @Description 
  @Author 久书
  @Data 2024/6/30 23:06
  @Version 1.0
"""
import time

import numpy
import numpy as np

# arr = np.arange(10000)
# time1 = time.time()
# for i in arr[:10000]:
#     arr1 = arr * 2
#     # print(arr[i])
#     # print(arr1[i])
# time2 = time.time()
# print(time2 - time1)

data = np.random.randn(3, 3)
print(data)
data1 = data * 100
print(data1)
data1 += data1
print(data1)
print(data.shape, data.dtype)

# # 一个列表转换
# arr1 = [1,2,3,8.7]
# nparr1 = np.array(arr1)
# print(nparr1, nparr1.shape, nparr1.dtype)
# # 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组：
# arr2 = [[1,2,3],[4,5,6]]
# nparr2 = np.array(arr2)
# print(nparr2, '\n', nparr2.shape, nparr2.dtype)

nparr3 = np.zeros((3, 3), numpy.int32)
print(nparr3)
print(np.empty((3, 3)))
print(np.ones((3, 3)))

