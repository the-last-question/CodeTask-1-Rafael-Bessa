

text = input("input the text\n")
shift = input("input the shift\n")
cypherString = ""
for c in text:
    
    if c.isalpha():
        #check limites
        num = ord(c)
        cipherValue = num + int(shift)
        if c.isupper():
            li = "A"
            ls = "Z"
        else:
            li = "a"
            ls = "z"

        #check upper and lower bounds
        if cipherValue < ord(li):
            cipherValue = ord(ls) - (ord(li) - cipherValue -1)
            # print(chr(cipherValue))
        if cipherValue > ord(ls):
            cipherValue = ord(li) + (cipherValue - ord(ls) ) -1
            # print(chr(cipherValue))
        
        cipherValue = chr(cipherValue)

    else:
        cipherValue = c

    cypherString += cipherValue
    
print(cypherString)