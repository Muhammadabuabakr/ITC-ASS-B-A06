## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR uniqueEntries GOES HERE ####
def uniqueEntries(v):
	"""it takes a list and seperate unique enteries from it and 
	the enteries which is repeating means duplicate enteries"""
			
		unique_entry = []
		dupicate_enteries = []
		for i in v:
			if i in unique_entry:
				dupicate_enteries.append(i)
			else:
				unique_entry.append(i)
		return unique_entry,dupicate_enteries

#### End OF MARKER ----uniqueEntries



if __name__ == '__main__':
    uniqueEntries([12,24,35,24,88,120,155,88,120,155])
