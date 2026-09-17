[Sample - Superstore.csv](https://github.com/user-attachments/files/32339793/Sample.-.Superstore.csv)# Retail Sales Data Analysis (零售销售数据分析)

## 📌 项目背景
基于Sample-Superstore的2014-2017年历史数据（9994行，21列），旨在通过Python数据分析，找出影响利润的核心因素，为业务运营提供优化方向。

## 🛠️ 使用工具
*   Python (Pandas, NumPy, Matplotlib)
*   数据分析方法：多维度交叉分析、分组聚合、趋势分析

## 📊 核心发现
1. **利润黑洞**：Furniture（家具）品类利润极低，其中Tables（桌子）子品类严重亏损。
2. **折扣陷阱**：亏损订单的平均折扣高达0.48，折扣超过0.3后平均利润转负。
3. **地区与客群**：West和East地区贡献主要利润；Consumer（消费者）是最核心的利润来源。

*(在此处插入你的图表，如：各产品类别总利润.png)*

## 💡 运营优化建议
1. **折扣管控**：对Tables等高亏损产品设置折扣上限（30%），高折扣订单需单独审批。
2. **精准营销**：针对利润贡献最大的Consumer客群，设计会员与复购活动以提升LTV（用户生命周期价值）。
3. **区域策略**：重点投入West与East地区，排查Central地区低利润的真实原因（成本或产品结构）。

## 📁 文件说明
*   `sales_analysis.py`：Python分析源码
*   `Sample-Superstore.csv`：原始数据
*   `task1__pictures`：生成的各项可视化图表
*   `Superstore销售数据分析报告.pdf`：完整版分析报告
