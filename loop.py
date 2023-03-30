sum = 0
for i in range(101):
    sum += i

# print(sum)

sum = 0
n = 9
while n > 0:
    sum += i
    n -= 2
# print(sum, n)

L = ["Bart", "Lisa", "Adam"]
for i in L:
    # print(f"Hello, {i}!")
    pass

L = [
    {"name": "Bart", "age": 12},
    {"name": "Lisa", "age": 6},
    {"name": "Adam", "age": 4},
]
for i in L:
    # print("Hello, %s! You are %d years old ~" % (i.get("name"), i.get("age")))
    pass

l = {
    "Bart": 12,
    "Lisa": 4,
    "Adam": 6,
}
for i in l.keys():
    print("Hello, %s! You are %d years old ~" % (i, l[i]))
    pass

