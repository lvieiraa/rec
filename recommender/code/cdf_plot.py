# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def read_numbers(filename):
	content = []
	with open(filename) as f:
		for l in f:
			n =  float(l.strip('\n').strip('\r'))
			content.append(n)
	return content

def cdf(data, max_range, salto=1):
	total_points = len(data)

	values_x = range(0, max_range+1)
	values_x = []
	values_y = []

	t = 0
	while t<=max_range:
		values_x.append(t)
		t += salto

	for x in values_x:
		cumulative = 0
		for d in data:
			if d<=x:
				cumulative += 1
		values_y.append(cumulative/float(total_points))

	return [values_x, values_y]

def cdf_plot(data_lines, xlabel, ylabel, xlim, filename, ylim=[]):

	use_step = False
	markersize = 12
	linewidth = 2

	fig, ax = plt.subplots()

	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	# Plota as linhas
	lines = []
	for l in data_lines:
		lstyle = l['linestyle'] if 'linestyle' in l else '-'
		mark = l['marker'] if 'marker' in l else 'o'
		cdf_data = l['data']
		if use_step:
			line_plot, = plt.step(cdf_data[0], cdf_data[1], linestyle=lstyle, marker=mark, color=l['color'], where='post', markersize=markersize, markeredgewidth=1, markeredgecolor=l['color'])
		else:
			line_plot, = plt.plot(cdf_data[0], cdf_data[1], linestyle=lstyle, marker=mark, color=l['color'], markersize=markersize, markeredgewidth=1, markeredgecolor=l['color'])
		plt.setp(line_plot, linewidth=linewidth)
		lines.append(line_plot)

	# Adiciona a legenda
	legendas = [l['legend'] for l in data_lines]
	plt.legend(lines, legendas, loc='lower right')

	# Define os limites
	plt.xlim(xlim[0], xlim[1])
	if ylim!=[]:
		plt.ylim(ylim[0], ylim[1])
	else:
		plt.ylim(0)

	plt.rcParams.update({'font.size': 22}) # tamanho da fonte
	ax.yaxis.grid(True) # usa grids
	ax.xaxis.set_major_locator(MaxNLocator(integer=True))
	# plt.grid(color='gray', linestyle='--')

	# plt.show()
	# exit()
	plt.savefig(filename, bbox_inches='tight', format='pdf', dpi=1000)



# FIGURA 6
dados1 = cdf(read_numbers('../statistics/nParticipantes'), 5000, 3)
data_lines = [
	{'legend': 'Pessoas', 'color': 'blue', 'marker': 'v', 'data': dados1},
]
cdf_plot(data_lines, 'Eventos', 'Fração acumulada de participantes', [0, 1000], 'nPessoas.pdf', [0, 1])
