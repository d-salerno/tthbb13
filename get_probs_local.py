#! /usr/bin/env python
import os
import subprocess
from ROOT import TH1F, TCanvas, TFile, TObject

sample = "qcd15_1Mev_cat8_2pcrel"
analyse = 1

path = "./Tests/"

if( analyse ):

    # num[hypo][category][method] hypo=0,1,2 category=7,8,9,10,11 method=322,422,421,022,021
    # prob[hypo][category][method] hypo=0,1,2 category=7,8,9,10,11 method=322,422,421,022,021 
    num = [[[0 for k in range(5)] for j in range(5)] for i in range(2)]
    prob = [[[0.0 for k in range(5)] for j in range(5)] for i in range(2)]

    s = subprocess.Popen("ls "+path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    print "cat method tth ttbb qcd"

    for line in s.stdout.readlines():
        if(line.find('.log') > 0 and line.find(sample) >= 0 ):
            outfile = line.split()[0]
            #print "outfile", outfile
            f = open(path+"/"+outfile)
            lines = f.readlines()
            hypo = -1
            cat = -1
            method = -1
            for l in lines:
                if(l.find('hypo=0')>0):
                    hypo = 0
                if(l.find('hypo=1')>0):
                    hypo = 1
                if(l.find('hypo=2')>0):
                    hypo = 2

                if(l.find('fh_j7_tge5')>0 or l.find('fh_j7_t4')>0):
                    cat = 7
                if(l.find('fh_j8_tge5')>0 or l.find('fh_j8_t4')>0):
                    cat = 8                    
                if(l.find('fh_jge9_tge5')>0 or l.find('fh_jge9_t4')>0):
                    cat = 9
                if(l.find('fh_j8_t3')>0 ):
                    cat = 10
                if(l.find('fh_j7_t3')>0 ):
                    cat = 11

                if(l.find('conf=FH_3w2h2t')>0):
                    method = 322
                if(l.find('conf=FH_4w2h2t')>0):
                    method = 422
                if(l.find('conf=FH_4w2h1t')>0):
                    method = 421
                if(l.find('conf=FH_0w0w2h2t')>0):
                    method = 022
                if(l.find('conf=FH_0w0w2h1t')>0):
                    method = 021

                if(l.find('Probability             = (')>0):
                    half = l.split('Probability             = (')[1]
                    probability = float(half.split()[0])
                    if(hypo==0):
                        print cat, method, probability,
                    if(hypo==1):
                        print probability,
                    if(hypo==2):
                        print probability
