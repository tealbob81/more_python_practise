#def square(num): return(num**2)

##sq2 = lambda num: num**2
##
##add = lambda a,b: a + b
##
##print(add(3,10))
##print(sq2(8))
##

##nums = [2,3,4,5,6]
##
##doubles = list(map(lambda num: num*2, nums))
##print(doubles)
##
##people = ['bear', 'cat', 'lynsay', 'david']
##
##upper_peeps = list(map(lambda x: x.upper(), people))
##print(upper_peeps)

##names = [
##    {'first':'Rusty', 'last':'Steele'},
##    {'first': 'Colt', 'last': 'Steele'},
##    {'first': 'Blue', 'last': 'Steele'}
##]
##
##first_names = list(map(lambda x: x['first'], names))
##last_names = list(map(lambda y: y['last'], names))

##li = [1,2,3,4]
##
##evens = list(filter(lambda x: x % 2 == 0, li))
##print(evens)
##
##names = ['bear', 'cat', 'lynsay', 'barry', 'david', 'billy']
##b_names = list(filter(lambda n: n[0] == 'b', names))
##print(b_names)

##users = [
##    {'username': 'samuel', 'tweets': ['I love cake', 'I love icecream', 'I love jelly']},
##    {'username': 'katie', 'tweets': ['I love Bear!']},
##    {'username': 'jeff', 'tweets': []},
##    {'username': 'bob123', 'tweets': []},
##    {'username': 'doggo_luvr', 'tweets': ['cats are the best', 'I am hungry']},
##    {'username': 'guitar_gal', 'tweets': []}
##]

##inactive_users = list(filter(lambda u: not u['tweets'] , users))
##print(inactive_users)
##inactive = list(map(lambda user: user['username'].upper(),
##                filter(lambda u: not u['tweets'], users)))
##print(inactive)

##inactive2 = [user["username"].upper() for user in users if not user["tweets"]]
##
##print(inactive2)
##
##             
####names = ['Bear', 'The Cat', 'Lynsay']
##
##new_names = list(map(lambda name: f'Your instructor is {name}',
##                     filter(lambda value: len(value) < 5, names)))
##print(new_names)

##print(sorted(users,key=lambda user: user['username']))
##print(sorted(users,key=lambda user: len(user['tweets']), reverse=True))
songs = [
    {'title': 'happy birthday', 'playcount': 1},
    {'title': 'survive', 'playcount': 6},
    {'title': 'YMCA', 'playcount': 99},
    {'title': 'Toxic', 'playcount': 31}
]

print(min(songs, key=lambda s: s['playcount']))
print(max(songs, key=lambda s: s['playcount'])['title'])

