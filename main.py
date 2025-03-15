import sys
import os
from format.integrate import integration 

lang = sys.argv[1]
arch = sys.argv[2]

integration(lang=lang, arch=arch)
