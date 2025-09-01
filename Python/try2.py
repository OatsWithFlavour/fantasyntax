from config.config_loader import load_config
from helper.io import TextFile
from pattern.muster import generiere_regex
from pattern.ersatz import generiere_ersatz
from processes.command_bedingung import bedingte_env
from processes.regex_executor import change_text

paths = load_config("paths")
txt_path = paths["txt"]
tex_path = paths["tex"]
tex = TextFile(tex_path)
txt = TextFile(txt_path)

mapping = load_config("mapping")
muster_vorlagen = load_config("muster_vorlage")
musterdaten = load_config("muster")
ersatz_vorlagen = load_config("ersatz_vorlage")
ersatzdaten = load_config("ersatz")

regex_dict = generiere_regex(muster_vorlagen, mapping, musterdaten)
bedingungs_dict = bedingte_env(musterdaten)
ersatz_dict = generiere_ersatz(ersatz_vorlagen, ersatzdaten)
text = txt.read()

print(f"Musterdict: {regex_dict}")
print(f"Bedingungsdict: {bedingungs_dict}")
print(f"Ersatzdict: {ersatz_dict}")
print(f"Originaltext: {text}")

text1 = change_text(text, regex_dict, bedingungs_dict, ersatz_dict)

print(f"Geänderter Text: {text1}")



regex_dict = {'itemize': '^liste:\\s*$(.*?)^\\s*$', 'item': '^\\-\\s+'}
bedingungs_dict = {'item': ['itemize']}
ersatz_dict = {'itemize': '\\\\begin{itemize}\n\\1\n\\\\end{itemize}', 'item': '\\\\item '}
text = """Einleitung

liste:
- Apfel
- Banane
- Kirsche

Zwischentext

liste:
- Eins
- Zwei
- Drei

Ende"""

print(f"Musterdict: {regex_dict}")
print(f"Bedingungsdict: {bedingungs_dict}")
print(f"Ersatzdict: {ersatz_dict}")
print(f"Originaltext: {text}")

text2 = change_text(text, regex_dict, bedingungs_dict, ersatz_dict)

print(f"Geänderter Text: {text2}")


text3 = """Einleitung

\\begin{itemize}

\item Apfel
\item Banane
\item Kirsche

\end{itemize}
Zwischentext

\\begin{itemize}

\item Eins
\item Zwei
\item Drei

\end{itemize}
Ende"""

print(repr(text1))
print(repr(text2))
print(repr(text3))

if text1 == text2 == text3:
    print("YES")
if repr(text1) == repr(text2) == repr(text3):
    print("YES")