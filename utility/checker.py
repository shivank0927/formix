LANGUAGES = {
    "lua", "html", "css", "java", "python", "javascript", "c", "cpp", "rust", "go",
    "php", "ruby", "swift", "kotlin", "typescript", "dart", "r", "perl", "shell",
    "sql", "csharp", "objective-c", "scala", "haskell", "elixir", "clojure", "fsharp",
    "c++", "visual-basic", "fortran", "cobol", "pascal", "assembly", "matlab", "julia",
    "ada", "nim", "d", "v", "zig", "groovy", "racket", "lisp", "prolog", "erlang", "ocaml",
    "crystal", "markdown", "c#"
}

def verify(language: str) -> bool: # method for verifying if language is valid
  
    return language.lower() in LANGUAGES
