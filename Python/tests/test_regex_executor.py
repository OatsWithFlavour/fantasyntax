from processes.regex_executor import change_text

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

expected = """Einleitung

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

def test_change_text():
    regex_dict = {'itemize': '^liste:\\s*$(.*?)^\\s*$', 'item': '^\\-\\s+'}
    bedingungs_dict = {'item': ['itemize']}
    ersatz_dict = {'itemize': '\\\\begin{itemize}\n\\1\n\\\\end{itemize}', 'item': '\\\\item '}


    result = change_text(text, regex_dict, bedingungs_dict, ersatz_dict)
    assert result == expected