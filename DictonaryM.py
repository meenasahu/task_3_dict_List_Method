#keys()

student={
    
    'name':'meena',
    'age':20,
    'grade':'A'
}

keys=student.keys()
print(keys)

print('=====================================')

#values

book={
    
    'title':1984,
    'author':'george',
    'year':'1949'
}

values=book.values()
print(values)

print('=====================================')

#items

car={
    
    'brand':'toyota',
    'model':'corolla',
    'year':2020
}

items= car.items()
print(items)
print('=====================================')

#get()

person={
    
    'name':'meena',
    'age':30
}

age=person.get('age')
print(age)

print('=====================================')

#update()

user={
    
    'username':'jonny',
    'email':'12 3@gmail.com'
    }
new_info={
        'email':'456@gmail.com',
        'phone':1234
    }



user.update(new_info)
print(user)


print('=====================================')

#pop()

inventory={
    
    'apple':10,
    'banana':5,
    'orange':7
    
}

banana_count=inventory.pop('banana')
print(banana_count)

print('=====================================')
print(inventory)

print('=====================================')

# popitem
pop={
    'stu':'Ram',
    'add':'add1',
    'sub':'math'
}
pop.popitem()
print(pop)
print('=====================================')

# setdefault
dfr={
     "fruit":'apple',
    'color':'red',
    'price':34
}
x=dfr.setdefault('price',100)
print(x)