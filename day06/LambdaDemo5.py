'''
python 裡沒有 switch
A123456789 (1:男生, 2:女生)
sex = 1
switch(sex) {
    case 1:
        print("男生");
        break;
    case 2:
        print("女生");
        break;
}

lambda 與 dict 的合作
'''
sex = 1
sex_info = {1: lambda : print("男生"), 2: lambda : print("女生")}
sex_info.get(sex)()

sex = 1
sex_info = {
                1: lambda money: print("男生", money),
                2: lambda momey: print("女生", momey * 1.2)
            }
sex_info.get(sex)(1000)


sex = 3
sex_error = lambda money : print("姓別錯誤", 0)
sex_info = {
                1: lambda money: print("男生", money),
                2: lambda momey: print("女生", momey * 1.2)
            }
sex_info.get(sex, sex_error)(1000)