def say_hello(name):
    print("Hello,",  name)

def say_goodbye(name):
    print("Goodbye, ", name)

#say_hello("random")
#say_goodbye("random")

#Area of a Circle
def area_circle(radius):
    print(3.14*(radius)**2)

#area_circle(5)

#4 RETURN FUNCTIONS
def subtract(a , b):
    return b - a

def multiply(a, b):
    return b*a

def divide(a, b):
    return b//a

#5 CONDITIONALS
#5.1

def what_to_wear(temperature):
    lowest =min(temperature)
    maximum = max(temperature)
    
    return(lowest, maximum)
reading = [15, 14, 17, 20, 23, 28, 20]
result =what_to_wear(reading)
#print(result)

#5.2
def is_weekend(day):
    if day ==0 or day ==7:
        return True
    else:
        return False
    
#5.3
def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used 

#5.4
def encrypt_number(num):
    last_digit = num % 10
    rest=num //10
    encrypted = int(str(last_digit)+str(rest))
    return encrypted


#6 LOOPS
#6.1
def power(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result

#print(power(2,3))
#print(power(5,0))

#6.2
def find_min_for(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


# print(find_min_for([4,7, 1, 9, 3]))


def find_max_for(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# print(find_max_for([4, 7, 1, 9, 3]))


def find_min_while(numbers):
    i = 0
    minimum = numbers[0]
    while i < len(numbers):
        if numbers[i] < minimum:
            minimum = numbers[i]
        i += 1
    return minimum
#print(find_min_while([4, 7, 1, 9, 3]))


def find_max_while(numbers):
    i = 0
    maximum = numbers[0]
    while i < len(numbers):
        if numbers[i] > maximum:
            maximum = numbers[i]
        i += 1
    return maximum

#print(find_max_while([4, 7, 1, 9, 3]))

#6.3
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10 
        total += digit
        num //= 10        
    return total

##FAVORITE PROBLEM IE. 7.1
def encrypt_number(num):
    last_digit = num % 10
    rest=num //10
    encrypted = int(str(last_digit)+str(rest))
    return encrypted

print("the result of the encrypted number is ", encrypt_number(12345))