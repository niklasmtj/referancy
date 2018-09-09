#!/usr/local/bin/python3

import sys, getopt

def main(argv):
  inputfile = ''
  outputfile = ''

  try:
    opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile"])
  except getopt.GetoptError:
    print ('referancy.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('referancy.py -i <inputfile> -o <outputfile>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg

  urlChanger(inputfile, outputfile)


def urlChanger(inputfile, outputfile):
  hostURL = input("Enter your blog name: ")
  with open(inputfile, 'r') as f:

    data = f.readlines()
    newUrls = []

    for url in data:
      while '\n' in url:
        url = url.replace('\n', '')
        url = url + '?ref=' + hostURL
        blogUrl = "[" + url + "]"
        newUrls.append(blogUrl)


  with open (outputfile, 'w+') as f: 
    for url in newUrls:
      f.write('%s\n' % url)

if __name__ == "__main__":
   main(sys.argv[1:])