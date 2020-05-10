#Write your lambda function here
contains_a = lambda word: 'a' in word
print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")

#Write your lambda function here
long_string = lambda str: len(str) > 12
print long_string("short")
print long_string("photosynthesis")

#Write your lambda function here
ends_in_a = lambda str: str[-1]=='a'
print ends_in_a("data")
print ends_in_a("aardvark")

#Write your lambda function here
double_or_zero = lambda num: num*2 if num > 10 else 0
print double_or_zero(15)
print double_or_zero(5)

#Write your lambda function here
even_or_odd = lambda num: 'even' if num%2==0 else 'odd'
print even_or_odd(10)
print even_or_odd(5)

#Write your lambda function here
multiple_of_three = lambda num: 'multiple of three' if num%3==0 else 'not a multiple'
print multiple_of_three(9)
print multiple_of_three(10)

#Write your lambda function here
rate_movie = lambda rating: 'I liked this movie' if rating>8.5 else 'This movie was not very good' 
print rate_movie(9.2)
print rate_movie(7.2)

#Write your lambda function here
ones_place = lambda num:num%10
print ones_place(123)
print ones_place(4)

#Write your lambda function here
double_square = lambda num: num**2*2
print double_square(5)
print double_square(3)

import random
#Write your lambda function here
add_random = lambda num: num+random.randint(1,10)
print add_random(5)
print add_random(100)
