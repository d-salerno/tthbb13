#This file knows about all the TTH samples as produced by the VHbb group
#LFN to PFN resolution is done with code in samples_base
#Cross-sections also defined in samples_base
from TTH.MEAnalysis.samples_base import *
import FWCore.ParameterSet.Config as cms
import os

samples_dict = {
    "sample": cms.PSet(
        name     = cms.string(os.environ.get("TTH_SAMPLE", "sample")),
        nickname = cms.string("sample"),
        xSec     = cms.double("1"),
        nGen     = cms.int64(0),
        skip     = cms.bool(False),
        isMC     = cms.bool(bool(int(os.environ.get("IS_MC", 1)))),
        treeName = cms.string(os.environ.get("INPUT_TREE", "vhbb/tree")),
        #subFiles = cms.vstring(os.environ["INPUT_FILE"]),
        subFiles = cms.vstring("/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_10.root",
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_11.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_12.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_13.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_14.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_15.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_16.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_17.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_18.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_19.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_20.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_21.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_22.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_23.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_24.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_25.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_26.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_27.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_28.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_29.root", 
                               "/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_30.root"),
    )
}
