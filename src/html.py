import os

class use:
    def __init__(self, content:dict):
        '''Send whatever the heck you want to be put in HTML via path.'''
        self.content = content
    def create(self, file, popex=False):
        '''Assemble HTML'''
        html = ''

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
        return html