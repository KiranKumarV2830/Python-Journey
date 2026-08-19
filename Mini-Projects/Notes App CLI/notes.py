
def add_note():
    note_text = input("Enter your notes : ")
    with open("notes.txt","a") as f:
        f.write(note_text + "\n")

def view_notes():
    try :
        with open("notes.txt","r") as f:
            notes = f.readlines()
        if not notes:
            print("No notes yet.")
        else:
            count = 1
            for note in notes:
                print(str(count) + ". " + note.strip())
                count += 1
    except FileNotFoundError:
        print("No notes yet") 

def delete_notes():
    view_notes()
    try :
        with open("notes.txt","r") as f:
            notes = f.readlines()
            choice = int(input("Enter note number to delete: "))
            index = choice - 1   
            del notes[index]

        with open("notes.txt","w") as f:
            for note in notes:
                f.write(note)

    except FileNotFoundError:
        print("No notes yet.")
delete_notes()

def search_notes():
    try :
        with open("notes.txt","r") as f:
            notes = f.readlines()
            choice = input("Enter the keyword ").lower()
            found = False
            for note in notes:
                if choice in note.lower():
                    print(note)
                    found = True
            if not found:
                print("Not Found")
    except FileNotFoundError:
        print("No notes yet")

while True:
    print("===== NOTES APP =====")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Delete a note")
    print("4. Search notes")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    match choice :
        case 1 :
            add_note()
        case 2 :
            view_notes()
        case 3 :
            delete_notes()
        case 4 :
            search_notes()
        case 5 : 
            break
        case _:
            print("Enter the correct number ")