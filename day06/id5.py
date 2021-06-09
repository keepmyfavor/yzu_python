id = "A123456789"
sex = lambda x : "男" if id[1] == '1' else "女"
area = id[2]
area_info ={
    '1' : lambda :print("台灣"),
    '2' : lambda :print("台灣"),
    '3' : lambda :print("台灣"),
    '4' : lambda :print("台灣"),
    '5' : lambda :print("台灣"),
    '6' : lambda :print("外國"),
    '7' : lambda :print("無國籍"),
    '8' : lambda :print("港澳"),
    '9' : lambda :print("大陸")
}
area_info.get(area)()

print(sex(1))