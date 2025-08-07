import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://raw.githubusercontent.com/kindo-tk/PRODIGY_DS_01/main/worldpopulationdata.csv"
df = pd.read_csv(url)

# Rename columns for convenience (optional)
df = df.rename(columns={'Country Name': 'Country', '2022': 'Population_2022'})

# Bar chart: Top 10 most populous countries in 2022
top10 = df.nlargest(10, 'Population_2022').set_index('Country')

plt.figure(figsize=(12, 6))
sns.barplot(x=top10.index, y=top10['Population_2022'], palette='viridis')
plt.title('Top 10 Most Populous Countries (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram: Distribution of all countries' population in 2022
plt.figure(figsize=(8, 5))
sns.histplot(df['Population_2022'], bins=30, log_scale=(False, True), color='skyblue')
plt.title('Distribution of Country Populations (2022)')
plt.xlabel('Population')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
