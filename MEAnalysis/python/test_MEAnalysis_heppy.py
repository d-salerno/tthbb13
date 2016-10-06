import subprocess
import copy, os
import unittest
import logging
import ROOT

class MEAnalysisTestCase(unittest.TestCase):
    testfiles = [                                 #actual file name is set in samples_local.py
        ("/store/user/jpata/tth/Sep13_testing_v1/ttHTobb_M125_13TeV_powheg_pythia8/Sep13_testing_v1/160913_124802/0000/tree_14.root", "tth"),
        #("/store/user/jpata/tth/Aug11_leptonic_nome_v1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/Aug11_leptonic_nome_v1/160811_212409/0000/tree_1.root", "ttjets")
    ]
    
    def launch_test_MEAnalysis(self, infile, sample):
        env = copy.copy(os.environ)
        CMSSW_BASE = os.environ["CMSSW_BASE"]
        env["ME_CONF"] = os.path.join(CMSSW_BASE, "src/TTH/MEAnalysis/python/cfg_local.py")
        env["INPUT_FILE"] = infile
        env["TTH_SAMPLE"] = sample
        outdir = "Loop_2_{0}".format(sample) #if this is anything but Loop_{0} the looper will number them Loop_sample_X, otherwise it requires no existing directory
        if os.path.isdir(outdir):
            raise Exception("output directory exists: {0}".format(outdir))

        import TTH.MEAnalysis.MEAnalysis_heppy as MEAnalysis_heppy
        import cProfile, time
        p = cProfile.Profile(time.clock)
        p.runcall(MEAnalysis_heppy.main)
        p.print_stats()
        return True
    
    def test_MEAnalysis(self):
        for infile, sample in self.testfiles:
            self.launch_test_MEAnalysis(infile, sample)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
