#Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её,
#читать список заметок, редактировать заметку, удалять заметку.

import json
from datetime import datetime

def read_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
        
    return notes

def write_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def add_note():
    notes = read_notes()
    note_id = len(notes) + 1
    note_title = input("Введите название заметки: ")
    note_body = input("Введите текст заметки: ")
    note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "date": note_date
    }
    
    notes.append(note)
    write_notes(notes)
    print("Заметка успешно добавлена!")

def show_notes():
    notes = read_notes()
    
    if len(notes) == 0:
        print("Заметки не найдены.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Date: {note['date']}")
            print()
        
def edit_note():
    notes = read_notes()
    
    if len(notes) == 0:
        print("Заметки не найдены.")
        return
    
    note_id = int(input("Введите ID заметки, которую вы хотите отредактировать: "))
    note_index = -1
    
    for i in range(len(notes)):
        if notes[i]['id'] == note_id:
            note_index = i
            break
            
    if note_index == -1:
        print("Заметка не найдена.")
        return
    
    note_title = input("Введите название новой заметки: ")
    note_body = input("Введите текст новой заметки: ")
    note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notes[note_index]['title'] = note_title
    notes[note_index]['body'] = note_body
    notes[note_index]['date'] = note_date
    
    write_notes(notes)
    print("Заметка успешно отредактирована!")

def delete_note():
    notes = read_notes()
    
    if len(notes) == 0:
        print("Заметки не найдены.")
        return
    
    note_id = int(input("Введите ID заметки, которую вы хотите удалить: "))
    note_index = -1
    
    for i in range(len(notes)):
        if notes[i]['id'] == note_id:
            note_index = i
            break
            
    if note_index == -1:
        print("Заметка не найдена.")
        return
    
    del notes[note_index]
    write_notes(notes)
    print("Заметка успешно удалена!")

def main():
    while True:
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Отредактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        
        choice = input("Введите свой выбор (1-5): ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            show_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Недопустимый выбор. Пожалуйста, повторите ещё раз.")

if __name__ == '__main__':
    main()