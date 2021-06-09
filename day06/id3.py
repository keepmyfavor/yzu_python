'''
HW use lambda to code
A123456789
second sex=1(1:male, 2:female) #id[1]
third  area=2(0-5:taiwan, 6:foreign 7:no area 8:hk 9:china "id[2]
print:taiwan male
'''
'''
id="A123456789" #id[1]==1 means male, id[1]==2 means female
id[1]=1
id_info1={1:lambda:print("male"), 2:lambda:print("female")}
id[2]=random.randit(0,5)
id_info2={random.randit(0,5):lambda:print("taiwan")}
print(id_info1,id_info2)
'''

id="A123456789"
def sex(id):
    if id[1]=="1":
        return "male"
    else:
        return "female"
print(sex(id))


def area(id):
    if id[2]== "6":
        return "foreign"
    elif id[2]=="7":
        return "no area"
    elif id[2]=="8":
        return "china"
    else:
        return "taiwan"
print(area(id))

sex_result = lambda id:"male" if id[1]=="1" else "female"
area_result= lambda id:"taiwan" if id[2]=="0"or"1"or"2"or"3"or"4"or"5" else "None"
print(sex_result(id),area_result(id))