import os
from CRABClient.UserUtilities import config
config = config()

config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'EXO-step1GS_Zp2HDM.py'

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True

config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/' 

config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'

from multiprocessing import Process

import sys

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand

    def submit(config):
        print " to do: ",config
        res = crabCommand('submit', config = config)

    ######### From now on this is what users should modify. It is the a-la-CRAB2 configuration part.
   
    print sys.argv
    if len(sys.argv) <= 1 :
       print "no arguments?"
       print "Usage to submit:     python crab_cfg_step1GS_Zp2HDM.py samples_file.py"
       print "Usage to get status: python crab_cfg_step1GS_Zp2HDM.py folder"
       exit()

    samples = {}
    SamplesFile = sys.argv[1]
    print " SamplesFile = ", SamplesFile
    
    additionalConfiguration = ''
    if len(sys.argv) == 4 :
      additionalConfiguration = sys.argv[3]
    print " additionalConfiguration = ", additionalConfiguration
    
    # submit
    if os.path.exists(SamplesFile) and not os.path.isdir(SamplesFile) :
       handle = open(SamplesFile,'r')
       exec(handle)
       handle.close()
                
       # samples to be analysed
                   
       for key, value in samples.iteritems():
           print key, ' -> ', value
        
           config.General.requestName = key
           config.Data.outputPrimaryDataset = value[0]
           config.Data.outputDatasetTag = value[1]
           config.Data.inputDataset = value[2]

#config.General.requestName = 'MonoHWW_Zp2HDM_MZP2500_13TeV_step1GS_76X'
#config.Data.outputPrimaryDataset = 'MonoHWW_Zp2HDM_MZP2500_13TeV_76X'
#config.Data.outputDatasetTag = 'MonoHWW_Zp2HDM_MZP2500_13TeV_76X_step1GS'

           p = Process(target=submit, args=(config,))
           p.start()
           p.join()
           #submit(config)
           # see https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Multiple_submission_fails_with_a
        
    # status and resubmit
    else :
       if len(sys.argv) >= 3 :
          if sys.argv[2] == 'report' :
           os.system("ls " + SamplesFile + " | awk '{print \" crab report "   + SamplesFile + "/\"$1" + "\" " + additionalConfiguration + "\"}' | /bin/sh")
          if sys.argv[2] == 'status' :
           os.system("ls " + SamplesFile + " | awk '{print \" crab status "   + SamplesFile + "/\"$1" + "\" " + additionalConfiguration + "\"}' | /bin/sh")
          if sys.argv[2] == 'resubmit' :
           os.system("ls " + SamplesFile + " | awk '{print \" crab resubmit " + SamplesFile + "/\"$1" + "\" " + additionalConfiguration + "\"}' | /bin/sh") 
          if sys.argv[2] == 'kill' :
           os.system("ls " + SamplesFile + " | awk '{print \" crab kill " + SamplesFile + "/\"$1" + "\" " + additionalConfiguration + "\"}' | /bin/sh") 
       else :
          os.system("ls " + SamplesFile + " | awk '{print \" crab status " + SamplesFile + "/\"$1}' | /bin/sh")
