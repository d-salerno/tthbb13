from TTH.MEAnalysis.vhbb_utils import lvec
import copy
import numpy as np

import math
import scipy
import scipy.special
from scipy.special import eval_legendre

#for some reason, root imports need to be after scipy
import ROOT
ROOT.gSystem.Load("libTTHMEAnalysis")

mva_enabled = False
from TTH.MEAnalysis.Analyzer import FilterAnalyzer
if mva_enabled:
    try:
        from sklearn.externals import joblib
    except Exception as e:
        print "Could not load scikit-learn. Please configure PYTHONPATH=/path/to/anaconda/lib/python2.7/site-packages:$PYTHONPATH PATH=/path/to/anaconda/bin/:$PATH"
        mva_enabled = False

CvectorTLorentzVector = getattr(ROOT, "std::vector<TLorentzVector>")
EventShapeVariables = getattr(ROOT, "EventShapeVariables")
TMatrixDSym = getattr(ROOT, "TMatrixDSym")
TMatrixDSymEigen = getattr(ROOT, "TMatrixDSymEigen")

class FoxWolfram:

    @staticmethod
    def w_s(objs, lv1, lv2):
        return (lv1.Vect().Mag() * lv2.Vect().Mag()) / (sum(objs, ROOT.TLorentzVector())).Mag2()

    @staticmethod
    def calcFoxWolfram(objects, orders, weight_func):
        """
        http://arxiv.org/pdf/1212.4436v1.pdf
        """
        lvecs = [lvec(o) for o in objects]

        h = np.zeros(len(orders))
        for i in range(len(lvecs)):
            for j in range(len(lvecs)):
                cos_omega_ij = (lvecs[i].CosTheta() * lvecs[j].CosTheta() +
                    math.sqrt((1.0 - lvecs[i].CosTheta()**2) * (1.0 - lvecs[j].CosTheta()**2)) *
                    (math.cos(lvecs[i].Phi() - lvecs[j].Phi()))
                )
                w_ij = weight_func(lvecs, lvecs[i], lvecs[j])
                vals = np.array([cos_omega_ij]*len(orders))

                p_l = np.array(eval_legendre(orders, vals))
                h += w_ij * p_l
        return h

class MVAVarAnalyzer(FilterAnalyzer):
    """
    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        self.conf = cfg_ana._conf
        super(MVAVarAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)

        if mva_enabled:
            self.cls = joblib.load(self.conf.tth_mva["filename"])

    def beginLoop(self, setup):
        super(MVAVarAnalyzer, self).beginLoop(setup)

    def process(self, event):
        for (syst, event_syst) in event.systResults.items():
            #print syst, event_syst.__dict__
            if event_syst.passes_btag:
                res = self._process(event_syst)
                event.systResults[syst] = res
            else:
                event.systResults[syst].passes_mva = False
        return self.conf.general["passall"] or np.any([v.passes_mva for v in event.systResults.values()])

    def _process(self, event):
        #FIXME: NEED COMMENTS HERE
        sumP2 = 0.0
        sumPxx = 0.0
        sumPxy = 0.0
        sumPxz = 0.0
        sumPyy = 0.0
        sumPyz = 0.0
        sumPzz = 0.0
        vecs = CvectorTLorentzVector()
        for jet in event.good_jets:
            obj = lvec(jet)
            vecs.push_back(lvec(jet))
            sumP2  += obj.P() * obj.P()
            sumPxx += obj.Px() * obj.Px()
            sumPxy += obj.Px() * obj.Py()
            sumPxz += obj.Px() * obj.Pz()
            sumPyy += obj.Py() * obj.Py()
            sumPyz += obj.Py() * obj.Pz()
            sumPzz += obj.Pz() * obj.Pz()
        evshape = EventShapeVariables(vecs)
        eigs = evshape.compEigenValues(2.0) #difference: this takes T^2-x^2-y^2-z^2 for P2
        event.momentum_eig0 = eigs[0]
        event.momentum_eig1 = eigs[1]
        event.momentum_eig2 = eigs[2]
        
        ##---- compute sphericity --------------------#DS
        Txx = sumPxx/sumP2
        Tyy = sumPyy/sumP2
        Tzz = sumPzz/sumP2
        Txy = sumPxy/sumP2
        Txz = sumPxz/sumP2
        Tyz = sumPyz/sumP2
        T = TMatrixDSym(3)
        T[0,0] = Txx
        T[0,1] = Txy
        T[0,2] = Txz
        T[1,0] = Txy
        T[1,1] = Tyy
        T[1,2] = Tyz
        T[2,0] = Txz
        T[2,1] = Tyz
        T[2,2] = Tzz
        TEigen = TMatrixDSymEigen(T)
        eigenValues = TEigen.GetEigenValues()
        event.sphericity = 1.5*(eigenValues(1)+eigenValues(2))
        event.aplanarity = 1.5*eigenValues(2)
        event.C = 3.0*(eigenValues(0)*eigenValues(1) + eigenValues(0)*eigenValues(2) + eigenValues(1)*eigenValues(2))
        event.D = 27.*eigenValues(0)*eigenValues(1)*eigenValues(2) #---------DS 

        event.isotropy = evshape.isotropy()

        event.mean_bdisc = np.mean([j.btagCSV for j in event.good_jets])
        event.mean_bdisc_btag = np.mean([j.btagCSV for j in event.selected_btagged_jets])
        event.std_bdisc = np.std([j.btagCSV for j in event.good_jets])
        event.std_bdisc_btag = np.std([j.btagCSV for j in event.selected_btagged_jets])
        drs = []
        for j1 in event.selected_btagged_jets:
            for j2 in event.selected_btagged_jets:
                if j1==j2:
                    continue
                l1 = lvec(j1)
                l2 = lvec(j2)
                drs += [(l1.DeltaR(l2), l1, l2)]
        drs = sorted(drs, key=lambda x: x[0])
        if len(drs)>0:
            lv = drs[0][1] + drs[0][2]
            event.mass_drpair_btag = lv.M()
            event.eta_drpair_btag = abs(lv.Eta())
            event.pt_drpair_btag = lv.Pt()
            event.min_dr_btag = drs[0][0]
            event.mean_dr_btag = np.mean([dr[0] for dr in drs], -1)
            event.std_dr_btag = np.std([dr[0] for dr in drs], -1)
        else:
            event.min_dr_btag = -1.0
            event.mean_dr_btag = -1.0
            event.std_dr_btag = -1.0
            event.mass_drpair_btag = -1.0
            event.eta_drpair_btag = -99
            event.pt_drpair_btag = -1.0

        for i in range(min(4, len(event.selected_btagged_jets_high))):
            setattr(event, "jet_btag_{0}".format(i), event.selected_btagged_jets_high[i])

        event.ht = np.sum([j.pt for j in event.good_jets])
        lvecs = [lvec(x) for x in event.good_jets + event.good_leptons]
        event.centrality = np.sum([l.Pt() / l.E() for l in lvecs])

        #orders of momenta to calculate
        orders = np.array([0, 1, 2, 3, 4, 5, 6, 7])
        event.fw_h_alljets = FoxWolfram.calcFoxWolfram(event.good_jets, orders, FoxWolfram.w_s)
        event.fw_h_btagjets = FoxWolfram.calcFoxWolfram(event.selected_btagged_jets_high, orders, FoxWolfram.w_s)
        event.fw_h_untagjets = FoxWolfram.calcFoxWolfram(event.buntagged_jets, orders, FoxWolfram.w_s)
        
        for ij in range(6):
            setattr(event, "jet{0}_pt".format(ij), 0)
            setattr(event, "jet{0}_aeta".format(ij), 0)
            setattr(event, "jet{0}_btag".format(ij), 0)

        for ij, jet in enumerate(event.good_jets):
            setattr(event, "jet{0}_pt".format(ij), jet.pt)
            setattr(event, "jet{0}_aeta".format(ij), abs(jet.eta))
            setattr(event, "jet{0}_btag".format(ij), jet.btagCSV)
       
        for i in range(2):
            setattr(event, "lep{0}_pt".format(i), 0.0)
            setattr(event, "lep{0}_aeta".format(i), 0.0)

        for ij, lep in enumerate(event.good_leptons):
            setattr(event, "lep{0}_pt".format(ij), lep.pt)
            setattr(event, "lep{0}_aeta".format(ij), abs(lep.eta))
        
        for io in orders:
            setattr(event, "fw_h{0}".format(io), event.fw_h_alljets[io])
        
        vararray = np.array([getattr(event, vname) for vname in self.conf.tth_mva["varlist"]])
        vararray[np.isnan(vararray)] = 0
        
        event.tth_mva = 0
        if mva_enabled:
            event.tth_mva = self.cls.predict_proba(vararray)[0,1]
        event.passes_mva = True

        return event
