from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path("us_treasury_yields_daily.csv")
lines = path.read_text().splitlines()

csv_reader = csv.reader(lines)
header_row = next(csv_reader)

# Extract dates, the one year yields, and twenty year yields.
dates, us_one_year_yields, us_twenty_year_yields = [], [], []
for row in csv_reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    one_year = float(row[4]) if row[4] else None
    twenty_year = float(row[10]) if row[10] else None
    dates.append(current_date)
    us_one_year_yields.append(one_year)

    us_twenty_year_yields.append(twenty_year)

# Plot the one year and twenty year yields
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, us_one_year_yields, color="blue")
ax.plot(dates, us_twenty_year_yields, color="orange")

# Format plot.
ax.set_title("United States One-Year and Twenty-Year Treasury Bill", fontsize=18)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Return (%)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
