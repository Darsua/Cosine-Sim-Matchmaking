import random

def generate_gaming_usernames(count=1000):
    adjectives = ['Dark', 'Epic', 'Shadow', 'Dragon', 'Cyber', 'Neon', 'Frost', 'Storm', 'Ninja', 'Ghost',
                  'Elite', 'Royal', 'Silent', 'Swift', 'Mystic', 'Flame', 'Toxic', 'Thunder', 'Pixel', 'Chaos']

    nouns = ['Slayer', 'Knight', 'Hunter', 'Warrior', 'Master', 'Legend', 'Phoenix', 'Demon', 'Wolf', 'Assassin',
             'Guardian', 'Striker', 'Sniper', 'Reaper', 'King', 'Beast', 'Hawk', 'Dragon', 'Phantom', 'Scout']

    gaming_terms = ['Pro', 'Gaming', 'Player', 'Boss', 'MVP', 'Elite', 'Ace', 'Champion', 'Prime', 'Master']

    usernames = set()

    while len(usernames) < count:
        pattern = random.randint(1, 4)

        if pattern == 1:
            username = f"{random.choice(adjectives)}{random.choice(nouns)}{random.randint(0, 999)}"
        elif pattern == 2:
            username = f"{random.choice(gaming_terms)}{random.choice(adjectives)}{random.randint(0, 99)}"
        elif pattern == 3:
            username = f"{random.choice(nouns)}{random.choice(gaming_terms)}{random.randint(0, 999)}"
        else:
            special_chars = ['x', '_', '-']
            char = random.choice(special_chars)
            username = f"{char}{random.choice(nouns)}{char}"

        usernames.add(username)
    return list(usernames)

usernames = generate_gaming_usernames(1000)

with open('gaming_usernames.txt', 'w') as f:
    for username in usernames:
        f.write(username + '\n')

print(f"Successfully generated {len(usernames)} unique usernames and saved them to 'gaming_usernames.txt'")