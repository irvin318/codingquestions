def buy_sell_stock_prices(stock_prices):
    current_buy = stock_prices[0] #starting buying value
    global_sell = stock_prices[1] #starting selling value
    global_profit = global_sell - current_buy #starting profit

    for i in range(1, len(stock_prices)):
        current_profit = stock_prices[i] - current_buy #new profit value with new stock_price the next one in the array

        if current_profit > global_profit: #compare the new profit with original profit, if higher change the profit value and sell value
            global_profit = current_profit #new max profit
            global_sell = stock_prices[i] #new sell value

        if current_buy > stock_prices[i]: #if the new value is lower than the buy value, change the starting buy
            current_buy = stock_prices[i] #new buy value

    return global_sell - global_profit, global_sell #cannot return current buy as it only shows the lowest value, where it could be after sell

stock_price_1 = [8, 4, 12, 9, 20, 1]
stock_price_2 = [8, 6, 5, 4, 3, 2, 1]

print(buy_sell_stock_prices(stock_price_1))
print(buy_sell_stock_prices(stock_price_2))