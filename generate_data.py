import pandas as pd
import random

names = ["Palak","Rahul","Aman","Sneha","Riya","Karan","Anjali","Vikas"]
branches = ["CSE","IT","ECE","ME"]

data = []

for i in range(200):
    name = random.choice(names)
    branch = random.choice(branches)
    cgpa = round(random.uniform(5.0, 9.5), 2)
    internship = random.randint(0,2)
    projects = random.randint(1,5)
    skills = random.choice(["Python,SQL","Java","C++","Python,ML","SQL,Excel"])
    
    # Placement Logic
    if cgpa > 7 and internship >=1 and projects >=2:
        status = "Placed"
        package = round(random.uniform(4,12),2)
        company = random.choice(["TCS","Infosys","Wipro","Accenture"])
    else:
        status = "Not Placed"
        package = 0
        company = "None"

    data.append([i,name,branch,cgpa,skills,internship,projects,status,company,package])

df = pd.DataFrame(data, columns=[
    "student_id","name","branch","cgpa","skills",
    "internship","projects","placement_status","company","package"
])

df.to_csv("placement_data.csv", index=False)
print("Dataset Generated!")