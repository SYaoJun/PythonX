import numpy as np

# 创建一个样本数据
data = np.array([4, 8, 6, 5, 3, 2, 8, 9, 1, 7])

# 计算均值
mean_value = np.mean(data)

# 计算方差
variance_value = np.var(data)

print("数据集:", data)
print("均值:", mean_value)
print("方差:", variance_value)