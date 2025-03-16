import sys, os , argparse, json
from utility.integrate import integration 
from utility.checker import verify

# to be uncommented later
# lang = sys.argv[1]
# arch = sys.argv[2] 

lang = "lua"
arch = "cli tool mini"

os.mkdir("tests")

if not verify(language=lang):
    sys.exit("language does not exit/ incorrect language")
    
response  = integration(language=lang, architecture=arch)
response = json.loads(response)

for i in response.keys():
    
    if not i:
        sys.exit("error")
        
    print(i)

for key in response.keys():
    
    if key == "LICENSE" or key == "README.md": 
        with open(f"tests/{key}", "w") as file: # remove tests/ later
            pass 
        
    else:
        print(response.get(key), "\n")
        dir_file = response.get(f"{key}") 
        
        os.mkdir(f"tests/{key}")  # rm tests/ later.

        if not dir_file:
            pass
        else:
            for i in dir_file:
                print(f"i is : {i}", "\n")
                
                with open(f"tests/{key}/{i}", "w") as file: # fix?
                    pass
       