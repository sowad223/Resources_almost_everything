two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
print(two_digit_number[0],"+" ,two_digit_number[1],"=" ,
int(two_digit_number[0])+int(two_digit_number[1]))
print(int(two_digit_number[0])+int(two_digit_number[1]))


weight=int(input("Enter Your weight: "))
height=(int(input("Enter Your height: ")))
a=weight/((height/100)**2)

print(f"BMI {a:.2f}")
