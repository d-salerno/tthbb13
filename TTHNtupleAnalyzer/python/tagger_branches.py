#sample branches file for headergen.py
#uses branch classes from headergen
from TTH.TTHNtupleAnalyzer.headergen import *

defines = ["#define ADD_TRUE_TOP_MATCHING_FOR_FJ 1",
           "#define ADD_TRUE_TOP_MATCHING_FOR_HTT 1"
           ]

#define branches to add here
process = [
	Scalar("gen_t__dpt_alt", "float"),
	Scalar("gen_tbar__dpt_alt", "float"),
]

# True Top Branches
for t in ["t", "tbar", "t2", "tbar2"]:
    for v in [
        ("eta"), ("mass"), ("phi"), ("pt"), ("status"),
        ("b__eta"), ("b__mass"), ("b__phi"), ("b__pt"), ("b__status"),
        ("w_d1__eta"), ("w_d1__mass"), ("w_d1__phi"), ("w_d1__pt"), ("w_d1__status"), ("w_d1__id"),
        ("w_d2__eta"), ("w_d2__mass"), ("w_d2__phi"), ("w_d2__pt"), ("w_d2__status"), ("w_d2__id")
    ]:
        typ = "float"
        if "status" in v or "id" in v:
            typ = "int"
        process += [Scalar("gen_%s__%s" % (t, v), typ)]

# Fatjet Branches
for fj_name in ["ca08", "ca08filtered", "ca08pruned", "ca08trimmed", 
                "ca15", "ca15filtered", "ca15pruned", "ca15trimmed"]:

    # How many of these objects do we have?
    full_counter_name = "n__jet_{0}".format(fj_name)
    process += [Scalar(full_counter_name, "int")]

    # And all the individual float branches
    for branch_name in [
            "pt", "eta", "phi", "mass",  # Kinematics
            "tau1", "tau2", "tau3",      # N-subjettiness
            "close_hadtop_pt",  "close_hadtop_dr" # truth matching
            ]:

        full_branch_name = "jet_{0}__{1}".format(fj_name, branch_name)
        process += [Dynamic1DArray(full_branch_name, 
                                   "float",
                                   full_counter_name,
                                   "N_MAX"
                               )]

    # End of loop over branches
# End of loop over fat jets


# HEPTopTagger Branches
htt_float_branches =  [
    "pt", "mass", "eta", "phi", "energy",       # Kinematics
    "fj_pt", "fj_mass", "fj_eta", "fj_phi",     # Original Fat-jet kinematics
    "fW", "massRatioPassed",                    # Standard HTT variables 
    "Rmin", "ptFiltForRminExp", "RminExpected", # MultiR variables
    "prunedMass", "topMass", "unfilteredMass",  # extra masses
    "close_hadtop_pt",  "close_hadtop_dr"       # truth matching
]

htt_int_branches = ["child_idx", "isMultiR", "n_sj"]

htt_sj_float_branches =  ["energy", "eta", "mass", "phi", "pt"]

htt_sj_int_branches =  ["parent_idx"]

for htt_name in ["looseMultiRHTT"]:

    # How many objects do we have?
    tagger_counter_name = "n__jet_{0}".format(htt_name)
    sj_counter_name = "n__jet_{0}_sj".format(htt_name)
    process += [Scalar(tagger_counter_name, "int")]
    process += [Scalar(sj_counter_name, "int")]

    # Float branches: One per tagger candidate
    for branch_name in htt_float_branches:
        full_branch_name = "jet_{0}__{1}".format(htt_name, branch_name)
        process += [Dynamic1DArray(full_branch_name, "float", tagger_counter_name, "N_MAX")]

    # Int branches: One per tagger candidate
    for branch_name in htt_int_branches:
        full_branch_name = "jet_{0}__{1}".format(htt_name, branch_name)
        process += [Dynamic1DArray(full_branch_name, "int", tagger_counter_name, "N_MAX")]

    # Float branches: One per tagger subjet
    for branch_name in htt_sj_float_branches:
        full_branch_name = "jet_{0}_sj__{1}".format(htt_name, branch_name)
        process += [Dynamic1DArray(full_branch_name, "float", sj_counter_name, "N_MAX")]

    # Int branches: One per tagger subjet
    for branch_name in htt_sj_int_branches:
        full_branch_name = "jet_{0}_sj__{1}".format(htt_name, branch_name)
        process += [Dynamic1DArray(full_branch_name, "int", sj_counter_name, "N_MAX")]

# End of loop over heptoptaggers
