import abc


class Item(object):
	""" Parent object for all html items """
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def write_item(self):
		"""Returns the html neccessary to properly display the item"""
		return

	@abc.abstractmethod
	def add_perameter(self, perameter_map):
		"""
		Adds the given perameter(s) to the html tag.
		-----
		parameter_map: a dictionary with the name of the perameter as the
		key and the value as the perameter value
		"""
		pass

# TODO: possibly parse the text to be put in the tag and insert </br> when a \n comes along
class Title(Item):
	def __init__(self, text, tag='title'):
		"""
		Create a new Title with the given text
		-----
		text: The text to put in the title
		tag: var for subclasses to insert their own tags in place of title
		"""
		self.text = text
		self.tags = "<{}{{}}>{{}}</{}>".format(tag, tag)
		self.perameters = {}

	def get_perameters(self):
		""" 
		Returns the perameters of the tag in string
		form for easy substitution
		"""
		if len(self.perameters) == 0:
			return ""
		output = " "
		for i in self.perameters:
			output += str(i) + "=" + str(self.perameters[i])
		return output + " "

	def write_item(self):
		"""Returns the html neccessary to properly display the item"""
		#NOTE: possibly need to strip text of \n here?
		if isinstance(self.text, Item):
			return self.tags.format(self.get_perameters(), self.text.write_item())
		return self.tags.format(self.get_perameters(), self.text)

	def add_perameter(self, perameter_map):
		"""
		Adds the given perameter(s) to the html tag.
		-----
		parameter_map: a dictionary with the name of the perameter as the
		key and the value as the perameter value
		"""
		self.perameters.update(perameter_map)


class Header(Title):
	""" Class for a header html item """
	def __init__(self, text, size):
		"""
		Makes a header with the given size and text. Automatically checks 
		that the header size is 1-6.
		-----
		text: The text to put in the header
		size: The size of the header
		"""
		if (not type(size) is int) or size > 6 or size < 1:
			raise ValueError("Header size must be 1-6")
		super().__init__(text, 'h' + str(size))


class Paragraph(Title):
	""" Class for a Paragraph html item """
	def __init__(self, text):
		super().__init__(text, 'p')

class Italic(Title):
	""" Class for italic html text """
	def __init__(self, text):
		""" Calls super constructor with specified format type """
		super().__init__(text, 'i')

class Underline(Title):
	""" Class for underlined html text """
	def __init__(self, text):
		""" Calls super constructor with specified format type """
		super(Underline, self).__init__(text, 'u')

class Table(Item):
	""" Class representing a table in html """
	DATA_FORMAT = "\t<td>{}</td>\n"
	HEADING_FORMAT = "\t<th>{}</th>\n"
	def __init__(self, headings):
		"""
		Construct a table with the given headings
		-----
		headings: An array with the table's headings
		"""
		self.headings = headings
		self.rows = []

	def add_row(self, row):
		"""Add a list of items as a row into the table"""
		if len(row) != len(self.headings):
			raise ValueError("Length of rows and number of headings must be equal")
		self.rows += [row]

	def write_item(self):
		"""Returns the html neccessary to properly display the item"""
		table_data = "<tr>\n"
		for heading in self.headings:
			if isinstance(heading, Item):
				table_data += self.HEADING_FORMAT.format(heading.write_item())
			else:
				table_data += self.HEADING_FORMAT.format(heading)
		table_data += "</tr>\n"
		for row in self.rows:
			table_data += "<tr>\n"
			for item in row:
				if isinstance(item, Item):
					table_data += self.DATA_FORMAT.format(item.write_item())
				else:
					table_data += self.DATA_FORMAT.format(item)
			table_data += "</tr>\n"
		return "<table>\n{}</table>\n".format(table_data)
