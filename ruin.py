import numpy as np
import matplotlib.pyplot as plt

def simulate_trades(initial_portfolio=10000, win_rate=0.5, win_roi=2.0, loss_percentage=0.5, risk_per_trade=0.01, num_trades=1000):
    """
    Simulates a series of trades and calculates the portfolio over time.

    Parameters:
        initial_portfolio (float): Starting value of the portfolio.
        win_rate (float): Probability of a winning trade.
        win_roi (float): Return on investment for winning trades (e.g., 2.0 = 200% return).
        loss_percentage (float): Loss as a fraction of the risked amount on losing trades (e.g., 0.5 = 50% loss).
        risk_per_trade (float): Fraction of the portfolio risked on each trade.
        num_trades (int): Number of trades to simulate.

    Returns:
        portfolio (list): Portfolio value over time.
        ruin (bool): Whether the portfolio reaches zero or below.
    """
    portfolio = [initial_portfolio]
    for _ in range(num_trades):
        current_portfolio = portfolio[-1]
        risk_amount = current_portfolio * risk_per_trade

        if np.random.rand() < win_rate:
            # Winning trade
            profit = risk_amount * win_roi
            new_portfolio = current_portfolio + profit
        else:
            # Losing trade
            loss = risk_amount * loss_percentage
            new_portfolio = current_portfolio - loss

        # Append new portfolio value
        portfolio.append(new_portfolio)

        # Check for ruin
        if new_portfolio <= 0:
            return portfolio, True

    return portfolio, False

# Parameters
initial_portfolio = 1000
win_rate = 0.3  # 30
win_roi = 3.0   # 200% return on investment for winning trades
loss_percentage = 0.7  # 50% loss on losing trades
risk_per_trade = 0.05  # 2% of the portfolio risked per trade
num_trades = 200  # Number of trades

# Run simulation
portfolio, ruin = simulate_trades(
    initial_portfolio=initial_portfolio,
    win_rate=win_rate,
    win_roi=win_roi,
    loss_percentage=loss_percentage,
    risk_per_trade=risk_per_trade,
    num_trades=num_trades
)

# Plot portfolio over time
plt.figure(figsize=(10, 6))
plt.plot(portfolio, label="Portfolio Value")
plt.axhline(0, color='red', linestyle='--', label="Ruin Threshold")
plt.title("Portfolio Simulation Over Time")
plt.xlabel("Trades")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid()
plt.show()

# Output result
if ruin:
    print("The portfolio reached ruin.")
else:
    print("The portfolio survived the simulation.")
