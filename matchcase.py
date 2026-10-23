#1

n = 1

match n:
    case 1:
        print("Hello")
    case _:
        print("Bye")


#2. 

n = 2

match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Invalid")


#3. 

color = "red"

match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case _:
        print("Unknown")


#4. 

fruit = "Apple"

match fruit:
    case "Apple":
        print("Apple is a fruit")
    case "Mango":
        print("Mango is a fruit")
    case _:
        print("Unknown fruit")



#5.

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")



#6. 

a = 5
b = 3
op = "+"

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case _:
        print("Invalid")


#7

msg = "hi"
match msg:
    case "hi":
        print("Hello")
    case "bye":
        print("Goodbye")
    case _:
        print("Unknown message")


#8.

n = 10

match n:
    case 5:
        print("Five")
    case 10:
        print("Ten")
    case _:
        print("Other number")


#9.

subject = "Python"

match subject:
    case "Python":
        print("Learn Coding")
    case "Maths":
        print("Solve Problems")
    case _:
        print("Unknown subject")


#10. 

choice = 1

match choice:
    case 1:
        print("Welcome")
    case _:
        print("Thank You")
