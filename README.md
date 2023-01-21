This script checks the availability of IP addresses over HTTP and HTTPS protocols. It utilizes a file named 'data.txt' which contains a list of IP addresses obtained through the use of the tool rustscan. 

# Installation
To run this script, you will need to have the following python packages installed:
- requests
- re

You can install these packages using pip by running the following command in your terminal:

`pip install requests re`

# Usage
To use this script, you will need a file named 'data.txt' containing a list of IP addresses obtained through rustscan in the format like:
```
Open 172.17.5.72:21
Open 172.17.5.9:135
Open 172.17.5.35:135
```

The script can then be run by calling the script with python:

`python script_name.py`

Note: the script will look for the 'data.txt' file in the same directory as the script.

# Output
When the script is run, it will check each IP address over both HTTP and HTTPS protocols. For each IP address, it will either print the URL if the IP address is available, or it will print a '.' if the IP address is not available. The output will look something like this:
```
.. 
http://172.17.5.72:21
.. 
https://172.17.5.72:21
..... 
http://172.17.5.9:135
..... 
https://172.17.5.9:135
.............
```

# Credit
This README.md was written by ChatGPT, and the script was created by Biplob Sutradhar, you can find more of his work on his GitHub repository at github.com/biplobsd.