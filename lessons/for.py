"""for loop practice."""

# pets: list[str] = ["Louie", "Bo", "Bear"]
# for i in pets:
# print(f"Good boy, {i}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for i in range(0, len(names)):
    print(f"{i}: {names[i]}")
