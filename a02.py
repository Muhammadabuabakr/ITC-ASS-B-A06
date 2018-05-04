## IMPORTS GO HERE if required

## END OF IMPORTS 
def netIncome(current_salary, income_tax_ratio = 2):
	""" function about  netIncome , takes current salary and income_tax_ratio(default value)
		return net_salary according to formula (current_salary) - (current_salary * income
		_tax_ratio in percentage) """
	
	net_salary = (current_salary) - (current_salary * income_tax_ratio/100.0)
	
	return net_salary


#### YOUR CODE FOR netIncome GOES HERE ####


#### End OF MARKER


