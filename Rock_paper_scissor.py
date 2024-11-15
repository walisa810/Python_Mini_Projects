import random

def play():
    user = input(" 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r','p','s'])

    # r > s , s > p , p > r
    if( user == computer):
        return 'tie'
    
    if( (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
    or (user == 'p' and computer == 'r')):
        return "You won!!"
    
    return "You lost!!"

count = 0
i = 0 
while( i < 5):
    x = play()
    print(x)
    if( x == "You won!!"):
        count += 1
    i += 1

if( count >= 3):
    print('You have won against Computer')
else:
    print('You have lost against Computer')