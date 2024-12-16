  # due to the nature of random numbers we import the random library
from random import randint

# here we create 4 bingo cards for each situation
# Then we return each bingo card with its evaluation
def main():
    vertical = create_cards(0)
    horizontal = create_cards(1)
    diagonal = create_cards(2)
    almost = create_cards(3)
    return f"{display_card(vertical)} {check_zeros(vertical)} \n{display_card(horizontal)} {check_zeros(horizontal)} \n{display_card(diagonal)} {check_zeros(diagonal)} \n{display_card(almost)} {check_zeros(almost)}"

# first we define the main function in which we create an empty dict and an empty list
# for each letter
def create_cards(x):
    bingoCard = {}
    B = []
    I = []
    N = []
    G = []
    O = []

# same construct of the 024 excersice to create a bingo card
    while len(B) < 5:
        num = randint(1, 15)
        B.append(num) if num not in B else B.remove(num)
    bingoCard["b"] = B

    while len(I) < 5:
        num = randint(16, 30)
        I.append(num) if num not in I else I.remove(num)
    bingoCard["i"] = I

    while len(N) < 5:
        num = randint(31, 45)
        N.append(num) if num not in N else N.remove(num)
    bingoCard["n"] = N

    while len(G) < 5:
        num = randint(46, 60)
        G.append(num) if num not in G else G.remove(num)
    bingoCard["g"] = G

    while len(O) < 5:
        num = randint(61, 75)
        O.append(num) if num not in O else O.remove(num)
    bingoCard["o"] = O

# depending on the arg of the function the returned dict should be winning horizontally,
# vertically, diagonally or almost winning
    if x == 0:
        bingoCard["b"][0] = 0
        bingoCard["b"][1] = 0
        bingoCard["b"][2] = 0
        bingoCard["b"][3] = 0
        bingoCard["b"][4] = 0

    elif x == 1:
        bingoCard["b"][0] = 0
        bingoCard["i"][0] = 0
        bingoCard["n"][0] = 0
        bingoCard["g"][0] = 0
        bingoCard["o"][0] = 0

    elif x == 2:
        bingoCard["b"][0] = 0
        bingoCard["i"][1] = 0
        bingoCard["n"][2] = 0
        bingoCard["g"][3] = 0
        bingoCard["o"][4] = 0

    elif x == 3:
        bingoCard["b"][0] = 0
        bingoCard["i"][1] = 0
        bingoCard["n"][2] = 0
        bingoCard["g"][4] = 0
        bingoCard["o"][3] = 0

    # finally we return the dictionary
    return bingoCard


def display_card(card):
# we use f strings to print a title "BINGO"  and each value of the same index
# from all the keys, creating a Table
    return f"\nB    I    N    G    O\n{card["b"][0]}   {card["i"][0]}   {card["n"][0]}   {card["g"][0]}   {card["o"][0]} \n{card["b"][1]}   {card["i"][1]}   {card["n"][1]}   {card["g"][1]}   {card["o"][1]} \n{card["b"][2]}   {card["i"][2]}   {card["n"][2]}   {card["g"][2]}   {card["o"][2]} \n{card["b"][3]}   {card["i"][3]}   {card["n"][3]}   {card["g"][3]}   {card["o"][3]} \n{card["b"][4]}   {card["i"][4]}   {card["n"][4]}   {card["g"][4]}   {card["o"][4]}"


def check_zeros(card):
# through an if, elif, else statement we check each index to match the conditions and
# return the designated result
    if (card["b"][0] == 0 and card["b"][1] == 0 and card["b"][2] == 0 and card["b"][3] == 0 and card["b"][4] == 0):
        return f"{True}, this is a winning card"
    elif (card["b"][0] == 0 and card["i"][0] == 0 and card["n"][0] == 0 and card["g"][0] == 0 and card["o"][0] == 0):
        return f"{True}, this is a winning card"
    elif (card["b"][0] == 0 and card["i"][1] == 0 and card["n"][2] == 0 and card["g"][3] == 0 and card["o"][4] == 0):
        return f"{True}, this is a winning card"
    else:
        return f"{False}, this is ALMOST a winning card"



if __name__ == "__main__":
    print(main())
