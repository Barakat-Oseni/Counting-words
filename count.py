number_of_words = 0
 
with open(r'counting.txt','r') as file:
 
    data = file.read()
 
    lines = data.split()
    for word in lines:
        if not word.isnumeric():         
 
            number_of_words += 1

print(number_of_words)
