from collections import deque

dq = deque()

dq.append(3)  # Add to right → [3]
dq.append(5)  # Add to right → [3, 5]
dq.popleft()  # Remove from left → [5]
dq.pop()  # Remove from right → []

print(dq)  # Output: deque([])
dq.appendleft(1)  # Add to left → [1]
print(dq[0])  # Access first element → IndexError if deque is empty
