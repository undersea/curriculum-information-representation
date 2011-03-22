\renewcommand\maketitle{%
  \newpage
  \null
  \begin{center}%
  \let \footnote \thanks
    
    \vskip 3em%
    {\large \@title \par}%
    \vskip 1.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
    \vskip 1em%
    {\large \date}%
  \end{center}%
  \par
  \vskip 1.5em}
