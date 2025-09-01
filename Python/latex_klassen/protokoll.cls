% protokoll.cls – Angepasste LaTeX-Klasse für Versuchsprotokolle (TU Ilmenau)
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{protokoll}[2025/05/10 Angepasste Klasse für Versuchsprotokolle]

% Basisklasse
\LoadClass[a4paper,12pt]{article}

% ----------------------------------------
% Schriftart und Layout
% ----------------------------------------

% Schriftart Helvetica (serifenlos)
\renewcommand{\rmdefault}{phv}
\renewcommand{\sfdefault}{phv}
\RequirePackage{newtxsf} % Anpassung an neue TeX-Standards für sans-serif

% Zeilenabstand: 1,5-fach wie in der Vorlage
\renewcommand{\baselinestretch}{1.5}

% Seitenränder wie in der Muster-Vorlage
\RequirePackage[a4paper, top=2cm, bottom=2cm, left=4cm, right=3cm]{geometry}

% ----------------------------------------
% Dokumentstruktur und Zeichencodierung
% ----------------------------------------

\RequirePackage[utf8]{inputenc}    % UTF-8 Eingabe
\RequirePackage[T1]{fontenc}       % T1-Schriften für Umlaute
\RequirePackage[ngerman]{babel}    % Neue deutsche Rechtschreibung
\RequirePackage{csquotes}          % Für korrektes Zitieren mit Babel
\RequirePackage{pdfx}              % PDF/A- und PDF/X-Konformität

% ----------------------------------------
% Mathematik & Einheiten
% ----------------------------------------

\RequirePackage{amsmath, amssymb}  % Mathematische Symbole & Umgebungen
\numberwithin{equation}{section}  % Gleichungsnummerierung mit Abschnitt

\RequirePackage{siunitx}           % SI-Einheiten
\sisetup{locale=DE}               % Deutsches Komma, Einheitendarstellung

% ----------------------------------------
% Grafiken, Tabellen und Layout
% ----------------------------------------

\RequirePackage{graphicx}         % Bilder einfügen
\RequirePackage{float}            % Positionierung [H] von Float-Objekten
\RequirePackage{booktabs}         % Professionelle Tabellenlinien
\RequirePackage{caption}          % Anpassung von Beschriftungen
\RequirePackage{fancyhdr}         % Kopf- und Fußzeilen
\RequirePackage{titlesec}         % Formatierung von Überschriften
\RequirePackage{parskip}          % Absätze mit Abstand statt Einzug
\RequirePackage{pgfplots}         % Diagramme/Plots
\RequirePackage{pgfplotstable}    % Tabellen aus CSV-Dateien
\pgfplotsset{compat=1.18}         % Kompatibilität auf aktuelle Version setzen

% ----------------------------------------
% String- & CSV-Verarbeitung
% ----------------------------------------

\RequirePackage{xstring}          % String-Manipulation (z. B. csv-Filenames)
\RequirePackage{mfirstuc}         % Großschreibung von Wörtern
\RequirePackage{array}            % Erweiterte Tabellenfunktionen
\RequirePackage{xparse}           % Neue Makros mit Argument-Parsing
\RequirePackage{etoolbox}         % Logische Bedingungen z. B. \IfBlankTF

% ----------------------------------------
% Hyperlinks
% ----------------------------------------

\RequirePackage{hyperref}         % Interne und externe Verlinkungen

% ----------------------------------------
% Spaltenumgebung
% ----------------------------------------

\RequirePackage{paracol}          % Flexible Spaltenlayouts
\NewDocumentEnvironment{spalten}{O{2}}{\begin{paracol}{#1}}{\end{paracol}}
\NewDocumentCommand{\anderespalte}{}{\switchcolumn}

% ----------------------------------------
% Kopf- & Fußzeile
% ----------------------------------------

\setlength{\headheight}{15pt}
\pagestyle{fancy}
\fancyhf{}
\lhead{Grundpraktikum Physik}
\rhead{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

% ----------------------------------------
% Abschnittsformatierung
% ----------------------------------------

\titleformat{\section}{\large\bfseries}{\thesection.}{1em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection.}{1em}{}
\numberwithin{figure}{section}
\captionsetup[figure]{labelsep=colon, name=Abb.}

% ----------------------------------------
% Metadaten
% ----------------------------------------

\newcommand{\versuchstitel}[1]{\def\@versuchstitel{#1}}
\newcommand{\autoren}[1]{\def\@autoren{#1}}
\newcommand{\studiengang}[1]{\def\@studiengang{#1}}
\newcommand{\datum}[1]{\def\@datum{#1}}
\newcommand{\praktikumstitel}[1]{\def\@praktikumstitel{#1}}

% Titelseite
\newcommand{\kopf}{
  \begin{center}
    \vspace{2em}
    \large\textbf{\@praktikumstitel} \\[1em]
    \textbf{Protokoll zum Versuch \@versuchstitel} \\[1em]
    \normalsize
    \@autoren \\
    Studiengang: \@studiengang \\
    Datum: \@datum
  \end{center}
  \vspace{1em}
  \hrule
  \vspace{2em}
}

% Titelseite beim Dokumentstart
\AtBeginDocument{\kopf}

% ----------------------------------------
% CSV-Tabellen aus Ordner "csv/"
% ----------------------------------------

\newcommand{\csvpath}{csv/}

% Automatischer Titel aus Dateinamen (z. B. "messwerte_feder.csv")
\newcommand{\csvtitle}[1]{%
  \StrSubstitute{#1}{_}{ }[\tmpA]%
  \StrBefore{\tmpA}{.csv}[\tmpB]%
  \textbf{\capitalisewords{\tmpB}}%
}

% Tabelle zeilenweise (z. B. Messreihen)
\newcommand{\zeilentabelle}[1]{%
  \noindent
  \begin{minipage}{\textwidth}
    {\csvtitle{#1}}\\[0.2cm]
    \pgfplotstabletypeset[
      col sep=comma,
      string type,
      assign column name/.style={/pgfplots/table/column name={\textbf{##1}}},
      every head row/.style={before row=\toprule, after row=\midrule},
      every last row/.style={after row=\bottomrule},
      column type=r
    ]{\csvpath#1}
  \end{minipage}\vspace{1cm}
}

% Tabelle spaltenweise (z. B. statistische Werte)
\newcommand{\spaltentabelle}[1]{%
  \noindent
  \begin{minipage}{\textwidth}
    {\csvtitle{#1}}\\[0.2cm]
    \pgfplotstabletypeset[
      col sep=comma,
      string type,
      header=true,
      every head row/.style={before row=\toprule, after row=\midrule},
      every last row/.style={after row=\bottomrule},
      every first column/.style={column type/.add={>{\bfseries}}{}}
    ]{\csvpath#1}
  \end{minipage}\vspace{1cm}
}

% ----------------------------------------
% Bildbefehle
% ----------------------------------------

% Bild einfügen aus "pics/", optional mit width
\NewDocumentCommand{\bild}{O{width=\textwidth} m}{%
  \begin{figure}[htbp]
    \centering
    \includegraphics[#1]{./pics/#2.pdf}
    \caption{#2}
  \end{figure}
}

\NewDocumentCommand{\grafik}{O{0.4} m}{%
  \begin{figure}[htbp]
    \centering
    \includegraphics[width=#1\textwidth]{./pics/#2.png}
    \caption{#2}
  \end{figure}
}

\NewDocumentCommand{\grafikpdf}{O{0.4} m}{%
  \begin{figure}[H]
    \centering
    \includegraphics[width=#1\textwidth]{./pics/#2.pdf}
    \caption{#2}
  \end{figure}
}


% Gleichungseinbindung
\newcommand{\eq}[1]{\begin{equation}#1\end{equation}}

% Liste von Gleichungen kommagetrennt verarbeiten
\newcommand{\gleqzeile}[1]{%
  \if\relax\detokenize{#1}\relax
    % ignorieren bei leerer Zeile
  \else
    \begin{equation}
      #1
    \end{equation}
  \fi
}

\NewDocumentCommand{\gl}{>{\SplitList{,}}m}{%
  \ProcessList{#1}{\gleqzeile}
}

% ----------------------------------------
% Spaltenumgebung nebeneinander
% ----------------------------------------

\newenvironment{zweiSpalten}[2][0.48\textwidth]
{%
  \begin{minipage}{#1}#2\end{minipage}\hfill
  \begin{minipage}{#1}
}
{%
  \end{minipage}
}

% ----------------------------------------
% Mathematische Kurzbefehle
% ----------------------------------------

\newcommand{\bruch}[2]{\frac{#1}{#2}}
\newcommand{\plusminus}{\pm}
\newcommand{\wurzel}[1]{\sqrt{#1}}
\newcommand{\mal}{\cdot}

% ----------------------------------------
% Abbildungen mit ausgelagerten Infos
% ----------------------------------------

\RequirePackage{biblatex}
\addbibresource{Quellen/literatur.bib}

\RequirePackage{expl3}
\ExplSyntaxOn

% Globale Property-Liste
\prop_new:N \g_protokoll_abbildungen_prop

% Registrierung eines Abbildungseintrags
\NewDocumentCommand{\abbinfo}{m m}
 {
  \prop_clear:N \l_tmpa_prop
  \prop_set_from_keyval:Nn \l_tmpa_prop {#2}
  \prop_gput:Nnn \g_protokoll_abbildungen_prop { #1/beschriftung } { \prop_item:Nn \l_tmpa_prop { beschriftung } }
  \prop_gput:Nnn \g_protokoll_abbildungen_prop { #1/quelle }       { \prop_item:Nn \l_tmpa_prop { quelle } }
 }


% Hilfsfunktion: Bild automatisch laden (pdf oder png)
\NewDocumentCommand{\includegraphicsauto}{O{1.0\linewidth} m}{
  \IfFileExists{Abbildungen/#2.pdf}
    {\includegraphics[width=#1]{Abbildungen/#2.pdf}}
    {
      \IfFileExists{Abbildungen/#2.png}
        {\includegraphics[width=#1]{Abbildungen/#2.png}}
        {\PackageWarning{protokoll}{Abbildung `#2` nicht gefunden (.pdf/.png)}}
    }
}


% Hauptfunktion zum Einfügen
\NewDocumentCommand{\abbildung}{ O{1.0} m }
 {
  \begin{figure}[h]
    \centering
    \includegraphicsauto[#1\linewidth]{#2}
    \caption{%
      \textbf{Abb.~\ref{fig:#2}:}~%
      \prop_item:Nn \g_protokoll_abbildungen_prop { #2/beschriftung }%
      \str_case:nnF { \prop_item:Nn \g_protokoll_abbildungen_prop { #2/quelle } }
      {
        {eigene Aufnahme}{~(eigene Aufnahme)}
        {Literaturverzeichnis}{~[\cite{#2}]}
      }
      {~(unbekannte Quelle)}%
    }
    \label{fig:#2}
  \end{figure}
 }


\ExplSyntaxOff
