#! /usr/bin/env python
import os
import subprocess
from ROOT import TH1F, TCanvas, TFile, TObject

sample = "1000ev_allcat_2pcrel_long"
analyse = 1

path = "./Tests/"

if( analyse ):

    # num[hypo][category][method] hypo=0,1 category=7,8,9,10,11 method=322,422,421,022,021   
    # time[hypo][category][method] hypo=0,1 category=7,8,9,10,11 method=322,422,421,022,021
    num = [[[0 for k in range(5)] for j in range(5)] for i in range(2)]
    time = [[[0.0 for k in range(5)] for j in range(5)] for i in range(2)]

    s = subprocess.Popen("ls "+path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
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

                if(l.find('Job done in...............')>0):
                    half = l.split('...............')[1]
                    seconds = float(half.split()[0])
                    if(hypo==0):
                        if(cat==7):
                            if(method==322):
                                num[0][0][0]  += 1
                                time[0][0][0] += seconds
                            if(method==022):
                                num[0][0][3]  += 1
                                time[0][0][3] += seconds    
                            if(method==021):
                                num[0][0][4]  += 1
                                time[0][0][4] += seconds
                        if(cat==8):
                            if(method==422):
                                num[0][1][1]  += 1
                                time[0][1][1] += seconds
                            if(method==322):
                                num[0][1][0]  += 1
                                time[0][1][0] += seconds
                            if(method==022):
                                num[0][1][3]  += 1
                                time[0][1][3] += seconds
                            if(method==021):
                                num[0][1][4]  += 1
                                time[0][1][4] += seconds
                        if(cat==9):
                            if(method==422):
                                num[0][2][1]  += 1
                                time[0][2][1] += seconds
                            if(method==022):
                                num[0][2][3]  += 1
                                time[0][2][3] += seconds
                            if(method==021):
                                num[0][2][4]  += 1
                                time[0][2][4] += seconds
                        if(cat==10):
                            if(method==421):
                                num[0][3][2]  += 1
                                time[0][3][2] += seconds
                            if(method==021):
                                num[0][3][4]  += 1
                                time[0][3][4] += seconds
                        if(cat==11):
                            if(method==421):
                                num[0][4][2]  += 1
                                time[0][4][2] += seconds
                            if(method==021):
                                num[0][4][4]  += 1
                                time[0][4][4] += seconds
                    if(hypo==1):
                        if(cat==7):
                            if(method==322):
                                num[1][0][0]  += 1
                                time[1][0][0] += seconds
                            if(method==022):
                                num[1][0][3]  += 1
                                time[1][0][3] += seconds    
                            if(method==021):
                                num[1][0][4]  += 1
                                time[1][0][4] += seconds
                        if(cat==8):
                            if(method==422):
                                num[1][1][1]  += 1
                                time[1][1][1] += seconds
                            if(method==322):
                                num[1][1][0]  += 1
                                time[1][1][0] += seconds
                            if(method==022):
                                num[1][1][3]  += 1
                                time[1][1][3] += seconds
                            if(method==021):
                                num[1][1][4]  += 1
                                time[1][1][4] += seconds
                        if(cat==9):
                            if(method==422):
                                num[1][2][1]  += 1
                                time[1][2][1] += seconds
                            if(method==022):
                                num[1][2][3]  += 1
                                time[1][2][3] += seconds
                            if(method==021):
                                num[1][2][4]  += 1
                                time[1][2][4] += seconds
                        if(cat==10):
                            if(method==421):
                                num[1][3][2]  += 1
                                time[1][3][2] += seconds
                            if(method==021):
                                num[1][3][4]  += 1
                                time[1][3][4] += seconds
                        if(cat==11):
                            if(method==421):
                                num[1][4][2]  += 1
                                time[1][4][2] += seconds
                            if(method==021):
                                num[1][4][4]  += 1
                                time[1][4][4] += seconds

    for i in range(2):
        for j in range(5):
            for k in range(5):
                if(num[i][j][k] > 0):
                    time[i][j][k] /= num[i][j][k]

    print "\n-----",sample,"-----\n"
    print "Method Events Mean"
    print "\n***cat7***"
    print "ttH_hypo"
    print "322 ", num[0][0][0], " ", time[0][0][0]
    print "022 ", num[0][0][3], " ", time[0][0][3]
    print "021 ", num[0][0][4], " ", time[0][0][4]    
    print "ttbb_hypo"
    print "322 ", num[1][0][0], " ", time[1][0][0]
    print "022 ", num[1][0][3], " ", time[1][0][3]
    print "021 ", num[1][0][4], " ", time[1][0][4]

    print "\n***cat8***"
    print "ttH_hypo"
    print "422 ", num[0][1][1], " ", time[0][1][1]
    print "322 ", num[0][1][0], " ", time[0][1][0]
    print "022 ", num[0][1][3], " ", time[0][1][3]
    print "021 ", num[0][1][4], " ", time[0][1][4]    
    print "ttbb_hypo"
    print "422 ", num[1][1][1], " ", time[1][1][1]
    print "322 ", num[1][1][0], " ", time[1][1][0]
    print "022 ", num[1][1][3], " ", time[1][1][3]
    print "021 ", num[1][1][4], " ", time[1][1][4]

    print "\n***cat9**"
    print "ttH_hypo"
    print "422 ", num[0][2][1], " ", time[0][2][1]
    print "022 ", num[0][2][3], " ", time[0][2][3]
    print "021 ", num[0][2][4], " ", time[0][2][4]    
    print "ttbb_hypo"
    print "422 ", num[1][2][1], " ", time[1][2][1]
    print "022 ", num[1][2][3], " ", time[1][2][3]
    print "021 ", num[1][2][4], " ", time[1][2][4]

    print "\n***cat10***"
    print "ttH_hypo"
    print "421 ", num[0][3][2], " ", time[0][3][2]
    print "021 ", num[0][3][4], " ", time[0][3][4]    
    print "ttbb_hypo"
    print "421 ", num[1][3][2], " ", time[1][3][2]
    print "021 ", num[1][3][4], " ", time[1][3][4]

    print "\n***cat11***"
    print "ttH_hypo"
    print "421 ", num[0][4][2], " ", time[0][4][2]
    print "021 ", num[0][4][4], " ", time[0][4][4]    
    print "ttbb_hypo"
    print "421 ", num[1][4][2], " ", time[1][4][2]
    print "021 ", num[1][4][4], " ", time[1][4][4]
