from config.config_loader import load_config
from helper.io import TextFile
from pattern.muster import generiere_regex

def main():
    paths = load_config("paths")
    txt_path = paths["txt"]
    tex_path = paths["tex"]
    txt = TextFile(txt_path)
    tex = TextFile(tex_path)
    print(txt.read())
    print(tex.read())
    mapping = load_config("mapping")
    muster_vorlagen = load_config("muster_vorlage")
    musterdaten = load_config("muster")
    regex_dict = generiere_regex(muster_vorlagen, mapping, musterdaten)
    print(regex_dict)
if __name__ == "__main__":
    main()
