#programmer: Prasath Ram R

a = int(input())
b = int(input())
total = a

for _ in range(b):
    total = (total - int(input())) + a

print(total)
