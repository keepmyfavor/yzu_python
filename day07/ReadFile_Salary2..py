file = open("salary.txt", "r", encoding="UTF-8")
rows = file.readlines()
# 進行資料結構化的整理
# [ {"name": John, "salary": 45000} ......]

employees = []
for row in rows:
    data = row.split(",")
    name = data[0]  # 員工姓名
    salary = int(data[1].strip("\n"))  # 員工薪水
    employee = {"name": name, "salary": salary}  # 字典格式
    employees.append(employee)

print(employees)

# 求薪資總合
sum = 0
h_s = 0
h_n = ""
for employee in employees:
    sum += employee["salary"]
    if employee["salary"] > h_s:
        h_s = employee["salary"]
        h_n = employee["name"]
avg = sum / len(employees)
print("薪資總合", sum)
print("薪資平均", avg)


# 請問最高薪的人名是
print("最高薪水", h_n)

emp_max = max(employees, key=lambda e: e["salary"])  # e = employee
print(emp_max, emp_max["name"])
emp_min = min(employees, key=lambda e: e["salary"])
print(emp_min, emp_min["name"])


