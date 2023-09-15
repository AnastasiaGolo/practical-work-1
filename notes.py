#Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её,
#читать список заметок, редактировать заметку, удалять заметку.

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class NotesApp:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def save_notes(self):
        with open('notes.txt', 'w') as file:
            for note in self.notes:
                file.write(f"{note.title}\n")
                file.write(f"{note.content}\n")
                file.write("=====\n")

    def read_notes(self):
        with open('notes.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                notes = []
                title = ''
                content = ''
                for line in lines:
                    if line.startswith("====="):
                        note = Note(title, content)
                        notes.append(note)
                        title = ''
                        content = ''
                    elif not title:
                        title = line.strip()
                    else:
                        content += line
                self.notes = notes

    def edit_note(self, note_index, new_content):
        if 0 <= note_index < len(self.notes):
            self.notes[note_index].content = new_content

    def delete_note(self, note_index):
        if 0 <= note_index < len(self.notes):
            del self.notes[note_index]


def main():
    app = NotesApp()
    
    while True:
        print("1. Create a note")
        print("2. Read notes")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            app.create_note(title, content)
            print("Note created successfully!")
        
        elif choice == '2':
            app.read_notes()
            if app.notes:
                for i, note in enumerate(app.notes):
                    print(f"{i+1}. {note.title}")
                    print(note.content)
                    print()
            else:
                print("No notes found.")
        
        elif choice == '3':
            app.read_notes()
            if app.notes:
                for i, note in enumerate(app.notes):
                    print(f"{i+1}. {note.title}")
                
                note_index = int(input("Enter the index of the note to edit: ")) - 1
                
                if 0 <= note_index < len(app.notes):
                    new_content = input("Enter new content: ")
                    app.edit_note(note_index, new_content)
                    print("Note edited successfully!")
                else:
                    print("Invalid note index.")
            else:
                print("No notes found.")
        
        elif choice == '4':
            app.read_notes()
            if app.notes:
                for i, note in enumerate(app.notes):
                    print(f"{i+1}. {note.title}")
                
                note_index = int(input("Enter the index of the note to delete: ")) - 1
                
                if 0 <= note_index < len(app.notes):
                    app.delete_note(note_index)
                    print("Note deleted successfully!")
                else:
                    print("Invalid note index.")
            else:
                print("No notes found.")
        
        elif choice == '5':
            app.save_notes()
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()