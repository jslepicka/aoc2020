from collections import deque
decks = {}

def load_decks():
    decks = {}
    with open("22.txt") as f:
        players = f.read().split("\n\n")
        for p in players:
            player_num = 0
            for l in [x.strip() for x in p.split("\n")]:
                if l.startswith("Player"):
                    player_num = int(l.split(" ")[1][:-1])
                    decks[player_num] = deque()
                else:
                    decks[player_num].append(int(l))
    return decks

def part1():
    decks = load_decks()
    while len(decks[1]) > 0 and len(decks[2]) > 0:
        p1 = decks[1].popleft()
        p2 = decks[2].popleft()
        winner = decks[1] if p1 > p2 else decks[2]
        winner.append(max(p1, p2))
        winner.append(min(p1, p2))
    
    winner = decks[1] if len(decks[1]) > 0 else decks[2]
    score = 0
    for i, val in enumerate(reversed(winner)):
        score += (i + 1) * val
    return score

def play_game(deck1, deck2):
    seen = {}
    while len(deck1) > 0 and len(deck2) > 0:
        h = hash((str(deck1) + str(deck2)))
        if h in seen:
            #this deck was seen before, end game, player 1 is winner
            return 1
        else:
            seen[h] = 1
        w = 0
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = deck1.copy()
            new_deck2 = deck2.copy()
            for _ in range(len(new_deck1) - card1):
                new_deck1.pop()
            for _ in range(len(new_deck2) - card2):
                new_deck2.pop()
            w = play_game(new_deck1, new_deck2)
        else:
            w = 1 if card1 > card2 else 2

        if w == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)


    winner = 1 if len(deck1) > len(deck2) else 2
    return winner

def part2():
    decks = load_decks()
    play_game(decks[1], decks[2])
    winner = decks[1] if len(decks[1]) > 0 else decks[2]
    score = 0
    for i, val in enumerate(reversed(winner)):
        score += (i + 1) * val
    return score

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
