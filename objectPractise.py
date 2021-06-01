class User():

    active_users = 0

    @classmethod
    def display_active_users(cls): # class method
        return f'There are currently {cls.active_users} active users.'

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(',')
        return cls(first, last, int(age))
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f'{self.first}'

    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out'

    def full_name(self):
        return f'{self.first} {self.last}'

    def initials(self):
        return f'{self.first[0]}.{self.last[0]}.'

    def likes(self, thing):
        return f'{self.first} likes {thing}'

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th birthday, {self.first}!'

    

        

#user1 = User('Lynsay', 'Goodman', 39)
#user2 = User('Bear', 'Goodman', 2)
##print(user1.first, user1.last, user1.age)
##print(user2.first, user2.last, user2.age)
##print(user1.full_name())
##print(user2.full_name())
##print(user1.initials())
##print(user2.initials())
##print(user2.likes('chicken!'))
##print(user1.likes(user2.first))
##print(user1.is_senior())
##print(user2.birthday())
##print(user2.age)
# _something = private attribute that should stay within class
# __something = name mangle: so the attribute can be different for child classes

#print(User.active_users)
#print(user2.logout())
#print(User.active_users)
#print(User.display_active_users())

bear = User.from_string('Bear,Goodman,2')
print(bear.birthday())
print(bear)
