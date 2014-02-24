import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = loadapp('config:offlinedevelopment.ini', relative_to='.')

    IP = "0.0.0.0"
    #IP = "192.168.178.35"
    serve(app, host=IP, port=port)
