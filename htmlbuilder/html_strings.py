import abc

class Tag:
	def __init__(self, tag, closing=True):
		self.tag = tag
		self.closing = closing

	def format_params(self, params):
		"""
		Returns a string to be inserted into the html tag where the
		html perameters would go
		"""
		output = ""
		for i in params:
			ouput += str(i) + "=" + str(params[i]) + " "
		return output.rstrip()

	def __call__(self, func):
		def wrapper(*args, **kwargs):
			tag_text = func(*args, **kwargs)[0]
			param_text = func(*args, **kwargs)[1]
			if self.closing:
				return "<{} {{}}>{}</{}>".format(self.tag, tag_text, self.tag).format(param_text)
			else:
				return "<{} {{}}/>".format(self.tag).format(param_text)
		return wrapper

@Tag('p')
def paragraph(text, params={}):
	return (text, params)

@Tag('i')
def italic(text, params={}):
	return (text, params)

@Tag('u')
def underline(text, params={}):
	return (text, params)

@Tag('strong')
def strong(text, params={}):
	return (text, params)

@Tag('title')
def title(text, params={}):
	return (text, params)

def header(text, size, params={}):
	if not (type(size) == int and (size > 0 and size < 7)):
		raise ValueError("Header size must be in range 1-6")
	@Tag('h' + str(size))
	def wheader(text, params):
		return (text, params)
	return wheader(text, params)

def table(table_data):
	"""
	Takes in a 2D array as the table, where the first row is used as
	the headings. Then returns a string representation of the table in html
	"""
	t = Table(table_data)
	return str(t)

class Table:
	""" Class representing a table in html """
	DATA_FORMAT = "\t<td>{}</td>\n"
	HEADING_FORMAT = "\t<th>{}</th>\n"
	def __init__(self, table):
		"""Construct a table using the given 2D array. The first row is taken as the headings"""
		self.headings = table[0]
		self.rows = table[1:]

	def __str__(self):
		"""Returns the html neccessary to properly display the item"""
		table_data = "<tr>\n"
		for heading in self.headings:
			table_data += self.HEADING_FORMAT.format(heading)
		table_data += "</tr>\n"
		for row in self.rows:
			table_data += "<tr>\n"
			for item in row:
				table_data += self.DATA_FORMAT.format(item)
			table_data += "</tr>\n"
		return "<table>\n{}</table>\n".format(table_data)
