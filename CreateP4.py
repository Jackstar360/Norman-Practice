restraunts = ["Raising Canes", "Chick Fil A", "Taco Bell", "McDonalds", "Burger King"]

print("Welcome to your restaurant ranker! your current ranking is ", restraunts, "! You can add and rank a new restraunt")
new_restraunt = input("What restraunt would you like to add?")

def rank_restaurant(new_restraunt, restraunts):

    for i in range(len(restraunts)):
        str = "do you like A) ", new_restraunt, "or B) ", restraunts[i], "more? A/B "
        ranking = input(str)
        if ranking == "A":
            restraunts.insert(i, new_restraunt)
        elif ranking == "B":
            continue

        return restraunts
    
print("Your new ranking is", rank_restaurant(new_restraunt, restraunts))