id = "A123456789"
sex = lambda x : "男" if id[1] == '1' else "女"
area = id[2]
area_code = {
    '1' : lambda :"台灣",
    '2' : lambda :"台灣",
    '3' : lambda :"台灣",
    '4' : lambda :"台灣",
    '5' : lambda :"台灣",
    '6' : lambda :"外國",
    '7' : lambda :"無國籍",
    '8' : lambda :"港澳",
    '9' : lambda :"大陸"
}
local = area_code.get(area)()

print(id,local,sex(1))