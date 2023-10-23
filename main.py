import random
import time
chislo_random = random.randint (0,25)
print(chislo_random)
popetki = 5
popetki1 = 5
timing = time.time()
while True:
    timerik = time.time() - timing
    if timerik <= 20:
        print("У вас есть 20 секунд чтобы отгадать число")
        print("Осталось", 10 - (timerik // 1), "сек.")
        chislo_polzovatela=int(input("Введите число от 0-25 :"))
        if chislo_polzovatela == chislo_random:
            print("Поздравляю вы угадали.")
            print("Вы потратили",popetki1-popetki,"попыток.")
            print("Вы потратили",timerik//1,"сек.")
            igrat_eshe_raz = str(input("Хотите сыграть ещё раз?"))
            if igrat_eshe_raz == "НЕТ":
                break
            elif igrat_eshe_raz == "ДА":
                print("Хорошо")
                chislo_random = random.randint(0, 25)
                print(chislo_random)
            else:
                break

        elif chislo_polzovatela < chislo_random:
            print("Попробуйте больше.")
            popetki=popetki-1
            if popetki == 0:
                print("У вас кончились попытки. ")
                igrat_eshe_raz = str(input("Хотите сыграть ещё раз?"))
                if igrat_eshe_raz == "НЕТ":
                    break
                elif igrat_eshe_raz == "ДА":
                    print("Хорошо")
                    chislo_random = random.randint(0, 25)
                    print(chislo_random)
                else:
                    break

        elif chislo_polzovatela > chislo_random:
            print("Попробуйте меньше.")
            popetki = popetki - 1
            if popetki == 0:
                print("У вас кончились попытки. ")
                igrat_eshe_raz = str(input("Хотите сыграть ещё раз?"))
                if igrat_eshe_raz == "НЕТ":
                    break
                elif igrat_eshe_raz == "ДА":
                    print("Хорошо")
                    chislo_random = random.randint(0, 25)
                    print(chislo_random)
                else:
                    break

        else:
            igrat_eshe_raz = str(input("Хотите сыграть ещё раз?"))
            if igrat_eshe_raz == "НЕТ":
                break
            elif igrat_eshe_raz == "ДА":
                print("Хорошо")
                chislo_random = random.randint(0, 25)
                print(chislo_random)
            else:
                break

    else:
        igrat_eshe_raz = str(input("Хотите сыграть ещё раз?"))
        if igrat_eshe_raz == "НЕТ":
            break
        elif igrat_eshe_raz == "ДА":
            print("Хорошо")
            chislo_random = random.randint(0, 25)
            print(chislo_random)
        else:
            break