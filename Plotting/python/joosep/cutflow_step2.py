import FWCore.ParameterSet.Types  as CfgTypes
import FWCore.ParameterSet.Config as cms

process = cms.Process("MEAnalysisNew")

process.fwliteInput = cms.PSet(
	outFile = cms.string("outfile.root"),
	elePt=cms.double(-1),
	muPt=cms.double(-1),

    samples = cms.VPSet([
        cms.PSet(
            fileNamesS1=cms.vstring(["/home/joosep/mac-docs/tth/data/TTHbb_s1_5b21f5f_tth_hbb_13tev.root"]),
            fileNamesS2=cms.vstring(["/home/joosep/mac-docs/tth/data/tthbb.root"]),
            nickName=cms.string("tthbb_13TeV"),
            fractionToProcess=cms.double(1.0),
            totalEvents=cms.int64(-1),
            type=cms.int32(3),
            process=cms.int32(0),
            skip=cms.bool(False),
        ),
        cms.PSet(
            fileNamesS1=cms.vstring([]),
            fileNamesS2=cms.vstring(["/home/joosep/mac-docs/tth/data/ttjets.root"]),
            nickName=cms.string("ttjets_13TeV"),
            fractionToProcess=cms.double(1.0),
            totalEvents=cms.int64(-1),
            type=cms.int32(3),
            process=cms.int32(1),
            skip=cms.bool(False),
        ),
        ]),
    evLimits=cms.vint64(0, -1)
)