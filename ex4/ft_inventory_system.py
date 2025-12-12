# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 15:50:22 by shaegels          #+#    #+#              #
#    Updated: 2025/12/12 16:10:19 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_inventory(name, inv):
    print(f"=== {name}'s Inventory ===")
    total_value = 0
    total_items = 0
    categories = {}

    for item, data in inv.items():
        qty = data["quantity"]
        value = data["value"]
        rarity = data["rarity"]
        category = data["category"]

        total_items += qty
        total_value += qty * value
        categories[category] = categories.get(category, 0) + qty

        print(f"{item} ({category}, {rarity}): {qty}x @ {value} gold each = {qty * value} gold")

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print("Categories:", ", ".join(f"{cat}({count})" for cat, count in categories.items()))
    return total_value, total_items


def transfer_item(sender, receiver, item, amount):
    print(f"=== Transaction: {sender_name} gives {receiver_name} {amount} {item}s ===")

    if item not in sender or sender[item]["quantity"] < amount:
        print("Transaction failed! Not enough items.")
        return False

    sender[item]["quantity"] -= amount

    if item not in receiver:
        receiver[item] = sender[item].copy()
        receiver[item]["quantity"] = 0

    receiver[item]["quantity"] += amount

    print("Transaction successful!")
    return True


def main():
    print("=== Player Inventory System ===")

    alice = {
        "sword": {"category": "weapon", "rarity": "rare", "quantity": 1, "value": 500},
        "potion": {"category": "consumable", "rarity": "common", "quantity": 5, "value": 50},
        "shield": {"category": "armor", "rarity": "uncommon", "quantity": 1, "value": 200},
    }

    bob = {
        "magic_ring": {"category": "accessory", "rarity": "rare", "quantity": 1, "value": 800},
    }

    alice_value, alice_items = print_inventory("Alice", alice)

    global sender_name, receiver_name
    sender_name, receiver_name = "Alice", "Bob"

    transfer_item(alice, bob, "potion", 2)

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(f"Bob potions: {bob.get('potion', {'quantity': 0})['quantity']}")

    print("\n=== Inventory Analytics ===")

    bob_value = sum(item["value"] * item["quantity"] for item in bob.values())
    bob_items = sum(item["quantity"] for item in bob.values())

    most_valuable = "Alice" if alice_value > bob_value else "Bob"
    print(f"Most valuable player: {most_valuable} ({max(alice_value, bob_value)} gold)")

    most_items = "Alice" if alice_items > bob_items else "Bob"
    print(f"Most items: {most_items} ({max(alice_items, bob_items)} items)")

    all_items = set(alice.keys()) | set(bob.keys())
    rare = [item for item in all_items
            if (item in alice) + (item in bob) == 1]
    print("Rarest items:", ", ".join(rare))


if __name__ == "__main__":
    main()
