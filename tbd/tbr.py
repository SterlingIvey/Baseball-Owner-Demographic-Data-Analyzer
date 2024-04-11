import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('value_over_time.csv')

plt.title('Tampa Bay Rays: Team Value Since 2002')

plt.show()

# Calculate annualized return

beginning_value = df['franchise_value'].iloc[0]