import toml

class Configuration:
	def __init__(self):
		data = toml.load('./config.toml')
		print(data)
		print(data.get('dbConfig').get('db_host'))
		print(data.get('dbConfig').get('db_port'))
		
		maxFilesCount = data.get('fileConfig').get('maxFilesCount')
		print("Values for file handling - max file count :: {}".format(maxFilesCount))

		weekends = data.get('weekends')
		print(weekends)

Configuration()
