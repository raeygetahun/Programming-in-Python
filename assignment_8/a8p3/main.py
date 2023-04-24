import mod_conversion

start=int(input())
end=int(input())
step=int(input())

lst=mod_conversion.in2cm_table(start,end,step)

print(lst)