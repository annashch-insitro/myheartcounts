#READS THROUGH BLOB JSON IN INPUT FILE AND PERFORMS THE FOLLOWING FILTERING STEPS: 
#1.) SORT BY TIMESTAMP 
#2.) REMOVE ANY FULLY DUPLICATED ENTRIES 
#3.) WRITE TO FILE WITH SUFFIX .clean  
import json 
import collections 
from Parameters import * 
from os import listdir 
from os.path import isfile,join 
import sys 

#reads in a datafile and splits by line 
#replace '\r\n' with '\n' for Linux & Windows compatible newline characters 
def split_lines(fname): 
	data=open(fname,'r').read().replace('\r\n','\n').split('\n')
	if '' in data:
		data.remove('') 

        return data



#reads in a blob file specified with hash notation in a table file 
def parse_blob(blob_hash):
        top_dir=blob_hash[-3::].lstrip('0') 
        if top_dir=="": 
                top_dir='0' 
        full_dir=synapse_dir+top_dir+'/'+blob_hash
        csv_files=[f for f in listdir(full_dir) if isfile(join(full_dir,f))]
        for f in csv_files: 
                if f.startswith('.'): 
                        continue 
                if f.endswith('.tmp')==False: 
                        continue 
                else: 
                    inputfname=full_dir+'/'+f
                    data=open(inputfname).read() 
                    return data, inputfname # slightly modified version does not call split lines because we want to preserve the json structure 



def get_timestamp_field(filename,blobindex):
    if filename=='cardiovascular-6MWT Displacement Data-v1.tsv': 
        return "timestamp" 
    elif filename== 'cardiovascular-6MinuteWalkTest-v2.tsv':
        if blobindex==8: 
            return "endDate" 
        elif blobindex==9: 
            return "timestamp" 
        elif blobindex==10: 
            return "timestamp" 
        elif blobindex==11: 
            return "startDate" 
        elif blobindex==12: 
            return "timestamp" 
        elif blobindex==13: 
            return "timestamp" 
        elif blobindex==14: 
            return "startDate" 
        else: 
            print "SHOULD NOT BE HERE (BAD BLOB INDEX) :"+str(blobindex) 
            exit() 
    else: 
        print "SHOULD NOT BE HERE:TABLE FILE IS:"+filename 
        exit() 


def main(): 
    #for parallelizing across 20 cores--> pass chunks of file for parsing     
    start_line=int(sys.argv[1])*620 
    end_line=int(sys.argv[2])*620
    end_line=min(end_line,12381) 
    #####################################################
    for f in blob_json_formats: 
        print str(f) 
        if f=='cardiovascular-6MWT Displacement Data-v1.tsv':
                continue 
        data=split_lines(table_dir+f)[1::]  
        counter=0 
        for line in data[start_line:end_line]:
                line=line.split('\t')     
                counter+=1 
                if counter%10==0: 
                        print "COUNTER:"+str(counter) 
                for blob_index in range(8,len(line)): 
                    blobname=line[blob_index]
                    if blobname=="NA": 
                        continue 
                    timestamp_field=get_timestamp_field(f,blob_index)
                    blob,blobfilename=parse_blob(blobname)
                    if "{" not in blob: 
                            #not a valid entry 
                            print "empty blob:"+str(blobfilename)+"-->"+str(blob)  
                            with open(blobfilename+'.clean','w') as outf: 
                                    json.dump([],outf) 
                            continue 
                    json_object=json.loads(blob) 
                    #print str(json_object) 
                    timestamp_dict=dict() 
                    for entry in json_object: 
                        timestamp=entry.get(timestamp_field)  
                        timestamp_dict[timestamp]=entry #any entries with a duplicated timestamp will be overwritten
                    #sort by timestamp 
                    sorted_timestamp_dict=collections.OrderedDict(sorted(timestamp_dict.items()))
                    out_list=[]
                    for k,v in sorted_timestamp_dict.iteritems(): 
                        out_list.append(v) 
                    with open(blobfilename+'.clean','w') as outf: 
                        json.dump(out_list,outf) 

if __name__=="__main__": 
	main() 