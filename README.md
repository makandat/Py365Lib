# Py365Lib
This library and tools help you to create small Python3 application quickly.
And it is consisted of the modules below.

- Common
- FileSystem
- Text
- DateTime
- MySQL
- AWSS3 (AWS S3)
- WebPage (CGI)
- CursesApp (curses)
- TkApp (Tkinter)
- HTApp (HTTP server)
- SVG
- CSS3
- JQuery (under consruction)

### Common
	#!/usr/bin/env python3
	from Py365Lib import Common
	
	# Confirm to exist the command line parameters.
	if Common.count_args() == 0 :
	  Common.stop(9, "A parameter must be exists.")
	
	# Define the error code (0 means non-error).
	err = 0
	
	#  Get a parameter.
	fileName = Common.args(0)
	print(fileName)
	
	try :
	  # Display the content of the file.
	  Common.printFile(fileName) 
	except Exception as e :
	  # Exception
	  Common.esc_print(Common.ESC_FG_RED, e.args)
	  err = 1
	
	
	if err == 0 :
	  print("Normal termination.")
	else :
	  print("Error(s) has been detected. The error code: {0:d}".format(err))
	
	# Exit with termination code (err).
	exit(err)


### FileSystem
	#!/usr/bin/env python3
	from Py365Lib import Common, FileSystem

	# Confirm to exist the command line parameters
	if Common.count_args() == 0 :
	  Common.stop(9, "A file path must be specified as the parameter.")

	# Define the error code (0 means non-error).
	err = 0

	#  #  Get a parameter.
	fileName = Common.args(0)
	Common.esc_print(Common.ESC_FG_CYAN, fileName)

	# Confirm the file exists.
	if not FileSystem.exists(fileName) :
	  Common.stop(8, "The file does not exist.")
	    
	# Get the attributes of the file.
	b = FileSystem.isFile(fileName)
	print("Is file?: {0}".format(b))
	b = FileSystem.isDirectory(fileName)
	print("Is directory?: {0}".format(b))
	b = FileSystem.isLink(fileName)
	print("Is link?: {0}".format(b))
	mode = FileSystem.getAttr(fileName)
	print("File mode: {0:09o}".format(mode))
	owner = FileSystem.getOwner(fileName)
	print("Owner: {0}".format(owner))
	group = FileSystem.getGroup(fileName)
	print("Group: {0}".format(group))

	# Exit with termination code (err).
	exit(err)


### Text
	#!/usr/bin/env python3
	from Py365Lib import Common, Text

	# Define variable "txt".
	txt = "0123456789"

	# Concat text.
	to = Text.concat(txt, "ABCDEF")
	print(to)

	# Slices
	print(Text.substring(to, 1, 4))  # Start position 1, length is 4 chars.
	print(Text.substr(to, 1, 4))     # From the position 1 to 4.
	print(Text.left(to, 4))   # Left side length 4 chars.
	print(Text.right(to, 4))  # Right side 4 chars.

	# Repeat '*' 10 times.
	to = Text.times('*', 10)
	print(to)


### DateTime
	#!/usr/bin/env python3
	from Py365Lib import DateTime as dt, Common, Text
	from pprint import pprint

	# Get the DateTime object with now (local time).
	dt1 = dt.DateTime()
	print(dt1.toString())

	# Print now date and time.
	print("Just nowF{0:%x %X}".format(dt.now()))

	# Get the elements of date and time.
	print("{0}/{1}/{2}".format(dt1.year, dt1.month, dt1.day))
	print("{0}:{1}:{2}".format(dt1.hour, dt1.minute, dt1.second))


### MySQL
	#!/usr/bin/python3
	from Py365Lib import MySQL as mysql, Common
	import sys

	# Get test number.
	if len(sys.argv) == 1 :
	    print("You must enter the test number.")
	    exit(9)
	else :
	    testNo = int(sys.argv[1])

	client = mysql.MySQL()

	if testNo == 1 :
	    print(client.connectInfo)
	elif testNo == 2 :
	    rows = client.query("SELECT * FROM m_tables")
	    if client.rows > 0 :
	        for row in rows :
	            print(row)
	elif testNo == 3:
	    n = client.execute("INSERT INTO Asset(`date`,`asset`,`profit_loss`) VALUES('2011-09-16',4574314,-874320)")
	    print(n)
	elif testNo == 4:
	    n = client.getValue("SELECT count(*) FROM Asset")
	    print(n)
	elif testNo == 5 :
	    cur = client.cursor("SELECT `database`, name FROM m_tables")
	    while True :
	        row = cur.fetchone()
	        if Common.isset(row) :
	            print(row[0] + "." + row[1])
	        else :
	            break
	    client.cursorClose()
	else :
	    print("Bad testnumber.")

### AWSS3
	#!/usr/bin/python3
	import sys
	from pprint import pprint
	from Py365Lib import AWSS3 as aws

	def cb_keys(key) :
	    print(key)
	    return
	    
	# Get the test number.
	if len(sys.argv) == 1 :
	    print("You must enter the test number.")
	    exit(9)
	else :
	    testNo = int(sys.argv[1])

	# Get AWSS3 object.
	s3 = aws.AWSS3()

	if testNo == 1 :
	    for bucket in s3.buckets :
	        print(bucket.name)
	elif testNo == 2 :
	    s3.query_folders(s3.buckets[2].name, 1, cb_keys)
	elif testNo == 3 :
	    s3.query_files(s3.buckets[2].name, "images/akagi/", cb_keys)
	elif testNo == 4 :
	    print("bucket10/temp/disk.cgi {0}".format(s3.exists("bucket10", "temp/disk.cgi")))
	    print("bucket10/temp/1000.txt {0}".format(s3.exists("bucket10", "temp/1000.txt")))
	elif testNo == 5:
	    s3.put_file("bucket10", "temp/testAWSS3.py", "testAWSS3.py")
	    print('Upload: bucket10/temp/testAWSS3.py <= testAWSS3.py')
	elif testNo == 6:
	    s3.get_file("bucket10", "temp/200000.txt", "/home/user/temp/200000.txt")
	    print('Download: bucket10/temp/200000.txt => /home/user/temp/200000.txt')
	elif testNo == 7:
	    s3.make_folder("bucket10", "folder/")
	    print("make folder: bucket10/folder/")
	elif testNo == 8:
	    s3.remove_object("bucket10", "folder/")
	    print("remove object: bucket10/folder/")
	else :
	    print("Bad test number.")


## WebPage (CGI)

![hello world CGI](http://www7b.biglobe.ne.jp/~makandat/Py365Lib/tutorial/CGI_hello_world.png)

### hello_world.cgi
	#!/usr/bin/env python3
	# Hello, world!
	import WebPage as page
	import FileSystem as fsys
	
	# CGI class
	class Hello(page.WebPage) :
	  # constructor
	  def __init__(self, template) :
	    super().__init__(template)
	    self.setPlaceHolder('message', "Hello, world!")

	# Start up
	wp = Hello('templates/hellow_world.html')
	wp.echo()

### hello_world.html (template file)
	<!doctype html>
	<html lang="ja-jp">
	<head>
	<meta charset="utf-8" />
	<title>hello world</title>
	<style>
	 a:link, a:visited {
	   color: royalblue;
	   text-decoration: none;
	 }
	</style>
	</head>

	<body style="margin-left:5%;margin-right:5%">
	<h1 style="text-align:center;color:crimson;padding:10px;">hellow_world.cgi</h1>
	<p style="margin-left:10%;"><a href="/cgi">CGI Index</a></p>
	<br />
	<p style="text-align:center;color:magenta;font-size:2em;">
	(*message*)
	</p>
	<p> </p>
	</body>
	</html>



## CursesApp

![Hello World!](http://www7b.biglobe.ne.jp/~makandat/Py365Lib/tutorial/CursesApp_HelloWorld.png)

	#!/usr/bin/python3

	from Py365Lib import CursesApp as cap
	import curses

	class Application(cap.CursesApp) :

	  # Initial view
	  def init_app(self) :
	    x = int(self.Columns / 2) - 6
	    y = int(self.Rows / 2) - 1
	    self.print("Hello, world!", x, y, Application.COL_GREEN)
	    self.print("'q': Quit.", x, y + 1)
	    return;

	  # Key input handler
	  def handler(self, key) :
	    rc = True
	    if key == 'q' :
	      rc = False
	    return rc
	        
	# Start up.
	Application()


## TkApp

![Hello World](http://www7b.biglobe.ne.jp/~makandat/Py365Lib/tutorial/Tk_Hello.png)

	import sys
	from Py365Lib import TkApp as tkapp
	import tkinter as tk

	# Get the widget def file name.
	deffile = sys.argv[0].replace('.py', '.json')

	# Create root
	root = tk.Tk()
	# Create application
	winprop = {"title":"Hello", "left":100, "top":100, "width":400, "height":200, "fixedborder":True}
	app = tkapp.TkApp(root, winprop, deffile)
	# Enter event loop
	app.mainloop()


## HTApp

![Hello World](http://www7b.biglobe.ne.jp/~makandat/Py365Lib/tutorial/HTApp_Hello_World.png)

	#!/usr/bin/env python3
	import os
	import urllib
	import http.server
	from Py365Lib import HTApp
	from pprint import pprint
	from syslog import syslog

	# The handler of the route '/'
	def root(path) :
	  html = """<html>
	<head>
	 <meta charset="utf-8" />
	 <title>HTApp1</title>
	 <style>
	  body {
	    margin-left: 5%;
	    margin-right: 5%;
	  }
	  h1 {
	    padding: 8px;
	    color: crimson;
	  }
	 </style>
	</head>
	<body>
	 <h1>HTApp1 (test_HTApp1.py)</h1>
	 <p>root (/) ‚Ì‰ž“š</p>
	 <ul>
	   <li><a href="/about">/about</a></li>
	 </ul>
	</body>
	</html>
	  """
	  return ('text/html', html)

	# The handler of the route '/about'
	def about(path) :
	  with open(HTApp.TEMPLATES + "/about.html") as f :
	    html = f.read()
	  # Show the content AppConf.ini
	  itemlist = ""
	  for k, v in conf.items() :
	    itemlist += HTApp.tag("li", f"{k}: {v}")
	  html = html.replace("(*appconf*)", itemlist)
	  return ('text/html', html)


	# Start up
	try :
	  #  Read config file.
	  conf = HTApp.readConf()
	  #  Register handlers.
	  HTApp.routes['/'] = root
	  HTApp.routes['/about'] = about
	  #  Create server
	  server_name = conf['server_name']
	  port = int(conf['port'])
	  server = http.server.HTTPServer((server_name, port), HTApp.HTApp)
	  print("START Server. Port=%d" % port)
	  #  Request loop
	  server.serve_forever()
	except KeyboardInterrupt :
	  print()






## Requirements
- Python 3.6 or upper.
- mysql-connector (option)
- boto3 (option)
- curses (option)
- tkinter (option)

## Usage
Only Japanese document is provided now.
[Py365Lib Document (ja)] (http://www7b.biglobe.ne.jp/~makandat/Py365Lib/index.html)


## Contributing
Contributions, issues and feature requests are welcome.

## Author
Github: makandat

## License
GNU GPL

