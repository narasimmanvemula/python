from flask import Flask
import manhole

class Counter:
    i = 0
    def increment(self):
        self.i += 1

    def __str__(self):
        return str(self.i)

_counter = Counter()
app = Flask(__name__)

@app.route("/")
def index():
    _counter.increment()
    return str(_counter) + "\n"


if __name__ == '__main__':
    manhole.install(patch_fork=False, daemon_connection=True)
    app.run()


"""
Check for PID
ps -ef 

Tail PID file

Invoke "http://localhost:5000"

"""

