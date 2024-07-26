alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

def caesar(start_text, shift_amount, cipher_direction):
    cipher_text = ""
    for i in start_text:
     if i in alphabet:
      position = alphabet.index(i)
      if cipher_direction == "encode":
        cipher_text += alphabet[position+shift_amount]
      else:
        cipher_text += alphabet[position-shift_amount]
     else:
       cipher_text += i
    print(f"The {direction}d text is {cipher_text}")
continuePlay = True
while continuePlay:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))
 shift %= 26
 caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
 restart = input("do you wanna play again?")
 if restart == "yes":
   continuePlay = True
 else:
   continuePlay = False
   print("Thank you!")