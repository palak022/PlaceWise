import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("placement_data.csv")

# Basic Info
print(df.head())

# Placement Count
print("\nPlacement Count:\n", df['placement_status'].value_counts())

# Average Package
avg_package = df[df['placement_status']=='Placed']['package'].mean()
print("\nAverage Package:", avg_package)

# Branch-wise Placement
branch_data = df.groupby('branch')['placement_status'].value_counts()
print("\nBranch Analysis:\n", branch_data)

# Visualization
df['placement_status'].value_counts().plot(kind='bar')
plt.title("Placement Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()