#for table in /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-23andmeTask-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-6MWT_Displacement_Data-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-NonIdentifiableDemographics-v2.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-day_one-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-HealthKitDataCollector-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-HealthKitWorkoutCollector-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-risk_factors_SchemaV2-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-NonIdentifiableDemographics-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-risk_factors-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-satisfied-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-regionInformation-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-daily_check-v2.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-appVersion.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-HealthKitSleepCollector-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-satisfied_SchemaV3-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-satisfied_SchemaV2-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-Diet_survey_cardio_SchemaV2-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-2-APHHeartAge-7259AC18-D711-47A6-ADBD-6CFCECDED1DF-v2.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-6MinuteWalkTest-v2_withSteps.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-ABTestResults-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-status.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-motionTracker-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-6-Minute_Walk_Test_SchemaV4-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-ios-survey-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/6minWalk_healthCode_steps.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-motionActivityCollector-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-ActivitySleep-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-AwsClientIdTask-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-daily_check-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-6MinuteWalkTest-v2_withSteps_filtered.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-displacement-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-NonIdentifiableDemographicsTask-v2.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-2-APHHeartAge-7259AC18-D711-47A6-ADBD-6CFCECDED1DF-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-heart_risk_and_age-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-par-q_quiz-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-Diet_survey_cardio-v1.tsv /scratch/PI/euan/projects/mhc/data/tables/derived_age_sex_predictions.tsv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-6MinuteWalkTest-v2.tsv /scratch/PI/euan/projects/mhc/data/tables/v2_data_subset/cardiovascular-NonIdentifiableDemographicsTask-v2.QC.txt.csv /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-NonIdentifiableDemographicsTask-v2.QC.txt.csv
for table in /scratch/PI/euan/projects/mhc/data/tables/cardiovascular-NonIdentifiableDemographicsTask-v2.tsv
do
    python intersect_subject_list_with_table.py --subjects_file /scratch/PI/euan/projects/mhc/data/tables/23andmesubjects.txt --table $table --fields_to_ignore recordId externalId dataGroups uploadDate createdOn appVersion phoneInfo --fields_to_use_for_gwas NonIdentifiableDemographics.patientGoSleepTime NonIdentifiableDemographics.patientHeightInches NonIdentifiableDemographics.patientWeightPounds NonIdentifiableDemographics.patientWakeUpTime welcome phys_activity work sleep_diagnosis1 sleep_time chestPain chestPainInLastMonth dizziness heartCondition jointProblem moderate_act vigorous_act activity1_option feel_worthwhile1 feel_worthwhile2 feel_worthwhile4 riskfactors1 riskfactors2 riskfactors4 satisfiedwith_life feel_worthwhile3 riskfactors3 education family_history heart_disease medications_to_treat race vascular sodium vegetable fish fruit sugar_drinks grains data.csv data.csv atwork activity2_option activity1_intensity activity1_time activity1_type bloodPressureInstruction data.csv heartAgeDataBloodGlucose heartAgeDataDiabetes heartAgeDataEthnicity heartAgeDataHdl heartAgeDataHypertension heartAgeDataLdl heartAgeDataSystolicBloodPressure heartAgeDataTotalCholesterol smokingHistory  NonIdentifiableDemographics.patientBiologicalSex NonIdentifiableDemographics.patientCurrentAge NonIdentifiableDemographics.patientBiologicalSex --outf gwas_phenotypes.txt
done