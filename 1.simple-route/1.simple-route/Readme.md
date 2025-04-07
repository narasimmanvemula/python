# How to run the application: 

```
pip3 install -r requirements.txt
pip3 install --upgrade Flask
```

```
env FLASK_APP=./src/simple-api.py flask run    
```

# How to run API Tests:

```
pytest --log-format="%(asctime)s %(levelname)s %(message)s" \
	   --log-date-format="%Y-%m-%d %H:%M:%S" \
	   --html=test-report.html
```
