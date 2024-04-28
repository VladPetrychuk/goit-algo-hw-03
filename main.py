def parse_input(user_input):

  command, *args = user_input.split()
  command = command.strip().lower()
  return command, args


def add_contact(contacts, name, phone):

  contacts[name] = phone
  print(f"Контакт {name} додано.")


def change_contact(contacts, name, new_phone):

  if name in contacts:
    contacts[name] = new_phone
    print(f"Номер телефону контакту {name} оновлено.")
  else:
    print(f"Контакт {name} не знайдено.")


def get_phone(contacts, name):

  if name in contacts:
    print(f"Номер телефону {name}: {contacts[name]}")
  else:
    print(f"Контакт {name} не знайдено.")


def show_all_contacts(contacts):

  if contacts:
    for name, phone in contacts.items():
      print(f"{name}: {phone}")
  else:
    print("Список контактів порожній.")


def main():
  
  contacts = {}

  while True:
    user_input = input("Введіть команду: ")
    command, args = parse_input(user_input)

    if command == "hello":
      print("Привіт! Чим я можу вам допомогти?")
    elif command == "add":
      if len(args) == 2:
        name, phone = args
        add_contact(contacts, name, phone)
      else:
        print("Неправильна кількість аргументів. Спробуйте: add [ім'я] [номер телефону]")
    elif command == "change":
      if len(args) == 2:
        name, new_phone = args
        change_contact(contacts, name, new_phone)
      else:
        print("Неправильна кількість аргументів. Спробуйте: change [ім'я] [новий номер телефону]")
    elif command == "phone":
      if args:
        name = args[0]
        get_phone(contacts, name)
      else:
        print("Введіть ім'я контакту.")
    elif command == "all":
      show_all_contacts(contacts)
    elif command in ["close", "exit"]:
      print("До побачення!")
      break
    else:
      print("Невідома команда.")


if __name__ == "__main__":
  main()