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
	
	# Confirm to exist the command line parameters
	if Common.count_args() == 0 :
	  Common.stop(9, "Enter the parameters.")
	
	# Define the error code (0 means non-error)
	err = 0
	
	#  Getting a parameter.
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

### Text

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

