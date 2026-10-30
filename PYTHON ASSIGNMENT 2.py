age_list=[24,25,26,27,28]
name_list=["Janaki","Sanju","Karthik","Adarsh","Elga"]

print(age_list)
print(name_list)
print(name_list.append("Yazhini"))
print(name_list)
print(age_list.insert(2,30))

print(age_list)
print(name_list.remove("Yazhini"))
print(name_list)
print(age_list.pop())
print(age_list)
print(age_list.extend([29,30,26]))
print(age_list)
print(age_list.sort())
print(age_list)
print(age_list.reverse())
print(age_list)
print(min(age_list))

print(max(age_list))
print(sum(age_list))


print(name_list[0])
print(name_list[-1])
print(name_list[2:])
print(name_list[::-1])


student_marks={"Vignesh":68,"Aiswarya":79,"Arathi":85,"Yadan":67,"Vaishnavi":90}
print(student_marks)
print(student_marks["Arathi"])
print(student_marks.update({"Janani":80}))
print(student_marks)
print(student_marks.update({"Vignesh":82}))
print(student_marks)

print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())



my_set={"a","e","i","o","u","a","a","i"}
print(my_set)
#SET doesnot allow duplicates.
print(my_set)

#Set is unchangeable.

set1={1,3,5,7,9}
set2={2,3,5,8,10}
print (set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))



score=int(input("Enter your score(0-10)"))
if score>7:
    print("Above average:Fantastic score! Keep up the great momentum")
elif score>=4:
    print("Average:Steady progress! A bit more effort will make a big difference")

else:
    print("Below average: Keep trying! Small steps every day lead to big results")
