user1 = input("enter the first user name")
user2 = input("enter the second user name ")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        print("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            print("Rock wins!")
        else:
            print("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            print("Scissors win!")
        else:
            print("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            print("Paper wins!")
        else:
            print("Scissors win!")


print(compare(user1_answer, user2_answer))