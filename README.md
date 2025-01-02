# Portfolio Simulation Tool

## Overview
This tool provides a simulation for evaluating the performance of a trading strategy over time. By varying parameters such as win rate, return on investment (ROI), and risk per trade, you can model how a portfolio evolves based on a series of trades.

---

## Features
- Simulates a series of trades with customizable parameters.
- Calculates portfolio value after each trade.
- Visualizes portfolio performance over time.
- Detects if the portfolio reaches ruin (value of zero or below).

---

## Requirements
- Python 3.x
- Libraries:
  - `numpy`
  - `matplotlib`

Install the required libraries using:
```bash
pip install numpy matplotlib
```

---

## Parameters
The simulation allows you to customize the following parameters:

- **`initial_portfolio`** *(float)*: Starting value of the portfolio. Default: `10000`
- **`win_rate`** *(float)*: Probability of a winning trade (e.g., `0.5` for 50%). Default: `0.5`
- **`win_roi`** *(float)*: Return on investment for winning trades (e.g., `2.0` for 200% ROI). Default: `2.0`
- **`loss_percentage`** *(float)*: Fraction of the risked amount lost on losing trades (e.g., `0.5` for 50%). Default: `0.5`
- **`risk_per_trade`** *(float)*: Fraction of the portfolio risked on each trade. Default: `0.01`
- **`num_trades`** *(int)*: Total number of trades to simulate. Default: `1000`

---

## Usage
1. **Define parameters:** Adjust the parameters based on your trading strategy.
2. **Run the simulation:** Use the provided `simulate_trades` function to simulate the portfolio performance.
3. **Visualize the results:** A plot will display portfolio value over time, highlighting the ruin threshold.

### Example
```python
# Import the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
initial_portfolio = 1000
win_rate = 0.3
win_roi = 3.0
loss_percentage = 0.7
risk_per_trade = 0.05
num_trades = 200

# Run simulation
portfolio, ruin = simulate_trades(
    initial_portfolio=initial_portfolio,
    win_rate=win_rate,
    win_roi=win_roi,
    loss_percentage=loss_percentage,
    risk_per_trade=risk_per_trade,
    num_trades=num_trades
)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(portfolio, label="Portfolio Value")
plt.axhline(0, color='red', linestyle='--', label="Ruin Threshold")
plt.title("Portfolio Simulation Over Time")
plt.xlabel("Trades")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid()
plt.show()

# Print result
if ruin:
    print("The portfolio reached ruin.")
else:
    print("The portfolio survived the simulation.")
```

---

## Outputs
- **`portfolio`** *(list)*: Portfolio value at each step.
- **`ruin`** *(bool)*: Indicates whether the portfolio value reached zero or below.

---

## License
This project is released under the MIT License. Feel free to use, modify, and share.

---

## Contact
For questions or contributions, feel free to reach out!

