convert = {
    0: {
        'label': [],
        'io': []
    },
    4: {
        'label': [
            'background',
            'foreground',
            'special background 1 (optional)',
            'special background 2 (optional)'
        ],
        'io': [
            'background',
            'foreground',
            'spe_background_1',
            'spe_background_2'
        ]
    },
    2: {
        'label': [
            'background',
            'foreground'
        ],
        'io': [
            'background',
            'foreground'
        ]
    },
    3: {
        'label': [
            'Dominant land cover 1 (Agriculture)',
            'Dominant land cover 2 (Natural)',
            'Dominant land cover 3 (Developed)'
        ],
        'io': [
            'lc_1',
            'lc_2',
            'lc_3'
        ]
    },
    5: { # there is no 5 class based module, it's just that the p223 module make too many different things and is not build on the same structure as the others
        'label': [
            'background',
            'foreground',
            'special background'
        ],
        'io': [
            'background',
            'foreground',
            'spe_background'
        ]
    }
}