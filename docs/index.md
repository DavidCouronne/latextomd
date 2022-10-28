# Welcome to latextomd

## Features

!!!tip "Easy to Use"

    latextomd was designed from the ground up to be easily installed and used to convert your latex files to markdown and running quickly.

!!!tip "TikZ and PsTricks"

    latextomd convert Tikz and PsTricks environnements in .jpg, and insert tags in markdown file.

!!!tip "Mkdocs admonition"

    latextomd can convert some LateX blocs in mkdocs admonition !

## Install dependencies

latextomd need some externals dependencies

- miktex or texlive
- pandoc: [https://pandoc.org/](https://pandoc.org/)
- perl: [http://strawberryperl.com/](http://strawberryperl.com/)
- Image Magick: [https://imagemagick.org/](https://imagemagick.org/)

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

2. Then run in a terminal, in the previous file folder:

```bash
latextomd sample-tikz.tex
```

3. It will produce `sample-tikz.md` and `sample-tikz-0.jpg`

`sample-tikz.tex`

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

`sample-tikz.md`

```md
![image](./sample-tikz-0.jpg)
```

`sample-tikz-0.jpg`

![image](/assets/sample-tikz-0.jpg)
