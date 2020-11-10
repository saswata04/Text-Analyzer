# getting the file name
filename = input('Enter the file name : ')

# retriving the text from the file
with open(filename) as f:
    text = f.read()

# print(text)

# count the number of times a character is present in the text
def count_char(text, char):
    count=0
    for i in text.lower():
        if i==char:
            count += 1
    
    return count

# print(count_char(text, 'r'))

# calculate percentage of character present in text
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100*count_char(text, char)/len(text)
    print("{0}-{1}%".format(char, round(perc,2)))