numbers={"1":"one","2":"two","3":"three","4":"four"}
#print(numbers[1])
phone=input("Enter ph no:")
output=""
for ch in phone:
    output+=numbers.get(ch,"!")
print(output)








'''numbers =[5,2,5,2,2]
for x_count in numbers:#x_count=[5,2,5,2,2]
    output=''
    for y_count in range(x_count):
        output+="*"
    print(output)'''
'''numbers = [1,9,3,4]
max=numbers[0]
for num in numbers:
    if num > max:
        max = num
        num+=num
print(max)'''







 # x(0)=5,x(1)=2,x(2)=5,x(3)=2
 # output=(x,y)==> (0,0 = * 0,1 = * 0,2 = * ... 0,4 = *
 # (1,0 =* 1, 1,1 = *
# (2,0 = * 2,1 = * .....2,4=*
# (3,0 = * 3,1 = *
# (4,0=* 4,1=*