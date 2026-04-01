def main():
    # Ska kunna lägga till loop så menyn visas igen efter varje val
    print("1. Lägg till kontakt")
    print("2. Visa alla kontakter")
    print("3. Sök kontakt")
    print("4. Ta bort kontakt")
    choice = input("Val: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        remove_contact()

def add_contact():
    # Ska kunna spara kontakten någonstans
    name = input("Namn: ")
    number = input("Telefonnummer: ")

def show_contacts():
    # Ska kunna hämta och visa alla sparade kontakter
    pass

def search_contact():
    # Ska kunna söka bland sparade kontakter
    search = input("Sök namn: ")

def remove_contact():
    # Ska kunna ta bort en kontakt
    name = input("Namn att ta bort: ")

main()