from operator import itemgetter

# l = [
#      {"name": "Json", "age": 23,"score": 120},
#      {"name": "John", "age": 20,"score": 80},
#     {"name": "Anna", "age": 18,"score": 70},
#      {"name": "Jony", "age": 19,"score": 95}
#      ]

# print("The list printed sorting by age: ")
# print(sorted(l, key=itemgetter('name', 'age', 'score')))

l = [
    ('Anna', 18, 70),
    ('Jony', 19, 95),
    ('John', 20, 80),
    ('Json', 23, 120)
]

print(sorted(l, key=itemgetter(0, 1, 2)))