import re
txt = " 1245"
if re.match("^[KL]|[TN]{0,2}", txt):
	print("valid")
