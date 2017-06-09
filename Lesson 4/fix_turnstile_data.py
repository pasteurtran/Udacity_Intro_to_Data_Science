#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:13:43 2017

@author: PasteurTran
"""

import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 
    
    MY SAMPLE
    A002,R051,02-00-00,05-21-11,00:00:00,REGULAR,003169391,001097585,
                       05-21-11,04:00:00,REGULAR,003169415,001097588
                       05-21-11,08:00:00,REGULAR,003169431,001097607,
                       
    MY SAMPLE
    A002|R0510|2-00-0005-21-11,00:00:00,REGULAR,003169391,001097585,
                       05-21-11,04:00:00,REGULAR,003169415,001097588
                       05-21-11,08:00:00,REGULAR,003169431,001097607,                   
                       
                       
    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        
        #First open file, then read it, with a delimieter (too many , in the files)
        file = open(name)
        reader = csv.reader(file, delimiter = ',')
        
        #Allocate the file out 
        f_out = open('updated_' + name, 'writer')
        writer = csv.writer(f_out, delimiter = ',')
        for row in reader:
            #Looking at the data, first 4 characters are the ID of the Tram
            tram_id = row[0:3]
            row = row[3:]
            #Store that tram ID for the length of entire row
            while len(row) > 0:
                #Writing process
                new_row = tram_id + row[:5]
                #Take first tram ID, delimit, take next tram line
                row = row[5:]
                writer.writerow(new_row)
        f_out.close()
        file.close()
        
        