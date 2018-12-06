"""
1.3
"""

def memory(n):
	def helper(fn):
		nonlocal n
		n = fn(n)
		print(n)
		return helper
	return helper
		

"""
2.2
"""

def add_this_many(x, el, lst):
	"""
	Adds el to the end of lst the number of times x occurs in lst.
	"""
	count = 0
	for element in lst:
		if element == x:
			count += 1
	while count > 0:
		lst.append(el)
		count -= 1
	
	
"""
2.3
"""

def reverse(lst):
	"""
	Reverses lst in place.
	"""
	if len(lst) > 1:
		item = lst.pop()
		reverse(lst)
		lst.insert(0, item)
		return lst
	'''
	for i in range(len(lst) // 2):
		lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
	'''
		
		
"""
3.2
"""

def group_by(s, fn):
	"""
	The values of the dictionary are lists of elements from s. Each element e in a list should constructed such that fn(e) is the same for all elements in that list. Finally, the key for each value should be fn(e).
	"""
	dic = {}
	for elem in s:
		if fn(elem) not in dic:
			dic[fn(elem)] = [elem]
		else:
			dic[fn(elem)].append(elem)
	return dic


"""
3.3
"""

def replace_all_deep(d, x, y):
	for key in d.keys():
		if type(d[key]) is dict:
			replace_all_deep(d[key], x, y)
		else:
			if d[key] == x:
				d[key] = y 
				
														
					






		
		
		
		