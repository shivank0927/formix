import sys, os , argparse, json
from utility.integrate import integration 
from utility.checker import verify

# to be uncommented later for now no.
# lang = sys.argv[1]
# arch = sys.argv[2] 

lang = "lua"
arch = "cli tool mini"

language = verify(language=lang)

if not language:
    sys.exit("language does not exit/ incorrect language")
    
response  = integration(lang=language, arch=arch)


print(response)
response = json.loads(response)
print(type(response))
print("\n")
print(response)

for dict_key in response:
    if dict_key == "LICENSE" or dict_key == "README.md": 
        with open(f"tests/{dict_key}", "w") as file: # remove tests/ later
            pass 
    else:
        os.mkdir(f"tests/{dict_key}")  # rm tests/ later.