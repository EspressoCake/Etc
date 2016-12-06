#!/usr/bin/python

import pyperclip

def main():
    inputString = raw_input("What is your memory address/offset?: ")
    if len(inputString) != 8:
        print "You must supply an offset address.\n"
        print "Example: 90492010\n"
        main()
    else:
        data = inputString
        splits = [data[i:i + 2] for i in range(0, len(data), 2)]
        concat = '"' + '\\x' + '\\x'.join(reversed(splits)) + '"'
        print 'Original:\t\t %s' % data
        print 'Little Endian: \t ' + concat
        pyperclip.copy(concat)
        print "!COPIED_TO_CLIPBOARD!".center(34, '=')

if __name__ == "__main__":
    main()

