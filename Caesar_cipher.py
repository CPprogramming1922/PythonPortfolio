alphabet = "abcdefghijklmnopqrstuvwxyzabc"
def encoder(Text):
    Result = ""
    for x in Text:
        if x == " ":
            Result += " "
            continue
        elif x.isdigit():
            Result += str(int(x)+3)
        else:
            index = alphabet.index(x.lower())
            Result += alphabet[index+3]
    print (Result)

encoder("3 is the password")

def decoder(Text):
    Result = ""
    for x in Text:
        if x == " ":
            Result += " "
            continue
        elif x.isdigit():
            Result += str(int(x)-3)
        else: 
            index = alphabet.index(x.lower())
            Result += alphabet[index-3]
    print (Result)

decoder("6 lv wkh sdvvzrug")