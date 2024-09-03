"""
  @FileName array_handle
  @Description 
  @Author 久书
  @Data 2024/7/23 14:39
  @Version 1.0
"""
import numpy as np
import matplotlib.pyplot as plt

# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
# print(xs)
# zs = np.sqrt(xs ** 2 + ys ** 2)
# print(zs)
# plt.imshow(zs, cmap=plt.get_cmap('jet'))
# plt.title('Image plot of $\sqrt{xs^2 + ys^2}$ for a grid of values')
# plt.show()

# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])

# """"
#     where(condition, [x, y], /):
#         根据condition返回,x/y的元素
#     当仅提供 'condition' 时，此函数是 ''np.asarray（condition）.nonzero（）'' 的简写。
#     直接使用“nonzero”应该是首选，因为它对于子类的行为是正确的。
# """
# zarr = np.where(cond, xarr, yarr)
# print(zarr)

# arr = np.random.randn(4, 4)
# arr1 = np.random.randn(3, 3)
# print(arr)
# print(np.where(arr > 0, 1, -1))
# # [[ 1.07412227 -0.89988959 -1.42862674 -0.48433742]
# #  [ 0.85388065 -1.15168922 -2.2994721   1.17801869]
# # [-0.02056903  0.01658992 -0.66251106  0.73234217]
# # [-0.68449445 -1.40815878  1.20124381 -0.63892402]]
# # [[ 1 -1 -1 -1]
# #  [ 1 -1 -1  1]
# # [-1  1 -1  1]
# # [-1 -1  1 -1]]
#
# print(np.where(arr > 0, 1, arr))
# # [[-0.66384462  1.          1.          1.        ]
# #  [ 1.         -0.71134976  1.         -0.44296096]
# # [ 1.         -0.98135017 -0.51546953 -0.47090388]
# # [ 1.          1.          1.         -0.01663538]]

# arr = np.random.randn(4,4)
# print('arr的和等于：', arr.sum())
# sum1 = 0
# for elem_arr in arr:
#     for elem in elem_arr:
#         sum1 += elem
# print('sum1= ', sum1)
# print(sum1 / 16)
# print(arr)
# # 计算指定轴向的算数平均值
# x = arr.mean()
# y = np.mean(arr)
# print(x, '\n', y)
# print('\n', arr.mean(axis=1))
# print('\n', arr.sum(axis=1))

# arr = np.arange(10)
# print(arr)
# arr_sum = arr.cumsum()
# print(arr_sum)
# arr1 = np.arange(9).reshape(3, 3)
# print(arr1)
# # 返回数组元素在给定轴上的累积乘积。
# print(arr1.cumprod(axis=0))
# # 若未指定轴向则会被压缩为一个一维数组
# print(arr1.cumprod())
# # [0 1 2 3 4 5 6 7 8 9]
# # [ 0  1  3  6 10 15 21 28 36 45]
# # [[0 1 2]
# #  [3 4 5]
# # [6 7 8]]
# # [[ 0  1  2]
# #  [ 0  4 10]
# # [ 0 28 80]]
# # [0 0 0 0 0 0 0 0 0]

# arr = np.random.randn(100)
# print((arr > 0).sum())
# arr_bool = np.array([True, False, True, False])
# print(arr_bool.all())
# print(arr_bool.any())
# # 57
# # False
# # True
#
# arr = np.random.randn(6)
# print(arr)
# arr.sort()
# print(arr)
# # [0.70480627 0.4956195  0.2680823  0.31612777 0.89898296 0.53086524]
# # [0.2680823  0.31612777 0.4956195  0.53086524 0.70480627 0.89898296]
#
# arr1 = np.random.randn(3, 3)
# print(arr1)
# arr1.sort(axis=1)
# print(arr1)
# arr1.sort(axis=0)
# print(arr1)
# # [[-0.57557726  0.3814267   0.91631978]
# #  [ 0.37041056 -0.11733325 -0.82948637]
# #  [ 0.78834361  0.46324695  0.19573421]]
# # [[-0.57557726  0.3814267   0.91631978]
# #  [-0.82948637 -0.11733325  0.37041056]
# # [ 0.19573421  0.46324695  0.78834361]]
# # [[-0.82948637 -0.11733325  0.37041056]
# #  [-0.57557726  0.3814267   0.78834361]
# # [ 0.19573421  0.46324695  0.91631978]]

# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# name = np.unique(names)
# print(name, ' dtype=', name.dtype)

values = np.array([6, 0, 0, 3, 2, 5, 6])
is_exist = np.in1d(values, [1,4,2])
print(is_exist)
print(np.intersect1d(values, [2, 3, 6]))











