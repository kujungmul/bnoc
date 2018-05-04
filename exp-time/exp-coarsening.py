import os

cset = ['rm', 'hem', 'lem']
rset = [0.1, 0.2, 0.3, 0.4, 0.5]
mset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 'result/'

for index, v in enumerate(range(1000, 4000, 1000)):
	v1 = (v / 2)
	v2 = (v / 2)
	f = 'dataset/' + str(index + 1) + '.ncol'
	for c in cset:
		for m in mset:
			for r in rset:
				o = c + '_' + str(v) + '_' + str(r).replace('.', '')
				print('python ../../opm/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')
				os.system('python ../../opm/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')

cset = ['greedy_twohops', 'greedy_seed_twohops']
rset = [0.1, 0.2, 0.3, 0.4, 0.5]
mset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 'result/'

for index, v in enumerate(range(1000, 4000, 1000)):
	v1 = (v / 2)
	v2 = (v / 2)
	f = 'dataset/' + str(index + 1) + '.ncol'
	for c in cset:
		for m in mset:
			for r in rset:
				o = c + '_' + str(v) + '_' + str(r).replace('.', '')
				print('python ../../mob/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')
				os.system('python ../../mob/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')

cset = ['greedy_seed_modularity']
rset = [0.1, 0.2, 0.3, 0.4, 0.5]
mset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 'result/'

for index, v in enumerate(range(1000, 4000, 1000)):
	v1 = (v / 2)
	v2 = (v / 2)
	f = 'dataset/' + str(index + 1) + '.ncol'
	for c in cset:
		for m in mset:
			for r in rset:
				o = c + '_' + str(v) + '_' + str(r).replace('.', '')
				print('python ../../mob_exp/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')
				os.system('python ../../mob_exp/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')

cset = ['greedy_seed_modularity_group', 'lpa_modularity']
rset = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
mset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 'result/'

for index, v in enumerate(range(1000, 4000, 1000)):
	v1 = (v / 2)
	v2 = (v / 2)
	f = 'dataset/' + str(index + 1) + '.ncol'
	for c in cset:
		for m in mset:
			for r in rset:
				o = c + '_' + str(v) + '_' + str(r).replace('.', '')
				print('python ../../mob_exp/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')
				os.system('python ../../mob_exp/coarsening.py -f ' + f + ' -v ' + str(v1) + ' ' + str(v2) + ' -c ' + str(c) + ' -m ' + str(m) + ' -r ' + str(r) + ' -d ' + str(d) + ' -o ' + str(o) + ' --save_timing_json')

