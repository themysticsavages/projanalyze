import warnings
import zipfile
import os

class use:
    def __init__(self, content:dict):
        '''Send whatever the heck you want to be put in HTML via path.'''
        self.content = content
    def create(self, file, popex=False):
        '''Assemble HTML'''
        html = '<body style="background-color: #404040; color: white; font-family: "Open Sans"; font-style: normal;"> <h1>All found assets for project</h1> <p>May not be 100% accurate!</p> <br><br>'

        print('Generating HTML file as requested...')
        for cnt in self.content:
            if popex == True:
                if str(cnt).find('pop.wav') != -1:
                    continue
            if cnt.split('.')[2] == 'mp3' or cnt.split('.')[2] == 'wav':
                html += '<audio controls src="{}"></audio> '.format(cnt)
            else:
                html += '<img src="{}" height="100"> '.format(cnt)
        
        os.chdir(os.getcwd())
        open(file, 'w').write(html)
        return html+'</body>'

def zip():
    warnings.filterwarnings('ignore')
    os.chdir(os.getcwd())

    print('Zipping assets as requested...')
    with zipfile.ZipFile('./assets.zip', 'w') as zip:
        for fld, sfld, fnm in os.walk('./assets'):
            for fn in fnm:
                fp = os.path.join(fld, fn)
                zip.write(fp, os.path.basename(fp))
    zip.close()