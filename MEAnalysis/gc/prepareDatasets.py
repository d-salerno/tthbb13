from __future__ import print_function
from TTH.MEAnalysis.samples_base import lfn_to_pfn
import sys, imp
import ROOT

samplefile = sys.argv[1]
samplefile = imp.load_source("samplefile", samplefile)
from samplefile import samples_dict

for sample_name, sample in samples_dict.items():
    ngen = 0
    ngenNeg = 0
    ngenPos = 0
    
    ngen2 = 0
    ngenNeg2 = 0
    ngenPos2 = 0

    files = sample.subFiles
    outfile = open(sample.nickname.value()+".dat", "a")
    outfile.write("[{0}]\n".format(sample_name))
    for f in files:
        pfn = lfn_to_pfn(f)
        #print("opening", pfn)
        tf = ROOT.TFile.Open(pfn)
        if (tf == None or tf is None or tf.IsZombie()):
            print("could not read file {0}, {1}, {2}".format(pfn, tf, tf.IsZombie()), file=sys.stderr)
        else:
            tt = tf.Get("tree")
            if (tt == None):
                print("could not read tree", file=sys.stderr)
            else:
                outfile.write("{0} = {1}\n".format(f, int(tt.GetEntries())))
                
                hc = tf.Get("Count")
                ngen += hc.GetBinContent(1)
                
                hc = tf.Get("CountNegWeight")
                if hc != None:
                    ngenNeg += hc.GetBinContent(1)
                hc = tf.Get("CountPosWeight")            
                if hc != None:
                    ngenPos += hc.GetBinContent(1)
                
                ngen2 += tt.GetEntries()
                if sample.isMC:
                    ngenNeg2 += tt.GetEntries("genWeight < 0")
                    ngenPos2 += tt.GetEntries("genWeight > 0")
                    
        tf.Close()
        del tf
        sys.stdout.flush()
        sys.stderr.flush()
    print("{0} {1} {2} {3} {4} {5} {6}".format(sample_name, ngen, ngenPos, ngenNeg, ngen2, ngenNeg2, ngenPos2))
    print(sample_name, ngenPos-ngenNeg)
    outfile.close()
