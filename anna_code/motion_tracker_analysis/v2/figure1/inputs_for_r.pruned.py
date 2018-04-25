data=open('within_subject_measures.phone.steps.4inter.txt','r').read().strip().split('\n')
outf_steps=open("HKQuantityTypeIdentifierStepCount.4inter.txt",'w')
outf_steps.write('Subject\tIntervention\tDeltaFromBaseline\n')
subject_steps=dict()
subject_steps_baseline=dict() 
for line in data[1::]:
    tokens=line.split('\t')
    subject=tokens[0]
    outcome=tokens[1]
    intervention=tokens[2]
    value=tokens[3]
    if intervention =="Baseline":
        subject_steps_baseline[subject]=float(value)
    else:
        if subject not in subject_steps:
            subject_steps[subject]=dict()
        subject_steps[subject][intervention]=float(value)
for subject in subject_steps: 
    try:
        cur_baseline=subject_steps_baseline[subject] 
        for task in subject_steps[subject]: 
            outf_steps.write(subject+'\t'+task+'\t'+str(subject_steps[subject][task]-cur_baseline)+'\n')
    except:
        print("skipping")
        continue


            
            
