import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('value_over_time.csv')

plt.title('Boston Red Sox: Team Value Since 2002')

plt.show()

# Calculate annualized return

beginning_value = df['franchise_value'].iloc[0]
ending_value = df['franchise_value'].iloc[1]
num_years = df['year'].iloc[-1] - df['year'].iloc[0]
annualized_return = ((ending_value / beginning_value) ** (1 / num_years)) - 1
annualized_return_percentage = annualized_return * 100

print(f"Annualized return since 2002: {annualized_return_percentage:.2f}%")