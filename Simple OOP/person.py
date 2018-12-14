class Person(object):
	def __init__(self,name):
		self.name = name
		self.parent = None
		self.child = []

	def is_child_of(self,name):
		if self.parent is not None : 
			return self.parent.name == name
		return False

	def is_parent_of(self,name):
		if len(self.child) != 0 : 
			for c in self.child:
				if c.name == name : return True
			return False
		else: return False

	def set_my_child(self, child):
		self.child.append(child)

	def set_my_parent(self, parent):
		self.parent = parent

	def get_my_parent_name(self):
		return self.parent.name

	def get_my_child_name(self):
		childsName = [c.name for c in self.child]
		return ','.join(childsName)
