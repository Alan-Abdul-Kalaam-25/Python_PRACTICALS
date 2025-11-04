# Write a program to show the working of Bar Graphs.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
product_a = [1200, 1500, 1700, 1600, 1800, 2000]
product_b = [800, 950, 1100, 1050, 1150, 1300]
product_c = [400, 600, 700, 850, 900, 1000]

data = {
    "Month": months,
    "Product A": product_a,
    "Product B": product_b,
    "Product C": product_c,
}

df = pd.DataFrame(data)
df["Total Sales"] = df["Product A"] + df["Product B"] + df["Product C"]
df["Average Sales"] = (df["Total Sales"] / 3).round(1)

x = np.arange(len(months))
width = 0.25

plt.figure(figsize=(10, 6))
plt.bar(x - width, df["Product A"], width, label="Product A")
plt.bar(x, df["Product B"], width, label="Product B")
plt.bar(x + width, df["Product C"], width, label="Product C")

plt.plot(
    x,
    df["Average Sales"],
    marker="o",
    linestyle="--",
    color="black",
    label="Average Sales",
)

plt.title("Monthly Product Sales (Jan–Jun)")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.xticks(x, months)
plt.legend()

for i, v in enumerate(df["Average Sales"]):
    plt.text(i, v + 50, str(v), ha="center", fontsize=8)

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
