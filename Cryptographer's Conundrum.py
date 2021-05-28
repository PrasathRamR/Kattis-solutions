#programmer : Prasath Ram R

new_cipher = input()
replacement = "PER"
replacementIndex = 0
count = 0
for index in range(len(new_cipher)):
    if(cipher[index] != replacement[replacementIndex]):
        count+=1
    replacementIndex = (replacementIndex + 1) % 3 
print(count)
