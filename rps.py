('rock pappers scissor game should inclued three, rounds each round contains diffrent moves from player 1 to player 2 ')
add(): str('if u win best outta 2/3 you automatcially win')
print (you cant go up to 4 rounds .)
add(): technical requirements: if one person win 2 rounds inna row the other person will automactially lose. but if the other person win an round and you too win a round thats when you go up to 4 rounds 


' we could use strings to represent each option an possibly intergeer for the selection '
"example input 1 for rock, inout 2 for the scissior, ubout for paper"

'we can use a comparison operator to who won more rounds '
'the person who won more rounds, wins'
' we use an loop to keepp the game going until someone wins.'







#development
def rpsgame():
    print("welcome to rock paper scissor: the game!")
    print("please select one of the following :")
    print("enter p to start games,")
    print('enter r to see rules, ')
    selection = input()
    if selection == 'p':
        print('the game is starting...')
    elif selection == 'r':
        print(' here are the game rules ...')
        choiceUser = input("please make selection, r = rock, p = paper, s = scissor,")
        choicecpu = random.choice(rpsoptions_cpu)
    else:
        print("sorry, we didnt undersyamd your entry")