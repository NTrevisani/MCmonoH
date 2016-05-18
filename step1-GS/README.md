Step1 - GEN-SIM
====

Use cmsrel CMSSW_7_1_21_patch1 and istall crab3:

    cd ../(..)/CMSSW_7_1_21_patch1/src

    cmsenv

    cd -

    source /cvmfs/cms.cern.ch/crab3/crab.sh

To test that everything works fine:

    cmsRun EXO-step1GS_Zp2HDM.py

To send jobs to crab, one by one:

    crab submit crab_cfg_step1GS_Zp2HDM.py 

To send all the jobs to crab automatically:

    python crabbing.py submit

To resubmit all the jobs to crab automatically:

    python crabbing.py resubmit


Backup
====

Remember to fill the list of the samples you want to GEN-SIM in:

	 step1-GS.py

