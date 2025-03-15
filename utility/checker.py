import os
import json

languages = [
              "lua", "html", "css", "java", "python", "javascript", "c", "cpp", "rust", "go", 
              "php", "ruby", "swift", "kotlin", "typescript", "dart", "r", "perl", "shell", 
              "sql", "csharp", "objective-c", "scala", "haskell", "elixir", "clojure", "fsharp", 
              "c++", "visual-basic", "fortran", "cobol", "pascal", "assembly", "matlab", "julia", 
              "ada", "nim", "d", "v", "zig", "groovy", "racket", "lisp", "prolog", "erlang", "ocaml", 
              "crystal", "markdown"
            ]

def verify(language: str):
  if language.lower() not in languages:
    return False
  return language