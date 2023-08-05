# Расчет финансовых показателей портфеля акций
import stock_portfolio.portfolio as pf

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

start_value = pf.calculate_portfolio_value(stocks, prices)
print(f"Начальная стоимость портфеля: {start_value}")

prices["AAPL"] = 250
current_value = pf.calculate_portfolio_value(stocks, prices)
print(f"Текущая стоимость портфеля: {current_value}")

portfolio_return = pf.calculate_portfolio_return(current_value)
print(f"Доходность портфеля: {portfolio_return}%")

prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
top_stock = pf.get_most_profitable_stock(prices)
print(f"Самая дорогая акция: {top_stock}")
