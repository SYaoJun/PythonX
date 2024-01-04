import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
sales_data = pd.read_csv('sales_data.csv')

# 显示数据集的前几行
print(sales_data.head())

# 获取销售额总和和平均销售额
total_sales = sales_data['Sales'].sum()
average_sales = sales_data['Sales'].mean()

print(f'Total Sales: ${total_sales:.2f}')
print(f'Average Sales: ${average_sales:.2f}')

# 根据日期绘制销售趋势图
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data.set_index('Date', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(sales_data['Sales'])
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
