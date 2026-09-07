names = ["Ram", "Hari", "Shyam", "Rita", "Sita", "Gita"]

index = names.index("Shyam")

print(any(name.lower() == 'ram' for name in names))
print(index)
