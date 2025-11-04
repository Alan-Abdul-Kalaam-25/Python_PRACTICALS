# Write a program to show the working of Pie Chart.

import matplotlib.pyplot as plt

brands = ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo", "Others"]
market_share = [22.5, 19.7, 12.8, 9.3, 8.1, 27.6]

colors = ["#4285F4", "#34A853", "#FBBC05", "#EA4335", "#AB47BC", "#8D6E63"]
explode = [0.05, 0.05, 0, 0, 0, 0]  # slightly separate top two slices

plt.figure(figsize=(8, 8))
plt.pie(
    market_share,
    labels=brands,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    shadow=True,
    explode=explode,
    textprops={"fontsize": 10},
)

plt.title(
    "Global Smartphone Market Share – 2025 (Approx.)", fontsize=13, fontweight="bold"
)
plt.legend(title="Brands", loc="upper right")
plt.tight_layout()
plt.show()
