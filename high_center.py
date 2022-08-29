num = 12355
string = "ewf@$%^#$dsgbdfh"

num = str(num)
num_list = []
result = []

for i in num:
    num_list.append(i)    

center = len(num_list)//2 

max = max(num_list)

num_list.remove(max)

num_list.insert(center, max)

res = "".join(num_list)

if len(res) <= len(string):
    for j in range(len(res)):
        result.append(res[j] + string[j])
    print("".join(result) + string[len(res):])
else:
    for k in range(len(string)):
        result.append(res[k] + string[k])
    print("".join(result) + res[len(string):])