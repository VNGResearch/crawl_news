import os, glob, pdb

dir_in = './data/zing/'
dir_out = './data_out/zing'

urls = set()

for filename in glob.iglob(dir_in + '*.tsv'):
    with open(filename) as f:
        corpus = os.path.basename(filename)
        print('process {}'.format(corpus))
        with open(os.path.join(dir_out, corpus), 'w') as fw: 
            for doc in f:
                if doc.strip() == '':
                    continue
                url = doc.split('\t')[0]
                if url not in urls:
                    urls.add(url)
                    fw.write(doc)
    #pdb.set_trace()
