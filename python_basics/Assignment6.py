


Salary=int(input("Enter yor gross salary :"))

if Salary < 50000:
    tax=(2.5/100)* Salary
net_salary = Salary - tax

print(f"Gross salary: {Salary}")
print(f"Net salary:{net_salary}")
print(f"Tax={tax}")

Salary=int(input("Enter yor gross salary :"))

if Salary>50000 and Salary <100000:
    tax=(4.5/100)*Salary
    net_salary= Salary-tax

print(f"Gross salary: {Salary}")
print(f"Net salary:{net_salary}")
print(f"Tax={tax}")

Salary=int(input("Enter yor gross salary :"))
if Salary>100000:
    tax=(7.5/100)* Salary
    net_salary= Salary-tax
print(f"Gross salary: {Salary}")
print(f"Net salary:{net_salary}")
print(f"Tax={tax}")

Salary=int(input("Enter yor gross salary :"))
if Salary<50000 and Salary>50000 and Salary<100000 and Salary>100000:
    tax=(2.5/100)* Salary
    tax=(4.5/100)*Salary
    tax=(7.5/100)* Salary
    net_salary= Salary-tax
print(f"Gross salary: {Salary}")
print(f"Net salary:{net_salary}")
print(f"Tax={tax}")