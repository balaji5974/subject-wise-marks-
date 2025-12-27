def about(name,sub):
    j=0
    b={}
    while j<len(name):
        a=[]
        grades={}


        for i in range(len(sub)):
            marks=int(input(f"enter marks of {name[j]} in:{sub[i]}"))
            a.append(marks)
            b[sub[i]]=marks
            total_marks=sum(a)
            avg_marks=sum(a)/(len(sub))
            if marks>=90:
                grades[sub[i]]="grade S"
            elif marks<90 and marks>80:
                grades[sub[i]]="grade A"
            elif marks<=80 and marks>70:
                grades[sub[i]]="grade B"
            elif marks<=70 and marks>60:
                grades[sub[i]]="grade C"
            elif marks<=60 and marks>50:
                grades[sub[i]]="grade D"
            elif marks<=50 and marks>40:
               grades[sub[i]]="grade E"
            else:
               grades[sub[i]]="FAIL"
        print(f"avarage marks of {name[j]} is {avg_marks}")
        print(f"total amrks of {name[j]} is {total_marks}")
        print(f"subject wise marks of {name[j]} is")
        print(b)
        print(f"subject wise grades of {name[j]} is")
        print(grades)
        j=j+1
    


          

n=int(input(f"enter requried no.students : "))
name=[]
while len(name)<n:
    x=input("enter name : ")
    name.append(x)

 
print(about(name,["maths","physics","chemistry"]))




