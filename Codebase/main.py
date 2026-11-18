# DIGITAL NOTES MANAGEMENT SYSTEM
print("""
------- DIGITAL NOTES MANAGEMENT SYSTEM--------

    1.Add Notes
    2.View All Notes
    3.Search Notes
    4.Edit Notes
    5.Delete Notes
    6.Exit
----------------------------------------------
""")

while True:

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter Your Title: ").strip()
            content = input("Enter Your Content: ").strip()
            if title == "":
                print("Title cannot be empty. Note not saved.")
            elif content == "":
                print("Content cannot be empty. Note not saved.")

            else:
                try:
                    with open("notes.txt", "r") as file:
                        notes = file.readlines()
                except FileNotFoundError:
                    notes = []
                max_id = 0
                for note in notes:
                    parts = note.strip().split("|", 2)

                    if len(parts) == 3 and parts[0].startswith("N"):
                        try:
                            number = int(parts[0][1:])
                            if number > max_id:
                                max_id = number
                        except ValueError:
                            continue
                note_id = f"N{max_id + 1}"
                with open("notes.txt", "a") as file:
                    file.write(f"{note_id}|{title}|{content}\n")
                print("Note saved. ID:", note_id, "|", title)

        elif choice == 2:
            try:
                with open("notes.txt", "r") as file:
                    data = file.read().strip()
                if data == "":
                    print("No notes found.")
                else:
                    for note in data.splitlines():
                        parts = note.strip().split("|", 2)
                        if len(parts) == 3:
                            print(
                                f"{parts[0]} | "
                                f"{parts[1]} | "
                                f"{parts[2]}"
                            )
            except FileNotFoundError:
                print("No notes found.")

        elif choice == 3:
            search_text = input("Enter title or content to search: ").strip().lower()
            if search_text == "":
                print("Search title or content cannot be empty.")
            else:
                found = False
                try:
                    with open("notes.txt", "r") as file:
                        notes = file.readlines()
                    for note in notes:
                        parts = note.strip().split("|", 2)
                        if len(parts) == 3:
                            note_id, title, content = parts
                            if (search_text in title.lower()
                                    or search_text in content.lower()):
                                print("\nNote found:")
                                print("ID:", note_id)
                                print("Title:", title)
                                print("Content:", content)
                                found = True
                    if not found:
                        print("Note not found.")
                except FileNotFoundError:
                    print("No notes found.")
        elif choice == 4:
            note_id = input("Enter note ID to edit: ").strip()
            if note_id == "":
                print("Note ID cannot be empty.")
            else:
                try:
                    with open("notes.txt", "r") as file:
                        notes = file.readlines()
                    found = False
                    for i in range(len(notes)):
                        parts = notes[i].strip().split("|", 2)
                        if len(parts) == 3 and parts[0] == note_id:
                            new_title = input("Enter New Title: ").strip()
                            new_content = input("Enter new content: ").strip()
                            if new_title == "":
                                print("Title cannot be empty.")
                            elif new_content == "":
                                print("Content cannot be empty.")
                            elif "|" in new_title or "|" in new_content:
                                print("Please do not use | in title or content.")
                            else:
                                notes[i] = (
                                    f"{note_id}|{new_title}|"
                                    f"{new_content}\n"
                                )
                                found = True
                            break
                    if found:
                        with open("notes.txt", "w") as file:
                            file.writelines(notes)
                        print("Note", note_id, "updated successfully.")
                    elif not found:
                        print("Note ID not found.")
                except FileNotFoundError:
                    print("No notes found.")

        elif choice == 5:
            note_id = input("Enter note ID to delete: ").strip()

            if note_id == "":
                print("Note ID cannot be empty.")
            else:
                try:
                    with open("notes.txt", "r") as file:
                        notes = file.readlines()
                    updated_notes = []
                    found = False
                    for note in notes:
                        parts = note.strip().split("|", 2)
                        if len(parts) == 3 and parts[0] == note_id:
                            found = True
                        else:
                            updated_notes.append(note)
                    if found:
                        with open("notes.txt", "w") as file:
                            file.writelines(updated_notes)
                        remaining = sum(
                            1 for note in updated_notes
                            if len(note.strip().split("|", 2)) == 3
                        )
                        print("Note", note_id, "deleted.")
                        print("Notes left:", remaining)
                    else:
                        print("Note ID not found.")
                except FileNotFoundError:
                    print("No notes found.")
        elif choice == 6:
            print(
                "Thank you for using Digital Notes "
                "Management System."
            )
            break
        else:
            print("Invalid Choice. Please select valid option.")
    except ValueError:
        print("Please enter a valid number!")
