#!/usr/bin/python

from sys import argv

with open(argv[1]) as templateFile:
    template = templateFile.read()

    for infile in argv[2:]:
        # stem the filename
        filebase = argv[1][:-4].split('/')[-1] + '_' + infile[:-4]

        with open(filebase + '.xml', 'w') as outfile:
            outfile.write(template.format(infile=infile, filebase=filebase))
            outfile.close()
                          

    
