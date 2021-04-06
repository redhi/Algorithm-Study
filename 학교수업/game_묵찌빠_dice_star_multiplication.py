import random
def exam1():
    print("===기본점수 5점===")
    print("1.묵찌빠게임(30점)  2.주사위게임(25점)  3.별표게임(20점)  4.구구단게임(15점)  0.게임종료")
    game = input("수행할 과제 번호를 선택하세요")
    while(True):
        if(game == "0"):
            print("게임을 종료합니다")
            break;
        else:
            if(game == "1"):
                print("1 묵찌빠 게임입니다")
                win = 0
                lose = 0
                draw = 0
                player =1
                while(True) :
                    if(player == "0") :
                        total = win+lose+draw
                        print(total," 전 ",win," 승 ",lose," 패 ",draw," 무")
                        print("게임을 종료합니다")
                        break
                    else :
                        print("안녕하세요? 묵찌빠 게임을 시작합니다")
                        player = input("묵 찌 빠 중 하나를 입력하세요")
                        if(player == "묵"):
                            print("당신은 묵 를 내셨습니다")
                            computer = random.choice(['묵','찌','빠'])
                            print("컴퓨터는 "+computer+" 를 냈습니다")
                            if(computer == "묵"):
                                print("비겼습니다")
                                draw += 1
                            elif(computer == "찌"):
                                print("이겼습니다")
                                win += 1
                            elif(computer == "빠"):
                                print("졌습니다")
                                lose += 1
                        elif(player == "찌") :
                            print("당신은 찌 를 내셨습니다")
                            computer = random.choice(['묵','찌','빠'])
                            print("컴퓨터는 "+computer+" 를 냈습니다")
                            if(computer == "묵"):
                                print("졌습니다")
                                lose += 1
                            elif(computer == "찌"):
                                print("비겼습니다")
                                draw += 1
                            elif(computer == "빠"):
                                print("이겼습니다")
                                win += 1
                        elif(player == "빠") :
                            print("당신은 빠 를 내셨습니다")
                            computer = random.choice(['묵','찌','빠'])
                            print("컴퓨터는 "+computer+" 를 냈습니다")
                            if(computer == "묵"):
                                print("이겼습니다")
                                win += 1
                            elif(computer == "찌"):
                                print("졌습니다")
                                lose += 1
                            elif(computer == "빠"):
                                print("비겼습니다")
                                draw += 1
                    player = input("게임을 계속합니다 엔터를 누르세요 종료를 원하시면 0을 누르세요")                
            elif(game == "2"):
                print("2 주사위 게임입니다")
                request = 1
                while(True):
                    if(request == "n"):
                        print("게임을 종료합니다")
                        break
                    else:
                        request = input("사용자 주사위를 던질까요? y / n")
                        if(request == "y"):
                            print("사용자가 주사위를 던졌습니다")
                            dice = []
                            sum_player = 0
                            for i in range(5):
                                dice.append(random.randint(1,6))
                                sum_player += dice[i]
                            print(dice)
                            request_com = input("컴퓨터 주사위를 던질까요? y / n")
                            if(request_com == "y"):
                                print("컴퓨터가 주사위를 던졌습니다")
                                dice_com = []
                                sum_com = 0
                                for i in range(5):
                                    dice_com.append(random.randint(1,6))
                                    sum_com += dice_com[i]
                                print(dice_com)
                                print("사용자가 던진 주사위의 합은 ",sum_player," 입니다")
                                print("컴퓨터가 던진 주사위의 합은 ",sum_com," 입니다")
                                if(sum_player == 20 and sum_com == 20):
                                    print("승부가 나지 않았습니다")
                                elif(sum_player == 20):
                                    print("사용자가 이겼습니다")
                                    print("게임을 종료합니다")
                                    break
                                elif(sum_com == 20):
                                    print("컴퓨터가 이겼습니다")
                                    print("게임을 종료합니다")
                                    break
                                else:
                                    print("승부가 나지 않았습니다")
                            elif(request_com == "n"):
                                print("게임을 종료합니다")
                                break
                        elif(request == "n"):
                            print("게임을 종료합니다")
                            break
                    request = input("게임을 다시할까요? y / n")                                                                        
            elif(game == "3"):
                print("3 별표 게임입니다")
                line = 1
                while(True):
                    line = int(input("출력하는 별표의 줄수를 입력해주세요 종료를 원하시면 0을 입력하세요"))
                    if(line == 0):
                        print("종료합니다")
                        break
                    for i in range(1,line+1):
                        for j in range(line+1-i):
                            print(" ", end="")
                        for j in range(2*i-1):
                            print("*", end="")
                        print()
            elif(game == "4"):
                print("4 구구단게임입니다")
                while(True):
                    num = int(input("단을 입력하세요. 종료를 원하시면 10을 입력하세요"))
                    if(num == 10):
                        break
                    print(num,"단")
                    for i in range(1, 9+1):
                        print(num," x ",i," = ",num*i)
            print("===기본점수 5점===")
            print("1.묵찌빠게임(30점)  2.주사위게임(25점)  3.별표게임(20점)  4.구구단게임(15점)  0.게임종료")
            game = input("수행할 과제 번호를 선택하세요")

exam1()
