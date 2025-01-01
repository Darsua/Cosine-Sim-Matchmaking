import random
import json

with open('gaming_usernames.txt', 'r', encoding='utf-8') as file:
    usernames = [line.strip() for line in file.readlines()]

vectors = []
for i in range(len(usernames)):
    vector = {
        "Username": usernames[i],
        "DamageScore": round(random.uniform(0, 400), 2),
        "SkillScore": round(random.uniform(0, 100), 2),
        "SynergyScore": round(random.uniform(0, 40), 2)
    }
    vectors.append(vector)

with open('players.json', 'w', encoding='utf-8') as file:
    json.dump(vectors, file, indent=4)

print(f"{len(usernames)} players generated and saved to players.json.")