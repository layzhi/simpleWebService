# simpleWebService

This is a simple web service where the user will enter a line number that the user wish returned from a text

base url: http://localhost:5000

how to does the system work?

1.) Download Python 3<br />
2.) git clone https://github.com/layzhi/simpleWebService.git<br />
3.) run pip install -r requirements.txt<br />
4.) /run.sh<br />
5.) open a web browser and enter http://localhost:5000<br />
6.) http://localhost:5000/GET/ then enter line number<br />
7.) ex.) http://localhost:5000/GET/5 will return the fifth line of the text

References - Stackoverflow.com, http://flask.pocoo.org/

The system is built with python 3 and flask. I chose to use flask because of the simplicity and light weight features it offers. It also make routing very simple. I spent ~ 6 hours on this assignment. Currently the system dont handle large text files too well.

Priority Backlog -

1.) Large file scalability (implement something like https://github.com/six8/pytailer)
2.) Large amount of users (queue up requests)
3.) Availability - (if one service fails, will there be another one to handle requests?)

Final note - There are alway room for improvements