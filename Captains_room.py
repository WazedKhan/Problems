k, rooms, multiple = input(), input().split(), set()
single = set(rooms)
for room in rooms:
    if room in multiple:
        multiple.add(room)

print(single.difference(multiple).pop())