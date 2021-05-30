print("Hello, I am here to help you convert")
print("So, let's begin....")
units = print("""What would you like to convert? :
(A) Kgs to gms
(B) Gms to kgs """)
choices = ["A", "B"]
choice = input("Choose an option from the above choices: ").upper()
def whole():
    
    if choice not in choices:
        print("Sorry, that's an invalid option")
        quit
    else:
            print("Ok, let's continue...")
    try:
        unit = int(input("Units  you want to convert: "))
    except ValueError:
            print("Invalid unit!")
            quit
    def converter(unit):
        if choice == "A":
            return unit * 1000
        elif choice == "B":
            return unit / 1000
        else:
            print("Sorry! I can't convert that!")


    if choice == "A":
            name = "gramms"
    elif choice == "B":
            name = "kilograms"
    answer = (print(f"That will be {converter(unit)}  {name}"))

            
whole()
