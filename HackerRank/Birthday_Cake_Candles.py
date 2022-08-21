candles = [3, 2, 1, 3]

count = 0
mx_candle = max(candles)

for i in candles:
    if mx_candle == i:
        count += 1

print(count)