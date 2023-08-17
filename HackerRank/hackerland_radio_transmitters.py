link: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def hackerLandRadioTransmitters(x: list, k):
    coverage = k + k
    house_number = len(range(min(x), max(x) + 1))
    if k >= house_number:
        return 1
    return round(house_number / coverage)


x = [7, 2, 4, 6, 5, 9, 12, 11]
x = [1, 2, 3, 4, 5]
# x = [2, 2, 2, 2, 1, 1, 1, 1]
k = 1

# ans is correct till the large input can't test with the huge amount of input

print(hackerLandRadioTransmitters(x, k))
