"""
id = "A123456789"
第二碼 sex =id[1] ==> 1 (1: 男生, 2, 女生)
第三碼 area =id[2] ==> 2 (0-5: 台灣, 6: 外國人, 7: 無戶籍 8: 港澳 9: 大陸)
印出: 台灣男
"""
id = "A223456789"
print(id[1], id[2])
print(id, "是", "台灣男")
x = int(id[1])
print(x)
id_error = lambda : print("不是")
id_info = {1: lambda : print("是")}
id_info.get(x, id_error)()

