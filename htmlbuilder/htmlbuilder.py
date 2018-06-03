"""
	file: htmlbuilder.py
	language: python 3.6
	description: 

"""
from html_items import *
from webbrowser import open_new_tab



class HTMLWriter:

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
		self.add_item(item, self.body_items)

	def add_to_head(self, item):
		self.add_item(item, self.head_items)

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
	header = Header("Hello World!", 3)
	table = Table(["test1", "test2"])
	table.add_row(["a", "b"])
	table.add_row(["c", "d"])
	title = Title("Hello there")
	writer.add_to_body(Underline(Paragraph("test")))
	writer.add_to_head(title)
	writer.add_to_body(table)

	writer.write_doc()
