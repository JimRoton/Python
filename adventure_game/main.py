from items import item, items

def main():
    itms = items()

    itms.add(item(1, "dagger", 4))
    itms.add(item(2, "sword", 6))
    itms.add(item(3, "great sword", 8))
    itms.add(item(4, "axe", 10))

    for i in itms.items:
        print(f"    ID: {i.id}")
        print(f"  Name: {i.name}")
        print(f"Damage: {i.damage}")
        print("----------")

main()