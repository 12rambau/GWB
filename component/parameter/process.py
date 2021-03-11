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
    {'text': 'FG-Density (FG-masked and normalised)', 'value': 1},
    {'text': 'FG-Contagion (FG-masked and normalised)', 'value': 2},
    {'text': 'FG-Adjacency (FG-masked and normalised)', 'value': 3},
    {'text': 'FG-Density (original spatcon output)', 'value': 11},
    {'text': 'FG-Contagion (original spatcon output)', 'value': 12},
    {'text': 'FG-Adjacency (original spatcon output)', 'value': 13},
    {'text': 'FG-Shannon (original spatcon output)', 'value': 14},
    {'text': 'FG-SumD (original spatcon output)', 'value': 15}
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