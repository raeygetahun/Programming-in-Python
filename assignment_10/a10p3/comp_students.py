from student import Student

s1 = Student("one", 3)
s2 = Student("two", 3)
s3 = Student("three", 3)
s4 = Student("two", 3)

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")
print(f"s4: {s4}")

print(f"s1 == s2: {s1 == s2}")
print(f"s2 == s4: {s2 == s4}")
print(f"s1 < s3: {s1 < s3}")
print(f"s3 <= s2: {s3 <= s2}")
print(f"s3 > s1: {s3 > s1}")
print(f"s4 >= s2: {s4 >= s2}")
print(f"s2 != s4: {s2 != s4}")