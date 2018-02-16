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








































# # FIGURA 4

# dados2009 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2009'), 24, 3)
# dados2010 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2010'), 24, 3)
# dados2011 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2011'), 24, 3)
# dados2012 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2012'), 24, 3)
# dados2013 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2013'), 24, 3)
# dados2014 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2014'), 24, 3)
# dados2015 = cdf(read_numbers('tempo_duracao_falhas/tempoRec2015'), 24, 3)

# data_lines = [
# 	{'legend': '2010', 'color': 'blue',   'marker': 'v', 'data': dados2010},
# 	{'legend': '2012', 'color': 'green',  'marker': '^', 'data': dados2012},
# 	{'legend': '2014', 'color': 'red',    'marker': '<', 'data': dados2014},
# 	{'legend': '2015', 'color': 'black',  'marker': 's', 'data': dados2015}
# ]
# cdf_plot(data_lines, 'Tempo de solução (horas)', 'Fração acumulada de incidentes', [0, 24], '1_tempo_duracao_falhas.pdf')

# dados2009 = cdf(read_numbers('tempo_rec_campo/tempoCampo2009'), 24, 3)
# dados2010 = cdf(read_numbers('tempo_rec_campo/tempoCampo2010'), 24, 3)
# dados2011 = cdf(read_numbers('tempo_rec_campo/tempoCampo2011'), 24, 3)
# dados2012 = cdf(read_numbers('tempo_rec_campo/tempoCampo2012'), 24, 3)
# dados2013 = cdf(read_numbers('tempo_rec_campo/tempoCampo2013'), 24, 3)
# dados2014 = cdf(read_numbers('tempo_rec_campo/tempoCampo2014'), 24, 3)
# dados2015 = cdf(read_numbers('tempo_rec_campo/tempoCampo2015'), 24, 3)

# data_lines = [
# 	{'legend': '2010', 'color': 'blue',   'marker': 'v', 'data': dados2010},
# 	{'legend': '2012', 'color': 'green',  'marker': '^', 'data': dados2012},
# 	{'legend': '2014', 'color': 'red',    'marker': '<', 'data': dados2014},
# 	{'legend': '2015', 'color': 'black',  'marker': 's', 'data': dados2015}
# ]
# cdf_plot(data_lines, 'Tempo de trabalho em campo (horas)', 'Fração acumulada de incidentes', [0, 24], '2_tempo_rec_campo.pdf')

# dados2009 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2009'), 360, 40)
# dados2010 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2010'), 360, 40)
# dados2011 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2011'), 360, 40)
# dados2012 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2012'), 360, 40)
# dados2013 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2013'), 360, 40)
# dados2014 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2014'), 360, 40)
# dados2015 = cdf(read_numbers('tempo_entre_falhas_consecutivas/tp2015'), 360, 40)

# data_lines = [
# 	{'legend': '2010', 'color': 'blue',   'marker': 'v', 'data': dados2010},
# 	{'legend': '2012', 'color': 'green',  'marker': '^', 'data': dados2012},
# 	{'legend': '2014', 'color': 'red',    'marker': '<', 'data': dados2014},
# 	{'legend': '2015', 'color': 'black',  'marker': 's', 'data': dados2015}
# ]
# cdf_plot(data_lines, 'Tempo entre incidentes (dias)', 'Fração acumulada de enlaces', [0, 360], '3_tempo_entre_falhas_consecutivas.pdf')

# dados2009 = cdf(read_numbers('4c_new/tp2009M'), 360, 40)
# dados2010 = cdf(read_numbers('4c_new/tp2010M'), 360, 40)
# dados2011 = cdf(read_numbers('4c_new/tp2011M'), 360, 40)
# dados2012 = cdf(read_numbers('4c_new/tp2012M'), 360, 40)
# dados2013 = cdf(read_numbers('4c_new/tp2013M'), 360, 40)
# dados2014 = cdf(read_numbers('4c_new/tp2014M'), 360, 40)
# dados2015 = cdf(read_numbers('4c_new/tp2015M'), 360, 40)

# data_lines = [
# 	{'legend': '2010', 'color': 'blue',   'marker': 'v', 'data': dados2010},
# 	{'legend': '2012', 'color': 'green',  'marker': '^', 'data': dados2012},
# 	{'legend': '2014', 'color': 'red',    'marker': '<', 'data': dados2014},
# 	{'legend': '2015', 'color': 'black',  'marker': 's', 'data': dados2015}
# ]
# cdf_plot(data_lines, 'Tempo entre incidentes (dias)', 'Fração acumulada de enlaces', [0, 360], '3_nova_tempo_entre_falhas_consecutivas.pdf')





















# FIGURA 6
dados1 = cdf(read_numbers('tempo_recuperacao_capital_interior/recuperacaoCapital'), 24, 3)
dados2 = cdf(read_numbers('tempo_recuperacao_capital_interior/recuperacaoInterior'), 24, 3)

data_lines = [
	{'legend': 'Capital', 'color': 'blue', 'marker': 'v', 'data': dados1},
	{'legend': 'Interior', 'color': 'red', 'marker': '^', 'data': dados2}
]
cdf_plot(data_lines, 'Tempo de solução (horas)', 'Fração acumulada de incidentes', [0, 24], '1_tempo_recuperacao_capital_interior.pdf', [0, 1])


























# FIGURA 5 (TEC)

dados1 = cdf(read_numbers('tempo_total_de_recuperacao_tec/DuracaoGPON'), 24, 3)
dados2 = cdf(read_numbers('tempo_total_de_recuperacao_tec/DuracaoMETRO'), 24, 3)
dados3 = cdf(read_numbers('tempo_total_de_recuperacao_tec/DuracaoSDH'), 24, 3)

data_lines = [
	{'legend': 'GPON',  'color': 'blue',  'marker': 'v', 'data': dados1},
	{'legend': 'METRO', 'color': 'green', 'marker': '^', 'data': dados2},
	{'legend': 'SDH',   'color': 'red',   'marker': 'o', 'data': dados3}
]
cdf_plot(data_lines, 'Tempo para recuperação (horas)', 'Fração acumulada de incidentes', [0, 24], 'tec_1_tempo_total_recuperacao.pdf')

dados1 = cdf(read_numbers('tempo_rec_em_campo_tec/escGPON'), 24, 3)
dados2 = cdf(read_numbers('tempo_rec_em_campo_tec/escMETRO'), 24, 3)
dados3 = cdf(read_numbers('tempo_rec_em_campo_tec/escSDH'), 24, 3)

data_lines = [
	{'legend': 'GPON',  'color': 'blue',  'marker': 'v', 'data': dados1},
	{'legend': 'METRO', 'color': 'green', 'marker': '^', 'data': dados2},
	{'legend': 'SDH',   'color': 'red',   'marker': 'o', 'data': dados3}
]
cdf_plot(data_lines, 'Tempo para recuperação (horas)', 'Fração acumulada de incidentes', [0, 24], 'tec_2_tempo_recuperacao_campo.pdf')

dados1 = cdf(read_numbers('tempo_entre_falhas_tec/diasEntreFalhasGPON'), 360, 40)
dados2 = cdf(read_numbers('tempo_entre_falhas_tec/diasEntreFalhasMETRO'), 360, 40)
dados3 = cdf(read_numbers('tempo_entre_falhas_tec/diasEntreFalhasSDH'), 360, 40)

data_lines = [
	{'legend': 'GPON',  'color': 'blue',  'marker': 'v', 'data': dados1},
	{'legend': 'METRO', 'color': 'green', 'marker': '^', 'data': dados2},
	{'legend': 'SDH',   'color': 'red',   'marker': 'o', 'data': dados3}
]
cdf_plot(data_lines, 'Tempo para recuperação (dias)', 'Fração acumulada de enlaces', [0, 360], 'tec_3_tempo_entre_falhas.pdf')


























































# dados2 = cdf(read_numbers('tempo_entre_falhas_dias/diasEntreFalhasGPON'), 100)
# dados3 = cdf(read_numbers('tempo_entre_falhas_dias/diasEntreFalhasMETRO'), 100)
# dados4 = cdf(read_numbers('tempo_entre_falhas_dias/diasEntreFalhasSDH'), 100)

# data_lines = [
# 	{'legend': '2010', 'color': 'blue',   'marker': 'v', 'data': dados2},
# 	{'legend': '2011', 'color': 'red',    'marker': '^', 'data': dados3},
# 	{'legend': '2012', 'color': 'green',  'marker': 'o', 'data': dados4}
# ]
# cdf_plot(data_lines, 'Tempo para recuperação (horas)', 'Fração acumulada de incidentes', [0, 100], 'tempo_entre_falhas_dias.pdf')






























# dados2 = cdf(read_numbers('tempo_entre_falhas_consecutivas_capital_interior/T_E_F_Interior'), 13)
# dados3 = cdf(read_numbers('tempo_entre_falhas_consecutivas_capital_interior/T_E_F_RMBH'), 13)

# data_lines = [
# 	{'legend': 'Interior', 'color': 'blue', 'marker': '.', 'data': dados2},
# 	{'legend': 'Capital', 'color': 'red',  'marker': '.', 'data': dados3}
# ]
# cdf_plot(data_lines, 'Tempo para recuperação (horas)', 'Fração acumulada de incidentes', [0, 13], 'tempo_entre_falhas_consecutivas_capital_interior.pdf')

# dados2 = cdf(read_numbers('taxa_falhas_anuais/interiorComZeros'), 10)
# dados3 = cdf(read_numbers('taxa_falhas_anuais/RMBHComZeros'), 10)

# data_lines = [
# 	{'legend': '2010', 'color': 'blue',   'marker': 'v', 'data': dados2},
# 	{'legend': '2011', 'color': 'red',    'marker': '^', 'data': dados3}
# ]
# cdf_plot(data_lines, 'Tempo para recuperação (horas)', 'Fração acumulada de incidentes', [0, 10], 'taxa_falhas_anuais.pdf')