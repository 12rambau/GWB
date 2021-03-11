# if you only have few io a module is not necessary and you can simply use a scripts.py file 
# in a big module with lot of io, it can make sense to split things in separate for the sake of maintenance

# if you use a module import all the functions here to only have 1 call to make
from .acc_io import *
from .dist_io import *
from .fad_io import *
from .frag_io import *
from .lm_io import *
from .mspa_io import *
from .p223_io import *
from .parc_io import *
from .rss_io import *
from .spa_io import *
from .rec_io import *