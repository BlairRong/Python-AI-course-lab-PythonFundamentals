course = "Python for Beginners" 
print(course.find("for"))

print(max(3, 6, 2, 8, 4, 10))

numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

martrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
martrix[0][1] = 20
print(martrix[0][1])
for row in martrix:
    for item in row:
        print(item)

numbers =[2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)
print(y)
print(z)

message = input(">")
words = message.split(" ")
emojis = {":)": "😊",
          ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

def add(a,b):
    return a + b
result = add(3,5)
print(result)

def emoji_converter(message):
    words = message.split(" ")
    emojis = {":)": "😊",
              ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))