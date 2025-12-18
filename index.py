with open('text.txt', 'w') as file:
    file.write('Write somthing')
file.close()
with open('text.txt', 'r') as file:
    data = file.readlines()
    print("words in this file are:")   
    for line in data:
        word = line.split() 
        print(word)
file.close()