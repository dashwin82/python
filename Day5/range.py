target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum_even = 0
for even_num in range(0, target+1, 2): # target in range is exclusive
    sum_even += even_num

print(sum_even)
