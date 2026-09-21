from rich.prompt import Prompt

from dataclasses import dataclass


wishlist = []

@dataclass
class ChristmasPresent:

    name: str
    price: float
    priority: int


wishlist.append(ChristmasPresent("PlayStation5", 4800.0, 19))
wishlist.append(ChristmasPresent("Strumpor", 20.0, 1))
wishlist.append(ChristmasPresent("Gummianka", 30.0, 3))
wishlist.append(ChristmasPresent("Ny dator", 15000.0, 4))
wishlist.append(ChristmasPresent("Datorväska", 299.0, 7))


sorted_list = sorted(wishlist, key=lambda wish: wish.priority, reverse=True)
total_value = sum(wish.price for wish in wishlist)


def user_choice() -> str:
    choice = Prompt.ask(
        "[bold yellow]Enter your choice[/]",
        choices=["1", "2", "3"],
        show_choices=False,
    )  
    return choice

while True:

    print("1. Visa önskelistan i prio-ordning")
    print("2. Visa totalt värde av önskelistan")
    print("3. Avsluta")

    choice = user_choice()

    if choice == "1":
        print()
        for wish in sorted_list:
            print(f"Grej: {wish.name}, pris: {wish.price}, prio: {wish.priority}")
        print()
        
    elif choice == "2":
        print(f"\nTotalt värde av grejjer: {total_value}\n")

    elif choice == "3":
        break