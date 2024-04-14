import matplotlib.pyplot as plt
import pandas as pd
# Since OCR is not needed, we will manually input the data from the provided table.

# Creating a DataFrame from the given values
df_manual = pd.DataFrame({
    'Frequency': [20, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 150000, 200000],
    'Z': [-89.977, -89.970, -89.967, -89.961, -89.955, -89.945, -89.927, -89.907, -89.878, -89.832, -89.745, -89.507, -89.135]
})

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(df_manual['Frequency'], df_manual['Z'], marker='o', linestyle='-')
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('θ')
plt.title('Frequency vs θ (Capacitor)')
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()
