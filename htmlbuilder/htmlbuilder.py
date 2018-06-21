"""
	file: htmlbuilder.py
	language: python 3.6
	description: 

"""
from html_items import *
from webbrowser import open_new_tab

class Style:
	def __init__(self):
		self.tags = "<style>\n{}\n</style>\n"
		self.text = ""
		self.styles = {}

	def add_style(self, style_id, style_values):
		"""
		Add a new style or styles to a new or existing css style class
		-----
		style_id: the name of the css class to add new style to
		style_values: a dictionary representing the perameter value
		pairs to add to the css class
		"""
		style_list = [] # List to put processed style_values in
		for i in style_values:
			style_list += [str(i) + ":" + str(style_values[i])]

		if style_id in self.styles:
			self.styles[style_id] += style_list
		else:
			self.styles[style_id] = style_list

	def get_styles(self):
		"""
		Gets all the style information and puts it into html format
		then returns it as a string
		"""
		output = ""
		for i in self.styles:
			output += str(i) + "{\n"
			for j in self.styles[i]:
				output += "\t" + str(j) + ";\n"
			output += "}\n"
		return self.tags.format(output)


class HTMLWriter:
	""" Main class which actually does the document writing """
	START_TAG = "<!DOCTYPE html>\n<html>\n"
	END_TAG = "</html>"
	START_BODY = "<body>\n"
	END_BODY = "</body>\n"
	START_HEAD = "<head>\n"
	END_HEAD = "</head>\n"

	def __init__(self):
		"""
			Initializes the head and body item lists to be none
		"""
		self.head_items = []
		self.body_items = []
		self.style = None

	def add_item(self, item, item_list):
		"""
			Adds the given item to the list of items in the html document
			item: can be either an Item subclass object or a list of item objects
		"""
		if type(item) is list:
			for i in item:
				if not isinstance(i, Item):
					raise TypeError("Make sure 'item' is a subclass of 'Item'")
			item_list += item
		else:
			if not isinstance(item, Item):
				raise TypeError("Make sure 'item' is a subclass of 'Item'")
			item_list += [item]
			

	def add_to_body(self, item):
		""" Adds the given item to the body """
		self.add_item(item, self.body_items)

	def add_to_head(self, item):
		""" Adds the given item to the head """
		self.add_item(item, self.head_items)

	def create_style(self):
		""" Create a new Style for this HTMLWriter to use """
		self.style = Style()

	def get_style(self):
		""" Gets the style of this HTMLWriter object """
		return self.style

	def write_doc(self, doc_name="out.html"):
		"""
			Writes the current items to the file
		"""
		if doc_name[-5:] != '.html':
			doc_name += '.html'

		file_ = open(doc_name, 'w')

		file_.write(self.START_TAG)
		if len(self.head_items) > 0:
			file_.write(self.START_HEAD)
			for i in self.head_items:
				file_.write(i.write_item() + "\n")

			file_.write(self.style.get_styles())
			file_.write(self.END_HEAD)

		if len(self.body_items) > 0:
			file_.write(self.START_BODY)
			for i in self.body_items:
				file_.write(i.write_item() + "\n")
			file_.write(self.END_BODY)
		
		file_.write(self.END_TAG)
		file_.close()
		open_new_tab(doc_name)

if __name__ == '__main__':
	"""
	Testing for base usage
	"""
	writer = HTMLWriter()
	writer.create_style()
	style = writer.get_style()
	style.add_style('p', {'color':'red'})
	header = Header("Hello World!", 3)
	table = Table(["test1", "test2"])
	table.add_row(["a", "b"])
	table.add_row(["c", "d"])
	title = Title("Hello there")
	p = Paragraph("This is a test paragraph")
	p.add_perameter({'href':'https://www.google.com'})
	writer.add_to_body(Underline(Paragraph("test")))
	writer.add_to_body(p)
	writer.add_to_head(title)
	writer.add_to_body(table)

	writer.write_doc()

