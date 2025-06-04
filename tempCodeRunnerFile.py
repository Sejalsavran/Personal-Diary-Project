def write_notes():
    notes=input("Enter you notes: ")
    with open("notes.txt","a") as file:
        file.write(notes+"\n")
    print("Notes added successfully.")

def read_notes():
    try:
        with open("notes.txt","r") as file:
            print("Your notes: ")
            print(file.read())
    except FileNotFoundError:
        print("No notes found")

def main():
    while True:
        print("1. write notes.")
        print("2. Read notes.")
        print("3. exit")
        
        choice=input("Enter you choice(1,2,3): ")
        if choice=="1":
            write_notes()
        elif choice=="2":
            read_notes()
        elif choice=="3":
            print("Exisiting the diary.")
            break
        else:
            print("Invalid Input. Please try again.")
            
if __name__ == "__main__":
    main()
        
            
        
        
        