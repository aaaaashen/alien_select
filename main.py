import random
alien_color = ["green", "yellow", "blue"]
while True:
    random.shuffle(alien_color)
    print(alien_color)
    for color in alien_color:
        if input() == '':  #按一次回车输出一个人名
            if alien_color[0] == "green":
                print("玩家获得了五个点")
                break
            elif alien_color[0] == "yellow":
                print("玩家获得了十个点")
                break
            elif alien_color[0] == "blue":
                print("玩家获得了十五个点")
                break
        elif input() == 'quit':
                print('游戏结束')
                break
    break
