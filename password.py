import random
lower_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "0123456789"
symbols = "!@#$%&*()|><?/"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = 20

password = "".join(random.sample(Use_for, length_for_pass))
print(password)
