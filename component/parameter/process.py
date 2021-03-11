###################
##      acc      ##
###################
connectivity = [8, 4]
acc_options = [
    {'value':'default', 'text': "stats + image of viewport" },
    {'value':'detailed', 'text': 'stats + images of ID, area, viewport'}
]

####################
##      dist      ##
####################
dist_options = [
    {'text': 'Euclidian distance only', 'value': 1},
    {'text': 'Euclidian distance + Hysometric Curve', 'value': 2}
]

###################
##      fad      ##
###################
fad_options = [
    {'text': 'per-pixel density, color-coded into 6 fragmentation classes', 'value': 'FAD'},
    {'text': 'average per-patch density, color-coded into 2 classes', 'value': 'FAD-APP2'},
    {'text': 'average per-patch density, color-coded into 5 classes', 'value': 'FAD-APP5'}
]

prescision = [
    {'text': "float precision (require more disk space)", 'value': 1},
    {'text': 'rounded byte', 'value': 0}
]

####################
##      p222      ##
####################
algo = [
    {'text': 'P2: Foreground Density (%)', 'value': 1},
    {'text': 'P22: Foreground Contagion (%)', 'value': 2}
]

###################
##      spa      ##
###################
spa_options = [
    {'text': 'Small & linear features (SLF), Coherent', 'value': 2},
    {'text': 'Core, Core-Openings, Margin', 'value': 3},
    {'text': 'Core, Core-Openings, Edge, Perforation, Margin', 'value': 5},
    {'text': 'Core, Core-Openings, Edge, Perforation, Islet, Margin', 'value': 6}
]