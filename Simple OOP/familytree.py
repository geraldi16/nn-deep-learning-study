class FamilyTree(object):
	def __init__(self,members):
		self.members = members

	def get_member(self,name):
		for member in self.members:
			if member.name == name : return member
		return None

	def add_member(self,person):
		 self.member.append(person)

	def parent(self,x,y):
		px = self.get_member(x)
		py = self.get_member(y)
		px.set_my_child(py)
		py.set_my_parent(px)

	@staticmethod
	def get_hierarcial_text(x):
		text ={
			-1: 'uncle/aunty',
			0: 'cousin',
			1: 'nephew/niece',
			2: 'grandchild',
			-2: 'grandparent'
		}
		
		return text.get(x,'mmm...')


	def relative(self,x,y):
		px = self.get_member(x)
		py = self.get_member(y)
		valx = 0
		valy = 0
		
		# cek sibling
		if self.is_same_parent(px,py):
			return 'sibling'
		if px.is_child_of(py.name):
			return 'child'
		if px.is_parent_of(py.name):
			return 'parent'

		while True:
			if self.is_same_person(px,py):
				break
			if px.parent != None:
				px = px.parent
				valx -= 1
				if self.is_same_person(px,py):
					break
			if py.parent != None:
				py = py.parent
				valy -= 1
				if self.is_same_person(px,py):
					break
		return self.get_hierarcial_text(valy-valx)

	@staticmethod
	def is_same_person(x,y):
		return x.name == y.name

	@staticmethod
	def is_same_parent(x,y):
		return x.parent == y.parent
