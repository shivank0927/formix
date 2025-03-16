import sys, os , argparse, json
from utility.integrate import integration 
from utility.checker import verify
# to be made func. later

parser = argparse.ArgumentParser()

parser.add_argument(
    "language",
    help="Name of the programming languages you want to create, separated by ','.\n"
         "Example: For web development: HTML, CSS, JS"
)

parser.add_argument(
    "architecture",
    help="Structure of your project. Enter them in string \n"
         "You can also provide a project description, as it's integrated with the Gemini API."
)

args = parser.parse_args()

lang = args.language
arch = args.architecture

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
