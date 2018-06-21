"""
	file: htmlbuilder.py
	language: python 3.6
	description: 

"""
from html_items import *
from webbrowser import open_new_tab



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

	def add_item(self, item, item_list):
		"""
			Adds the given item to the list of items in the html document
			item: a string representing the item
		"""
		item_list += [item]

	def add_to_body(self, item):
		""" Adds the given item to the body """
		self.add_item(item, self.body_items)

	def add_to_head(self, item):
		""" Adds the given item to the head """
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
				file_.write(i + "\n")
			file_.write(self.END_HEAD)

		if len(self.body_items) > 0:
			file_.write(self.START_BODY)
			for i in self.body_items:
				file_.write(i + "\n")
			file_.write(self.END_BODY)
		
		file_.write(self.END_TAG)
		file_.close()
		open_new_tab(doc_name)

if __name__ == '__main__':
	"""
	Testing for base usage
	"""
	writer = HTMLWriter()
	header = header("This is a header", 1)
	table = Table(["test1", "test2"])
	table.add_row(["a", "b"])
	table.add_row(["c", "d"])
	doc_title = title("Hello there")
	p = paragraph("This is a test paragraph", {'href':'https://www.google.com'})
	print(underline("test"))
	print(underline(paragraph("test")))
	writer.add_to_body(underline(paragraph("test")))
	writer.add_to_body(p)
	writer.add_to_head(title)
	writer.add_to_body(table)

	writer.write_doc()
	
