#NOTE: tested on pythoon 3.6 w/ anaconda 3
#Author: annashch@stanford.edu
import numpy as np
from datetime import datetime,timedelta
from dateutil.parser import parse
import pdb 
sample_gap_thresh=timedelta(minutes=15) 

def get_activity_fractions_from_duration(duration_dict):
    fraction_dict=dict()
    for day in duration_dict:
        fraction_dict[day]=dict()
        total_duration=timedelta(minutes=0)
        for activity in duration_dict[day]:
            for blob in duration_dict[day][activity]: 
                total_duration+=abs(duration_dict[day][activity][blob])
        total_duration=total_duration.total_seconds()
        if total_duration > 0:
            for entry in duration_dict[day]:
                fraction_dict[day][entry]=dict() 
                for blob in duration_dict[day][entry]:
                    fraction_dict[day][entry][blob]=duration_dict[day][entry][blob].total_seconds()/total_duration
    return fraction_dict

def parse_motion_activity(file_path):
    duration_dict=dict()
    fraction_dict=dict()
    numentries=dict() 
    cur_blob=file_path.split('/')[-2]

    #read in the data
    dtype_dict=dict()
    dtype_dict['names']=('startTime',
                         'activityType',
                         'confidence')
    dtype_dict['formats']=(datetime,
                           'U36',
                           'i')
    try:
        data=np.genfromtxt(file_path,
                           dtype=dtype_dict['formats'],
                           names=dtype_dict['names'],
                           delimiter=',',
                           skip_header=True,
                           loose=True,
                           invalid_raise=False,
                           converters={0:lambda x: parse(x)})
    except:
        return [duration_dict,fraction_dict,numentries]
    
    #get the duration of each activity by day 
    first_row=0
    try:
        num_rows=len(data)
        cur_time=data['startTime'][first_row]
        cur_day=data['startTime'][first_row].date() 
        cur_activity=data['activityType'][first_row]
        while (cur_activity=="not available") and (first_row <(num_rows-1)):
            first_row+=1
            cur_time=data['startTime'][first_row]
            cur_day=data['startTime'][first_row].date() 
            cur_activity=data['activityType'][first_row]
    except:
        return[duration_dict,fraction_dict,numentries]

    for row in range(first_row+1,len(data)):
        try:
            new_activity=data['activityType'][row]
            new_time=data['startTime'][row]
            new_day=data['startTime'][row].date()
            if(new_time-cur_time)<=sample_gap_thresh:
                if new_activity=="not available":
                    #carry forward from the previous activity 
                    new_activity=cur_activity
                duration=abs(new_time-cur_time)
                if cur_day not in duration_dict:
                    duration_dict[cur_day]=dict()
                    numentries[cur_day]=0
                if cur_activity not in duration_dict[cur_day]:
                    duration_dict[cur_day][cur_activity]=dict() 
                if cur_blob not in duration_dict[cur_day][cur_activity]: 
                    duration_dict[cur_day][cur_activity][cur_blob]=duration 
                else:
                    duration_dict[cur_day][cur_activity][cur_blob]+=duration
                numentries[cur_day]+=1  
            cur_activity=new_activity
            cur_time=new_time
            cur_day=new_day
        except:
            continue
    #get the activity fractions relative to total duration
    fraction_dict=get_activity_fractions_from_duration(duration_dict)
    return [duration_dict,fraction_dict,numentries]
        
def parse_healthkit_steps(file_path):
    tally_dict=dict()
    #keep track of the blob that yielded this data 
    cur_blob=file_path.split('/')[-2]
    #read in the data
    dtype_dict=dict()
    dtype_dict['names']=('startTime',
                         'endTime',
                         'type',
                         'value',
                         'unit',
                         'source',
                         'sourceIdentifier')
    dtype_dict['formats']=(datetime,
                           datetime,
                           'S36',
                           'f',
                           'S36',
                           'S36',
                           'S36')
    try:
        data=np.genfromtxt(file_path,
                           dtype=dtype_dict['formats'],
                           names=dtype_dict['names'],
                           delimiter=',',
                           skip_header=True,
                           loose=True,
                           invalid_raise=False,
                           converters={0:lambda x: parse(x),
                                       1:lambda x: parse(x)})
    except:
        print("There was a problem importing:"+str(file_path))
        return tally_dict
    #get the duration of each activity by day
    try:
        if ((data is not None) and (data.size>0)):
            if(data.size==1): 
                datatype=data['type'].tolist() 
                source=str(data['source'])
                sourceIdentifier=str(data['sourceIdentifier'])
                source_tuple=tuple([source,sourceIdentifier])
                value=data['value'].tolist()
                day=data['startTime'].tolist().date()
                if day not in tally_dict:
                    tally_dict[day]=dict()                
                if datatype not in tally_dict[day]:
                    tally_dict[day][datatype]=dict()
                if source_tuple not in tally_dict[day][datatype]:
                    tally_dict[day][datatype][source_tuple]=dict() 
                if cur_blob not in tally_dict[day][datatype][source_tuple]: 
                    tally_dict[day][datatype][source_tuple][cur_blob]=value 
                else:
                    tally_dict[day][datatype][source_tuple][cur_blob]+=value
            else:
                for row in range(data.size):
                    if data['startTime'][row] is not None:
                        datatype=data['type'][row]
                        source=data['source'][row]
                        sourceIdentifier=data['sourceIdentifier'][row]
                        source_tuple=tuple([source,sourceIdentifier])
                        day=data['startTime'][row].date()
                        value=data['value'][row]
                        if day not in tally_dict:
                            tally_dict[day]=dict()
                        if datatype not in tally_dict[day]:
                            tally_dict[day][datatype]=dict()
                        if source_tuple not in tally_dict[day][datatype]:
                            tally_dict[day][datatype][source_tuple]=dict() 
                        if cur_blob not in tally_dict[day][datatype][source_tuple]:
                            tally_dict[day][datatype][source_tuple][cur_blob]=value
                        else:
                            tally_dict[day][datatype][source_tuple][cur_blob]+=value
    except:
        print("There was a problem importing:"+str(file_path))
    return tally_dict

if __name__=="__main__":
    #TESTS for sherlock
    import pdb
    base_dir="/scratch/PI/euan/projects/mhc/data/synapseCache/"
    [motion_tracker_duration,motion_tracker_fractions,num_entries]=parse_motion_activity(base_dir+"638/14145638/data-054aa9f4-cb94-4663-b3df-e98ef3421dcb.csv")
    
    #health_kit_data=parse_healthkit_steps('/scratch/PI/euan/projects/mhc/data/synapseCache/135/21923135/data-e2853996-39d1-43f5-b060-f315bcd8725d.csv.filtered')
    pdb.set_trace() 

    
