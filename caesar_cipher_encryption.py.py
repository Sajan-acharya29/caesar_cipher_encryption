encryption_option = input("Would you like to Encode or Decode? ") 
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

cipher_char= ""
if should_encode:
 cipher_key = int(input("enter the secret cipher number: "))
 your_msz= str(input("enter you message: "))
 for i in range(0, len(your_msz)):
   if ord(your_msz[i])>=97 and ord(your_msz[i])<=122:
     #to keep the ord between
     cipher_char_ord = (ord(your_msz[i]) + cipher_key-97) % 26 + 97
     cipher_char= chr(cipher_char_ord )
     print(cipher_char, end="")

   elif ord(your_msz[i])>=65 and ord(your_msz[i]) <=90:
     cipher_char_ord = ((ord(your_msz[i]) + cipher_key -65)) % 26 + 65
     
     cipher_char= chr(cipher_char_ord )
     print(cipher_char, end= "")

   elif ord(your_msz[i])==32:
     cipher_char_ord = 32
     
     cipher_char= chr(cipher_char_ord )
     print(cipher_char, end= "")
    
   else:
     cipher_char= chr(ord(your_msz[i]))
     print(cipher_char, end= "") 
 print("")

elif should_decode:
 cipher_key = int(input("enter the secret cipher number: "))
 your_msz= str(input("enter you message: "))
 for i in range(0, len(your_msz)):
   if ord(your_msz[i])>=97 and ord(your_msz[i])<=122:
     cipher_char_ord = ((ord(your_msz[i]) - cipher_key- 97)) % 26 + 97
     cipher_char= chr(cipher_char_ord )
     print(cipher_char, end= "")

   elif ord(your_msz[i])>=65 and ord(your_msz[i]) <=90:
     cipher_char_ord = ((ord(your_msz[i]) - cipher_key-65)) % 26 + 65

     cipher_char= chr(cipher_char_ord )
     print(cipher_char, end ="")

   elif ord(your_msz[i])==32:
     cipher_char_ord = 32
     
     cipher_char= chr(cipher_char_ord )
     print(cipher_char, end= "")

   else:
     cipher_char= chr(ord(your_msz[i]))
     print(cipher_char, end= "") 
 print("") 

else:
    print("Sorry...")
    print("We can only encode or decode")
    pass
