import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.Config as cms

triggerPathNames = cms.vstring([
        #'digitisation_step',
        #'L1simulation_step',
        #'digi2raw_step',
        #'HLTriggerFirstPath',
        #'HLT_Activity_Ecal_SC7_v14',
        #'HLT_L1SingleJet16_v7',
        #'HLT_L1SingleJet36_v7',
        #'HLT_PFJet40_v9',
        #'HLT_PFJet80_v10',
        #'HLT_PFJet140_v10',
        #'HLT_PFJet200_v10',
        #'HLT_PFJet260_v10',
        #'HLT_PFJet320_v10',
        #'HLT_Jet370_NoJetID_v15',
        #'HLT_PFJet400_v10',
        #'HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v5',
        #'HLT_SingleForJet25_v4',
        #'HLT_SingleForJet15_v4',
        #'HLT_DiPFJetAve40_v10',
        #'HLT_DiPFJetAve80_v11',
        #'HLT_DiPFJetAve140_v11',
        #'HLT_DiPFJetAve200_v11',
        #'HLT_DiPFJetAve260_v11',
        #'HLT_DiPFJetAve320_v11',
        #'HLT_DiPFJetAve400_v11',
        #'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11',
        #'HLT_DoubleJet20_ForwardBackward_v4',
        'HLT_DiJet80_DiJet60_DiJet20_v6',
        #'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v10',
        #'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v10',
        #'HLT_DiJet40Eta2p6_BTagIP3DFastPV_v8',
        'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v8',
        'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v8',
        'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v8',
        'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v8',
        'HLT_QuadJet45_v1',
        'HLT_QuadJet50_v5',
        'HLT_QuadJet60_DiJet20_v6',
        'HLT_QuadJet70_v6',
        'HLT_QuadJet80_v6',
        'HLT_QuadJet90_v6',
        #'HLT_QuadJet75_55_35_20_BTagIP_VBF_v9',
        #'HLT_QuadJet75_55_38_20_BTagIP_VBF_v9',
        #'HLT_QuadJet75_55_35_20_VBF_v2',
        #'HLT_QuadPFJet78_61_44_31_BTagCSV_VBF_v7',
        #'HLT_QuadPFJet78_61_44_31_VBF_v2',
        #'HLT_QuadPFJet82_65_48_35_BTagCSV_VBF_v7',
        'HLT_SixJet35_v6',
        'HLT_SixJet45_v6',
        'HLT_SixJet50_v6',
        'HLT_EightJet30_eta3p0_v5',
        'HLT_EightJet35_eta3p0_v5',
        #'HLT_ExclDiJet35_HFOR_v4',
        #'HLT_ExclDiJet35_HFAND_v4',
        #'HLT_ExclDiJet80_HFAND_v4',
        #'HLT_JetE30_NoBPTX_v14',
        #'HLT_JetE30_NoBPTX3BX_NoHalo_v16',
        #'HLT_JetE50_NoBPTX3BX_NoHalo_v13',
        #'HLT_JetE70_NoBPTX3BX_NoHalo_v5',
        #'HLT_HT200_AlphaT0p57_v8',
        #'HLT_HT200_v6',
        #'HLT_HT250_AlphaT0p55_v8',
        #'HLT_HT250_AlphaT0p57_v8',
        #'HLT_HT250_v7',
        #'HLT_HT300_AlphaT0p53_v8',
        #'HLT_HT300_AlphaT0p54_v14',
        #'HLT_HT300_v7',
        #'HLT_HT300_DoubleDisplacedPFJet60_v11',
        #'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v11',
        #'HLT_HT300_SingleDisplacedPFJet60_v11',
        #'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v11',
        #'HLT_HT350_v7',
        #'HLT_HT350_AlphaT0p52_v8',
        #'HLT_HT350_AlphaT0p53_v19',
        #'HLT_HT400_v7',
        #'HLT_HT400_AlphaT0p51_v19',
        #'HLT_HT400_AlphaT0p52_v14',
        #'HLT_HT450_AlphaT0p51_v14',
        #'HLT_HT450_v7',
        #'HLT_HT500_v7',
        #'HLT_HT550_v7',
        #'HLT_HT650_v7',
        #'HLT_HT650_Track50_dEdx3p6_v11',
        #'HLT_HT650_Track60_dEdx3p7_v11',
        #'HLT_HT750_v7',
        #'HLT_PFNoPUHT350_v5',
        #'HLT_PFNoPUHT650_v5',
        #'HLT_PFNoPUHT650_DiCentralPFNoPUJet80_CenPFNoPUJet40_v5',
        #'HLT_PFNoPUHT700_v5',
        #'HLT_PFNoPUHT750_v5',
        #'HLT_PFMET150_v8',
        #'HLT_PFMET180_v8',
        #'HLT_DiCentralJetSumpT100_dPhi05_DiCentralPFJet60_25_PFMET100_HBHENoiseCleaned_v6',
        #'HLT_DiCentralPFJet30_PFMET80_v7',
        #'HLT_DiCentralPFNoPUJet50_PFMETORPFMETNoMu80_v5',
        #'HLT_DiCentralPFJet30_PFMET80_BTagCSV07_v6',
        #'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d03_v6',
        #'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05d05_v6',
        #'HLT_DiPFJet80_DiPFJet30_BTagCSVd07d05_v6',
        #'HLT_MET80_v5',
        #'HLT_MET80_Parked_v5',
        #'HLT_MET80_Track50_dEdx3p6_v7',
        #'HLT_MET80_Track60_dEdx3p7_v7',
        #'HLT_MET100_HBHENoiseCleaned_v2',
        #'HLT_MET120_v13',
        #'HLT_MET120_HBHENoiseCleaned_v7',
        #'HLT_MET200_v12',
        #'HLT_MET200_HBHENoiseCleaned_v6',
        #'HLT_MET300_v4',
        #'HLT_MET300_HBHENoiseCleaned_v6',
        #'HLT_MET400_v7',
        #'HLT_MET400_HBHENoiseCleaned_v6',
        #'HLT_L1SingleMuOpen_v7',
        #'HLT_L1SingleMu12_v2',
        #'HLT_L2Mu70_2Cha_eta2p1_PFMET55_v3',
        #'HLT_L2Mu70_2Cha_eta2p1_PFMET60_v3',
        #'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v4',
        #'HLT_L2Mu20_eta2p1_NoVertex_v2',
        #'HLT_L2Mu20_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
        #'HLT_L2Mu30_NoVertex_2Cha_NoBPTX3BX_NoHalo_v1',
        #'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v9',
        #'HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v9',
        #'HLT_Mu5_v21',
        #'HLT_Mu8_v19',
        #'HLT_Mu12_v19',
        #'HLT_Mu17_v6',
        #'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v8',
        #'HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v4',
        #'HLT_Mu15_eta2p1_v6',
        'HLT_Mu24_v17',
        'HLT_Mu24_eta2p1_v6',
        'HLT_Mu30_v17',
        'HLT_Mu30_eta2p1_v6',
        'HLT_Mu40_v15',
        'HLT_Mu40_eta2p1_v12',
        'HLT_Mu50_eta2p1_v9',
        #'HLT_RelIso1p0Mu5_v7',
        #'HLT_RelIso1p0Mu20_v4',
        'HLT_IsoMu15_eta2p1_L1ETM20_v8',
        'HLT_IsoMu20_eta2p1_v8',
        'HLT_IsoMu24_v18',
        'HLT_IsoMu24_eta2p1_v16',
        'HLT_IsoMu30_v12',#
        'HLT_IsoMu30_eta2p1_v16',
        'HLT_IsoMu34_eta2p1_v14',
        'HLT_IsoMu40_eta2p1_v11',
        'HLT_Mu40_eta2p1_Track50_dEdx3p6_v6',
        'HLT_Mu40_eta2p1_Track60_dEdx3p7_v6',
        #'HLT_L2DoubleMu23_NoVertex_v11',
        #'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3',
        #'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v3',
        #'HLT_DoubleMu11_Acoplanarity03_v6',
        #'HLT_DoubleMu4_Jpsi_Displaced_v13',
        #'HLT_DoubleMu4_JpsiTk_Displaced_v8',
        #'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v6',
        #'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v6',
        #'HLT_DoubleMu4_Dimuon7_Bs_Forward_v6',
        #'HLT_DoubleMu3p5_LowMass_Displaced_v7',
        #'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v7',
        #'HLT_Dimuon0_Jpsi_v18',
        #'HLT_Dimuon0_Jpsi_NoVertexing_v15',
        #'HLT_Dimuon0_Upsilon_v18',
        #'HLT_Dimuon0_PsiPrime_v7',
        #'HLT_Dimuon5_Upsilon_v7',
        #'HLT_Dimuon5_PsiPrime_v7',
        #'HLT_Dimuon7_Upsilon_v8',
        #'HLT_Dimuon7_PsiPrime_v4',
        #'HLT_Dimuon8_Jpsi_v8',
        #'HLT_Dimuon8_Upsilon_v7',
        #'HLT_Dimuon10_Jpsi_v7',
        #'HLT_Dimuon11_Upsilon_v7',
        #'HLT_Dimuon0_Jpsi_Muon_v19',
        #'HLT_Dimuon0_Upsilon_Muon_v19',
        #'HLT_Dimuon3p5_SameSign_v7',
        #'HLT_DoubleMu4_Acoplanarity03_v6',
        #'HLT_Tau2Mu_ItTrack_v8',
        'HLT_Mu13_Mu8_v23',
        'HLT_Mu17_Mu8_v23',
        'HLT_Mu13_Mu8_NoDZ_v2',
        'HLT_Mu17_TkMu8_v15',
        'HLT_Mu17_TkMu8_NoDZ_v2',
        'HLT_Mu22_TkMu8_v10',
        'HLT_Mu22_TkMu22_v10',
        #'HLT_TripleMu5_v20',
        #'HLT_DoubleMu5_IsoMu5_v21',
        #'HLT_Mu5_L2Mu3_Jpsi_v9',
        #'HLT_Mu5_Track2_Jpsi_v22',
        #'HLT_Mu5_Track3p5_Jpsi_v8',
        #'HLT_Mu7_Track7_Jpsi_v21',
        #'HLT_Mu15_TkMu5_Onia_v2',
        #'HLT_BTagMu_Jet20_Mu4_v3',
        #'HLT_BTagMu_Jet60_Mu4_v3',
        #'HLT_Photon20_CaloIdVL_v5',
        #'HLT_Photon20_CaloIdVL_IsoL_v17',
        #'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v6',
        #'HLT_Photon26_Photon18_v13',
        #'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v3',
        #'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v6',
        #'HLT_Photon30_v2',
        #'HLT_Photon30_CaloIdVL_v15',
        #'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_v2',
        #'HLT_Photon30_R9Id90_CaloId_HE10_Iso40_EBOnly_Met25_HBHENoiseCleaned_v2',
        #'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v6',
        #'HLT_Photon36_Photon22_v7',
        #'HLT_Photon36_R9Id85_Photon22_R9Id85_v5',
        #'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v7',
        #'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v7',
        #'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v7',
        #'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v7',
        #'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v6',
        #'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v2',
        #'HLT_Photon50_CaloIdVL_v11',
        #'HLT_Photon50_CaloIdVL_IsoL_v18',
        #'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v6',
        #'HLT_Photon60_CaloIdL_MHT70_v12',
        #'HLT_Photon60_CaloIdL_HT300_v5',
        #'HLT_Photon70_CaloIdXL_PFNoPUHT400_v5',
        #'HLT_Photon70_CaloIdXL_PFNoPUHT500_v5',
        #'HLT_Photon70_CaloIdXL_PFMET100_v8',
        #'HLT_Photon75_CaloIdVL_v14',
        #'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v6',
        #'HLT_Photon90_CaloIdVL_v11',
        #'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v6',
        #'HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25_v5',
        #'HLT_DisplacedPhoton65EBOnly_CaloIdVL_IsoL_PFMET30_v5',
        #'HLT_Photon135_v8',
        #'HLT_Photon150_v5',
        #'HLT_Photon160_v5',
        #'HLT_Photon300_NoHE_v6',
        #'HLT_DoublePhoton48_HEVT_v10',
        #'HLT_DoublePhoton53_HEVT_v4',
        #'HLT_DoublePhoton70_v7',
        #'HLT_DoublePhoton80_v8',
        #'HLT_L1SingleEG5_v6',
        #'HLT_L1SingleEG12_v6',
        #'HLT_L1DoubleEG3_FwdVeto_v2',
        #'HLT_L1ETM30_v2',
        #'HLT_L1ETM40_v2',
        #'HLT_L1ETM70_v2',
        #'HLT_L1ETM100_v2',
        #'HLT_Ele8_CaloIdT_TrkIdVL_v6',
        #'HLT_Ele8_CaloIdT_TrkIdVL_EG7_v3',
        #'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v8',
        #'HLT_Ele8_CaloIdL_CaloIsoVL_v18',
        #'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v16',
        #'HLT_Ele17_CaloIdL_CaloIsoVL_v18',
        #'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v7',
        #'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v20',
        #'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v7',
        #'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v8',
        #'HLT_Ele22_CaloIdL_CaloIsoVL_v7',
        #'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v12',
        #'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v9',
        #'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v9',
        #'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v9',
        #'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet30_v6',
        #'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet45_35_25_v4',
        #'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_TriCentralPFNoPUJet50_40_30_v6',
        'HLT_Ele27_WP80_v13',
        #'HLT_Ele27_WP80_PFMET_MT50_v9',
        'HLT_Ele30_CaloIdVT_TrkIdT_v7',
        'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v12',
        'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v7',
        'HLT_Ele80_CaloIdVT_GsfTrkIdT_v3',
        'HLT_Ele90_CaloIdVT_GsfTrkIdT_v3',
        'HLT_DoubleEle8_CaloIdT_TrkIdVL_v13',
        'HLT_DoubleEle33_CaloIdL_v15',
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v8',
        'HLT_DoubleEle33_CaloIdT_v11',
        'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v7',
        #'HLT_LooseIsoPFTau35_Trk20_Prong1_v11',
        #'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v11',
        #'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v11',
        #'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v11',
        #'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_L1ETM26_v2',
        #'HLT_IsoMu8_eta2p1_LooseIsoPFTau20_v2',
        #'HLT_Mu8_eta2p1_LooseIsoPFTau20_L1ETM26_v2',
        #'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_L1ETM36_v2',
        #'HLT_Ele13_eta2p1_WP90NoIso_LooseIsoPFTau20_L1ETM36_v2',
        #'HLT_Ele13_eta2p1_WP90Rho_LooseIsoPFTau20_v2',
        #'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v6',
        #'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_v5',
        #'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v5',
        #'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v5',
        #'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v5',
        #'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_Jet30_v2',
        #'HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Reg_v2',
        #'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_Reg_v2',
        #'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v2',
        #'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_Reg_v2',
        #'HLT_DoubleIsoL2Tau30_eta2p1_v1',
        #'HLT_BTagMu_DiJet20_Mu5_v7',
        #'HLT_BTagMu_DiJet40_Mu5_v7',
        #'HLT_BTagMu_DiJet70_Mu5_v7',
        #'HLT_BTagMu_DiJet110_Mu5_v7',
        #'HLT_BTagMu_Jet300_Mu5_v7',
        #'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v8',
        'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v10',
        #'HLT_Mu8_DiJet30_v8',
        #'HLT_Mu8_TriJet30_v8',
        #'HLT_Mu8_QuadJet30_v8',
        #'HLT_IsoMu12_DoubleCentralJet65_v5',
        #'HLT_Mu15_eta2p1_L1ETM20_v6',
        #'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_v2',
        #'HLT_IsoMu18_PFJet30_PFJet25_Deta3_v2',
        #'HLT_Mu18_CentralPFJet30_CentralPFJet25_v2',
        #'HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v2',
        #'HLT_IsoMu18_CentralPFJet30_CentralPFJet25_PFMET20_v2',
        #'HLT_IsoMu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v2',
        #'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v3',
        #'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v3',
        #'HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v3',
        #'HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v3',
        #'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v5',
        #'HLT_IsoMu17_eta2p1_CentralPFNoPUJet30_v5',
        #'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_v5',
        #'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet45_35_25_v3',
        #'HLT_IsoMu17_eta2p1_TriCentralPFNoPUJet30_v5',
        #'HLT_Mu17_eta2p1_CentralPFNoPUJet30_BTagIPIter_v5',
        #'HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v3',
        'HLT_IsoMu20_WCandPt80_v5',
        #'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v10',
        #'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v9',
        #'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v9',
        #'HLT_Mu12_eta2p1_DiCentral_40_20_v9',
        #'HLT_Mu12_eta2p1_DiCentral_20_v9',
        #'HLT_Mu15_eta2p1_DiCentral_40_20_v2',
        #'HLT_Mu15_eta2p1_DiCentral_20_v2',
        #'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v9',
        #'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v9',
        #'HLT_Mu15_eta2p1_TriCentral_40_20_20_v9',
        #'HLT_Mu30_Ele30_CaloIdL_v9',
        #'HLT_IsoMu17_eta2p1_DiCentralPFNoPUJet30_PFNoPUHT350_PFMHT40_v4',
        #'HLT_IsoMu20_eta2p1_CentralPFJet80_v10',
        #'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT175_v5',
        #'HLT_DoubleRelIso1p0Mu5_Mass8_PFNoPUHT225_v5',
        #'HLT_DoubleMu8_Mass8_PFNoPUHT175_v5',
        #'HLT_DoubleMu8_Mass8_PFNoPUHT225_v5',
        #'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v6',
        #'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v6',
        #'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v6',
        #'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v6',
        #'HLT_PFNoPUHT350_Mu15_PFMET45_v5',
        #'HLT_PFNoPUHT350_Mu15_PFMET50_v5',
        #'HLT_PFNoPUHT400_Mu5_PFMET45_v5',
        #'HLT_PFNoPUHT400_Mu5_PFMET50_v5',
        #'HLT_Mu40_PFNoPUHT350_v5',
        #'HLT_Mu60_PFNoPUHT350_v5',
        #'HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v17',
        #'HLT_DoubleMu_Ele8_CaloIdT_TrkIdVL_v6',
        #'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v8',
        #'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v19',
        #'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v19',
        #'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v19',
        #'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v8',
        #'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v10',
        #'HLT_Ele25_CaloIdVT_CaloIsoVL_TrkIdVL_TrkIsoT_DiCentralPFNoPUJet30_v4',
        #'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v11',
        #'HLT_Ele27_WP80_CentralPFJet80_v11',
        #'HLT_Ele27_WP80_WCandPt80_v11',
        #'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v9',
        #'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v9',
        #'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT175_v5',
        #'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFNoPUHT225_v5',
        #'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v13',
        #'HLT_TripleEle10_CaloIdL_TrkIdVL_v19',
        #'HLT_RsqMR40_Rsq0p04_v6',
        #'HLT_RsqMR45_Rsq0p09_v5',
        #'HLT_RsqMR55_Rsq0p09_MR150_v6',
        #'HLT_RsqMR60_Rsq0p09_MR150_v6',
        #'HLT_RsqMR65_Rsq0p09_MR150_v5',
        #'HLT_IsoMu12_RsqMR30_Rsq0p04_MR200_v5',
        #'HLT_IsoMu12_RsqMR40_Rsq0p04_MR200_v5',
        #'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v5',
        #'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v5',
        #'HLT_Ele12_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v5',
        #'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v7',
        #'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v7',
        #'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v7',
        #'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v7',
        #'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v7',
        #'HLT_Mu22_Photon22_CaloIdL_v8',
        #'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v8',
        #'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v8',
        #'HLT_DoubleMu14_Mass8_PFMET40_v9',
        #'HLT_DoubleMu14_Mass8_PFMET50_v9',
        #'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v9',
        #'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v9',
        #'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v9',
        #'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v9',
        #'HLT_PFNoPUHT350_PFMET100_v5',
        #'HLT_PFNoPUHT400_PFMET100_v5',
        #'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v4',
        #'HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v4',
        #'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v4',
        #'HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v4',
        #'HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v4',
        #'HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_TrkIdT_v4',
        #'HLT_Ele5_SC5_Jpsi_Mass2to15_v6',
        #'HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v1',
        #'HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v1',
        #'HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v5',
        #'HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v5',
        #'HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v5',
        #'HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v8',
        #'HLT_Ele22_eta2p1_WP90NoIso_LooseIsoPFTau20_v8',
        #'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v8',
        #'HLT_Mu17_eta2p1_LooseIsoPFTau20_v8',
        #'HLT_PixelTracks_Multiplicity70_v4',
        #'HLT_PixelTracks_Multiplicity80_v13',
        #'HLT_PixelTracks_Multiplicity90_v4',
        #'DST_HT250_v5',
        #'DST_L1HTT_Or_L1MultiJet_v4',
        #'DST_Mu5_HT250_v5',
        #'DST_Ele8_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT250_v6',
        #'HLT_BeamGas_HF_Beam1_v5',
        #'HLT_BeamGas_HF_Beam2_v5',
        #'HLT_BeamHalo_v13',
        #'HLT_HcalUTCA_v1',
        #'HLT_IsoTrackHE_v16',
        #'HLT_IsoTrackHB_v15',
        #'HLT_HcalPhiSym_v11',
        #'HLT_HcalNZS_v10',
        #'HLT_GlobalRunHPDNoise_v8',
        #'HLT_L1Tech_HBHEHO_totalOR_v6',
        #'HLT_L1Tech_HCAL_HF_single_channel_v4',
        #'HLT_ZeroBias_v7',
        #'HLT_ZeroBias_Parked_v1',
        #'HLT_ZeroBiasPixel_DoubleTrack_v2',
        #'HLT_Physics_v5',
        #'HLT_Physics_Parked_v1',
        #'DST_Physics_v5',
        #'HLT_DTCalibration_v2',
        #'HLT_EcalCalibration_v3',
        #'HLT_HcalCalibration_v3',
        #'HLT_TrackerCalibration_v3',
        #'HLT_Random_v2',
        #'HLT_L1SingleMuOpen_AntiBPTX_v7',
        #'HLT_L1TrackerCosmics_v7',
        #'HLT_DTErrors_v3',
        #'HLT_L1DoubleJet36Central_v7',
        #'AlCa_EcalPi0EBonly_v6',
        #'AlCa_EcalPi0EEonly_v6',
        #'AlCa_EcalEtaEBonly_v6',
        #'AlCa_EcalEtaEEonly_v6',
        #'AlCa_EcalPhiSym_v13',
        #'AlCa_RPCMuonNoTriggers_v9',
        #'AlCa_RPCMuonNoHits_v9',
        #'AlCa_RPCMuonNormalisation_v9',
        #'AlCa_LumiPixels_v8',
        #'AlCa_LumiPixels_ZeroBias_v4',
        #'AlCa_LumiPixels_Random_v1',
        #'DQM_FEDIntegrity_v11',
        #'HLT_LogMonitor_v4',
        #'HLTriggerFinalPath',
        #'raw2digi_step',
        #'L1Reco_step',
        ])
