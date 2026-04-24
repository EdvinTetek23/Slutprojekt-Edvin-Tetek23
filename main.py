def main():
    while True:
        print("\n--- TELEFONBOK ---")
        print("1. Lägg till kontakt")
        print("2. Visa alla kontakter")
        print("3. Sök kontakt")
        print("4. Ta bort kontakt")
        print("5. Avsluta")
        
        choice = input("Val: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            break
        else:
            print("Ogiltigt val!")


def add_contact():
    name = input("Namn: ")
    number = input("Telefonnummer: ")

    with open("kontakter.txt", "a") as file:
        file.write(f"{name},{number}\n")

    print("Kontakt sparad!")


def show_contacts():
    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()

        if not kontakter:
            print("Inga kontakter sparade.")
            return

        for kontakt in kontakter:
            name, number = kontakt.strip().split(",")
            print(f"Namn: {name}, Nummer: {number}")

    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")


def search_contact():
    search = input("Sök namn: ").lower()

    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()

        found = False
        for kontakt in kontakter:
            name, number = kontakt.strip().split(",")
            if search in name.lower():
                print(f"Hittad: {name} - {number}")
                found = True

        if not found:
            print("Ingen kontakt hittades.")

    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")


def remove_contact():
    name_to_remove = input("Namn att ta bort: ").lower()

    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()

        with open("kontakter.txt", "w") as file:
            removed = False
            for kontakt in kontakter:
                name, number = kontakt.strip().split(",")
                if name.lower() != name_to_remove:
                    file.write(kontakt)
                else:
                    removed = True

        if removed:
            print("Kontakt borttagen.")
        else:
            print("Kontakt hittades inte.")

    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")


main()