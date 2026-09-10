def hello(name):
    print("hello",name)

# Static list
static_list = [3,4,6,5] 
length = 0 
for x in static_list:
    length = length+1

print(f"the length of the list is",length)

# INPUT

list1 = [int(x) for x in input("Enter comma separated values: ").split(",")]
value = int(input("Enter the value you want to search: "))

# VARIABLES

leng = 0
for x in list1:
    leng += 1

sum_list = 0
max_val = min_val = list1[0]
second_max = second_min = None

even_numbers = []
odd_numbers = []
count_even = count_odd = 0
sum_e = sum_o = 0

prime_numbers = []
non_prime_numbers = []
prime_or_not = []
count_prime = count_non_prime = 0
sum_prime = sum_non_prime = 0

palindrome = []
not_palindrome = []
palindrome_or_not = []
count_palindrome = count_not_palindrome = 0
sum_palindrome = sum_not_palindrome = 0

armstrong = []
not_armstrong = []
arm_or_not = []
count_arm = count_non_arm = 0
sum_arm = sum_non_arm = 0

fact_list = []
sum_fact = 0

found = 0
target_freq = 0


# find length
for i in range(0, leng):

    x = list1[i]
    sum_list += x

    # Highest, second highest, lowest, second lowest

    if x > max_val:
        second_max = max_val
        max_val = x

    elif x != max_val and (second_max is None or x > second_max):
        second_max = x

    if x < min_val:
        second_min = min_val
        min_val = x

    elif x != min_val and (second_min is None or x < second_min):
        second_min = x


    # even-odd

    if x % 2 == 0:
        even_numbers.append(x)
        count_even += 1
        sum_e += x
    else:
        odd_numbers.append(x)
        count_odd += 1
        sum_o += x


    # prime , Not prime

    is_prime = 1

    if x <= 1:
        is_prime = 0
    else:
        j = 2
        while j <= x // 2:
            if x % j == 0:
                is_prime = 0
                break
            j += 1

    if is_prime:
        prime_numbers.append(x)
        prime_or_not.append(1)
        count_prime += 1
        sum_prime += x
    else:
        non_prime_numbers.append(x)
        prime_or_not.append(0)
        count_non_prime += 1
        sum_non_prime += x


    # Palindrome

    temp = x
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if x == reverse:
        palindrome.append(x)
        palindrome_or_not.append(1)
        count_palindrome += 1
        sum_palindrome += x
    else:
        not_palindrome.append(x)
        palindrome_or_not.append(0)
        count_not_palindrome += 1
        sum_not_palindrome += x


    # Armstrong

    temp = x
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit * digit * digit
        temp //= 10

    if digit_sum == x:
        armstrong.append(x)
        arm_or_not.append(1)
        count_arm += 1
        sum_arm += x
    else:
        not_armstrong.append(x)
        arm_or_not.append(0)
        count_non_arm += 1
        sum_non_arm += x


    # Factorial

    fact = 1
    temp = x

    while temp > 0:
        fact *= temp
        temp -= 1

    fact_list.append(fact)
    sum_fact += fact


    # Search

    if x == value:
        found = 1
        target_freq += 1


# ASCENDING

ascending = []
for x in list1:
    ascending.append(x)

for i in range(leng - 1):
    for j in range(i + 1, leng):
        if ascending[i] > ascending[j]:
            temp = ascending[i]
            ascending[i] = ascending[j]
            ascending[j] = temp


# DESCENDING

descending = []
for x in list1:
    descending.append(x)

for i in range(leng - 1):
    for j in range(i + 1, leng):
        if descending[i] < descending[j]:
            temp = descending[i]
            descending[i] = descending[j]
            descending[j] = temp


# OUTPUT

print("\n your list:", list1)
print("Length:", leng)

if found:
    print(f"\nYes, {value} is found")
    print("Frequency:", target_freq)
else:
    print(f"\nNo, {value} is not present")


print("\nSum of all elements:", end=" ")
for i in range(leng - 1):
    print(list1[i], end=" + ")
print(list1[leng - 1], "=", sum_list)


print("\nHighest value:", max_val)
print("Second highest:", second_max)
print("Lowest value:", min_val)
print("Second lowest:", second_min)


print("\nNumber of even elements:", count_even)
print("Sum of even:", end=" ")
for i in range(count_even - 1):
    print(even_numbers[i], end=" + ")
if count_even:
    print(even_numbers[count_even - 1], "=", sum_e)
else:
    print(0)


print("\nNumber of odd elements:", count_odd)
print("Sum of odd:", end=" ")
for i in range(count_odd - 1):
    print(odd_numbers[i], end=" + ")
if count_odd:
    print(odd_numbers[count_odd - 1], "=", sum_o)
else:
    print(0)


print("\nNumber of prime elements:", count_prime)
print("Sum of prime:", end=" ")
for i in range(count_prime - 1):
    print(prime_numbers[i], end=" + ")
if count_prime:
    print(prime_numbers[count_prime - 1], "=", sum_prime)
else:
    print(0)


print("\nNumber of not prime elements:", count_non_prime)
print("Sum of not prime:", end=" ")
for i in range(count_non_prime - 1):
    print(non_prime_numbers[i], end=" + ")
if count_non_prime:
    print(non_prime_numbers[count_non_prime - 1], "=", sum_non_prime)
else:
    print(0)


print("\nNumber of palindrome elements:", count_palindrome)
print("Sum of palindrome:", end=" ")
for i in range(count_palindrome - 1):
    print(palindrome[i], end=" + ")
if count_palindrome:
    print(palindrome[count_palindrome - 1], "=", sum_palindrome)
else:
    print(0)


print("\nNumber of not palindrome elements:", count_not_palindrome)
print("Sum of not palindrome:", end=" ")
for i in range(count_not_palindrome - 1):
    print(not_palindrome[i], end=" + ")
if count_not_palindrome:
    print(not_palindrome[count_not_palindrome - 1], "=", sum_not_palindrome)
else:
    print(0)


print("\nNumber of Armstrong elements:", count_arm)
print("Sum of Armstrong:", end=" ")
for i in range(count_arm - 1):
    print(armstrong[i], end=" + ")
if count_arm:
    print(armstrong[count_arm - 1], "=", sum_arm)
else:
    print(0)


print("\nNumber of not Armstrong elements:", count_non_arm)
print("Sum of not Armstrong:", end=" ")
for i in range(count_non_arm - 1):
    print(not_armstrong[i], end=" + ")
if count_non_arm:
    print(not_armstrong[count_non_arm - 1], "=", sum_non_arm)
else:
    print(0)


print("\nSum of factorial:", end=" ")
for i in range(leng - 1):
    print(fact_list[i], end=" + ")
print(fact_list[leng - 1], "=", sum_fact)


print("\nAscending values:", ascending)
print("Sum of ascending values:", end=" ")
for i in range(leng - 1):
    print(ascending[i], end=" + ")
print(ascending[leng - 1], "=", sum_list)


print("\nDescending values:", descending)
print("Sum of descending values:", end=" ")
for i in range(leng - 1):
    print(descending[i], end=" + ")
print(descending[leng - 1], "=", sum_list)