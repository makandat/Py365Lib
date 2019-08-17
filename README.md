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
	print("Is file?： {0}".format(b))
	b = FileSystem.isDirectory(fileName)
	print("Is directory?： {0}".format(b))
	b = FileSystem.isLink(fileName)
	print("Is link?： {0}".format(b))
	mode = FileSystem.getAttr(fileName)
	print("File mode： {0:09o}".format(mode))
	owner = FileSystem.getOwner(fileName)
	print("Owner： {0}".format(owner))
	group = FileSystem.getGroup(fileName)
	print("Group： {0}".format(group))

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

### MySQL

### AWSS3





## Requirements
- Python3

## Usage
Only Japanese document is provided now.
[Py365Lib Document (ja)] (http://www7b.biglobe.ne.jp/~makandat/Py365Lib/index.html)


## Contributing
Contributions, issues and feature requests are welcome.

## Author
Github: makandat

## License
GNU GPL

