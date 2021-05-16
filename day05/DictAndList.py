e1 = {"name": "john", "salary": 50000}
e2 = {"name": "mary", "salary": 60000}
e3 = {"name": "bob", "salary": 70000}
emps = [e1, e2, e3]
print(len(emps), emps)

# 求總薪資 = ?
sum = 0
for emp in emps:
    sum += emp["salary"]
print(sum)


# 最高薪資
# 預先建立空字串
salary = []
for emp in emps:
   salary.append(emp["salary"])
print(max(salary))

# 最低薪資
print(min(salary))