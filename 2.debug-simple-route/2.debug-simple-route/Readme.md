# How to run the application: 

```
env FLASK_APP=./src/simple-api.py flask run    
```

# How to run API Tests:

```
pytest --log-format="%(asctime)s %(levelname)s %(message)s" \
	   --log-date-format="%Y-%m-%d %H:%M:%S" \
	   --html=test-report.html
```

# How to debug
```

```
# View debug information 

### Caution: Donot enable debug mode in production server

```
Open: 

http://localhost:5000/_debug 

- shows some information about the application, such as a list of registered views, url maps or configuration values.

```
