from random import choice

print('Enter the number of friends joining (including you):')
number_of_friends = int(input(''))

if number_of_friends < 1:
    print('No one is joining for the party')
else:
    friends = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(number_of_friends):
        friends[input('')] = 0

    print('Enter the total bill value:')
    final_bill = float(input())
    split_value = round(final_bill / number_of_friends, 2)

    for friend in friends.keys():
        friends[friend] = split_value
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if input().upper() == 'YES':
        lucky_one = choice(list(friends.keys()))
        print(f'{lucky_one} is the lucky one!')
        if number_of_friends > 1:
            new_split_value = round(split_value / (number_of_friends - 1), 2)
            for friend in friends.keys():
                if friend == lucky_one:
                    friends[friend] = 0
                else:
                    friends[friend] += new_split_value
    else:
        print('No one is going to be lucky')

    print(friends)
