# Name - vishnu shon
# Roll No - 2020414

from a2 import*

import json


def read_data_from_file(file_path="data.json"):

	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records
records=read_data_from_file()

print('''
=================================================
                   QUERY DESK            
=================================================
Hello! Welcome to the query desk            
Following are the actions that you can make:

-------------------------------------------------
       CODE              |     DESCRIPTION  
-------------------------------------------------    
       1                 |     filter by first name         
       2                 |     filter by last name          
       3                 |     filter by full name 
       4                 |     filter by age range  
       5                 |     count by gender         
       6                 |     filter by address      
       7                 |     find alumni          
       8                 |     find toppers         
       9                 |     find blood donors        
       10                |     get common friends           
       11                |     is related           
       12                |     delete by id 
       13                |     add friend           
       14                |     remove friend       
       15                |     add education           
------------------------------------------------''')
print("Please enter -1 to quit the program")
read_data_from_file()
n=0
l=[]
for i in records:
	l.append(i["id"])
while n!= -1:
	n=int(input("Please enter the code: "))
	if n==1:
		fn=input("Enter the first name: ")
		print("Here are the related ids found", filter_by_first_name(records,fn))
	if n==2:
		ln=input("Enter the last name: ")
		print("Here are the related ids found", filter_by_last_name(records,ln))
	if n==3:
		fln=input("Enter the full name: ")
		print("Here are the related ids found", filter_by_full_name(records,fln))
	if n==4:
		minage=int(input("Enter the minimum age: "))
		maxage=int(input("Enter the maximum age: "))
		print("Here are the related ids found", filter_by_age_range(records,minage,maxage))
	if n==5:
		print(count_by_gender(records))
	if n==6:
		a={}
		print("""
        the type of the adress parameters that are vailable are
        house_no ,block ,town ,city ,state ,pincode
        """)
		n=int(input("Enter the number of adress parameters: "))
		adr=""
		while adr=="":
			for i in range(n):
				adr=input("Enter the parameter type: ")
				if adr!="":
					a[adr]=input("Enter the parameter value: ")
			if adr =="":
				print("Try again")

		print("Here are the related ids found",filter_by_address(records,a))

	if n==7:
		In=input("Enter the institute name: ")
		print("Here are the related ids found", find_alumni(records,In))
	if n==8:
		print(find_topper_of_each_institute(records))
	if n==9:
		k=0
		while k==0:
			rpi=int(input("Enter the reciever person's id: "))
			if rpi not in l:
				print("invalid id try again")
			if rpi in l:	
				print("Here are the related ids found", find_blood_donors(records,rpi))
				k+=1
	if n==10:
		k=0
		while k==0:
			fl= list(map(int,input("Enter the list of Ids in a space separated manner: ").split()))
			for i in fl:
				if i in l:
					if fl.index(i)==len(fl)-1:
						k+=1
						print("Here are the related ids found", get_common_friends(records,fl))
				if i not in l:
					print("try again one of the input is wrong")
					break
	if n==11:
		k=0
		while k==0:
			p1=int(input("enter first person id: "))
			p2=int(input("enter second person id: "))
			if p1 in l and p2 in l:
				print(is_related(records,p1,p2))
				k+=1
			if p1 not in l and p2 not in l:
				print("try again")
	if n==12:
		k=0
		while k==0:
			Id=int(input("Enter the id of the person: "))
			if Id in l:
				delete_by_id(records,Id)
				l.remove(Id)
				print("Records have been updated successfully.")
				print(records)
				k+=1
			if Id not in l:
				print("Id not present try again")

	if n==13:
		k=0
		while k==0 :
			pi=int(input("Enter the id of the person: "))
			fi=int(input("Enter the id of the friend: "))
			if pi in l and fi in l:
				k+=1
			if pi not in l and fi not in l:
				print("try again")
		add_friend(records,pi,fi)
		print("Records have been updated successfully.")
		print(records)
	if n==14:
		k=0
		while k==0 :
			pi=int(input("Enter the id of the person: "))
			fi=int(input("Enter the id of the friend: "))
			if pi in l and fi in l:
				k+=1
			if pi not in l and fi not in l:
				print("try again")
		remove_friend(records,pi,fi)
		print("Records have been updated successfully.")
		print(records)

	if n==15:
		k=True
		per=0
		pi=int(input("Enter the id of the person: "))
		Ins=input("Enter the institute name: ")
		on=(input("Is the person's studies ongoing(True/False): "))
		if on.lower()=="false":
			k=False
		if on.lower()=="true":
			k=True
		if k==False:
			per=int(input("Enter the percentage of the person: "))
		add_education(records,pi,Ins,k,per)
		if pi not in l:
			l.append(pi)
		print("Records have been updated successfully.")
		print(records)
	if n==-1:
		print("Thank You")
		exit()
	if n not in range(1,16) and n !=-1:
		print("Try again")
	else:
		print("Anything else ?")



