enc = ""
dec = ""
text = input("Enter your secret message: ")
shift = int(input("Number to shift by: "))
for i in text:
    if i.isupper():
        i_uni = ord(i)
        i_index = ord(i) - ord("A")
        new_index = (i_index + shift) % 26
        new_uni = (new_index + ord("A"))
        new_letter = chr(new_uni)
        enc = enc + new_letter
    elif i.islower():
        i_uni = ord(i)
        i_index = ord(i) - ord("a")
        new_index = (i_index + shift) % 26
        new_uni = (new_index + ord("a"))
        new_letter = chr(new_uni)
        enc = enc + new_letter
    else:
        enc += i
print(f"Encrypted text: {enc}")
s = input("Do you want to decrypt your secret message? Y/N: ")
if s == "Y":
    for i in enc:
        if i.isupper():
            i_uni = ord(i)
            i_index = ord(i) - ord("A")
            new_index = (i_index - shift) % 26
            new_uni = (new_index + ord("A"))
            new_letter = chr(new_uni)
            dec = dec + new_letter
        elif i.islower():
            i_uni = ord(i)
            i_index = ord(i) - ord("a")
            new_index = (i_index - shift) % 26
            new_uni = (new_index + ord("a"))
            new_letter = chr(new_uni)
            dec = dec + new_letter
        else:
            dec += i
    print(f"Decrypted text: {dec}")
else:
    print("Process terminated.")
    
