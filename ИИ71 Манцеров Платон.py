#сложный уровень, 3 задание

print("сеодня лето?")
summer = input()
if summer == "да":
    print("сегодня жарко?")
    temp = input()
    if temp == "да":
        print("одень шорты и майку")
    elif temp == "нет":
        print("одень тонкую кофту и штаны")
elif summer == "нет":
    print("сегодня зима?")
    winter = input()
    if winter == "да":
        print("ветер сильный?")
        wind = input()
        if wind == "да":
            print("одень кофту, куртку, штаны, шапку, шарф")
        elif wind == "нет":
            print("одень кофту, куртку, штаны, шапку")
    elif winter == "нет":
        print("сегодня осень?")
        autumn = input()
        if autumn == "да":
            print("Одень штаны и кофту")
        elif autumn == "нет":
            print("сегодня весна?")
            spring = input()
            if spring == "да":
                print("одень спорт. костюм")




