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
        
        
        print(f"\n{'Namn':<20} {'Telefon':<15} {'Email'}")
        print("-" * 55)
        for kontakt in kontakter:
            delar = kontakt.strip().split(",")
            name, number, email = delar[0]
            number = delar[1] if len(delar) > 1 else ""
            email = delar[2] if len(delar) > 2 else ""
            print(f"{name:<20} {number:<15} {email}")
            
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
            email = delar[2] if len(delar) > 2 else ""
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
        

def edit_contact():
    name_to_edit = input("Namn att redigera: ").lower()
 
    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()
 
        updated = False
        new_list = []
        for kontakt in kontakter:
            delar = kontakt.strip().split(",")
            if delar[0].lower() == name_to_edit:
                print(f"Hittad: {delar[0]} - {delar[1] if len(delar)>1 else ''} - {delar[2] if len(delar)>2 else ''}")
                print("Lämna tomt för att behålla nuvarande värde.")
                new_name   = input(f"Nytt namn [{delar[0]}]: ").strip() or delar[0]
                new_number = input(f"Nytt nummer [{delar[1] if len(delar)>1 else ''}]: ").strip() or (delar[1] if len(delar)>1 else "")
                new_email  = input(f"Ny email [{delar[2] if len(delar)>2 else ''}]: ").strip() or (delar[2] if len(delar)>2 else "")
                new_list.append(f"{new_name},{new_number},{new_email}\n")
                updated = True
            else:
                new_list.append(kontakt)
 
        with open("kontakter.txt", "w") as file:
            file.writelines(new_list)
 
        if updated:
            print("Kontakt uppdaterad!")
        else:
            print("Kontakt hittades inte.")
 
    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")
 
 
def export_contacts():
    """Export contacts to a readable text summary."""
    try:
        with open("kontakter.txt", "r") as file:
            kontakter = file.readlines()
 
        if not kontakter:
            print("Inga kontakter att exportera.")
            return
 
        with open("kontakter_export.txt", "w") as out:
            out.write("=== Kontaktlista ===\n\n")
            for i, kontakt in enumerate(kontakter, 1):
                delar = kontakt.strip().split(",")
                name   = delar[0]
                number = delar[1] if len(delar) > 1 else "–"
                email  = delar[2] if len(delar) > 2 else "–"
                out.write(f"{i}. {name}\n   Tel: {number}\n   Email: {email}\n\n")
 
        print(f"Exporterat {len(kontakter)} kontakter till kontakter_export.txt")
 
    except FileNotFoundError:
        print("Ingen kontaktlista finns ännu.")
 
 
def count_contacts():
    try:
        with open("kontakter.txt", "r") as file:
            lines = [l for l in file.readlines() if l.strip()]
        print(f"Antal kontakter: {len(lines)}")
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
        elif val == "5":
            edit_contact()
        elif val == "6":
            export_contacts()
        elif val == "7": 
            remove_contact()
        elif val == "0":
            break
        else:
            print("Ogiltigt val.")
 
main()