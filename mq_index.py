import glob


mgf_files = glob.glob('./*.mgf')

for in_file in mgf_files:
    file_name = in_file.split('.mgf')[0]
    file_name = file_name+'_MQ_index.mgf'
    print('Processing: '+file_name)
    counter = 0
    with open(in_file) as in_file, open(file_name, 'wt') as out_file:
        for line in in_file:
            line = line.rstrip()
            if line.startswith('TITLE='):
                out_file.write(line+', MQIndex='+str(counter)+'\n')
                counter += 1
            else:
                out_file.write(line+'\n')
