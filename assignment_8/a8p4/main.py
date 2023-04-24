import mod_conversion

start=int(input())
end=int(input())
step=int(input())

input=input()

lst=mod_conversion.in2cm_table(start,end,step)

if input == 's':
    print(lst)
else:
    with open("in2cm.html", "w") as f:
        f.write(lst)