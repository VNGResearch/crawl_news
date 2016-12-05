import os, sys, glob

sys.path.append('../models')
from vietpro import vietpro

dir_in = './data/zing/'
dir_out = './data_out/zing_token'

for filename in glob.iglob(dir_in + '*.tsv'):
    with open(filename) as f:
        corpus = os.path.basename(filename)
        print('process {}'.format(corpus))
        with open(os.path.join(dir_out, corpus), 'w') as fw: 
            for doc in f:
                if doc.strip() == '':
                    pdb.set_trace()
                    continue
                paths = doc.split('\t')
                for i, path in enumerate(paths[1:]):
                    if path.strip()=='':
                        continue
                    text = vietpro.standardize(path)
                    tokens = vietpro.tokenize(path)
                    paths[i+1] = vietpro.standardize(' '.join(tokens))
                doc = '\t'.join(paths) + '\n'

                fw.write(doc)
