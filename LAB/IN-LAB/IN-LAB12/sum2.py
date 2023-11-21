class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.parents = []
        self.children = []

    def add_parent(self, parent):
        self.parents.append(parent)
        parent.children.append(self)

    def is_parent_of(self, child):
        return child in self.children

    def is_child_of(self, parent):
        return parent in self.parents

    def is_grandparent_of(self, grandchild):
        for child in self.children:
            if child.is_parent_of(grandchild):
                return True
        return False

    def is_grandchild_of(self, grandparent):
        for parent in self.parents:
            if parent.is_parent_of(grandparent):
                return True
        return False

    def is_sibling_of(self, sibling):
        if self.is_child_of(sibling) or sibling.is_child_of(self):
            return False
        for parent in self.parents:
            if sibling.is_child_of(parent):
                return True
        return False

    def is_cousin_of(self, cousin):
        if self.is_sibling_of(cousin):
            return False
        for parent in self.parents:
            if parent.is_sibling_of(cousin.parent):
                return True
        return False

    def is_uncle_of(self, niece_nephew):
        if self.gender != "male":
            return False
        for child in self.children:
            if child.is_sibling_of(niece_nephew):
                return True
        return False


# example usage:
jane = Person("Jane", "female")
john = Person("John", "male")
jim = Person("Jim", "male")
jane.add_parent(jim)
jane.add_parent(john)

susan = Person("Susan", "female")
susan.add_parent(jane)

print(jim.is_parent_of(jane))  # True
print(john.is_parent_of(jane))  # True
print(jim.is_grandparent_of(susan))  # True
print(jane.is_grandchild_of(jim))  # True
print(susan.is_sibling_of(jim))  # False
# print(susan.is_cousin_of(jim)) # False
# print(john.is_uncle_of(susan)) # True
