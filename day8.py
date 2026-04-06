import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MedHouseVal'] = housing.target

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

print(df['MedHouseVal'].mean())
print(df.groupby(pd.cut(df['MedHouseVal'], bins=5)).size())

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['MedInc'], df['MedHouseVal'], alpha=0.5, s=10)
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('California Housing: Income vs House Value')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(x, y, 'b-', linewidth=2)
plt.plot(x, y, 'ro', markersize=2, alpha=0.5)
plt.xlabel('X')
plt.ylabel('sin(X)')
plt.title('Sine Curve')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()

correlation = df.corr()['MedHouseVal'].sort_values(ascending=False)
print(correlation)