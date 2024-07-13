#creates a file for the user and writes the content given by the user to it
while True:
    print("Would you like to write or read into a file ?")
    key=input("Press 'w' to write, 'r' to read, 'x' to escape: ")
    
    if key == 'x':
        break
    if key == 'r':
        f1=input("Please write the name of the file you would like to read: ")
        with open(f1, "r") as f:
            print(f.read())
            
            
    if key == 'w':
        f2=input("Please write the name of the file you would like to create: ")
        wr=input("Write the message you want to print on the file: ")
        with open(f2, "w") as file:
            file.write(wr)
            print("Your message has been written!")
        res=input("Would you like to see the printed message?: ")
        
        if res == 'yes':
            with open(f2, "r") as file:
                content=file.read()
                print(content)
                
        else:
            break
    
        












