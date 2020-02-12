---
id: installation
title: Installation
---

## Install dependencies

latextomd need some externals dependencies:

+ miktex or texlive
+ pandoc
+ perl: [http://strawberryperl.com/](http://strawberryperl.com/)
+ Image Magick: [https://imagemagick.org/](https://imagemagick.org/)

## Install with PIP

```bash
pip install latextomd
```

## Test your installation

1. Create a latex file: `sample-tikz.tex`

```latex
\documentclass{article}
\usepackage{tikz}
\begin{document}
  \begin{tikzpicture}
  \draw[thick,rounded corners=8pt] (0,0) -- (0,2) -- (1,3.25) 
   -- (2,2) -- (2,0) -- (0,2) -- (2,2) -- (0,0) -- (2,0);
  \end{tikzpicture}
\end{document}
```

2. The run in terminal, in the previous file folder: 

```bash
latextomd -i sample-tikz.tex
```

3. It will produce `sample-tikz.md` and `sample-tikz-0.jpg`

```md
![image](./sample-tikz-0.jpg)
```

![image](./sample-tikz-0.jpg)
