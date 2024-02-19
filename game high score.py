def game():
    return 500
score=game()
with open('highscore.txt')as f:
    highscore=int(f.read())
if highscore<score or highscore=='':
    with open("highscore.txt",'w')as f:
        f.write(str(score))
    
