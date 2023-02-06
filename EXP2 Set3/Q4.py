def display_items(tup):
  count = {}
  for item in tup:
    if item in count:
      count[item] += 1
    else:
      count[item] = 1

  duplicates = []
  for item, frequency in count.items():
    if frequency > 1:
      duplicates.append(item)

  print("The items with duplicate elements in the tuple are:", duplicates)
  print("The number of items in the tuple is:", len(tup))