with open(“excerpt.txt”) as fh1, open(“out.txt”) as fh2:
	
	for line1, line2 in zip(fh1, fh2):
    	# line1 from abc.txt, line2 from test.txtg
    	print(line1+line2)