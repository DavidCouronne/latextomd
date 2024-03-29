# Live Cycle

## Basic description

When you run: `latextomd input.tex - o output.tex`:

1. Pre-Pandoc processing: process enumerate, process tikz/pstricks, ...
2. Convert with pandoc to markdown
3. Post-Pandoc processing: process math mode, ...

## Pre-Pandoc

A class of `LatexToMd`is instentiate whith the `content` of `input.tex`.

### \_remove_comments

=== "before"

    ```latex
    some text % some comments
    ```

=== "after"

    ```latex
    some text
    ```

### \_replace_simple

Process basics replacements without regex. See `config.replace_simple`. For example:

=== "before"

    ```latex
    \begin{enumerate}
        \item One item \begin{enumerate}
            \item let \[x=12\]
        \end{enumerate}
    \end{enumerate}
    ```

=== "after"

    ```latex
    \begin{enumerate}
        \item One item
    \begin{enumerate}
            \item let \[x=12\]
        \end{enumerate}
    \end{enumerate}
    ```

### \_strip_lines

strip all lines.

=== "before"

    ```latex
    \begin{enumerate}
        \item One item
    \begin{enumerate}
            \item let $$x=12$$
        \end{enumerate}
    \end{enumerate}
    ```

=== "after"

    ```latex
    \begin{enumerate}
    \item One item
    \begin{enumerate}
    \item let $$x=12$$
    \end{enumerate}
    \end{enumerate}
    ```

### \_process_preamble

Split the `content` whith `preamble`.

Default preamble is `\documentclass{article}`.

<Tabs
defaultValue="before"
values={[
{ label: 'Before', value: 'before', },
{ label: 'After', value: 'after', },
{ label: 'Preamble', value: 'preamble', },
]
}>
<TabItem value="before">

```latex
\documentclass{article}
\usepackage{tikz}
\begin{document}
\begin{enumerate}
    \item One
    \item Two
\end{enumerate}
\end{document}
```

</TabItem>
<TabItem value="after">

```latex
\begin{enumerate}
\item One
\item Two
\end{enumerate}
```

</TabItem>
<TabItem value="preamble">

```latex
\documentclass{article}
\usepackage{tikz}
```

</TabItem>
</Tabs>

### \_convert_enumerate

=== "before"

    ```latex
    \begin{enumerate}
        \item Resolve $x^2=4$
        \item Resolev $x^2=-2$
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

=== "after"

    ```latex
    \textbf{1.} Resolve $x^2=4$

    \textbf{2.} Resolve $x^2=-2$

    \textbf{1.} Let $f: x \mapsto \ln(x)-x$

    \textbf{1.a)} Calculate $f'(x)$

    \textbf{1.b)} Calculate $\displaystyle\lim_{x\to +\infty}f(x)$

    \textbf{2.} Sketch the graph
    ```

=== "markdown"

    ```markdown
    **1.** Resolve $x^2=4$

    **2.** Resolve $x^2=-2$

    **1.** Let $f: x \mapsto \ln(x)-x$

    **1.a)** Calculate $f'(x)$

    **1.b)** Calculate $\displaystyle\lim_{x\to +\infty}f(x)$

    **2.** Sketch the graph
    ```

=== "render"

    **1.** Resolve $x^2=4$

    **2.** Resolve $x^2=-2$

    **1.** Let $f: x \mapsto \ln(x)-x$

    **1.a)** Calculate $f'(x)$

    **1.b)** Calculate $\displaystyle\lim_{x\to +\infty}f(x)$

    **2.** Sketch the graph

!!!tip

    You can let `pandoc` handle the enumerate environnements whith the flag `--pandoc-enumerate`

!!!example

    With:

    ```bash
    latextomd input.tex --pandoc-enumerate
    ```

    === "before"

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
