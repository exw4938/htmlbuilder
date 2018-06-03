import abc


class Item(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def write_item(self):
		"""
		Returns the html neccessary to properly display the item
		"""
		return

class Title(Item):
	def __init__(self, text):
		self.text = text
		self.tags = "<title>{}</title>"

	def write_item(self):
		#NOTE: possibly need to strip text of \n here?
		if isinstance(self.text, Item):
			return self.tags.format(self.text.write_item())
		return self.tags.format(self.text)


class Header(Title):
	def __init__(self, text, size):
		"""
		Makes a header with the given size and text. Automatically checks 
		that the header size is 1-6.
		"""
		if (not type(size) is int) or size > 6 or size < 1:
			raise ValueError("Header size must be 1-6")

		self.text = text
		self.tags = "<h{}>{}</h{}>".format(size,'{}', size)


class Paragraph(Title):
	def __init__(self, text):
		self.text = text
		self.tags = "<p>{}</p>"

class Formatted(Title):
	formatting = ["<i>{}</i>", "<u>{}</u>"]
	ITALICS = 0
	UNDERLINE = 1
	def __init__(self, text, form):
		self.text = text
		self.tags = self.formatting[form]


class Italic(Formatted):
	def __init__(self, text):
		super().__init__(text, self.ITALICS)

class Underline(Formatted):
	def __init__(self, text):
		super().__init__(text, self.UNDERLINE)

class Table(Item):
	DATA_FORMAT = "\t<td>{}</td>\n"
	HEADING_FORMAT = "\t<th>{}</th>\n"
	def __init__(self, headings):
		"""Construct a table with the given headings"""
		self.headings = headings
		self.rows = []

	def add_row(self, row):
		"""Add a list of items as a row into the table"""
		if len(row) != len(self.headings):
			raise ValueError("Length of rows and number of headings must be equal")
		self.rows += [row]

	def write_item(self):
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
