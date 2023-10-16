from collections import Counter
words = [ 
   'London', 'Oslo', 'Paris', 'Rome', 'Paris', 'Geneva', 'Paris', 'Milano', 
   'Geneva', 'Paris', 'Granada', 'Rome', 'Rome', 'London', 'London', 'Geneva', 
   'Geneva', "Oslo", 'Rome', 'Oslo', 'Oslo', 'Rome', 'Oslo', 'Rome', 
   'Geneva', 'Granada', "Granada", 'London']

print(Counter(words).most_common(4))
