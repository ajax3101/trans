import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ace_tools import display_dataframe_to_user

# Таблиця 2.3 – Зовнішні характеристики та падіння напруги у вольтах
table_2_3 = pd.DataFrame({
    "β": [0, 0.25, 0.5, 0.75, 1, 1.25],
    "U2(RL), B": [13800, 13797.52, 13795.03, 13792.55, 13790.07, 13787.58],
    "U2(R), B": [13800, 13798.88, 13797.76, 13796.64, 13795.52, 13794.4],
    "U2(RC), B": [13800, 13800.29, 13800.57, 13800.86, 13801.14, 13801.43],
    "dU2(RL), B": [0, 2.48, 4.97, 7.45, 9.93, 12.42],
    "dU2(R), B": [0, 1.12, 2.24, 3.36, 4.48, 5.6],
    "dU2(RC), B": [0, -0.29, -0.57, -0.86, -1.14, -1.43],
})

# Таблиця 2.4 – Зовнішні характеристики та падіння напруги у відсотках
table_2_4 = pd.DataFrame({
    "β": [0, 0.25, 0.5, 0.75, 1, 1.25],
    "U2(RL), %": [100, 99.48, 98.95, 98.43, 97.91, 97.38],
    "U2(R), %": [100, 99.76, 99.53, 99.29, 99.05, 98.82],
    "U2(RC), %": [100, 100.06, 100.12, 100.18, 100.24, 100.3],
    "dU2(RL), %": [0, 0.52, 1.05, 1.57, 2.09, 2.62],
    "dU2(R), %": [0, 0.24, 0.47, 0.71, 0.95, 1.18],
    "dU2(RC), %": [0, -0.06, -0.12, -0.18, -0.24, -0.3],
})

# Відображення таблиць
display_dataframe_to_user("Таблиця 2.3 – Вольти", table_2_3)
display_dataframe_to_user("Таблиця 2.4 – Відсотки", table_2_4)

# Побудова графіків
plt.figure()
plt.plot(table_2_3["β"], table_2_3["U2(RL), B"], label="U2(RL), B")
plt.plot(table_2_3["β"], table_2_3["U2(R), B"], label="U2(R), B")
plt.plot(table_2_3["β"], table_2_3["U2(RC), B"], label="U2(RC), B")
plt.xlabel("β")
plt.ylabel("U2, B")
plt.title("Зовнішні характеристики у вольтах")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(table_2_3["β"], table_2_3["dU2(RL), B"], label="dU2(RL), B")
plt.plot(table_2_3["β"], table_2_3["dU2(R), B"], label="dU2(R), B")
plt.plot(table_2_3["β"], table_2_3["dU2(RC), B"], label="dU2(RC), B")
plt.xlabel("β")
plt.ylabel("ΔU2, B")
plt.title("Падіння напруги у вольтах")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(table_2_4["β"], table_2_4["U2(RL), %"], label="U2(RL), %")
plt.plot(table_2_4["β"], table_2_4["U2(R), %"], label="U2(R), %")
plt.plot(table_2_4["β"], table_2_4["U2(RC), %"], label="U2(RC), %")
plt.xlabel("β")
plt.ylabel("U2, %")
plt.title("Зовнішні характеристики у відсотках")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(table_2_4["β"], table_2_4["dU2(RL), %"], label="dU2(RL), %")
plt.plot(table_2_4["β"], table_2_4["dU2(R), %"], label="dU2(R), %")
plt.plot(table_2_4["β"], table_2_4["dU2(RC), %"], label="dU2(RC), %")
plt.xlabel("β")
plt.ylabel("ΔU2, %")
plt.title("Падіння напруги у відсотках")
plt.legend()
plt.grid(True)
plt.show()
