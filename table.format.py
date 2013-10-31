#! /usr/bin/env python 
# table.format.py
# 
# Author: Richard Barajas
# Date: 31-10-2013
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delimiter', 
                    action='store',
                    default='|', 
                    dest='delimiter',
                    help='Delimiter character seperating columns; default "|".')
parser.add_argument('-f', '--file',
                    action='store',
                    dest='filename',
                    required=True,
                    help='Filenames of delimited output.')
parser.add_argument('--header', 
                    action='store_true',
                    dest='header',
                    help='Use first line in file as header of table: default False.')

def horizontalEdge(columnLengths):
    edge = ''
    for colLength in columnLengths:
        edge += '+' + '-'*(colLength)
    return edge + '+'

def dataTable(data):
    colSpaces = maxColumnLengths(data)
    
    horizontalLine = horizontalEdge(colSpaces)
    
    useHeader = vars(parser.parse_args())['header']
    dataStart = 1
    if useHeader:
        printHeader(data[0], colSpaces, horizontalLine)
    else:
        dataStart = 0
        print horizontalLine

    for row in xrange(dataStart, len(data)):
        if row % 40 == 0 and useHeader:
            printHeader(data[0], colSpaces, horizontal)
        printRow(data[row], colSpaces)
    print horizontalLine

def maxColumnLengths(data):
    # Additional 2 spaces for margin
    colSpaces = [0 for string in data[0]]
    for row in data:
        for col in xrange(len(row)):
            colLength = len(row[col]) + 2
            if colLength > colSpaces[col]:
                colSpaces[col] = colLength
    return colSpaces

def parseData(filename):
    delim = vars(parser.parse_args())['delimiter']
    data = []
    f = open(filename, 'r')
    for line in f.read().split('\n'):
        if line != '':
            data.append([string for string in  line.split(delim)])
    return data

def main():
    data = parseData(vars(parser.parse_args())['filename'])
    dataTable(data)

def printHeader(header, colSpaces, horizontalLine):
    print horizontalLine
    printRow(header, colSpaces)
    print horizontalLine
    
def printRow(row, colSpaces):
    for col in xrange(len(row)):
        string = row[col]
        leftMargin = (colSpaces[col] - len(string)) / 2
        sys.stdout.write('|' + ' '*leftMargin + string)
        rightMargin = colSpaces[col] - leftMargin - len(string)
        sys.stdout.write(' '*rightMargin)
    sys.stdout.write('|\n')
    
if __name__ == "__main__":
    main()
