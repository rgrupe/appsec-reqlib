# Experiments from examples @  
# http://zetcode.com/python/requests/
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# Fail http://rgrupe.com header contains 'Server': 'Apache', 'X-Powered-By': 'PHP/7.3.9',

import sys, getopt, requests

def urlstatus(x):
    return resp.status_code

def urlheader(x):
    return resp.headers

def urlcontents(x): 
    return resp.text

def main(argv):
   url = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["iurl="])
   except getopt.GetoptError:
      print("read_url.py -i <url>")
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         resp = requests.get(arg)
         print(url, "status = ", urlstatus(resp))
         print(url, "headers: ", urlheader(resp))
         print(urlcontents(resp))
      elif opt in ("-o", "--ofile"):
         outputfile = arg

if __name__ == "__main__":
   main(sys.argv[1:])