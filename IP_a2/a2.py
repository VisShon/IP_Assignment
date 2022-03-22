# Assignment - 2
# Name - Vishnu Shon
# Roll No - 2020414

import json


def read_data_from_file(file_path="data.json"):

	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	l=[]
	for i in range(len(records)):
		if records[i]["first_name"].lower()==first_name.lower():
			l.append(records[i]["id"])
	return(l)

def filter_by_last_name(records, last_name):
	l=[]
	for i in range(len(records)):
		if records[i]["last_name"].lower()==last_name.lower():
			l.append(records[i]["id"])
	return(l)


def filter_by_full_name(records, full_name):
	l=[]
	fl=full_name.lower()
	for i in range(len(records)):
		if [records[i]["first_name"].lower(),records[i]["last_name"].lower()]==fl.split():
			l.append(records[i]["id"])
	return(l)

def filter_by_age_range(records, min_age, max_age):
	l=[]
	for i in range(len(records)):
		if records[i]["age"] in range(min_age,max_age+1):
			l.append(records[i]["id"])
	return(l)

def count_by_gender(records):
	d={}
	m=0
	fm=0
	for i in range(len(records)):
		if records[i]["gender"]=="female":
			fm+=1
		if records[i]["gender"]=="male":
			m+=1
	d["male"]=m
	d["female"]=fm
	return(d)

def filter_by_address(records, address):
	l=[]
	lr=[]
	for k in range(len(records)):				
		d={}
		d["first_name"]=records[k]["first_name"]
		d["last_name"]=records[k]["last_name"]
		lr.append(d)
	for i in range(len(records)):
		for j in address.keys():
			if j!="house_no" and j!="pincode":
				if address[j].lower()!=records[i]["address"][j].lower():
					l.append(lr[i])
					break
			if j=="house_no" or j=="pincode":
				if address[j]!=records[i]["address"][j]:
					l.append(lr[i])
					break
	for q in l:				
		lr.remove(q)
	return(lr)


def find_alumni(records, institute_name):
	lr=[]
	for j in range(len(records)):
		for i in range(len(records[j]["education"])):
			if records[j]["education"][i]["institute"].lower()==institute_name.lower() and records[j]["education"][i]["ongoing"]==False:			
				d={}
				d["first_name"]=records[j]["first_name"]
				d["last_name"]=records[j]["last_name"]
				d["percentage"]=records[j]["education"][i]["percentage"]
				lr.append(d)
				break
	return(lr)

def find_topper_of_each_institute(records):
	d={}
	di={}
	for i in range(len(records)):
		for j in records[i]["education"]:
			if j["ongoing"]==False and j["institute"] not in d.keys():
				d[j["institute"]]=j["percentage"]
				di[j["institute"]]=records[i]["id"]
			if j["ongoing"]==False and j["institute"] in d.keys() and j["percentage"]>d[j["institute"]]:
				d[j["institute"]]=j["percentage"]
				di[j["institute"]]=records[i]["id"]
	for k in d.keys():
		d[k]=di[k]
	return d

def find_blood_donors(records, receiver_person_id):
	d={}
	for i in range(len(records)):
		if receiver_person_id==records[i]["id"]:
			bg = records[receiver_person_id]["blood_group"]
	cr=[]
	if bg=="A":
		cr=["A","O"]
	if bg=="B":
		cr=["B","O"]
	if bg=="AB":	
		cr=["A","B","AB","O"]
	if bg=="O":
		cr=["O"]
	for i in range(len(records)):
		if records[i]["blood_group"] in cr:
			d[i]=records[i]["contacts"]
	del d[receiver_person_id]
	return d

def get_common_friends(records, list_of_ids):
	l=[]
	lr=[]
	for a in records:
		if a["id"] in list_of_ids:
			for j in a["friend_ids"]:
				l.append(j)
	for q in l:
		if l.count(q)==len(list_of_ids) and q not in lr:
			lr.append(q)
	return lr

def is_related(records, person_id_1, person_id_2):
	def relate(records,p1,p2,d):
		for j in range(len(records)):
			if p1==records[j]["id"]:
				a=j
		if p2 in records[a]["friend_ids"]:
		    return True
		for i in records[a]["friend_ids"] :
			if i not in d:
				d.append(i)
				x= relate(records,i,p2,d)
				if x:
					return True 
		return False
	d=[]	
	return relate(records,person_id_1,person_id_2,d)



def delete_by_id(records, person_id):
	for j in range(len(records)):
		if records[j]["id"]==person_id:
			records.remove(records[j])
			break
	for i in range(len(records)):
		if person_id in records[i]["friend_ids"] :
			records[i]["friend_ids"].remove(person_id)
	return records		


def add_friend(records, person_id, friend_id):
	for i in range(len(records)):	
		if person_id==records[i]["id"]:
			if friend_id not in records[i]["friend_ids"]:
				records[i]["friend_ids"].append(friend_id)
				records[i]["friend_ids"].sort()
		if friend_id==records[i]["id"]:
			if person_id not in records[i]["friend_ids"]:
				records[i]["friend_ids"].append(person_id)
				records[i]["friend_ids"].sort()
	return records

def remove_friend(records, person_id, friend_id):
	for i in range(len(records)):	
		if person_id==records[i]["id"]:
			if friend_id in records[i]["friend_ids"]:
				records[i]["friend_ids"].remove(friend_id)
		if friend_id==records[i]["id"]:
			if person_id in records[i]["friend_ids"]:
				records[i]["friend_ids"].remove(person_id)
	return records


def add_education(records, person_id, institute_name, ongoing, percentage):
	d={"institute":institute_name,"ongoing":ongoing}
	if ongoing==False:
		d["percentage"]=percentage
	for i in range(len(records)):
		if records[i]["id"]==person_id:
			records[i]["education"].append(d)
	return records
