from extract import from_tsv_get, hist, hists
from config import smoothing_value
from operator import mul

def expected_value(line ,m, dicm, dicm1):
	mgram = [tuple(line[i:i+m]) for i in range(len(line)-m+1)]
	m1gram = [tuple(line[i:i+m+1]) for i in range(len(line)-m)]

	total = float(dicm.get(mgram[0], smoothing_value)) / sum(dicm.itervalues())

	if len(line) == m:
		return total

	total *=  float(reduce(mul,[dicm1.get(i, smoothing_value) for i in m1gram])) / \
					reduce(mul,[dicm.get(i, smoothing_value) for i in mgram][:-1])

	return total



if __name__=="__main__":
	train, test = from_tsv_get("data/data.tsv", "\t", 'Search term', 'Added/Excluded', 'Conv. (1-per-click)')

	m = 2
	rel_hist, non_rel_hist = hists(train, m)
	rel_histm1, non_rel_histm1 = hists(train, m+1)


	tot_freq_rel = sum(rel_hist.itervalues())
	tot_freq_non_rel = sum(non_rel_hist.itervalues())
	
	print tot_freq_non_rel


	print expected_value("how to create social".split(), m, non_rel_hist, non_rel_histm1)

