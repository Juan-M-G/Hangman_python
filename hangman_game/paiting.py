#With this module, I can draw a hangman in a game.
def paint(lifes):
    floor = [
                "                          .==========================. ",
                "                         |                            |",
                "                          '==========================' "]
    post = "                                     |     |"
    roof = [
                "         .=================================. ", 
                "        |                                   |", 
                "         '=================================' "]
    rope = [
                "            ||                       |     |",
                "            ||                       |     |",
                "            ||                       |     |",
                "            ||_                      |     |"
    ]
    head = [
                "           /x x\                     |     |",
                "           | ° |                     |     |",
                "          __|´|__                    |     |"        
    ]

    right_arm = [
                "                  \                  |     |",
                "          |     |\ \                 |     |",
                "          |     | \ \                |     |",
                "          |     |  ¨¨                |     |"
    ]
    complete_body = [
                "        /         \                  |     |",
                "       / /|     |\ \                 |     |",
                "      / / |     | \ \                |     |",
                "      ¨¨  |     |  ¨¨                |     |"
    ]
    body = [
                "                                     |     |",
                "          |     |                    |     |",
                "          |     |                    |     |",
                "          |     |                    |     |"
    ]
    left_leg = [
                "         /´                          |     |",
                "        /   /                        |     |",
                "        |  |                         |     |",
                "       _|  |                         |     |",
                "      (____|                         |     |"
    ]

    legs = [
                "         /´     ´\                   |     |",
                "        /   / \   \                  |     |",
                "        |  |   |  |                  |     |",
                "       _|  |   |  |_                 |     |",
                "      (____|   |____)                |     |"
    ]

    post_high = 17
    if lifes <=7:
        for i in range(len(roof)):
            print(roof[i])
    if lifes <=6:
        post_high = 13
        for i in range(len(rope)):
            print(rope[i])
    if lifes <=5:
        post_high = 10
        for i in range(len(head)):
            print(head[i])
    if lifes <=2:
        post_high = 6
        for i in range(len(complete_body)):
            print(complete_body[i])
    elif lifes <=3:
        post_high = 6
        for i in range(len(right_arm)):
            print(right_arm[i])
    elif lifes <=4:
        post_high = 6
        for i in range(len(body)):
            print(body[i])
    if lifes <=0:
        post_high = 1
        for i in range(len(legs)):
            print(legs[i])
    elif lifes <=1:
        post_high = 1
        for i in range(len(left_leg)):
            print(left_leg[i])
    if lifes <=8:
        for i in range(post_high):
            print(post)
    if lifes <= 9:
        for i in range(len(floor)):
            print(floor[i])
    
       