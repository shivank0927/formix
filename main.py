import sys, os, argparse, json
from utility.integrate import integration
from utility.checker import verify

config = "config.json"

def command():
    
    parser = argparse.ArgumentParser()

    parser.add_argument("language", nargs="?", help="name of the programming language.")
    parser.add_argument("architecture", nargs="?", help="project structure description.")
    parser.add_argument("directory", nargs="?", help="directory name for the project.")
    parser.add_argument("--add-key", help="add your Gemini API key to use the tool.")

    return parser.parse_args()

def setup(lang, arch, direc):
    try:
        
        key = loadKey()
        if not key:
             sys.exit("No api key found.")
             
        os.mkdir(direc)

        if not verify(language=lang):
            sys.exit("language does not exist/incorrect language")
            
        response = integration(language=lang, architecture=arch, api_key=key)

        try:
            response = json.loads(response)
        except json.JSONDecodeError:
            sys.exit("error in response format.")

        if not response:
            sys.exit("error")

        return response
    
    except Exception as e:
        sys.exit(f"{e}")

def create(direc, response):
    try:
        
        for key, value in response.items():
            path = f"{direc}/{key}"

            if key in {"LICENSE", "README.md"}:
                with open(path, "w") as file:
                    pass  
                
            else:
                os.makedirs(path, exist_ok=True)
                
                if value:
                    for file_name in value:
                        with open(f"{path}/{file_name}", "w") as file:
                            pass  

    except Exception as e:
        sys.exit(f"{e}")

def saveKey(api_key):
    try:
        
        with open(config, "w") as file:
            json.dump({"api_key": api_key}, file)
            
    except Exception as e:
        sys.exit(f"error in api key saving\n{e}")

def loadKey():
    try:
        
        if os.path.exists(config):
            with open(config, "r") as file:
                data = json.load(file)
                return data.get("api_key")
        return None
    
    except Exception as e:
        sys.exit(f"error in key loading\n{e}")

if __name__ == "__main__":
    argus = command()

    if argus.add_key:
        saveKey(argus.add_key)
        sys.exit(0)
    lang = argus.language or "lua"
    arch = argus.architecture or "default"
    dire = argus.directory or "project"

    response = setup(lang, arch, dire)
    create(dire, response)
