# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shaegels <shaegels@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 15:50:22 by shaegels          #+#    #+#              #
#    Updated: 2025/12/15 13:14:51 by shaegels         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_inventory(player_name, inventory):
    """
    Display a player's inventory with statistics.

    Args:
        player_name (str): Name of the player.
        inventory (dict): Inventory data.

    Returns:
        tuple: Total inventory value and total item count.
    """
    print(f"=== {player_name}'s Inventory ===")

    total_value = 0
    total_items = 0
    categories = {}

    for item, data in inventory.items():
        quantity = data["quantity"]
        value = data["value"]
        rarity = data["rarity"]
        category = data["category"]

        total_items += quantity
        total_value += quantity * value
        categories[category] = categories.get(category, 0) + quantity

        print(
            f"{item} ({category}, {rarity}): "
            f"{quantity}x @ {value} gold each = {quantity * value} gold"
        )

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print(
        "Categories:",
        ", ".join(f"{cat}({count})" for cat, count in categories.items()),
    )

    return total_value, total_items


def transfer_item(sender, receiver, item, amount, sender_name, receiver_name):
    """
    Transfer items from one inventory to another.

    Args:
        sender (dict): Sender's inventory.
        receiver (dict): Receiver's inventory.
        item (str): Item name.
        amount (int): Quantity to transfer.
        sender_name (str): Sender's name.
        receiver_name (str): Receiver's name.

    Returns:
        bool: True if transfer succeeded, False otherwise.
    """
    print(
        f"=== Transaction: {sender_name} gives "
        f"{receiver_name} {amount} {item}(s) ==="
    )

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
    """
    Run the player inventory system demonstration.
    """
    print("=== Player Inventory System ===")

    alice = {
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500,
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50,
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200,
        },
    }

    bob = {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "value": 800,
        },
    }

    alice_value, alice_items = print_inventory("Alice", alice)

    transfer_item(
        sender=alice,
        receiver=bob,
        item="potion",
        amount=2,
        sender_name="Alice",
        receiver_name="Bob",
    )

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(
        f"Bob potions: "
        f"{bob.get('potion', {'quantity': 0})['quantity']}"
    )

    print("\n=== Inventory Analytics ===")

    bob_value = sum(
        item["value"] * item["quantity"] for item in bob.values()
    )
    bob_items = sum(item["quantity"] for item in bob.values())

    most_valuable = "Alice" if alice_value > bob_value else "Bob"
    print(
        f"Most valuable player: {most_valuable} "
        f"({max(alice_value, bob_value)} gold)"
    )

    most_items = "Alice" if alice_items > bob_items else "Bob"
    print(
        f"Most items: {most_items} "
        f"({max(alice_items, bob_items)} items)"
    )

    all_items = set(alice) | set(bob)
    rare_items = [
        item for item in all_items
        if (item in alice) + (item in bob) == 1
    ]

    print("Rarest items:", ", ".join(rare_items))


if __name__ == "__main__":
    main()
