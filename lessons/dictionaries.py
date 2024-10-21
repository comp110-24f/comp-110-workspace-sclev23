"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of key-value entries
print(len(ice_cream))

# add key-value entries using subscription notation
ice_cream["pbj"] = 1
ice_cream["pbj"] += 10

# accesss values by their key using subscription
print(ice_cream["pbj"])

# re-assign values by their key using assignment
ice_cream["vanilla"] += 110
print(ice_cream)

# remove items by their key using the pop method
ice_cream.pop("strawberry")

# test for keys in dictionary
print("American Dream" in ice_cream)
print("vanilla" in ice_cream)

# loop through items using for-in loops
total_orders: int = 0
# the variable (e.g. flavor) iterates over each key one-by-one in the dictionary
for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]
print(f"Total orders: {total_orders}")
print(ice_cream["mint"])
