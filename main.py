def add_contact():
    name = input("Namn: ")
    number = input("Telefonnummer: ")
    email = input("Email: ")
    
    with open("kontakter.txt", "a") as file:
        file.write(f"{name},{number},{email}\n")
    
    print("Kontakt sparad!")

def show_contacts():
    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()
        
        if not kontakter:
            print("Inga kontakter sparade.")
            return
        
for kontakt in kontakter:
            delar = kontakt.strip().split(",")
            name, number, email = delar[0], delar[1], delar[2] if len
    
    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")

def search_contact():
    search = input("Sök namn: ").lower()
    
    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()
        
        found = False
        for kontakt in kontakter:
            delar = kontakt.strip().split(",")
            name, number, email = delar[0], delar[1], delar[2] if len(delar) > 2 else ""
            if search in name.lower():
                print(f"Hittad: {name} - {number} - {email}")
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
        
        removed = False
        kvar = []
        for kontakt in kontakter:
            delar = kontakt.strip().split(",")
            if delar[0].lower() != name_to_remove:
                kvar.append(kontakt)
            else:
                removed = True
                
        with open ("kontakt borttagen.txt", "w") as file:
            file.writelines(kvar)
        
        if removed:
            print("Kontakt borttagen.")
        else:
            print("Kontakt hittades inte.")
    
    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")
        
def main():
    while True:
        print("\n1. Lägg till kontakt")
        print("2. Visa alla kontakter")
        print("3. Sök kontakt")
        print("4. Ta bort kontakt")
        print("0. Avsluta")
        
        val = input("\nVal: ")
        
        if val == "1":
            add_contact()
        elif val == "2":
            show_contacts()
        elif val == "3":
            search_contact()
        elif val == "4":
            remove_contact()
        elif val == "0":
            break
        else:
            print("Ogiltigt val.")
 
main()