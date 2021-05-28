#programmer : Prasath Ram R

your_name = input(" Enter Name: ")
abbrev = ""

for name in your_name.split("-"):
abbrev = abbrev + name[0]

print(abbrev)
