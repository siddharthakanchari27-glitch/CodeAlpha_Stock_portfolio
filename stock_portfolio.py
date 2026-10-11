# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter the stocks you own.")
print("Type 'done' to finish.\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number.")

print("\n===== Your Stock Portfolio =====")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(
        f"{stock}: {quantity} shares "
        f"x ${stock_prices[stock]} = ${investment}"
    )

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save the result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("=======================\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares = ${investment}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_investment}\n")

print("Portfolio saved to portfolio.txt")
