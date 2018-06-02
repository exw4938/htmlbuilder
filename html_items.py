import abc


class Item(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def write_item(self):
		"""
		Returns the html neccessary to properly display the item
		"""
		return


class Header(Item):
	def __init__(self, text, size):
		"""
		Makes a header with the given size and text. Automatically checks 
		that the header size is 1-6.
		"""
		if (not type(size) is int) or size > 6 or size < 1:
			raise ValueError("Header size must be 1-6")

		self.text = text
		self.size = size

	def get_tags(self):
		"""
		Returns a tuple where the first item is the opening tag and
		the second item is the closing tag
		"""
		return ("<h{}>".format(self.size), "</h{}>".format(self.size))

	def write_item(self):
		"""
		Returns the html neccessary to properly display the item
		"""
		tags = self.get_tags()
		#NOTE: possibly need to strip text of \n here?
		return tags[0] + self.text + tags[1] + "\n"
