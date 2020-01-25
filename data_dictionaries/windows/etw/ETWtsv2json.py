#!/usr/bin/env python3

# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

import csv
import json
import glob
from os import path
import re
import argparse

# Bannner
print(r"""
________________________      __   __                ________  
\_   _____/\__    ___/  \    /  \_/  |_  _________  _\_____  \ 
 |    __)_   |    |  \   \/\/   /\   __\/  ___/\  \/ //  ____/ 
 |        \  |    |   \        /  |  |  \___ \  \   //       \ 
/_______  /  |____|    \__/\  /   |__| /____  >  \_/ \_______ \
        \/                  \/              \/               \/
     ____. _________________    _______                        
    |    |/   _____/\_____  \   \      \                       
    |    |\_____  \  /   |   \  /   |   \                      
/\__|    |/        \/    |    \/    |    \                     
\________/_______  /\_______  /\____|__  /                     
                 \/         \/         \/  V0.1
 
 Creator: Roberto Rodriguez @Cyb3rWard0g
 License: GPL-3.0
 """)

# Initial description
text = "This script allows you to translate and transform etw tsv files to json files.."
example_text = '''example:

 python3 ETWtsv2json -d Windows10EtwEvents/ -o json/
 '''
# Initiate the arguments parser
parser = argparse.ArgumentParser(description=text,epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-d", "--tsv-directory", help="path to a directory where the tsv files exist", type=str , required=True)
parser.add_argument("-o", "--output-directory", help="path to a directory where you want to create the json files", type=str , required=True)
args = parser.parse_args()

print("[+] Processing all TSV files.. ")
schemafiles = glob.glob("{}/**/*.tsv".format(args.tsv_directory), recursive=True)

for sf in schemafiles:
    print("[  >>] Reading contents of {}.. ".format(sf))
    filename = path.splitext(path.basename(sf))[0] 
    with open(sf) as tsvfile:
        reader = list(csv.DictReader(tsvfile, delimiter="\t"))
        for r in reader:
            if 'event(fields)' in r.keys():
                r['event_fields'] = []
                reFields = re.search('.*\((.*)\).*', r['event(fields)'], re.IGNORECASE).group(1)
                if reFields:
                    fieldsList = reFields.split(',')
                    for fl in fieldsList:
                        fieldDict = dict()
                        newField = (fl.strip()).split(" ")
                        fieldDict['field_type'] = newField[0]
                        fieldDict['field_name'] = newField[1] 
                        r['event_fields'].append(fieldDict)
    with open('{}/{}.json'.format(args.output_directory,filename), 'w', encoding='utf-8') as jsonfile:
        json.dump(reader, jsonfile, ensure_ascii=False, indent=4)