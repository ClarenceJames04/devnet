pets = []


def display_menu():
    print("\n=== Pet Adoption Records Manager ===")
    print("1. Add Pet")
    print("2. View Pets")
    print("3. Count Available/Adopted")
    print("4. Find Pet")
    print("5. Remove Pet")
    print("6. Exit")

    choice = input("Enter your choice: ")
    return choice


def add_pet(pet_list):
    name = input("Enter pet name: ")
    animal_type = input("Enter animal type: ")
    status = input("Enter status (Available/Adopted): ")

    pet = name + " | " + animal_type + " | " + status
    pet_list.append(pet)

    print("Pet added successfully!")


def view_pets(pet_list):
    if len(pet_list) == 0:
        print("No pets found.")
    else:
        print("\n=== Pet List ===")

        for pet in pet_list:
            print(pet)


def count_available_adopted(pet_list):
    available = 0
    adopted = 0

    for pet in pet_list:
        if "Available" in pet:
            available += 1
        elif "Adopted" in pet:
            adopted += 1

    return available, adopted


def find_pet(pet_list):
    search_name = input("Enter pet name to find: ")

    found = False

    for pet in pet_list:
        parts = pet.split(" | ")
        name = parts[0]

        if name.lower() == search_name.lower():
            print("Pet found:", pet)
            found = True

    if found == False:
        print("Pet not found.")


# BONUS
def remove_pet(pet_list):
    search_name = input("Enter pet name to remove: ")

    for pet in pet_list:
        parts = pet.split(" | ")
        name = parts[0]

        if name.lower() == search_name.lower():
            pet_list.remove(pet)
            print("Pet removed successfully!")
            return

    print("Pet not found.")


def main():
    running = True

    while running:
        choice = display_menu()

        if choice == "1":
            add_pet(pets)

        elif choice == "2":
            view_pets(pets)

        elif choice == "3":
            available, adopted = count_available_adopted(pets)
            print("Available:", available)
            print("Adopted:", adopted)

        elif choice == "4":
            find_pet(pets)
        elif choice == "5":
            remove_pet(pets)

        elif choice == "6":
            print("Exiting program...")
            running = False

        else:
            print("Invalid choice.")


main()
