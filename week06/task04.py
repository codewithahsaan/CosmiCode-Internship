from collections import Counter, defaultdict, deque

# Counter Example (counts frequency of elements)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print("🔢 Word Count using Counter:", word_count)

# defaultdict Example (default value if key not found)
scores = defaultdict(int)  # default value = 0
scores["Ali"] += 10
scores["Sara"] += 15
print("📊 Scores using defaultdict:", dict(scores))

# deque Example (efficient double-ended queue)
d = deque([1, 2, 3])
d.append(4)       # add right
d.appendleft(0)   # add left
d.pop()           # remove right
d.popleft()       # remove left
print("📂 Deque after operations:", d)
