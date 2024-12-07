

items = [1,2,3,4,5]
squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]

new_items = []
for x in items:
    squared.append(func(x))
