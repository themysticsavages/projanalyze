# projanalyze
Cool script to fetch Scratch project assets in Python!

## What it basically does
```
Throw together all the assets of a Scratch projects as local files.

Fetches the project.json file from the Scratch project API
Finds all the MD5 filenames
Downloads the files using those names and is put into folders by sprite names
Creates an optional HTML file showing all the assets
```

## Script args
### **--help** 
show this help message and exit
```
python build.py --help -h
```

### **--id (required)** 
Project ID for fetching assets. Totally required!
```
python build.py --id 98210971
```

### **--html** 
Create an HTML file showing all the assets in one place. Creates in local directory.
```
python build.py --id 98210971 --html filename.html
```
Also, if you want to exclude the default `pop.wav`, enter the filename and add `//popex` after.
