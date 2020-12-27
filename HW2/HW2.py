F_Name=input("Enter First Name:")
L_Name=input("Enter Last Name:")
Date_Of_Birth=int(input("Enter Date Of Birth(Just Year):"))
Age=2020-Date_Of_Birth

u=[]
u.append([F_Name,L_Name,Date_Of_Birth,Age])

for i in u:
	print(i)
	if i[3]<18:
		print("You can't go out because it's too dangerous")
	else:
		print("You can go to the street")
				