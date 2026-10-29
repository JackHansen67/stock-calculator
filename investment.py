# Version 1 - Calculate Investment Cost

cost_per_share = 150
number_shares = 10
investment_cost = (cost_per_share * number_shares)
new_share_price = 175
new_investment_value = (new_share_price * number_shares)
profit_loss = (new_investment_value - investment_cost)
percetnage_return = (profit_loss/investment_cost) *100

print("Investment Cost")
print(f"Number of Shares: {number_shares}")
print(f"Purchase Price per Share: ${cost_per_share:.2f}")
print(f"Investment Cost: ${investment_cost:.2f}")

print("Investment Performance")
print(f"New Share Price: ${new_share_price:.2f}")
print(f"New Investment Value: ${new_investment_value:.2f}")
print(f"Profit or Loss: ${profit_loss:.2f}")
print(f"Percentage Return: {percentage_return:.2f}%)
