@ECHO Off
cd ../../app
REM The original call
REM python -m SimpleHTTPServer 8080
REM 
REM Accepting POST with this solution, see http://georgik.sinusgear.com/2011/01/07/how-to-dump-post-request-with-python/
python ../tools/local_server/SimpleServer.py
PAUSE