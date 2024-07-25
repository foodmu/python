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

arr = np.random.randn(4, 4)
arr1 = np.random.randn(3, 3)
print(arr)
print(np.where(arr > 0, 1, -1))
# [[ 1.07412227 -0.89988959 -1.42862674 -0.48433742]
#  [ 0.85388065 -1.15168922 -2.2994721   1.17801869]
# [-0.02056903  0.01658992 -0.66251106  0.73234217]
# [-0.68449445 -1.40815878  1.20124381 -0.63892402]]
# [[ 1 -1 -1 -1]
#  [ 1 -1 -1  1]
# [-1  1 -1  1]
# [-1 -1  1 -1]]

print(np.where(arr > 0, 1, arr))
# [[-0.66384462  1.          1.          1.        ]
#  [ 1.         -0.71134976  1.         -0.44296096]
# [ 1.         -0.98135017 -0.51546953 -0.47090388]
# [ 1.          1.          1.         -0.01663538]]
