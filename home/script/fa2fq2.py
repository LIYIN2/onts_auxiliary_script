raw_fq = open(r'raw_sort.fq','r')
trim_polya_fa = open(r'trim_sort.fa','r')

result_txt = open(r'result4.fq','w')

while(1):


    if trim_polya_fa.readline()=='':
        break
    else:
        trim_polya_fa_2 = trim_polya_fa.readline()
        len_trim = len(trim_polya_fa_2) - 1

        raw_fq_1 = '@' + raw_fq.readline()[1:]
        raw_fq.readline()
        raw_fq.readline()
        raw_fq_4 = raw_fq.readline()[:len_trim]

        if raw_fq_4[-1] != '\n':
            raw_fq_4 += '\n'

        temp = raw_fq_1 + trim_polya_fa_2 + '+\n' + raw_fq_4

        result_txt.write(temp)

raw_fq.close()
trim_polya_fa.close()
result_txt.close()
