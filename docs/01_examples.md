# Basics Examples

## Process enumerate

### Whithout pandoc

```latex
\begin{enumerate}
  \item Item One
  \item Item Two
\end{enumerate}
```

will produce

```md
1. Item One
2. Item Two
```

With nested enumerate:

=== "latex"

    ```latex
    \begin{enumerate}
      \item Item One
      \begin{enumerate}
        \item Subitem One
        \item Subitem two
      \end{enumerate}
      \item Item Two
    \end{enumerate}
    ```

=== "markdown"

    ```markdown
    1. Item One
    1. a) Subitem One
    1. b) Subitem Two
    1. Item Two
    ```

=== "render"

    1. Item One
    1. a) Subitem One
    1. b) Subitem Two
    1. Item Two

### whith pandoc

!!!tip

    You can let `pandoc` handle the enumerate environnements whith the flag `--pandoc-enumerate`

!!!example

    With:

    ```bash
    latextomd input.tex --pandoc-enumerate
    ```

    === "latex"

        ```latex
        \begin{enumerate}
            \item Resolve $x^2=4$
            \item Resolve $x^2=-2$
        \end{enumerate}

        \begin{enumerate}
            \item Let $f: x \mapsto \ln(x)-x$
            \begin{enumerate}
                \item Calculate $f'(x)$
                \item Calculate $\displaystyle\lim_{x\to +\infty}f(x)$
            \end{enumerate}
            \item Sketch the graph
        \end{enumerate}
        ```

    === "markdown"

        ```markdown
        1.  Resolve $x^2=4$

        2.  Resolve $x^2=-2$

        3.  Let $f: x \mapsto \ln(x)-x$

            1.  Calculate $f'(x)$

            2.  Calculate $\displaystyle\lim_{x\to +\infty}f(x)$

        4.  Sketch the graph
        ```

    === "render"

        1.  Resolve $x^2=4$

        2.  Resolve $x^2=-2$

        3.  Let $f: x \mapsto \ln(x)-x$

            1.  Calculate $f'(x)$

            2.  Calculate $\displaystyle\lim_{x\to +\infty}f(x)$

        4.  Sketch the graph

## Include pictures

```latex
\documentclass{article}
\usepackage{graphicx}
\begin{document}
The universe is immense and it seems to be homogeneous,
in a large scale, everywhere we look at.

\includegraphics{universe.png}

There's a picture of a galaxy above
\end{document}
```

```md
The universe is immense and it seems to be homogeneous, in a large
scale, everywhere we look at.

![image](universe.png)

There's a picture of a galaxy above
```

## Working with TikZ or PsTricks

In `sample-tikz.tex`:

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

will produce `sample-tikz.md` and `sample-tikz-0.jpg`

```md
![image](./sample-tikz-0.jpg)
```

![Image](./assets/sample-tikz-0.jpg)

## Admonitions

```latex title="sample_theorem.tex"
\documentclass{article}
\usepackage{amsthm}
\newtheorem{theorem}{Theorem}
\begin{document}

Theorems can easily be defined:

\begin{theorem}
Let \(f\) be a function whose derivative exists in every point, then \(f\)
is a continuous function.
\end{theorem}
\end{document}
```

By default, when Pandoc don't recognize a LaTeX bloc, he produce:

```bash
latextomd sample_theorem.tex
```

=== "markdown"

    ````markdown title="sample_theorem.md"
    Theorems can easily be defined:

    ```{=latex}
    \begin{theorem}
    Let \(f\) be a function whose derivative exists in every point, then \(f\)
    is a continuous function.
    \end{theorem}
    ```
    ````

=== "render"

    Theorems can easily be defined:

    ```{=latex}
    \begin{theorem}
    Let \(f\) be a function whose derivative exists in every point, then \(f\)
    is a continuous function.
    \end{theorem}
    ```

### Mkdocs admonitions

When the `flag` `--mkdocs` is set to `true`:

```bash
latextomd sample_theorem.tex --mkdocs
```

=== "markdown"

    ```markdown title="sample_theorem.md"
    Theorems can easily be defined:

    !!!tip "Theorem "

        Let $f$ be a function whose derivative exists in every point, then $f$
        is a continuous function.
    ```

=== "render"

    Theorems can easily be defined:

    !!!tip "Theorem "

        Let $f$ be a function whose derivative exists in every point, then $f$
        is a continuous function.

### Docusaurus admonitions

When the `flag` `--docusaurus` is set to `true`:

```bash
latextomd sample_theorem.tex --docusaurus
```

=== "markdown"

    ```markdown title="sample_theorem.md"
    Theorems can easily be defined:

    :::tip Theorem:

    Let $f$ be a function whose derivative exists in every point, then $f$
    is a continuous function.

    :::
    ```
