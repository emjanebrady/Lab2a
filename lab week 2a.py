#Emma Brady

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
big_string = my_string.upper()
print(big_string)

#4
z = ['a', 'b', 'c', 'd']
z[3] = 'd'

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
color = 'blue'
color_string = 'My favorite color is %s, what is yours?' % color
print(color_string)

#7
new_color = 'yellow'
new_color_string = 'My favorite color is {}, what is yours?'.format(new_color)
print(new_color_string)

#8
final_color = 'red'
final_color_string = f'My favorite color is {final_color}, what is yours?'
print(final_color_string)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools_set = {'harris', 'booth', 'crown', 'harris', 'harris'}

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = ['bird', 'horse', 'dog', 'fish']
animals[2] = 'cat'

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
fixed_sent = my_sent.split()
print(fixed_sent)
