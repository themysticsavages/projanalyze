from src.exceptions import InvalidInt
from src.analyze import *
import src.pack
import argparse

parser = argparse.ArgumentParser(description='Throw together all the assets of a Scratch projects as local files.')

parser.add_argument('--html', action='store', help='Create an HTML file showing all the assets in one place. Creates in local directory.')
parser.add_argument('--id', help='Project ID for fetching assets. Totally required!', required=True)
parser.add_argument('--zip', action='store_true', help='Put all the assets in a zip file.')

args = parser.parse_args()

if int(args.id) <= 142:
    raise InvalidInt(message='You need a project ID higher than 142! Projects before this ID do not exist.')
else:
    res = fetch(str(args.id))
    if args.html:
        try:
            args.html.split('//')[1] == 'popex'
            src.pack.use(res).create(str(args.html).split('//')[0], popex=True)
        except IndexError:    
            src.pack.use(res).create(str(args.html))
    if args.zip:
        src.pack.zip()