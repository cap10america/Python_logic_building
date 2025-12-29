def best_time_tobuy_sell_stock(arr):
    profit=0
    min_price= float('inf')
    for price in arr:
        min_price= min (price , min_price)
        profit =max(price - min_price,profit)
    return profit ,min_price ,f"the best time to buy stock at this price : {min_price}  nd the profit will be high at if we sell it at  : {profit + min_price } the profit will be : {profit} "
print(best_time_tobuy_sell_stock([1,6,7,8,92,3,4,5]))
