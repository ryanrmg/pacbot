from bot import Bot
import time
import random

ghosts = ['red', 'blue', 'orange', 'pink']
def test():
    t = time.time()

    b = Bot()
    b.startGame()
    b.pacLeft()
    while time.time() - t < 100000000:
        b.setScreen()
        pos = b.getPacPosition()

        if (time.time() % .5) < 0.1:
            b.setScreen()
            b.clearBoard()
            b.getBoard
            hasmoved = False
            #b.setScreen()
            
            while hasmoved == False:

                #random.choice([b.pacLeft(), b.pacRight(), b.pacDown(), b.pacUp()])
                b.setScreen()
                for ghost in ghosts:
                    b.setScreen()
                    print(b.getGhostDistance(ghost))

                    if b.getGhostDistance(ghost) < 250:
                        if ghost == 'pink':
                            p = b.getPinkPosition()
                        if ghost == 'red':
                            p = b.getPinkPosition()
                        if ghost == 'blue':
                            p = b.getBluePosition()
                        if ghost == 'orange':
                            p = b.getOrangePosition()

                        if p < b.getPacPosition():
                            random.choice([b.pacRight, b.pacDown()])
                            print('yeah')
                            hasmoved = True
                        if p > b.getPacPosition():
                            random.choice([b.pacUp(), b.pacLeft()])
                            print('see ya')
                            hasmoved = True
                    else:
                        pos = b.getPacPosition()
                        while pos == b.getPacPosition():
                            random.choice([b.pacLeft(), b.pacRight(), b.pacDown(), b.pacUp()])
                            hasmoved = True

            #print("pink ghost distance : " + str(b.getGhostDistance('pink')))

            #if b.board[122] == 1:
            #    b.pacDown()
            #print(b.getPacPosition())





test()
