def print_pet_names(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


print_pet_names("Jonathan",
                dog="Brock",
                fish=["Larry", "Curly", "Moe"],
                turtle="Sheldon")
