from config.config_loader import load_config
from helper.io import TextFile
from helper.pfad_manager import listen_textpath
from pattern.muster import generiere_regex
from pattern.ersatz import generiere_ersatz
from processes.command_bedingung import bedingte_env
from processes.regex_executor import change_text
from latex.kompilieren import kompiliere_tex
from helper.transform_path import to_tex
from latex.class_path import class_to_text
from table_data.csv_plotter import plotte_einzelne_csv, verarbeite_alle_csvs

def main():

    try:
        txt_path = listen_textpath()
    except:
        txt_path = load_config("paths")["txt"]
    tex_path = to_tex(txt_path)

    latex_class_path = load_config("paths")["latex_class"]
    txt = TextFile(txt_path)
    tex = TextFile(tex_path)
    # plotte_einzelne_csv(txt_path, "Freifallversuch_Fehlerbetrachtung.csv", kopf="zeile")
    # verarbeite_alle_csvs(txt_path)

    mapping = load_config("mapping")
    muster_vorlagen = load_config("muster_vorlage")
    musterdaten = load_config("muster")
    ersatz_vorlagen = load_config("ersatz_vorlage")
    ersatzdaten = load_config("ersatz")

    regex_dict = generiere_regex(muster_vorlagen, mapping, musterdaten)
    # print(regex_dict)
    bedingungs_dict = bedingte_env(musterdaten)
    ersatz_dict = generiere_ersatz(ersatz_vorlagen, ersatzdaten)

    text = txt.read()
    text = change_text(text, regex_dict, bedingungs_dict, ersatz_dict)
    text = class_to_text(text, latex_class_path)
    tex.write(text)
    # kompiliere_tex(tex_path)

if __name__ == "__main__":
    main()
