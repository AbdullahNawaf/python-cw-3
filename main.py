favorite_animals = ['dog', 'cat', 'monkey','rabbit']
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove('monkey') 
favorite_animals.append('lion')     
for animal in favorite_animals:
    print(f'i love {animal}')       
numbers = [5,4,3,2,1]
number_sum = 0
for number in numbers:
    number_sum += number
print(number_sum)