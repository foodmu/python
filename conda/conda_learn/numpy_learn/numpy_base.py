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

arr = np.arange(10000)
time1 = time.time()
for i in arr[:10000]:
    arr1 = arr * 2
    # print(arr[i])
    # print(arr1[i])
time2 = time.time()
print(time2 - time1)

data = np.random.randn(3, 3)
print(data)
data1 = data * 100
print(data1)
data1 += data1
print(data1)
print(data.shape, data.dtype)

# 一个列表转换
arr1 = [1,2,3,8.7]
nparr1 = np.array(arr1)
print(nparr1, nparr1.shape, nparr1.dtype)
# 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组：
arr2 = [[1,2,3],[4,5,6]]
nparr2 = np.array(arr2)
print(nparr2, '\n', nparr2.shape, nparr2.dtype)

nparr3 = np.zeros((3, 3), numpy.int32)
array4 = np.zeros_like(nparr3)
print('-------------------')
print(array4)
print('-------------------')
print(nparr3)
print(np.empty((3, 3)))
print(np.ones((3, 3)))

print(np.arange(20))
print(np.identity(5))

# 使用astype改变数据类型
arr2 = [[1,2,3],[4,5,6]]
nparr2 = np.array(arr2)
asarr = nparr2.astype(np.float32)
print(asarr)
print(asarr.dtype)


arr = [[1.,2., 3.], [4., 5., 6.], [7., 8., 9.]]
arr1 = np.array(arr)
print(arr1)
print(arr1 * arr1)
print(arr1 + 2)
print(1 / arr1)
# [[1. 2. 3.]
#  [4. 5. 6.]
# [7. 8. 9.]]
# [[ 1.  4.  9.]
#  [16. 25. 36.]
# [49. 64. 81.]]
# [[ 3.  4.  5.]
#  [ 6.  7.  8.]
# [ 9. 10. 11.]]
# [[1.         0.5        0.33333333]
#  [0.25       0.2        0.16666667]
# [0.14285714 0.125      0.11111111]]
arr = [[1.,2.3, 3.55], [3.1, 3.78, 6.1], [5.986, 8.1, 2.43]]
arr2 = np.array(arr)
print(arr2 > arr1)
# [[False  True  True]
#  [False False  True]
# [False  True False]]

arr = np.arange(10)
print(arr[4])
print(arr[2: 5])
arr[2: 5] = 20
print(arr)
# 4
# [2 3 4]
# [ 0  1 20 20 20  5  6  7  8  9]

# 创建arr切片，得到arr_slice视图
arr_slice = arr[2:5]
print(arr_slice)
# 修改arr_slice试图，arr也会随着修改
arr_slice[0: 2] = 1000
print(arr_slice)
print(arr)
arr[:] = 62
print(arr)
# [20 20 20]
# [1000 1000   20]
# [   0    1 1000 1000   20    5    6    7    8    9]
# [62 62 62 62 62 62 62 62 62 62]

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_arr = np.array(arr)
print(np_arr)
print(np_arr[0])
# [[1 2 3]
#  [4 5 6]
# [7 8 9]]
# [1 2 3]

print(np_arr[1][1])
print(np_arr[1, 1])

arr = np.arange(10)
print(arr[1: 7])
# [1 2 3 4 5 6]
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_arr = np.array(arr)
print(np_arr[1, :3])
# [[4 5 6]]

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print('data = \n', data)
print('names == \'Bob\': \n', names == 'Bob')
print('data[names == \'Bob\']: \n', data[names == 'Bob'])
# data =
# [[-2.06312192 -0.47269856 -1.92389771  0.91278498]
#  [-2.58358617 -0.03263164 -0.08267246 -0.69128665]
#  [ 0.52652726 -0.48812597  0.09661174  1.18237505]
# [-0.25987874 -1.07423519  0.52132457  0.04803203]
# [-0.16248655 -0.98312311 -0.35371249 -0.26627604]
# [-0.75293904 -1.11616931  0.17385702 -0.55176087]
# [ 0.71264865 -0.25099606  0.36425637  0.41166286]]
# names == 'Bob':
# [ True False False  True False False False]
# data[names == 'Bob']:
# [[-2.06312192 -0.47269856 -1.92389771  0.91278498]
#  [-0.25987874 -1.07423519  0.52132457  0.04803203]]
print('data[names != \'Bob\']: \n', data[names != 'Bob'])
print('data[names != \'Bob\']: \n', data[~(names == 'Bob')])
# data[names != 'Bob']:
# [[ 0.16468039 -1.03862911 -1.17996131  0.05199666]
#  [-1.43097098 -0.0990478   1.03564949  0.95265985]
# [-1.46271439 -2.02827434 -1.33157357 -1.14378972]
# [-0.66219836 -0.40306316 -0.62727381 -0.21806554]
# [ 0.40196128  1.11803113 -0.51840519 -1.18794547]]
# data[names != 'Bob']:
# [[ 0.16468039 -1.03862911 -1.17996131  0.05199666]
#  [-1.43097098 -0.0990478   1.03564949  0.95265985]
# [-1.46271439 -2.02827434 -1.33157357 -1.14378972]
# [-0.66219836 -0.40306316 -0.62727381 -0.21806554]
# [ 0.40196128  1.11803113 -0.51840519 -1.18794547]]

arr = np.arange(15).reshape(3, 5)
print(arr)
print(arr.T)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
# [10 11 12 13 14]]
# [[ 0  5 10]
#  [ 1  6 11]
# [ 2  7 12]
# [ 3  8 13]
# [ 4  9 14]]
print(np.dot(arr, arr.T))
# [[ 30  80 130]
#  [ 80 255 430]
# [130 430 730]]

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr[1, 1, 1])
print(arr.transpose(1, 0, 2))
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
# [10 11 12 13 14]]
# [[ 0  5 10]
#  [ 1  6 11]
# [ 2  7 12]
# [ 3  8 13]
# [ 4  9 14]]
# [[ 30  80 130]
#  [ 80 255 430]
# [130 430 730]]
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]

arr = np.arange(32).reshape(8, 4)
print(arr)
print(arr[[1, 3, 4]])
print(arr[[1, 3, 4], [0, 3, 2]])
# [[ 0  1  2  3]
#  [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]
# [16 17 18 19]
# [20 21 22 23]
# [24 25 26 27]
# [28 29 30 31]]

# [[ 4  5  6  7]
#  [12 13 14 15]
# [16 17 18 19]]

# [ 4 15 18]

arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))
# [0.         1.         1.41421356 1.73205081 2.         2.23606798
#  2.44948974 2.64575131 2.82842712 3.        ]

# [1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
#  5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03
#  2.98095799e+03 8.10308393e+03]

arr1 = np.random.randn(10)
arr2 = np.random.randn(10)
print(arr1)
print(arr2)
add_arr = np.add(arr1, arr2)
print(add_arr)
print(np.sqrt(add_arr))
max_arr = np.maximum(arr1, arr2)
print(max_arr)
# [ 1.38436386 -1.15920008 -0.14072652  0.18714392 -0.02133517 -0.45635813
#   2.23557513  0.60269672  0.57079306 -0.30629098]
# [-0.70702438  0.81761517  1.1078126  -2.25015848  0.32766901 -2.14322612
#  -0.18305529 -0.90640026  0.30361236  0.15709559]
# [ 0.67733948 -0.34158491  0.96708608 -2.06301456  0.30633383 -2.59958425
#   2.05251984 -0.30370355  0.87440541 -0.1491954 ]
# [0.82300637        nan 0.98340535        nan 0.55347433        nan
#  1.4326618         nan 0.93509647        nan]
# [ 1.38436386  0.81761517  1.1078126   0.18714392  0.32766901 -0.45635813
#   2.23557513  0.60269672  0.57079306  0.15709559]

arr1 = np.random.randn(10) * 10
arr_float, arr_int = np.modf(arr1)
print(arr_int)
print(arr_float)
# [  1.  -1.  -3.  17.  -9.   2.  -5.   1. -22.  -1.]
# [ 0.47596625 -0.74938756 -0.06916514  0.11201267 -0.19124248  0.72119225
#   -0.2189372   0.60465544 -0.75157779 -0.83174716]
