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
		return self.tags.format(self.text) + "\n"


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
