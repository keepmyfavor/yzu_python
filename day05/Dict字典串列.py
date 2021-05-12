# dict 是 key:value 的組合數組
salary = {"john": 50000, "mary": 60000}
print(salary)
print("john 的薪資:", salary["john"])

for key in salary:
    print("%s 的薪資: %d" % (key, salary[key]))

# 新增元素
salary.setdefault("bob", 70000)
print(salary)

total = 0
for key in salary:
    total += salary[key]

print(total)