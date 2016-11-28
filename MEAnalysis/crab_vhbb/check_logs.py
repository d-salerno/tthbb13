#! /usr/bin/env python
import os
import subprocess
from ROOT import TH1F, TCanvas, TFile, TObject

samples = ["QCD300","QCD300x","QCD500","QCD500x","QCD700","QCD700x","QCD1000","QCD1500","QCD2000","TTbar","ttHbb","ttHNon"]
copy = 0
extract = 0
analyse = 0
report = 1

#se = "root://storage01.lcg.cscs.ch/pnfs/lcg.cscs.ch/cms/trivcat//store/user/dsalerno"
se = "storage01.lcg.cscs.ch"
folder = "/pnfs/lcg.cscs.ch/cms/trivcat//store/user/dsalerno"

path = {
    # "QCD300":"tth/VHBBHeppyV21_tthbbV9_v3/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBBHeppyV21_tthbbV9_v3/160514_193325",
    # "QCD500":"tth/VHBBHeppyV21_tthbbV9_v3/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBBHeppyV21_tthbbV9_v3/160514_194135",
    # "QCD700":"tth/VHBBHeppyV21_tthbbV9_v3/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBBHeppyV21_tthbbV9_v3/160514_193622",
    # "QCD1000":"tth/VHBBHeppyV21_tthbbV9_v3/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBBHeppyV21_tthbbV9_v3/160514_193740",
    # "QCD1500":"tth/VHBBHeppyV21_tthbbV9_v3/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBBHeppyV21_tthbbV9_v3/160514_194255",
    # "QCD2000":"tth/VHBBHeppyV21_tthbbV9_v3/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBBHeppyV21_tthbbV9_v3/160514_193858",
    # "TTbar":"tth/VHBBHeppyV21_tthbbV9_v3_2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/VHBBHeppyV21_tthbbV9_v3_2/160515_085747",
    # "ttHbb":"tth/VHBBHeppyV21_tthbbV9_v3_3/ttHTobb_M125_13TeV_powheg_pythia8/VHBBHeppyV21_tthbbV9_v3_3/160518_110721",
    # "ttHNon":"tth/VHBBHeppyV21_tthbbV9_v3_3/ttHToNonbb_M125_13TeV_powheg_pythia8/VHBBHeppyV21_tthbbV9_v3_3/160518_110839",

    # "QCD300":"tth/FHwithme_2pcrel_1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_115507",
    # "QCD300x":"tth/FHwithme_2pcrel_1/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_120322",
    # "QCD500":"tth/FHwithme_2pcrel_1/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_121140",
    # "QCD500x":"tth/FHwithme_2pcrel_1/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_120959",
    # "QCD700":"tth/FHwithme_2pcrel_1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_120003",
    # "QCD700x":"tth/FHwithme_2pcrel_1/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_115645",
    # "QCD1000":"tth/FHwithme_2pcrel_1/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_120143",
    # "QCD1500":"tth/FHwithme_2pcrel_1/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_121320",
    # "QCD2000":"tth/FHwithme_2pcrel_1/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/FHwithme_2pcrel_1/161003_120503",
    # "TTbar":"tth/FHwithme_2pcrel_1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/FHwithme_2pcrel_1/161003_120820",
    # "ttHbb":"tth/FHwithme_2pcrel_1/ttHTobb_M125_13TeV_powheg_pythia8/FHwithme_2pcrel_1/161003_115824",
    # "ttHNon":"tth/FHwithme_2pcrel_1/ttHToNonbb_M125_13TeV_powheg_pythia8/FHwithme_2pcrel_1/161003_120642",
    # #"data":"",

    "QCD300":"tth/test_4bqcdmem_2/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_101839",
    "QCD300x":"tth/test_4bqcdmem_2/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102330",
    "QCD500":"tth/test_4bqcdmem_2/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102655",
    "QCD500x":"tth/test_4bqcdmem_2/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102544",
    "QCD700":"tth/test_4bqcdmem_2/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102100",
    "QCD700x":"tth/test_4bqcdmem_2/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_101949",
    "QCD1000":"tth/test_4bqcdmem_2/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102222",
    "QCD1500":"tth/test_4bqcdmem_2/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102803",
    "QCD2000":"tth/test_4bqcdmem_2/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/test_4bqcdmem_2/161108_102439",
    "TTbar":"tth/test_4bqcdmem_1/TT_TuneCUETP8M1_13TeV-powheg-pythia8/test_4bqcdmem_1/161108_093525",
    "ttHbb":"tth/test_4bqcdmem_1/ttHTobb_M125_13TeV_powheg_pythia8/test_4bqcdmem_1/161108_092825",
    "ttHNon":"tth/test_4bqcdmem_1/ttHToNonbb_M125_13TeV_powheg_pythia8/test_4bqcdmem_1/161108_093413",
}

endpath = "/scratch/dsalerno/tth/80x_test2/FHwithme_2pcrel_1/" #test_4bqcdmem_2/"    

for sample in samples:
    print ""
    print sample
    destination = endpath+sample
    if( copy ):
        #listdir = "gfal-ls "+se+"/"+path[sample]
        listdir = "xrdfs "+se+" ls "+folder+"/"+path[sample]
        p = subprocess.Popen(listdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        if not os.path.exists(destination):
            os.makedirs(destination)

        for line in p.stdout.readlines():
            #directory = line.split()[0]
            directory = (line.split("/")[-1]).split()[0]
            print ""
            print "directory ", directory
            listlog = listdir+"/"+directory+"/log"
            q = subprocess.Popen(listlog, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            for line in q.stdout.readlines():
                #logfile = line.split()[0]
                logfile = (line.split("/")[-1]).split()[0]
                print "logfile ", logfile
                if( os.path.isfile(destination+"/"+logfile) ):
                    print logfile, " already copied"
                    continue
                half = logfile.split("_")[1]
                num = half.split(".")[0]
                stdoutfile = "cmsRun-stdout-"+num+".log"
                if( os.path.isfile(destination+"/"+stdoutfile) ):
                    print logfile, " already extracted"
                    continue
                #copylog = "gfal-copy "+se+"/"+path[sample]+"/"+directory+"/log/"+logfile+" file://"+destination
                copylog = "xrdcp root://"+se+"/"+folder+"/"+path[sample]+"/"+directory+"/log/"+logfile+" /"+destination
                print copylog
                os.system(copylog)

    if( extract ):
        r = subprocess.Popen("ls "+destination, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for line in r.stdout.readlines():
            zipfile = line.split()[0]
            if(zipfile.find('log.tar.gz')<0):
                continue
            #print "zipfile ", zipfile
            half = zipfile.split("_")[1]
            num = half.split(".")[0]
            stdoutfile = "cmsRun-stdout-"+num+".log"
            #print "stdoutfile", stdoutfile
            if( os.path.isfile(destination+"/"+stdoutfile) ):
                print stdoutfile, " already extracted"
                continue
            unzip = "tar -C "+destination+" -zxvf "+destination+"/"+zipfile
            os.system(unzip)
        os.system("rm "+destination+"/cmsRun_*.log.tar.gz")
        os.system("rm "+destination+"/FrameworkJobReport-*.xml")   

    if( analyse ):
        outf = TFile.Open(endpath+"/jobtime.root","UPDATE")
        outf.cd()
        htime_total = TH1F("htime_total","htime_total",100,0,50)
        htime_vhbb  = TH1F("htime_vhbb" ,"htime_vhbb" ,100,0,20)
        htime_mem   = TH1F("htime_mem"  ,"htime_mem"  ,100,0,50)

        h_0_7_322   = TH1F("h_0_7_322","h_0_7_322",200,0,200)
        h_0_7_022   = TH1F("h_0_7_022","h_0_7_022",300,0,300)
        h_0_7_021   = TH1F("h_0_7_021","h_0_7_021",300,0,300)

        h_0_8_422   = TH1F("h_0_8_422","h_0_8_422",200,0,200)    
        h_0_8_322   = TH1F("h_0_8_322","h_0_8_322",500,0,500)
        h_0_8_022   = TH1F("h_0_8_022","h_0_8_022",300,0,300)
        h_0_8_021   = TH1F("h_0_8_021","h_0_8_021",300,0,300)

        h_0_9_422   = TH1F("h_0_9_422","h_0_9_422",2000,0,2000)    
        h_0_9_022   = TH1F("h_0_9_022","h_0_9_022",2000,0,2000)
        h_0_9_021   = TH1F("h_0_9_021","h_0_9_021",2000,0,2000)

        h_0_10_421   = TH1F("h_0_10_421","h_0_10_421",300,0,300)    
        h_0_10_021   = TH1F("h_0_10_021","h_0_10_021",200,0,200)

        h_0_11_421   = TH1F("h_0_11_421","h_0_11_421",200,0,200)    
        h_0_11_021   = TH1F("h_0_11_021","h_0_11_021",200,0,200)

        h_1_7_322   = TH1F("h_1_7_322","h_1_7_322",300,0,300)
        h_1_7_022   = TH1F("h_1_7_022","h_1_7_022",500,0,500)
        h_1_7_021   = TH1F("h_1_7_021","h_1_7_021",500,0,500)

        h_1_8_422   = TH1F("h_1_8_422","h_1_8_422",200,0,200)    
        h_1_8_322   = TH1F("h_1_8_322","h_1_8_322",800,0,800)
        h_1_8_022   = TH1F("h_1_8_022","h_1_8_022",500,0,500)
        h_1_8_021   = TH1F("h_1_8_021","h_1_8_021",500,0,500)

        h_1_9_422   = TH1F("h_1_9_422","h_1_9_422",2000,0,2000)    
        h_1_9_022   = TH1F("h_1_9_022","h_1_9_022",2000,0,2000)
        h_1_9_021   = TH1F("h_1_9_021","h_1_9_021",2000,0,2000)

        h_1_10_421   = TH1F("h_1_10_421","h_1_10_421",500,0,500)    
        h_1_10_021   = TH1F("h_1_10_021","h_1_10_021",300,0,300)

        h_1_11_421   = TH1F("h_1_11_421","h_1_11_421",200,0,200)    
        h_1_11_021   = TH1F("h_1_11_021","h_1_11_021",200,0,200)

        s = subprocess.Popen("ls "+destination, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for line in s.stdout.readlines():
            if(line.find('stdout') > 0):
                outfile = line.split()[0]
                #print "outfile", outfile
                f = open(destination+"/"+outfile)
                lines = f.readlines()
                hypo = -1
                cat = -1
                method = -1
                for l in lines:
                    if(l.find('timeto_doVHbb') == 0):
                        time_vhbb = float(l.split()[1])/3600
                        htime_vhbb.Fill( time_vhbb )
                    if(l.find('timeto_doMEM') == 0):
                        htime_mem.Fill( (float(l.split()[1]) - time_vhbb*3600)/3600 )
                    if(l.find('timeto_totalJob') == 0):
                        htime_total.Fill( float(l.split()[1])/3600 )
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
                        time = float(half.split()[0])
                        if(hypo==0):
                            if(cat==7):
                                if(method==322):
                                    h_0_7_322.Fill(time)
                                if(method==022):
                                    h_0_7_022.Fill(time)
                                if(method==021):
                                    h_0_7_021.Fill(time)
                            if(cat==8):
                                if(method==422):
                                    h_0_8_422.Fill(time)
                                if(method==322):
                                    h_0_8_322.Fill(time)
                                if(method==022):
                                    h_0_8_022.Fill(time)
                                if(method==021):
                                    h_0_8_021.Fill(time)
                            if(cat==9):
                                if(method==422):
                                    h_0_9_422.Fill(time)
                                if(method==022):
                                    h_0_9_022.Fill(time)
                                if(method==021):
                                    h_0_9_021.Fill(time)
                            if(cat==10):
                                if(method==421):
                                    h_0_10_421.Fill(time)
                                if(method==021):
                                    h_0_10_021.Fill(time)
                            if(cat==11):
                                if(method==421):
                                    h_0_11_421.Fill(time)
                                if(method==021):
                                    h_0_11_021.Fill(time)
                        if(hypo==1):
                            if(cat==7):
                                if(method==322):
                                    h_1_7_322.Fill(time)
                                if(method==022):
                                    h_1_7_022.Fill(time)
                                if(method==021):
                                    h_1_7_021.Fill(time)
                            if(cat==8):
                                if(method==422):
                                    h_1_8_422.Fill(time)
                                if(method==322):
                                    h_1_8_322.Fill(time)
                                if(method==022):
                                    h_1_8_022.Fill(time)
                                if(method==021):
                                    h_1_8_021.Fill(time)
                            if(cat==9):
                                if(method==422):
                                    h_1_9_422.Fill(time)
                                if(method==022):
                                    h_1_9_022.Fill(time)
                                if(method==021):
                                    h_1_9_021.Fill(time)
                            if(cat==10):
                                if(method==421):
                                    h_1_10_421.Fill(time)
                                if(method==021):
                                    h_1_10_021.Fill(time)
                            if(cat==11):
                                if(method==421):
                                    h_1_11_421.Fill(time)
                                if(method==021):
                                    h_1_11_021.Fill(time)

                # t = subprocess.Popen("grep 'timeto' "+destination+"/"+outfile, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                # for line in t.stdout.readlines():
                #     if(line.find('totalJob') > 0):
                #         jobtime = line.split()[1]
                #         #print "jobtime ", float(jobtime)/3600
                #         htime.Fill(float(jobtime)/3600)

        treedir = outf.GetDirectory( sample)
        if(treedir==None):
            treedir = outf.mkdir( sample )

        treedir.cd()
        htime_total.Write("", TObject.kOverwrite)
        htime_vhbb.Write("", TObject.kOverwrite)
        htime_mem.Write("", TObject.kOverwrite)

        h_0_7_322.Write("", TObject.kOverwrite)
        h_0_7_022.Write("", TObject.kOverwrite)
        h_0_7_021.Write("", TObject.kOverwrite)
        h_0_8_422.Write("", TObject.kOverwrite)
        h_0_8_322.Write("", TObject.kOverwrite)
        h_0_8_022.Write("", TObject.kOverwrite)
        h_0_8_021.Write("", TObject.kOverwrite)
        h_0_9_422.Write("", TObject.kOverwrite)
        h_0_9_022.Write("", TObject.kOverwrite)
        h_0_9_021.Write("", TObject.kOverwrite)
        h_0_10_421.Write("", TObject.kOverwrite)
        h_0_10_021.Write("", TObject.kOverwrite)
        h_0_11_421.Write("", TObject.kOverwrite)
        h_0_11_021.Write("", TObject.kOverwrite)

        h_1_7_322.Write("", TObject.kOverwrite)
        h_1_7_022.Write("", TObject.kOverwrite)
        h_1_7_021.Write("", TObject.kOverwrite)
        h_1_8_422.Write("", TObject.kOverwrite)
        h_1_8_322.Write("", TObject.kOverwrite)
        h_1_8_022.Write("", TObject.kOverwrite)
        h_1_8_021.Write("", TObject.kOverwrite)
        h_1_9_422.Write("", TObject.kOverwrite)
        h_1_9_022.Write("", TObject.kOverwrite)
        h_1_9_021.Write("", TObject.kOverwrite)
        h_1_10_421.Write("", TObject.kOverwrite)
        h_1_10_021.Write("", TObject.kOverwrite)
        h_1_11_421.Write("", TObject.kOverwrite)
        h_1_11_021.Write("", TObject.kOverwrite)

        outf.Close()

    if( report ):
        outf = TFile.Open(endpath+"/jobtime.root")
        outf.cd()

        hvhbb   = outf.Get(sample+"/htime_vhbb")
        hmem    = outf.Get(sample+"/htime_mem")
        htotal  = outf.Get(sample+"/htime_total")

        hh_0_7_322   = outf.Get(sample+"/h_0_7_322")
        hh_0_7_022   = outf.Get(sample+"/h_0_7_022")
        hh_0_7_021   = outf.Get(sample+"/h_0_7_021")

        hh_0_8_422   = outf.Get(sample+"/h_0_8_422")
        hh_0_8_322   = outf.Get(sample+"/h_0_8_322")
        hh_0_8_022   = outf.Get(sample+"/h_0_8_022")
        hh_0_8_021   = outf.Get(sample+"/h_0_8_021")

        hh_0_9_422   = outf.Get(sample+"/h_0_9_422")
        hh_0_9_022   = outf.Get(sample+"/h_0_9_022")
        hh_0_9_021   = outf.Get(sample+"/h_0_9_021")

        hh_0_10_421   = outf.Get(sample+"/h_0_10_421")
        hh_0_10_021   = outf.Get(sample+"/h_0_10_021")

        hh_0_11_421   = outf.Get(sample+"/h_0_11_421")
        hh_0_11_021   = outf.Get(sample+"/h_0_11_021")

        hh_1_7_322   = outf.Get(sample+"/h_1_7_322")
        hh_1_7_022   = outf.Get(sample+"/h_1_7_022")
        hh_1_7_021   = outf.Get(sample+"/h_1_7_021")

        hh_1_8_422   = outf.Get(sample+"/h_1_8_422")
        hh_1_8_322   = outf.Get(sample+"/h_1_8_322")
        hh_1_8_022   = outf.Get(sample+"/h_1_8_022")
        hh_1_8_021   = outf.Get(sample+"/h_1_8_021")

        hh_1_9_422   = outf.Get(sample+"/h_1_9_422")
        hh_1_9_022   = outf.Get(sample+"/h_1_9_022")
        hh_1_9_021   = outf.Get(sample+"/h_1_9_021")

        hh_1_10_421   = outf.Get(sample+"/h_1_10_421")
        hh_1_10_021   = outf.Get(sample+"/h_1_10_021")

        hh_1_11_421   = outf.Get(sample+"/h_1_11_421")
        hh_1_11_021   = outf.Get(sample+"/h_1_11_021")

        print "\nMethod Events Mean StdDev"
        print "\n***cat7***"
        print "ttH_hypo"
        print "322", hh_0_7_322.GetEntries(), hh_0_7_322.GetMean(), hh_0_7_322.GetStdDev()
        print "022", hh_0_7_022.GetEntries(), hh_0_7_022.GetMean(), hh_0_7_022.GetStdDev()
        print "021", hh_0_7_021.GetEntries(), hh_0_7_021.GetMean(), hh_0_7_021.GetStdDev()
        print "ttbb_hypo"
        print "322", hh_1_7_322.GetEntries(), hh_1_7_322.GetMean(), hh_1_7_322.GetStdDev()
        print "022", hh_1_7_022.GetEntries(), hh_1_7_022.GetMean(), hh_1_7_022.GetStdDev()
        print "021", hh_1_7_021.GetEntries(), hh_1_7_021.GetMean(), hh_1_7_021.GetStdDev()

        print "\n***cat8***"
        print "ttH_hypo"
        print "422", hh_0_8_422.GetEntries(), hh_0_8_422.GetMean(), hh_0_8_422.GetStdDev()
        print "322", hh_0_8_322.GetEntries(), hh_0_8_322.GetMean(), hh_0_8_322.GetStdDev()
        print "022", hh_0_8_022.GetEntries(), hh_0_8_022.GetMean(), hh_0_8_022.GetStdDev()
        print "021", hh_0_8_021.GetEntries(), hh_0_8_021.GetMean(), hh_0_8_021.GetStdDev()
        print "ttbb_hypo"
        print "422", hh_1_8_422.GetEntries(), hh_1_8_422.GetMean(), hh_1_8_422.GetStdDev()
        print "322", hh_1_8_322.GetEntries(), hh_1_8_322.GetMean(), hh_1_8_322.GetStdDev()
        print "022", hh_1_8_022.GetEntries(), hh_1_8_022.GetMean(), hh_1_8_022.GetStdDev()
        print "021", hh_1_8_021.GetEntries(), hh_1_8_021.GetMean(), hh_1_8_021.GetStdDev()

        print "\n***cat9***"
        print "ttH_hypo"
        print "422", hh_0_9_422.GetEntries(), hh_0_9_422.GetMean(), hh_0_9_422.GetStdDev()
        print "022", hh_0_9_022.GetEntries(), hh_0_9_022.GetMean(), hh_0_9_022.GetStdDev()
        print "021", hh_0_9_021.GetEntries(), hh_0_9_021.GetMean(), hh_0_9_021.GetStdDev()
        print "ttbb_hypo"
        print "422", hh_1_9_422.GetEntries(), hh_1_9_422.GetMean(), hh_1_9_422.GetStdDev()
        print "022", hh_1_9_022.GetEntries(), hh_1_9_022.GetMean(), hh_1_9_022.GetStdDev()
        print "021", hh_1_9_021.GetEntries(), hh_1_9_021.GetMean(), hh_1_9_021.GetStdDev()

        print "\n***cat10***"
        print "ttH_hypo"
        print "421", hh_0_10_421.GetEntries(), hh_0_10_421.GetMean(), hh_0_10_421.GetStdDev()
        print "021", hh_0_10_021.GetEntries(), hh_0_10_021.GetMean(), hh_0_10_021.GetStdDev()
        print "ttbb_hypo"
        print "421", hh_1_10_421.GetEntries(), hh_1_10_421.GetMean(), hh_1_10_421.GetStdDev()
        print "021", hh_1_10_021.GetEntries(), hh_1_10_021.GetMean(), hh_1_10_021.GetStdDev()

        print "\n***cat11***"
        print "ttH_hypo"
        print "421", hh_0_11_421.GetEntries(), hh_0_11_421.GetMean(), hh_0_11_421.GetStdDev()
        print "021", hh_0_11_021.GetEntries(), hh_0_11_021.GetMean(), hh_0_11_021.GetStdDev()
        print "ttbb_hypo"
        print "421", hh_1_11_421.GetEntries(), hh_1_11_421.GetMean(), hh_1_11_421.GetStdDev()
        print "021", hh_1_11_021.GetEntries(), hh_1_11_021.GetMean(), hh_1_11_021.GetStdDev()

        print "\nVHBB_mean stdev MEM_mean stdev Total_mean stdev"
        print hvhbb.GetMean(), hvhbb.GetStdDev(), hmem.GetMean(), hmem.GetStdDev(), htotal.GetMean(), htotal.GetStdDev()
