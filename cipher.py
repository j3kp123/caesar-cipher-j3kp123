def encrypt_text(plaintext,n):
    ans = ""
        # iterate over text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        if ch==" ":
            ans+=" "
        # check if a character is uppercase 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

plaintext = "HELLO EVERYONE"
n = 5
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext,n))



