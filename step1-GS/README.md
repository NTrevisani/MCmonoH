Step1 - GEN-SIM
====

Use cmsrel CMSSW_7_1_21_patch1 and istall crab3:

    cd ../(..)/CMSSW_7_1_21_patch1/src

    cmsenv

    cd -

    source /cvmfs/cms.cern.ch/crab3/crab.sh

To test that everything works fine:

    cmsRun EXO-step1GS_Zp2HDM.py

To send jobs to crab:

    crab submit crab_cfg_step1GS_Zp2HDM.py 
