#Original Guestlist
guests=["Karl Marx", "Vernon Chwe", "Zendaya"]

name=guests[0]
print(f"{name}, please come to dinner.")

name=guests[1]
print(f"{name}, please come to dinner.")

name=guests[2]
print(f"{name}, please come to dinner.")

name=guests[2]
print(f"\n{name} is busy and won't be able to come.")

#New Person
del(guests[2])
guests.insert(2, "Sabrina Carpenter")

#New Invitation
name=guests[0]
print(f"\n{name}, please come to dinner.")

name=guests[1]
print(f"{name}, please come to dinner.")

name=guests[2]
print(f"{name}, please come to dinner.")

#Table won't arrive on time
print("\nDue to circumstances, the dinner table only has room for two other people.")

name=guests.pop()
print(f"Sorry {name}, there's no more room at the table.")

#Final Guestlist
name=guests[0]
print(f"\n{name}, please come to dinner.")

name=guests[1]
print(f"{name}, please come to dinner.")

#Empty List
del(guests[0])
del(guests[0])

print(guests)
