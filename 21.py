#ingredients are keyed by ingredient and contain a list of allergens they could be
ingredients = {}
ingredient_appearances = {}

input = []
with open("21.txt") as f:
    input = [x.strip() for x in f.readlines()]

for l in input:
    ing, all = l.split("(")
    aa = []
    for a in [x.replace(",", "").replace(")", "") for x in all.split()[1:]]:
        aa.append(a)
    for i in [x.strip() for x in ing.split(" ")[:-1]]:
        if i not in ingredient_appearances:
            ingredient_appearances[i] = 1
        else:
            ingredient_appearances[i] += 1
        if i not in ingredients:
            ingredients[i] = aa.copy()
        else:
            for a in aa:
                if a not in ingredients[i]:
                    ingredients[i].append(a)

def part1():
    for l in input:
        ing, all = l.split("(")
        ii = [x.strip() for x in ing.split(" ")[:-1]]
        #for each allergen
        for a in [x.replace(",", "").replace(")", "") for x in all.split()[1:]]:
            #for each ingredient in the list dict of ingredients->possible allergens
            for i in ingredients:
                #if the allergen is in the list of possible allergens but it's not in the ingredient
                #list in this line of input, it can't be the correct ingredient->allergen
                if a in ingredients[i] and i not in ii:
                    ingredients[i].remove(a)
    count = 0
    for i in ingredients:
        if len(ingredients[i]) == 0:
            count += ingredient_appearances[i]

    return count

def part2():
    ing = {}
    #get a dict of ingredients that have at least one allergen
    for i in ingredients:
        if len(ingredients[i]) != 0:
            ing[i] = ingredients[i].copy()
    print(ing)
    sd = {}
    while True:
        #sort the list of ingredient ordered by number of allergens
        #if there's only one allergen, we know this is the correct ingredient->allergen
        sd = {k: v for k, v in sorted(ing.items(), key=lambda item: len(item[1]))}
        resolved = []
        progress = 0
        for i in sd:
            #if only one allergen, add this allergen to the list of "resolved" allergens
            if len(sd[i]) == 1:
                resolved.append(sd[i][0])
            else:
                #otherwise, loop through the ingredients and remove the list of resolved allergens from their
                #possible allergens
                for r in resolved:
                    if r in sd[i]:
                        sd[i].remove(r)
                        progress = 1
        #loop until every ingredient is down to one allergen
        if progress == 0:
            break

    r = {k: v for k, v in sorted(ing.items(), key=lambda item: item[1][0])}
    result = ",".join(str(x) for x in r.keys())
    return result
    
print("Part 1: %d" % part1())
print("Part 2: %s" % part2())

     