#importing module 
import logging 
  
# Create and configure logger 
# /var/log/applicationName/logger.log
# Stream to AWS Cloudwatch using aws cloudwatch agent
logging.basicConfig(filename="./log/sfs.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
  
#Test messages 
logger.debug("Harmless debug Message") 
logger.info("Just an information") 
logger.warning("Its a Warning") 
logger.error("Did you try to divide by zero") 
logger.critical("Internet is down") 