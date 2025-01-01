import random
import numpy as np
import json

def read_players():
    with open('players.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def vector(player):
    return [player['DamageScore'], player['SkillScore'], player['SynergyScore']]

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def calculate_score(player1, player2):
    playstyle_similarity = cosine_similarity(vector(player1), vector(player2))
    skill_gap = abs(np.linalg.norm(vector(player1)) - np.linalg.norm(vector(player2)))
    score = playstyle_similarity / (skill_gap if skill_gap > 1 else 1)
    return score

def matchmake(players, user, n):
    scores = []
    for player in players:
        if player['Username'] != user['Username']:
            score = calculate_score(user, player)
            scores.append((player['Username'], score))
    scores.sort(key=lambda x: -x[1])
    return scores[:n]

def get_ratings(players):
    norms = [np.linalg.norm(vector(p)) for p in players]
    min_norm = min(norms).round(2)
    max_norm = max(norms).round(2)
    avg_norm = (sum(norms) / len(norms)).__round__(2)

    print(f"(Min: {min_norm}, Max: {max_norm}, Avg: {avg_norm})\n")

def main():
    players = read_players()
    user = players[int(random.uniform(0, len(players)))]
    matches = matchmake(players, user, 9)
    print(f"Match for {user['Username']} with rating {np.linalg.norm(vector(user)).round(2)}:")
    get_ratings(players)

    print("Ally Team:")
    print(user['Username'])
    for i in range(1, 9, 2):
        print(f"{matches[i][0]} ({matches[i][1].round(2)})")

    print("\nEnemy Team:")
    for i in range(0, 9, 2):
        print(f"{matches[i][0]} ({matches[i][1].round(2)})")

if __name__ == '__main__':
    main()