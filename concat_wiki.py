'''The code is suing to format wiki text after used WikiExtractor for dump archieve.'''
import os, glob, pdb

dir_in = './data/wiki/text/'
dir_out = './data/wiki/'

with open(os.path.join(dir_out, 'wiki_concat.txt'), 'w') as fw: 
    for d in os.listdir(dir_in):
        print('===================', d)
        for filename in glob.iglob(os.path.join(dir_in, d) + '/wiki_*'):
            #print('process {}'.format(filename))
            content = ''
            title = True
            with open(filename) as f:
                for line in f:
                    line = line.strip()
                    if line== '':
                        continue
                    if line.startswith('<doc'):
                        content = ''
                        title = True
                        continue
                    if title ==True:
                        title = False
                        continue
                    if line.startswith('</doc'):
                        fw.write(content.strip() + '\n')
                        #pdb.set_trace()
                    else:
                        content += ' ' + line
