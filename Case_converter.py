#This program converts pascal case into snake case through the use of list comprehensions
def case_converter(Pcase):
    Scase = ""
    converted_case = [
        "_" + char.lower() if char.isupper()
        else char
        for char in Pcase
    ]
    Scase = "".join(converted_case).strip("_")
    print (Scase)

case_converter("PascalCaseHelloHello")