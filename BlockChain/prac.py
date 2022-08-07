

Id = hash('Jack123')
print(Id)


pas = str(input("Enter the ID: "))
check = hash(pas)

if check == Id:
    print("yes")
else:
    print("no")