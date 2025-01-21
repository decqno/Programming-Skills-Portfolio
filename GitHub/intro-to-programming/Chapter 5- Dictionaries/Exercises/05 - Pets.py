pets=[]

pet={
    'Animal Type': 'Tiger',
    'Name': 'Tamtam',
    'Owner': 'Hoshi',
    'Favorite Food': 'Kimchi',
    'MBTI': 'INFP'
}
pets.append(pet)

pet={
    'Animal Type': 'Fox',
    'Name': 'Fireball',
    'Owner': 'Wonwoo',
    'Favorite Food': 'Tteokbokki',
    'MBTI': 'ROCK'
}
pets.append(pet)

pet={
    'Animal Type': 'Rabbit',
    'Name': 'Chocherry',
    'Owner': 'Cheol',
    'Favorite Food': 'Salmon Steak',
    'MBTI': 'ISFJ'
}
pets.append(pet)

pet={
    'Animal Type': 'Otter',
    'Name': 'Chandal',
    'Owner': 'Chan',
    'Favorite Food': 'Gamjatang',
    'MBTI': 'INFJ'
}
pets.append(pet)

for pet in pets:
    print(f"\nAbout {pet['Name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
