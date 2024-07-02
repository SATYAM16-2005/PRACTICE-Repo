#Seaborn is a well-known Python library for data visualization that offers a user-friendly interface for producing visually appealing and informative statistical graphics. 

#Example: Date and time Graph
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='H')
data = pd.DataFrame(date_rng, columns=['date'])
data['data'] = np.random.randn(len(date_rng))


data.set_index('date', inplace=True)


plt.figure(figsize=(14, 7))
sns.lineplot(x=data.index, y='data', data=data)


plt.title('Date and Time Graph using Seaborn', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


#EXAMPLE
import seaborn as sns
import matplotlib as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

sns.lineplot(x=x,y=y)
data=sns.load_dataset("flights")
sns.lineplot(x="year",y="passengers",data=data)
sns.lineplot(x="year",y="passengers",data=data,hue="month",style="month",markers=True,dashes=False)   
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
sns.lineplot(x="year",y="passengers",data=data,hue="month",style="month",markers=True,dashes=False)   # hue is just like to give extra information of a particular (month )
plt.title("monthly passenger")
plt.xlabel("year")
plt.ylabel("no of passengers")
plt.show()

# Example: Histogram 
import seaborn as sns
import matplotlib.pyplot as plt

data = [12, 15, 14, 10, 12, 16, 14, 13, 15, 12, 14, 13, 12, 11, 15, 16, 13, 14, 15, 16, 17, 18, 19, 20, 21, 15, 16, 17, 18, 19, 20]
sns.histplot(data, kde=True)
plt.show()

# Example
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Sex': ['Male', 'Female'] * 50,
    'Count': [100] * 50 + [95] * 50
}
df = pd.DataFrame(data)

sns.histplot(df, x='Sex', weights='Count', discrete=True)

plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Male-Female Sex Ratio')
plt.show()


#Example:Barplot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
}
df = pd.DataFrame(data)

sns.barplot(x='Category', y='Value', data=df)

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()


#Example:Scatterplot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50),
    'category': np.random.choice(['A', 'B', 'C'], 50)
})


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='x', y='y', hue='category', style='category', palette='deep', s=100)


plt.title('Scatter Plot using Seaborn and Matplotlib', fontsize=16)
plt.xlabel('X-axis Label', fontsize=14)
plt.ylabel('Y-axis Label', fontsize=14)
plt.legend(title='Category')
plt.grid(True)
plt.show()

#Example:KDEPLOT
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = np.random.randn(100)


plt.figure(figsize=(10, 6))
sns.kdeplot(data, shade=True)


plt.title('Graph', fontsize=16)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.grid(True)
plt.show()

#Example:Rugplot
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = np.random.randn(100)

plt.figure(figsize=(10, 6))
sns.rugplot(data, height=0.5)

plt.title('Rug Plot using Seaborn', fontsize=16)
plt.xlabel('Values', fontsize=14)
plt.grid(True)
plt.show()



#Example:Boxplot
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = np.random.randn(100)

plt.figure(figsize=(10, 6))
sns.boxplot(data)


plt.title('Box Plot using Seaborn', fontsize=16)
plt.ylabel('Values', fontsize=14)
plt.grid(True)
plt.show()

#Example:Violinplot
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(0)
data = np.random.randn(100)
plt.figure(figsize=(10, 6))
sns.violinplot(data, inner='quartile')
plt.title('Violin Plot using Seaborn', fontsize=16)
plt.ylabel('Values', fontsize=14)
plt.grid(True)
plt.show()





