from CRABClient.UserUtilities import config
config = config()
config.General.requestName = 'MonoHWW_Zp2HDM_MZP2500_MA0500_13TeV_step1GS_76X'
config.General.workArea = 'crab_projects'
config.JobType.pluginName = 'PrivateMC'
config.JobType.generator = 'lhe'
config.JobType.psetName = 'EXO-step1GS_Zp2HDM.py'
config.Data.outputPrimaryDataset = 'MonoHWW_Zp2HDM_MZP2500_MA0500_13TeV_76X'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'MonoHWW_Zp2HDM_MZP2500_MA0500_13TeV_76X_step1GS'
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/'
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
