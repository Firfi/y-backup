import os
import sys

from paste.deploy import loadapp
from waitress import serve

env = sys.argv[1] if len(sys.argv) > 1 else 'production'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = loadapp('config:{env}.ini'.format(env=env), relative_to='.')

    IP = "0.0.0.0"
    #IP = "192.168.178.35"
    serve(app, host=IP, port=port)
