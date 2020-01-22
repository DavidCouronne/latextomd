\pstree[treemode=R,nodesep=4pt]{\Tdot}{
\pstree{\TR{$A$}\taput{$0,8$}}{
\Tdot~[tnpos=r]{$S$}\taput{$0,1$}
\Tdot~[tnpos=r]{$\overline{S}$}\tbput{$0,9$}
}
\pstree{\TR{$B$}\tbput{$0,2$}}{
\Tdot~[tnpos=r]{$S$}\taput{$0,2$}
\Tdot~[tnpos=r]{$\overline{S}$}\tbput{$0,8$}
}
}

\psset{unit=1cm}

\begin{pspicture}(7,3)
\psframe(7,3)\psline(0,2)(7,2)\psline(0,2.5)(7,2.5)
\psline(1,0)(1,3)
\uput[u](0.,2.5){$x$} \uput[u](1.5,2.5){$- \infty$} \uput[u](4,2.5){$0$} \uput[u](6.5,2.5){$ + \infty$}
\rput(0.5,2.25){$f'(x)$}\rput(2.5,2.25){$-$}\rput(4,2.25){$0$}\rput(5.5,2.25){$+$}
\psline{->}(1.5,1.5)(3.5,0.5)
\psline{->}(4.5,0.5)(6.5,1.5)
\uput[d](1.2,2){1}\uput[d](6.5,2){$+ \infty$}
\uput[u](4,0){$- 1$}\rput(0.5,1){$f(x)$}
\end{pspicture}

\psset{unit=1.3cm}
\begin{pspicture*}(-5,-3.5)(5.1,5)
\psgrid[gridlabels=0pt,subgriddiv=1,gridwidth=0.2pt,gridcolor=orange]
\psaxes[linewidth=1pt](0,0)(-5,-3.5)(5,4.99)
\psaxes[linewidth=1.5pt]{->}(0,0)(1,1)
\psplot[plotpoints=8000,linewidth=1.25pt,linecolor=blue]{-4.5}{1.55}{2.71828 x exp}
\psplot[plotpoints=8000,linewidth=1.25pt,linecolor=red]{-1.5}{5}{1 2.71828 x neg exp sub}
\uput[dr](0,0){O}
\rput(1.05,3.5){\blue $\mathcal{C}_{f}$}
\rput(2.4,0.7){\red $\mathcal{C}_{g}$}
\psplot{-4}{4}{0.186374 x 1.68 add mul 0.186374 add}
\psplot{-4}{4}{2.15977 x 0.77 sub mul 2.15977 add}
\end{pspicture*}