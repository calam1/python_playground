favorite_number = 111
print favorite_number
print favorite_number ** 3

name = "Jessica"
location = "Grendel's Cupcake Den"
time = "7:30PM"

print ("You are invited to a birhtday party for " + name)
print("The party will be at " + location + " and starts at " + time)

monday_vegetable = "asparagus"
monday_entree = "pasta primavera"

tuesday_vegetable = "artichoke"
tuesday_entree = "steak frites"

print("Monday's specials are " + monday_vegetable + " and " + monday_entree)
print("Tuesday's specials are " + tuesday_vegetable + " and " + tuesday_entree)

html = "Test message"
print("<b>" + html + "</b>")
print("<code>" + html + "</code>")
print("<h1>" + html + "</h1>")

today = "Saturday"

if today == "Saturday" or today == "Sunday":
    print("SLEEPING IN")

ladybugs = 2600
trees = 20

if ladybugs >= 125 * trees:
    print("OK")
else:
    print("NOT OK")

message1 = "The Analytical Engine weaves algebraic patterns, just as the Jacquard loom weaves flowers and leaves. -- Ada Lovelace, the first programmer"
message2 = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty , and dedicated to the proposition that ll men are created equal."
message3 = "They told me computers could only do arithmetic. -- Computer pioneer Grace Hopper"

print("length of message 1 ", len(message1))
print("length of message 2 ", len(message2))
print("length of message 3 ", len(message3))

message_list = [message1, message2, message3]
for message in message_list:
    if len(message) <= 140:
        print(message)

good_weather = False
on_vacation = True
no_bears = True

if good_weather == True and on_vacation == True and no_bears == True:
    print("camping")
else:
    print("staying home")    

groceryList = ["apples", "cereal", "coffee", "bread"]

print(groceryList[0])
print(groceryList[len(groceryList) - 1])

student = "Alice"
all_students = ['Henry', 'Beatrice', 'Wanda', 'Evan', 'Adam', 'Tanya', 'Alice', 'Sean']

#for person in all_students:
#    if person == student:
#        print("PRESENT")
#    else:
#        print("ABSENT")

if student in all_students:
    print "PRESENT"
else:
    print "ABSENT"


myList = ['Jessica', 'likes', 'ice cream']
myList.append('!')

print(len(myList))

names = ['Adam', 'Tonya', 'Alice', 'Sean']
for name in names:
    print "Hello " + name

words = ['zip', 'blip', 'croissant', 'toast', 'quip', 'quail', 'quetzal', 'quizzical']
for word in words:
    if word.startswith('q'):
        print word

words =["pizzaz", "python", "zebra", "pizza"]

for word in words:
    if word.startswith('z') or word.endswith('z'):
        print word

honor_roll_count = 0
student_grades = ["A", "C", "B", "B", "C", "A", "F", "B", "B", "B", "C", "A"]
for grade in student_grades:
    if grade == "A" or grade == "B":
        honor_roll_count += 1

print honor_roll_count

spaces_count = 0
sentence = "It was the best of times, it was the worst of times"

wordList = sentence.split(" ")
print len(wordList) - 1

spaces_count = sentence.count(" ")
print spaces_count

spaces_count = 0
for letter in sentence:
    if letter == " ":
        spaces_count += 1

print spaces_count

sentence = "Finished files are the result of years of scientific study combined with the experience of years"
counter = 0
for letter in sentence:
    if letter.lower() == "f":
        counter += 1

print counter

headlines = ["Man Takes First Steps on the Moon",
            "Titanic Sinks Four Hours after Hitting Iceberg",
            "Dewey Defeats Truman",
            "Greatest Crash in Wall street's History"]

maximum_headline_length = 35

for headline in headlines:
    if len(headline) > maximum_headline_length:
        print headline

phrase_without_vowels = ""
phrase = "Perfection is achieved, not when there is nothing more to add, but when there si nothing left to take away."
vowels = ["a", "e", "i", "o", "u"]
for letter in phrase:
    if letter not in vowels:
        phrase_without_vowels += letter
print phrase_without_vowels
