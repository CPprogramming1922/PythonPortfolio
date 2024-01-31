CC_no = "4032039028350448"
def valid_check(CC_no):
    total = 0
    odd_digits = CC_no[::2]
    for x in odd_digits:
        y=int(x)
        y *= 2
        if y>10:  
            total += sum([int(d) for d in str(y)])
        else:
            total += y
    even_digits = CC_no[1::2]
    total += sum([int(a) for a in even_digits])
    if str(total)[-1] == "0":
        print ("Your credit card number is VALID")
    else:
        print ("Your credit card number is INVALID")
    
valid_check(CC_no)

# The credit card number generator used to verify the program is https://developer.paypal.com/api/rest/sandbox/card-testing/#link-creditcardgenerator