
# DIGITAL NOTES MANAGEMENT SYSTEM
# Load Notes:
def load_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            return notes
    except FileNotFoundError:
        return []
#Save Note;
def save_notes(notes):
    with open("notes.txt", "w") as file:
        file.writelines(notes)
#Generate Note ID
def generate_note_id(notes):
    max_id = 0
    for note in notes:
        parts = note.strip().split("|", 2)
        if len(parts) == 3 and parts[0].startswith("N"):
            try:
                number = int(parts[0][1:])
                max_id = max(max_id, number)
            except ValueError:
                continue
    return f"N{max_id + 1}"

#Add notes:
def add_note():
    notes = load_notes()
    title = input("Enter Your Title: ")
    content = input("Enter Your Content: ")
    if title.strip() == "":
        print("Title cannot be empty. Note not saved.")
        return
    note_id = generate_note_id(notes)
    notes.append(f"{note_id}|{title}|{content}\n")
    save_notes(notes)
    print("Note saved. ID:", note_id, "|", title)


#View all notes
def view_notes():
    notes = load_notes()
    if len(notes) == 0:
        print("No notes found.")
        return
    print("\n------ ALL NOTES -----")
    for note in notes:
        parts = note.strip().split("|", 2)
        if len(parts) == 3:
            print("ID:", parts[0])
            print("Title:", parts[1])
            print("Content:", parts[2])

# Search notes
def search_notes():
    notes = load_notes()
    if len(notes) == 0:
        print("No notes found.")
        return
    search_text = input("Enter keyword to search: ").strip().lower()
    if search_text == "":
        print("Search keyword cannot be empty.")
        return
    found = False
    for note in notes:
        parts = note.strip().split("|", 2)
        if len(parts) == 3:
            note_id, title, content = parts
            if (search_text in title.lower() or
                    search_text in content.lower()):
                print("\nNote found:")
                print("ID:", note_id)
                print("Title:", title)
                print("Content:", content)
                found = True
    if not found:
        print("Note not found.")


#Edit Notes
def edit_note():
    notes = load_notes()
    if len(notes) == 0:
        print("No notes found.")
        return
    note_id =input("Enter note ID to edit:").strip()
    found = False
    for i in range(len(notes)):
        parts = notes[i].strip().split("|", 2)
        if len(parts) == 3 and parts[0] == note_id:
            new_title = input("Enter New Title:")
            new_content = input("Enter New Content:")
            if new_title.strip() == "":
                print("title cannot be empty.")
                return
            notes[i] = f"{note_id}|{new_title}|{new_content}\n"
            found = True
            break
    if found:
        save_notes(notes)
        print("Note", note_id, "Updated successfully.")

    else:
        print("Note ID not found.")


#Delete Notes
def delete_note():
    notes = load_notes()

    if len(notes) == 0:
        print("No notes found.")
        return
    note_id = input("Enter note ID to delete: ").strip()
    updated_notes = []
    found = False
    for note in notes:
        parts = note.strip().split("|", 2)
        if len(parts) == 3 and parts[0] == note_id:
            found = True
        else:
            updated_notes.append(note)
    if found:
        save_notes(updated_notes)
        print("Note", note_id, "deleted.")
        print("Notes left:", len(updated_notes))
    else:
        print("Note ID not found.")

while True:
    print("""
------- DIGITAL NOTES MANAGEMENT SYSTEM ------

    1. Add Notes
    2. View All Notes
    3. Search Notes
    4. Edit Notes
    5. Delete Notes
    6. Exit

""")

    try:
        choice = int(input("Enter your choice:"))

    except ValueError:
        print("please enter a valid number!")
        continue
    if choice ==1:
        add_note()
    elif choice ==2:
        view_notes()
    elif choice ==3:
        search_notes()
    elif choice ==4:
        edit_note()
    elif choice ==5:
        delete_note()
    elif choice ==6:
        print("Thank you for using Digital Notes Management System.")
        break
    else:
        print("Invalid Choice. Please select valid option.")
