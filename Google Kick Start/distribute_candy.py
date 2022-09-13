def distribute_candy(test_cases):
    num_candy_bags, num_kids = map(int, input().split())
    candy_count = list(map(int, input().split()))
    total_candy = sum(candy_count)
    print(f"Case #{test_cases}: {total_candy % num_kids}")

test_cast = int(input())
for x in range(test_cast):
    distribute_candy(x+1)




