from person import Person
from familytree import FamilyTree

p1 = Person('Andi')
p2 = Person('Budi')
p3 = Person('Charlie')
p4 = Person('Cimplung')

p2.set_my_child(p3)
p2.set_my_child(p4)
p2.set_my_parent(p1)
# print(p2.get_my_parent_name())
print('%s adalah ayah dari %s' %(p2.get_my_parent_name(), p2.name))
print('%s adalah anak dari %s' %(p2.get_my_child_name(), p2.name))
# print(p1.name)
# print(p2.is_child_of('Andi'))
# print(p1.is_child_of('Andi'))
# print(p3.is_child_of('Andi'))
# print(p2.is_parent_of('Charlie'))
# print(p2.is_parent_of('Dedi'))

# Family Tree
print('----------------------------')
print('---- family tree ----')
andi = Person('andi')
budi = Person('budi')
badu = Person('badu')
charlie = Person('charlie')
cimplung = Person('cimplung')
coklat = Person('coklat')
charles = Person('charles')

ft = FamilyTree([andi,budi,badu,charlie,cimplung,coklat,charles])
# print(ft.members[1].name)

ft.parent('andi','budi')
ft.parent('andi','badu')
ft.parent('badu','coklat')
ft.parent('badu','cimplung')
ft.parent('budi','charlie')
ft.parent('budi','charles')
print(ft.members[0].child[0].name)
print(ft.members[1].parent.name)

x = ft.members[2].name
y = ft.members[4].name
print("%s is %s's %s" %(x,y,ft.relative(x,y)))