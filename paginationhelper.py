import math

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self._c = collection
      self._i = items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self._c)
      
  
  # returns the number of pages
  def page_count(self):
      self._page_count = math.ceil(len(self._c)/self._i)
      return self._page_count
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self, page_index):
      if(page_index < self._page_count -1):
          return self._i
      elif(page_index == self._page_count -1):
          return len(self._c)%self._i
      elif(page_index > self._page_count -1):
          return -1
      

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self, item_index):
      if(item_index > len(self._c)-1 or item_index < 0):
          return -1
      elif(item_index <= len(self._c)-1):
          return math.floor(item_index/self._i)
      