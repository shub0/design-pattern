#! /usr/bin/python

ingredients = "spam eggs apple"
line = '-' * 10

# Skeletons
def iter_elements(getter, action):
	"""Template skeletons that iterates items"""
	for element in getter():
		action(element)
		print(line)

def rev_elements(getter, action):
	"""Template skeletons that iterates items in reverse order"""
	for element in getter()[::-1]:
		action(element)
		print(line)

# Getters
def get_list():
	return ingredients.split()

def get_lists():
	return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
	print(item)

def reverse_item(item):
	print(item[::-1])


# Makes templates
def make_template(skeleton, getter, action):
	"""Instantiate a template method with getter and action"""
	def template():
		skeleton(getter, action)
	return template

def main():
    # Create our template functions
    templates = [make_template(s, g, a)
                            for g in (get_list, get_lists)
                            for a in (print_item, reverse_item)
                            for s in (iter_elements, rev_elements)]

    for template in templates:
            template()

if __name__ == "__main__":
    main()
