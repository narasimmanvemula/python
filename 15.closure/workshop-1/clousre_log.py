
import logging 
logging.basicConfig(filename='example.log', level=logging.INFO) 


def logger(func): 
	def log_func(*args): 
		counter =100
		logging.info( 
			'Running "{}" with arguments {}: {}'.format(func.__name__, args, counter)) 
		counter = counter + 1
		print(func(*args)) 
	# Necessary for closure to work (returning WITHOUT parenthesis) 
	return log_func			 

def add(x, y): 
	return x+y 

def sub(x, y): 
	return x-y 

add_logger = logger(add) 
sub_logger = logger(sub) 

add_logger(3, 3) 
add_logger(4, 5) 

sub_logger(10, 5) 
sub_logger(20, 10) 
