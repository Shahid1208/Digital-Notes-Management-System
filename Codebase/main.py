# DIGITAL NOTES MANAGEMENT SYSTEM
def load_notes():
    try:
        with open("notes.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open("notes.txt", "w") as file:
        file.writelines(notes)

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


def add_note():
    notes = load_notes()
    title = input("Enter Your Title: ").strip()
    content = input("Enter Your Content: ").strip()

    if title == "":
        print("Title cannot be empty. Note not saved.")
        return
    note_id = generate_note_id(notes)
    notes.append(f"{note_id}|{title}|{content}\n")
    save_notes(notes)
    print(f"Note saved. ID: {note_id} | {title}")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            data = file.read().strip()
        if data == "":
            print("No notes found.")
            return
        for note in data.splitlines():
            parts = note.strip().split("|", 2)
            if len(parts) == 3:
                print(f"{parts[0]} | {parts[1]} | {parts[2]}")
    except FileNotFoundError:
        print("No notes found.")

def search_notes():
    notes = load_notes()
    search_text = input("Enter title or content to search: ").strip().lower()
    if search_text == "":
        print("Search title or content cannot be empty.")
        return
    found = False

    for note in notes:
        parts = note.strip().split("|", 2)
        if len(parts) == 3:
            note_id, title, content = parts
            if search_text in title.lower() or search_text in content.lower():
                print(f"{note_id} | {title} | {content}")
                found = True
    if not found:
        print("Note not found.")


def edit_note():
    notes = load_notes()
    note_id = input("Enter note ID to edit: ").strip()
    found = False

    for i in range(len(notes)):
        parts = notes[i].strip().split("|", 2)
        if len(parts) == 3 and parts[0] == note_id:
            new_content = input("Enter New Content: ").strip()
            notes[i] = f"{parts[0]}|{parts[1]}|{new_content}\n"
            found = True
            break

    if found:
        save_notes(notes)
        print(f"Note {note_id} updated.")
    else:
        print("Note ID not found.")


# DELETE NOTE
def delete_note():
    notes = load_notes()
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
        remaining = sum(
            1 for note in updated_notes
            if len(note.strip().split("|", 2)) == 3
        )
        print(f"Note {note_id} deleted. Notes left: {remaining}")
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
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if choice == 1:
        add_note()
    elif choice == 2:
        view_notes()
    elif choice == 3:
        search_notes()
    elif choice == 4:
        edit_note()
    elif choice == 5:
        delete_note()
    elif choice == 6:
        print("Thank you for using Digital Notes Management System.")
        break
    else:
        print("Invalid Choice. Please select valid option.")
