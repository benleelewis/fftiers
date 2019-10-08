import os 

def set_path():
	user = os.popen('whoami').read()[:-1]
	if user == 'benle':
		mypath = '/Users/benle/projects/fftiers'
	elif user == 'borischen':
		mypath = '/Users/borischen/projects/fftiers'
	else:	
		mypath = 'C:/users/benle/projects/fftiers'
	return mypath

head_path = set_path()

cmd1 = 'Rscript %s/src/main.R t' % head_path
os.system(cmd1)

#cmd2 = 'python %s/src/push-to-s3.py' % head_path
#os.system(cmd2)

