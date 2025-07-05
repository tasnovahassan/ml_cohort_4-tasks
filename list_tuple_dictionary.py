#Task-1
list_value=[2,6,9,7,5]
list_value.append(1)
list_value.remove(6)
print(list_value)
print(f"Sum = {sum(list_value)}")
#Task-2
tuple_value=("chattogram","Dhaka","Sylhet","Rangpur","Comilla")
print(tuple_value[2])
Converted_list= list(tuple_value)
Converted_list.append("Paris")
converted_tuple=tuple(Converted_list)
print(converted_tuple)
#Task-3
marks_dictionary={
    "Bangla": 87,
    "English":97,
    "Math": 95
}
print(marks_dictionary)
marks_dictionary["ICT"]=83
marks_dictionary["Bangla"]=93
print(marks_dictionary)
avg_marks= sum(marks_dictionary.values())/ len(marks_dictionary)
print(f"Average Marks = {avg_marks: .2f}")
