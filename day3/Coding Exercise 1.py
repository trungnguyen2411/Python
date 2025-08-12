country_variable = input("Type USA, India or Germany: ")

match country_variable:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")

Solution:
country = "India"

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")