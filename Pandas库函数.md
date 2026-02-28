# Pandas库函数详解（新手必背）

## 一、Pandas数据结构
### 1. Series（一维数据）
```python
import pandas as pd
import numpy as np

# 创建Series
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s3 = pd.Series({'a': 1, 'b': 2, 'c': 3})

# 常用属性
s.values      # 获取值数组
s.index       # 获取索引
s.dtype       # 获取数据类型
s.size        # 元素个数
s.shape       # 形状
s.name        # 名称
# 创建DataFrame
df1 = pd.DataFrame([[1,2,3],[4,5,6]])
df2 = pd.DataFrame([[1,2,3],[4,5,6]], columns=['A','B','C'], index=['x','y'])
df3 = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]})

# 常用属性
df.shape      # (行数,列数)
df.columns    # 列名
df.index      # 行索引
df.dtypes     # 数据类型
df.values     # 转numpy
df.info()     # 基本信息
df.size       # 总元素数
二、数据读取与写入
1. 读取 CSV

pd.read_csv('file.csv')
pd.read_csv('file.csv', encoding='utf-8')
pd.read_csv('file.csv', header=None)
pd.read_csv('file.csv', names=['A','B','C'])
pd.read_csv('file.csv', index_col=0)
pd.read_csv('file.csv', usecols=[0,1,2])
pd.read_csv('file.csv', nrows=100)
pd.read_csv('file.csv', skiprows=2)
pd.read_csv('file.csv', na_values=['NA','NULL'])
2. 读取 Excel

pd.read_excel('file.xlsx')
pd.read_excel('file.xlsx', sheet_name='Sheet1')
pd.read_excel('file.xlsx', sheet_name=[0,1])
3. 写入文件

df.to_csv('file.csv')
df.to_csv('file.csv', index=False)
df.to_csv('file.csv', encoding='utf-8-sig')
df.to_excel('file.xlsx')
df.to_excel('file.xlsx', sheet_name='Sheet1')
三、数据查看与检查
1. 查看数据

df.head()
df.head(10)
df.tail()
df.tail(3)
df.sample(5)
df.sample(frac=0.1)
2. 基本信息
python
运行
df.info()
df.describe()
df.describe(include='all')
df.dtypes
df.columns
df.index
3. 统计信息
python
运行
df.count()
df.sum()
df.mean()
df.median()
df.mode()
df.std()
df.var()
df.min()
df.max()
df.quantile(0.25)
df.quantile([0.25,0.5,0.75])
df.cumsum()
df.cumprod()
四、数据选择与过滤
1. 选择列

df['A']
df[['A','B']]
df.A
2. 选择行
python
运行
df[0:3]
df[:5]
df[-5:]
3. loc & iloc
python
运行
# loc 标签
df.loc[0]
df.loc[0:5]
df.loc[0,'A']
df.loc[0:5,['A','C']]
df.loc[df['A']>5]

# iloc 位置
df.iloc[0]
df.iloc[0:5]
df.iloc[0,1]
df.iloc[0:5,0:3]
df.iloc[:,[0,2,4]]
4. 条件过滤
python
运行
# 单条件
df[df['A']>5]
df[df['A'].isin([1,3,5])]
df[df['A'].isnull()]
df[df['A'].notnull()]

# 多条件
df[(df['A']>5) & (df['B']<10)]
df[(df['A']>5) | (df['B']<10)]

# query
df.query('A>5')
df.query('A>5 and B<10')
df.query('A in [1,2,3]')
五、数据清洗
1. 缺失值

# 检查
df.isnull()
df.isnull().sum()
df.isnull().any()
df.isnull().sum().sum()

# 删除
df.dropna()
df.dropna(axis=1)
df.dropna(how='all')
df.dropna(thresh=3)
df.dropna(subset=['A','B'])

# 填充
df.fillna(0)
df.fillna(df.mean())
df.fillna(method='ffill')
df.fillna(method='bfill')
df['A'].fillna(df['A'].median())
df.fillna({'A':0,'B':1})
2. 重复值

df.duplicated()
df.duplicated(subset=['A'])
df.drop_duplicates()
df.drop_duplicates(keep='first')
df.drop_duplicates(keep='last')
df.drop_duplicates(keep=False)
3. 类型转换
df['A'].astype('int')
df['A'].astype('float')
df['A'].astype('str')
df['A'].astype('datetime64')
pd.to_numeric(df['A'])
pd.to_datetime(df['A'])
六、数据处理
1. 排序

df.sort_values('A')
df.sort_values('A', ascending=False)
df.sort_values(['A','B'])
df.sort_values(['A','B'], ascending=[True,False])
df.sort_index()
2. 添加 / 删除列
# 添加
df['新列'] = 0
df['新列'] = df['A']+df['B']
df.insert(1,'新列',0)

# 删除
df.drop('列名', axis=1)
df.drop(['A','B'], axis=1)
df.pop('列名')
3. 重命名
df.rename(columns={'旧名':'新名'})
df.rename(index={'旧行名':'新行名'})
df.rename(columns=str.upper)
df.columns = ['A','B','C']
4. 函数应用
df['A'].apply(lambda x:x*2)
df.apply(lambda x:x.mean())
df.apply(lambda x:x.mean(), axis=1)
df.applymap(lambda x:x*2)
df['A'].map({1:'a',2:'b'})
七、分组与聚合
1. groupby
df.groupby('A')
df.groupby(['A','B'])

df.groupby('A').sum()
df.groupby('A').mean()
df.groupby('A').count()
df.groupby('A').size()
df.groupby('A').agg('sum')
df.groupby('A').agg(['sum','mean','count'])
df.groupby('A').agg({'B':'sum','C':'mean'})

df.groupby('A')['B'].sum()
df.groupby('A')[['B','C']].mean()
df.groupby('A').get_group('值')
2. agg
df.agg('sum')
df.agg(['sum','mean'])
df.agg({'A':'sum','B':'mean'})
df.agg(x=('A','sum'), y=('B','mean'))

八、数据合并

1. concat
pd.concat([df1,df2])
pd.concat([df1,df2], axis=1)
pd.concat([df1,df2], ignore_index=True)
pd.concat([df1,df2], keys=['x','y'])

2. merge
pd.merge(df1,df2,on='key')
pd.merge(df1,df2,left_on='左键',right_on='右键')
pd.merge(df1,df2,on='key',how='left')
pd.merge(df1,df2,on='key',how='right')
pd.merge(df1,df2,on='key',how='outer')
pd.merge(df1,df2,on='key',how='inner')

3. join
df1.join(df2)
df1.join(df2,how='inner')
九、时间序列

1. 创建日期
pd.date_range('2023-01-01',periods=10)
pd.date_range('2023-01-01','2023-01-10')
pd.date_range('2023-01-01',periods=10,freq='D')
pd.date_range('2023-01-01',periods=10,freq='M')
pd.date_range('2023-01-01',periods=10,freq='Y')
pd.to_datetime(['2023-01-01','2023-01-02'])

2. 日期操作
df['日期'].dt.year
df['日期'].dt.month
df['日期'].dt.day
df['日期'].dt.weekday
df['日期'].dt.dayofweek
df['日期'].dt.quarter
df['日期'].dt.strftime('%Y-%m-%d')

十、数据透视表

pd.pivot_table(df,values='值列',index='行索引',columns='列索引')
pd.pivot_table(df,values='销售额',index='地区',columns='产品')
pd.pivot_table(df,values='销售额',index='地区',aggfunc='sum')
pd.pivot_table(df,values='销售额',index='地区',aggfunc=['sum','mean'])
pd.pivot_table(df,values='销售额',index='地区',fill_value=0)
pd.pivot_table(df,values='销售额',index='地区',margins=True)

十一、实用技巧

1. 显示设置
pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.precision',2)
pd.reset_option('all')

2. 抽样
df.sample(n=10)
df.sample(frac=0.1)

3. 排名
df['排名'] = df['分数'].rank()
df['排名'] = df['分数'].rank(method='dense')
df['排名'] = df['分数'].rank(ascending=False)

4. 替换
df['A'].where(df['A']>0,0)
df['A'].mask(df['A']<0,0)
df['A'].clip(lower=0,upper=100)
df.replace(1,100)
df.replace([1,2,3],0)

十二、新手代码模板

1. 导入查看
import pandas as pd
df = pd.read_csv('数据.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

2. 数据清洗
df = df.dropna()
df = df.drop_duplicates()
df['列名'] = df['列名'].astype('int')
df = df.rename(columns={'旧名':'新名'}
 
 3. 数据分析
df.groupby('分组列')['数值列'].mean()
df_filtered = df[(df['列1']>10) & (df['列2']=='值')]
df_sorted = df.sort_values('列名', ascending=False)
df['新列'] = df['列1']+df['列2']

4. 链式操作
result = (df.query('年龄>18')
          .groupby('城市')
          .agg({'收入':'mean','姓名':'count'})
          .sort_values('收入',ascending=False)
          .head(10))
