#coding:utf-8
import re

def find_http_pattern(infn):
    infile = open(infn, 'r')
    lines = infile.read()
    infile.close()
    pattern = r'(http:\/\/[A-Z0-9]+)\.([A-Z09]+)\.([A-Z0-9]+)'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    results=regex.findall(lines)
    print(results)

def find_email_pattern(infn):
    #fill out


if __name__ == "__main__":
    find_http_pattern('data/한국학.txt')
    find_email_pattern('data/한국학.txt')




