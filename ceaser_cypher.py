# Caesar Cipher Program
def caesar_cipher():
    print ("Caesar Cipher Program")
    mode = input(("choose mode (encrypt/decrypt): ")).lower()

    while True:
        mode = input("Choose mode (encrypt/decrypt): ").lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
     
    text = input("Enter the text: ")
    key = int(input("Enter the key: "))
    ceaser_list = []
    result = ""

    for char in text :
        if mode == "encrypt" :
            new_char = chr((ord(char) + key) % 256)
           
        elif mode == "decrypt" :
            new_char = chr((ord(char) - key) % 256)
        ceaser_list.append(new_char)

    result = ''.join(ceaser_list)
    print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} text: {result}")    
caesar_cipher()
        
  