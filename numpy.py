import numpy as np

# 创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数
arr = np.arange(12).reshape(3, 4)
print("原始数组：")
print(arr)
print()

# 查看数组的 shape、dtype、ndim 属性
print("数组的形状 (shape):", arr.shape)
print("数组的数据类型 (dtype):", arr.dtype)
print("数组的维度 (ndim):", arr.ndim)
print()

# 将数组变形为 (4,3)
arr_reshaped = arr.reshape(4, 3)
print("变形为 (4,3) 的数组：")
print(arr_reshaped)
print()

# 展平为一维数组
arr_flattened = arr.flatten()  # 或者使用 arr.ravel() 或 arr.reshape(-1)
print("展平为一维数组：")
print(arr_flattened)
print("展平后的形状:", arr_flattened.shape)