e1 = {"name": "john", "salary": 50000, "program": ["HTML", "JS"]}
e2 = {"name": "mary", "salary": 60000, "program": ["HTML", "Python"]}
e3 = {"name": "bob", "salary": 70000, "program": ["Java", "Python", "C#"]}
emps = [e1, e2, e3]
# # 請求出會Python的員工人名, 並將放入到 names = [] 中
# names = []
# for emp in emps:
#     # print(emp["program"])
#     for i in emp["program"]:
#         # print(i)
#         if i == "Python":
#             # print(emp["name"])
#             names.append(emp["name"])
#
# print("會Python的員工有: %s" % names)
names = []
target = "Python"
for emp in emps:
    # print(emp["name"], emp["program"])
    for p in emp["program"]:
        # print(p)
        if p == target:
            # print(emp["name"], p)
            names.append(emp["name"])

print(names)