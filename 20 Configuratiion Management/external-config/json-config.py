# main_with_json.py
import json

with open('config.json', 'r') as f:
    config = json.load(f)

secret_key = config['DEFAULT']['SECRET_KEY'] # 'secret-key-of-myapp'
ci_hook_url = config['CI']['HOOK_URL'] # 'web-hooking-url-from-ci-service'

print(secret_key)
print(ci_hook_url)