from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path("OHUR.csv")
lines = path.read_text().splitlines()

csv_reader = csv.reader(lines)
header_row = next(csv_reader)

# Extract dates, and high and low temperatures.
dates, unemployment_rates = [], []
for row in csv_reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    dates.append(current_date)
    unemployment_rates.append(float(row[1]))

print(dates)
# Plot the high and low temperatures.

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, unemployment_rates, color="red", alpha=0.5)
# ax.plot(dates, lows, color="blue", alpha=0.5)
# ax.fill_between(dates, ohur, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title("Ohio Unemployment Rate since 1975", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Unemployment Rate (%)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
