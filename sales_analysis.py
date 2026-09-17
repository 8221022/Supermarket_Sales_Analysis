#%%

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#让图表在 notebook 里显示
# %matplotlib inline

# 读取数据
df  =pd.read_csv('Sample - Superstore.csv' , encoding='latin1')

df.head()

##=查看数据的基本信息
df.info()

#%%
#查看数据的基本统计信息

df.describe()

#计算总销售额和总利润
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"总销售额：${total_sales:,.0f}")
print(f'总利润：${total_profit:,.0f}')

#计算利润率
profit_margin = (total_profit / total_sales) * 100
print(f'利润率：{profit_margin:.2f}%')
#%%
# 按类型分组，计算总销售额和总利润
category_profit = df.groupby('Category')['Profit'].sum().sort_values()
category_sales = df.groupby('Category')['Sales'].sum()
# 绘制利润图
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure(figsize=(10, 6))
category_profit.plot(kind ='bar',color=['red','blue','green'])
plt.title('各产品类别总利润',)
plt.ylabel('总利润')
plt.show()

print(category_profit)

#%%
subcat_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values()

#绘制利润图
plt.figure(figsize=(10, 6))
subcat_profit.plot(kind ='bar',color=['red','blue','green'])
plt.title('各产品子类别总利润',)
plt.ylabel('总利润')
plt.show()

print("最赚钱的5个子类别：")
print(subcat_profit.tail(5))
print('最不赚钱的5个子类别：')
print(subcat_profit.head(5))


#%%
# 按地区分组，计算总销售额和总利润
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
region_sales = df.groupby('Region')['Sales'].sum()
# 绘制利润图
plt.figure(figsize=(10, 6))
region_profit.plot(kind='bar',color=['gold','green','blue','silver'])
plt.title('各地区总利润')
plt.ylabel('总利润')
plt.xlabel('地区')
plt.show()
print(region_profit)



#%%
# 利润和打折之间的关系

loss_df =df[df['Profit'] < 0]

#计算亏损订单的平均折扣
avg_discount_loss = loss_df['Discount'].mean()

#计算非亏损订单的平均折扣

impro_df = df[df['Profit'] >= 0]

#计算非亏损订单的平均折扣
avg_discount_impro = impro_df['Discount'].mean()
print(f"亏损订单的平均折扣：{avg_discount_loss:.2f}")
print(f"增长订单的平均折扣：{avg_discount_impro:.2f}")

#可视化：绘制不同折扣区间的平均利润
discount_groups =df.groupby(pd.cut(df['Discount'],bins=[0,0.1,0.2,0.3,0.4,0.5,0.8]),observed= True)
avg_profit_by_discount = discount_groups['Profit'].mean()

plt.figure(figsize=(10, 6))
avg_profit_by_discount.plot(kind='bar',color=['red','blue','green','yellow','purple','pink','orange'])
plt.title('不同折扣区间的平均利润')
plt.ylabel('平均利润')
plt.xlabel('折扣区间')
plt.show()

#根据上述切分得到的区间标签对数据框 df 进行分组，所有折扣落在同一区间的行被归为一组。
#%%
# 按客户细分分组，计算总利润和总销售额
segment_profit = df.groupby('Segment')['Profit'].sum().sort_values()

plt.figure(figsize=(8, 6))
segment_profit.plot(kind='bar')
plt.title('不同客户细分的总利润')
plt.ylabel('总利润')
plt.show()

print(segment_profit)
#%%
