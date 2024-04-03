EXP_NAME = "cmplx"
RUN_NAME = "cmplx_1"

###########################
# ITERATIONS
ITERS = 5
SEED_ADDL=13
N = [400]
PLOT_ALL=True
###########################

# comp_1
SPLIT_RULES1 =  [
    "pmb.ContinuousSplitRule()", # time
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
]
MODEL_DICT1 = {"trees": 10,
	"split_rules": SPLIT_RULES1
}
SAMPLER_DICT1 = {
	"draws": 10,
	"tune": 10,
	"cores": 4,
	"chains": 4,
	"compute_convergence_checks": False,
	# "pgbart": {"num_particles":10}
}


###########################
# Comp2
SPLIT_RULES2 =  [
    "pmb.ContinuousSplitRule()", # time
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
	"pmb.OneHotSplitRule()",
]
MODEL_DICT2 = {"trees": 25,
	"split_rules": SPLIT_RULES1
}
SAMPLER_DICT2 = {
	"draws": 500,
	"tune": 100,
	"cores": 4,
	"chains": 4,
	"compute_convergence_checks": False
}

# comp 3
SPLIT_RULES3 =  [
    "pmb.ContinuousSplitRule()", # time
    "pmb.ContinuousSplitRule()", 
 	"pmb.ContinuousSplitRule()",
  	"pmb.ContinuousSplitRule()",
  	"pmb.ContinuousSplitRule()",
	"pmb.ContinuousSplitRule()",
	"pmb.ContinuousSplitRule()",
	"pmb.ContinuousSplitRule()",
	# "pmb.ContinuousSplitRule()",
 	# "pmb.ContinuousSplitRule()",
  	# "pmb.ContinuousSplitRule()"
]
MODEL_DICT3 = {"trees": 100,
	"split_rules": SPLIT_RULES1
}
SAMPLER_DICT3 = {
	"draws": 300,
	"tune": 50,
	"cores": 5,
	"chains": 5,
	"compute_convergence_checks": False
}


