# Start the server using a command line #

```
#!shell
cd yarnee
python -m SimpleHTTPServer 8080
```
Open http://localhost:8080

For more details and Windows Batch script check: /src/master/misc/tools/local_server/

# Start the server using Python #

```
#!shell
source bin/activate
python runapp.py
```

# Start the server using Python with offline Database #

```
#!shell
source bin/activate
python runofflineapp.py
```

This is based on SQLite, so you may have to run this command to initialize the database:

```
#!shell
bin/initialize_yarnee.pyramid_db offlinedevelopment.ini 
```
------------
## Executing a POST request manually ##

```
#!shell
import urllib2
import json
json_payload = json.dumps({'a':1})
headers = {'Content-Type':'application/json; charset=utf-8'}
req = urllib2.Request('http://192.168.178.35:5000/yarnee/123', json_payload, headers)
resp = urllib2.urlopen(req)
```

## Run functional tests ##

```
#!shell
source bin/activate
python ftests.py
```

## Install App ##

```
#!shell
python setup.py develop
```

## List installed packages and versions ##

```
#!shell
heroku run pip list
```

## Deploy as App to Heroku ##

```
#!shell
heroku create
git push heroku master
```

## Real time logs from Heroku ##

```
#!shell
heroku logs --tail
```

or App out only:

```
#!shell
heroku logs --ps=web.1 --tail
heroku logs --ps=web.1 --tail --app y-api-1
```

## Authenticate with Heroku
```
#!shell
heroku auth:login
```

## Reconnect Heroku
When 
```
#!shell
git remote -v
```
lists only the Bitbucket repository, then the Heroku repository was disconnected. Connect it again via
```
#!shell
git remote add heroku git@heroku.com:y-api-1.git
```

## Resolving problems with dependencies

For example when problems like this ```requests 2.0.0 conflicts with requirement``` show up in the log.
```
#!shell
heroku plugins:install https://github.com/lstoll/heroku-repo.git
heroku repo:purge_cache -a y-api-1
heroku repo:rebuild -a y-api-1

```

## Deploy on Beanstalk

Create an instance if there is no one - eb create
On first instance create ans on any dependencies change use
```
#!shell
cd /opt/python/current/app
sudo su
source /opt/python/run/baselinenv/bin/activate
easy_install -U distribute
python setup.py develop

```
To deploy code changes - eb push


