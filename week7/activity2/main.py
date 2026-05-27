from  aquarium import Aquarium
from fish import FishFactory




def main():
    print("----------------AUCKLAND AQUARIUM----------------")
    print("1 - Add a new fish")
    print("2 - View fish information")
    print("3 - Exit")


    aquarium = Aquarium()


    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            fish_type = input("Enter the type of fish to add (goldfish/shark): ")
            quantity = int(input("Enter the quantity of fish to add: ")) 
            aquarium.add_fish(fish_type, quantity)

        elif choice == "2": 
            aquarium.display_all_fish( )

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")









if __name__ == "__main__":
    main()