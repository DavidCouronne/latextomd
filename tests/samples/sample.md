{**~Corrigé du baccalauréat S Asie
18 juin 2013~ **}

**Exercice 1  5 points**

**Commun  à tous les candidats**

**Partie A**

1.
Le grossiste a deux fournisseurs et il y a dans chaque boîte des traces de pesticides ou non. On a donc un arbre $2 \times 2$ :

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

2.

a)
En suivant la quatrième branche :

$p\left(B \cap \overline{S}\right)  = p(B) \times p_{B}\left(\overline{S} \right) = 0,2 \times 0,8 = 0,16$.

b)
On calcule de même :

$p\left(A \cap \overline{S}\right)  = p(A) \times p_{A}\left(\overline{S} \right) = 0,8 \times 0,9 = 0,72$.

$\{A~;~B\}$ étant une partition de l'univers, on a donc :

$p\left(\overline{S}\right) = p\left(A \cap \overline{S}\right)  + 	p\left(B \cap \overline{S}\right)  = 0,72 + 0,16 = 0,88$.

3.  Il faut donc calculer :

$p_{S}(B) = \dfrac{p(S \cap B)}{p(S)}$.

On a vu que $p\left(\overline{S}\right) = 0,88$, donc $p(S) = 1 - p\left(\overline{S}\right) = 0,12$.

Donc $p_{S}(B) =\dfrac{0,2 \times 0,2}{0,12} = \dfrac{4}{12} = \dfrac{1}{3} \approx 0,33$ au centième près.

**Partie B**

1.
On a vu que la probabilité de tirer une boîte de façon aléatoire dans le stock du grossiste sans trouver de pesticides est égale à $0,88$. C'est une épreuve de Bernoulli.

Répéter de façon indépendante 10 fois cette expérience est donc une épreuve de Bernoulli de paramètres $n = 10$ et $p = 0,88$.

La variable $X$ suit donc une loi binomiale $\mathcal{B}(10~;~0,88)$.

2.
Il faut trouver $p(X = 10) = \binom{10}{10}\times 0,88^{10}\times (1 - 0,88)^{10 - 10} = 0,88^{10} \approx 0,28$ au centième près.

3.
Il faut trouver :

$p(X \geqslant 8) = p(X = 8) + p(X = 9) + p(X = 10) =$

$\binom{10}{8}\times 0,88^{8}\times (1 - 0,88)^{10 - 8} + \binom{10}{9}\times 0,88^{9}\times (1 - 0,88)^{10 - 9} + \binom{10}{10}\times 0,88^{10}\times (1 - 0,88)^{10 - 10} \approx$

$0,233043 + 0,379774 + 0,278501 \approx 0,891318 \approx 0,89$ au centième près

**Partie C**

1.
On vérifie tout d'abord que :

$\bullet~~$ $n = 50$ et $50 \geqslant 30$ ;

$\bullet~~$ $np = 50 \times 0,88 = 44$ et $44 \geqslant 5$ ;

$\bullet~~$ $n(1 - p) = 50 \times 0,12 = 6$ et $6 \geqslant 5$.

On sait qu'alors l'intervalle de fluctuation asymptotique au seuil de 95\,\% est égale à :

I$_{f} = \left[0,88 - \dfrac{1,96 \times \sqrt{0,88 \times (1 - 0,88)}}{\sqrt{50}}~;~0,88 + \dfrac{1,96 \times \sqrt{0,88 \times (1 - 0,88)}}{\sqrt{50}}\right]$, d'où au centième près :

I$_{f} = [0,79~;~0,98]$.

2.
L'inspecteur de la brigade de répression constate une proportion de lots sans pesticides de

$\dfrac{50 - 12}{50} \approx 0,76$.
Or $0,76 \notin \text{I}_{f}$, donc il doit constater au risque de 5\,\% que la publicité est mensongère.

**Exercice 2  6 points**

**Commun  à tous les candidats**

**Partie A**

Voir la figure.

**Partie B**

1.

a)

Le coefficient directeur de la tangente à la courbe $\mathcal{C}_{f}$ au point A est égal à $f'(a)$. Or

$f'(x)  = \text{e}^{x}$, donc $f'(a) = \text{e}^{a}$.

b)
De même le coefficient directeur de la tangente à la courbe $\mathcal{C}_{g}$ au point B est égal à $g'(b)$. Or $g'(x) = - \left(- \text{e}^{-x}\right)$, donc  $g'(b) = \text{e}^{- b}$.

c)
Si les deux tangentes sont égales le coefficient directeur de leurs équations réduites sont égaux, soit :

$f'(a) = g'(b) \iff \text{e}^{a} = \text{e}^{- b}$ et par croissance de la fonction logarithme népérien :

$a = - b \iff b = - a$.

2.

Une équation réduite de la tangente à la courbe $\mathcal{C}_{f}$ au point A est égale à :

$y - \text{e}^a = \text{e}^{a}(x - a) \iff y = x\text{e}^{a} + \text{e}^a(1  - a)$.

Une équation réduite de la tangente à la courbe $\mathcal{C}_{g}$ au point B est égale à :

$y - \left(1 - \text{e}^{- b}\right) = \text{e}^{- b}(x - b) \iff y = x\text{e}^{ - b} + 1 - \text{e}^{- b} - b\text{e}^{- b}$.

Ou en remplaçant $- b$ par $a$ :

$y = x\text{e}^{a} + 1 - \text{e}^{a} + a\text{e}^{a} \iff y = x\text{e}^{a} + 1 + \text{e}^{a}(a - 1)$.

Si les deux tangentes sont égales, leurs équations réduites sont les mêmes. On a déjà vu l'égalité des coefficients directeurs. Les ordonnées à l'origine sont aussi les mêmes soit :

$\text{e}^a(1  - a) = 1 + \text{e}^{a}(a - 1) \iff \text{e}^a(2  - 2a) = 1 \iff 2(a - 1)\text{e}^a + 1 = 0$.

Donc $a$ est solution de l'équation dans $\R$ :

$$
2(x - 1)\text{e}^x + 1 = 0.
$$

**Partie C**

1.

a)
Sur $\R$, \: $\varphi(x) = 2x\text{e}^x - \text{e}^x + 1$.

On sait que $\displaystyle\lim_{x \to - \infty} \text{e}^x = 0$ et $\displaystyle\lim_{x \to - \infty} x\text{e}^x = 0$, d'où par somme de limite :

$\displaystyle\lim_{x \to - \infty} \varphi(x) = 1$.

La droite d'équation $y = 1$ est asymptote horizontale à la courbe représentative de $\varphi$.

On a $\displaystyle\lim_{x to + \infty} (x - 1) = + \infty$ et  $\displaystyle\lim_{x \to + \infty} \text{e}^x = + \infty$, d'où par somme de limites : $\displaystyle\lim_{x \to + \infty} \varphi(x) = + \infty$.

b)
Somme de fonctions dérivable sur $\R$, $\varphi$ est dérivable sur $\R$ et :

$\varphi'(x) = 2\text{e}^x + 2(x - 1)\text{e}^x = 2x\text{e}^x$.

Comme,  quel que soit $x \in \R$; \: $\text{e}^x > 0$, le signe de $\varphi'(x)$ est celui de $x$. Donc sur $]- \infty~;~0[,$

$\varphi'(x) < 0$ : la fonction est décroissante sur cet intervalle et sur $]0~;~+ \infty[$, \:$\varphi'(x) > 0$ : la fonction $\varphi$ est croissante sur cet intervalle. D'où le tableau de variations :

c)
~
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

2.

a)
Sur $]- \infty~;~0]$ la fonction $\varphi$ est continue et strictement décroissante à valeurs dans $[- 1~;~1]$. Comme $0 \in  [- 1~;~1]$ il existe un réel unique $\alpha$ de $]- \infty~;~0]$ tel que $f(\alpha) = 0$.

Le même raisonnement sur l'intervalle $[0~;~+\infty[$ montre qu'il existe un réel unique de cet intervalle $\beta$ tel que $f(\beta) = 0$.

Donc l'équation $\varphi(x) = 0$ admet exactement deux solutions dans $\R$.

b)

La calculatrice donne successivement :

$\varphi(- 2) \approx 0,18$ et $\varphi(- 1) \approx -0,47$, donc $- 2 < \alpha < - 1$ ;

$\varphi(- 1,7) \approx 0,013$ et $\varphi(- 1,6) \approx -0,05$, donc $- 1,7 < \alpha < - 1,6$ ;

$\varphi(- 1,68) \approx 0,001$ et $\varphi(- 1,67) \approx -0,005$, donc $- 1,68 < \alpha < - 1,67$ ;

$\varphi(- 1,679) \approx 0,00041$ et $\varphi(- 1,678) \approx -0,0002$, donc $- 1,679 < \alpha < - 1,678$.

Conclusion au centième près $\alpha \approx - 1,68$.

De la même façon on obtient $\beta \approx 0,77$.

**Partie D**

1.
Le coefficient directeur de la tangente en E à $\mathcal{C}_{f}$ est $\text{e}^{\alpha}$.

Le coefficient directeur de la droite (EF) est: $\dfrac{1 - \text{e}^{\alpha} - \text{e}^{\alpha}}{- \alpha - \alpha} = \dfrac{1 - 2\text{e}^{\alpha}}{- 2\alpha}$.

Or $\alpha$ est solution de l'équation : $2(x - 1)\text{e}^x + 1 = 0$, autrement dit

$2(\alpha - 1)\text{e}^{\alpha} + 1 = 0 \iff 2\alpha\text{e}^{\alpha} = 2\text{e}^{\alpha} - 1$, d'où en revenant au coefficient directeur de la droite (EF) : $\dfrac{1 - 2\text{e}^{\alpha}}{- 2\alpha} = \dfrac{- 2 \alpha\text{e}^{\alpha}}{-2\alpha} = \text{e}^{\alpha}$

Conclusion : la droite (EF) est bien la tangente à la courbe $\mathcal{C}_{f}$ au point d'abscisse $\alpha$ et la tangente à la courbe $\mathcal{C}_{g}$ au point d'abscisse $-\alpha$.

2.
Le coefficient directeur de la tangente à la courbe $\mathcal{C}_{g}$ au point d'abscisse $- \alpha$ est $\text{e}^{- (- \alpha)} = \text{e}^{\alpha}.$

On a vu dans la question précédente que la droite (EF) a pour coefficient directeur $\text{e}^{\alpha}$ et contient le point F.

Conclusion la droite (EF) est la tangente à la courbe $\mathcal{C}_{g}$ au point d'abscisse $- \alpha$.

**Exercice 3  4 points**

**Commun  à tous les candidats**

1.  **Affirmation 1** : VRAIE

On a $\overrightarrow{\text{AB}}\left(- \sqrt{3} - 2~;~- 1\right)$ et $\overrightarrow{\text{AC}}\left(- 1~;~\sqrt{3} - 2\right)$.

D'où $\overrightarrow{\text{AC}} = \left(2 - \sqrt{3}\right)\overrightarrow{\text{AB}}$.

Les vecteurs sont colinéaires donc les points A, B et C sont alignés.

2.  **Affirmation 2** : FAUSSE

On calcule successivement :

EB$^2  = 8 ~; ~ \text{EC}^2 = 8$ et ED$^2
= \dfrac{19}{4} + 2\sqrt{3} \neq 8$.

Les points B, C et D ne sont pas équidistants de E.

3.

**Affirmation 3** : VRAIE

Une équation du plan (IJK) est $x + y + z = 1$. Un  point commun à ce plan et à la droite $\mathcal{D}$ a ses coordonnées telles que :

$2 - t + 6 - 2t - 2 + t = 1 \iff 5 = 2t \iff t = \dfrac{5}{2}.$

Ce point commun existe donc et a pour coordonnées $\left(- \dfrac{1}{2}~;~1~;~\dfrac{1}{2} \right)$.

4.

**Affirmation 4** : VRAIE

(EFGH) est un carré donc le milieu T de [HF] est le milieu de [EG].

On a donc $\overrightarrow{\text{ET}} = \dfrac{1}{2}\overrightarrow{\text{EG}}$.

En prenant par exemple le repère $\left(\text{A},~\overrightarrow{\text{AB}}~;~\overrightarrow{\text{AD}}~;~\overrightarrow{\text{AE}}\right)$ calculons le produit scalaire :

$\overrightarrow{\text{AT}} \cdot \overrightarrow{\text{EC}} = \left(\overrightarrow{\text{AE}} + \overrightarrow{\text{ET}} \right) \cdot \left(\overrightarrow{\text{EG}} + \overrightarrow{\text{GC}} \right) =
\left(\overrightarrow{\text{AE}} + \dfrac{1}{2}\overrightarrow{\text{EG}} \right) \cdot \left(\overrightarrow{\text{EG}} + \overrightarrow{\text{GC}} \right) =$

$\overrightarrow{\text{AE}}\cdot \overrightarrow{\text{EG}} + \overrightarrow{\text{AE}} \cdot \overrightarrow{\text{GC}} + \dfrac{1}{2}\overrightarrow{\text{EG}} \cdot \overrightarrow{\text{EG}} + \dfrac{1}{2}\overrightarrow{\text{EG}}\cdot\overrightarrow{\text{GC}}$.

Or ABCDEFGH est un cube, donc $\overrightarrow{\text{AE}} \cdot \overrightarrow{\text{EG}} = 0$ et $\overrightarrow{\text{EG}} \cdot \overrightarrow{\text{GC}} = 0$.

De plus $\overrightarrow{\text{AE}} = - \overrightarrow{\text{GC}}$ et EG $= c\sqrt{2}$, $c$ étant la mesure du côté du cube.

Finalement : $\overrightarrow{\text{AT}} \cdot \overrightarrow{\text{EC}} = - c^2  + \dfrac{1}{2}\left(c \sqrt{2} \right)^2 = - c^2 + c^2 = 0$.

Les vecteurs sont orthogonaux donc les droites (AT) et (EC) sont orthogonales.

**Exercice 4  5 points**

**Candidats n'ayant pas choisi l'enseignement de spécialité**

**Partie A**

1.
_Initialisation_ : la relation est vraie au rang $0$ ;

_Hérédité_ : supposons que pour tout naturel $p$ tel que $u_{p} > 1$.

$\dfrac{1 + 3u_{p}}{3 + u_{p}} = \dfrac{3 + u_{p} - 2 + 2u_{p}}{3 + u_{p}} =  \dfrac{\left(3 + u_{p}\right) + \left(2u_{p} - 2\right)}{3 + u_{p}} = 1  + 2\dfrac{u_{p} - 1}{3 + u_{p}}$.

Par hypothèse de récurrence on a :

$u_{p} - 1$ et comme $u_{p} > 1,\, 3 + u_{p} > 4 > 0$ donc son inverse $\dfrac{1}{3 + u_{p}} > 0$ et finalement $\dfrac{u_{p} - 1}{3 + u_{p}} > 0$, c'est-à-dire que $u_{p+1} = \dfrac{1 + 3u_{p}}{3 + u_{p}} > 1$

Conclusion : la propriété est vraie au rang $0$, et elle est héréditaire à partir de tout rang, donc d'après le principe de récurrence,   pour tout entier naturel $n$, \, $u_{n} > 1$.

2.

a)
Quel que soit le naturel $n$, \, $u_{n+1}- u_{n} = \dfrac{1 + 3u_{n}}{3 + u_{n}} - u_{n} = \dfrac{1 + 3u_{n} - 3u_{n}- u_{n}^2}{3 + u_{n}} = \dfrac{1 - u_{n}^2}{3 + u_{n}} = \dfrac{\left(1 - u_{n} \right)\left(1 + u_{n} \right)}{3+ u_{n}}$.

b)
On sait que quel que soit le naturel $n$, \, $u_{n} > 1 \Rightarrow u_{n}^2 > 1^2 \Rightarrow 1 - u_{n}^2 < 0$ et comme $3 + u_{n} > 0$ et finalement $u_{n+1}  - u_{n} < 0$ ce qui signifie que la suite $\left(u_{n}\right)$ est décroissante.

La suite $\left(u_{n}\right)$ est décroissante et minorée par $1$ : elle converge vers une limite supérieure ou égale à $1$.

**Partie B**

1.

\begin{tabularx}{0.6\linewidth}{|*{4}{>{\centering \arraybackslash}X|}}\hline
$i$&1&2& 3\\ \hline
$u$&0,800&1,077&0,976\\ \hline
\end{tabularx}

2.

Il semble que la suite converge vers $1$ par valeurs alternativement supérieures et inférieures.

3.

a)
$V_{n+1} = \dfrac{u_{n+1} - 1}{u_{n+1} + 1} = \dfrac{\frac{1 + 0,5u_{n}}{0,5 + u_{n}} - 1}{\frac{1 + 0,5u_{n}}{0,5 + u_{n}} + 1}  = \dfrac{0,5 - 0,5u_{n}}{1,5 + 1,5u_{n}} = \dfrac{- 0,5\left(u_{n} - 1\right)}{1,5\left(u_{n} + 1 \right)} = -\dfrac{1}{3}v_{n}$.

La suite $\left(v_{n}\right)$ est donc géométrique de raison $- \dfrac{1}{3}$.

b)
On a $v_{0} = \dfrac{2 - 1}{2 + 3} = \dfrac{1}{3}$.

On sait qu'alors pour tout naturel $n,\, v_{n} = \dfrac{1}{3}\times \left(- \dfrac{1}{3} \right)^n$.

4.

a)
Quel que soit le naturel $n$, \, $\left(- \dfrac{1}{3} \right)^n \leqslant 1$, donc $v_{n} \leqslant \dfrac{1}{3}$ et par conséquent $v_{n}\neq 1$.

b)
$v_{n} = \dfrac{u_{n} - 1}{u_{n} + 1} \iff v_{n}\left(u_{n} + 1 \right) = u_{n} - 1 \iff
v_{n}u_{n} + v_{n} = u_{n} - 1 \iff$

$v_{n}u_{n} - u_{n}+  =  - 1  - v_{n} \iff u_{n}\left(v_{n} - 1\right) = - 1  - v_{n}$ et comme $v_{n} \neq 1$,

$u_{n} = \dfrac{- 1 - v_{n}}{v_{n} - 1} = \dfrac{1 + v_{n}}{1 - v_{n}}$.

c)
Comme $- 1 < - \dfrac{1}{3} < 1$, on sait que $\displaystyle \lim_{n \to + \infty} \left(- \dfrac{1}{3} \right)^n = 0$, soit  $\displaystyle \lim_{n \to + \infty} v_{n} = 0$, donc d'après le résultat précédent $\displaystyle \lim_{n \to + \infty} u_{n} = \dfrac{1}{1} = 1$.

**Exercice 4  5 points**

**Candidats ayant choisi l'enseignement de spécialité**

**Partie A**

1.

a)
On a :

$\left\{\begin{array}{l c l}
x_{\text{E}'}&=&\frac{5}{4}\times 2 + \frac{3}{4}\times 2\\
y_{\text{E}'}&=&\frac{3}{4}\times 2 + \frac{5}{4}\times 2\\
\end{array}\right. \iff \left\{\begin{array}{l c l}
x_{\text{E}'}&=& 4\\
y_{\text{E}'}&=&4
\end{array}\right.$

$\left\{\begin{array}{l c l}
x_{\text{F}'}&=&\frac{5}{4}\times (- 1) + \frac{3}{4}\times 5\\
y_{\text{F}'}&=&\frac{3}{4}\times (- 1) + \frac{5}{4}\times 5\\
\end{array}\right. \iff \left\{\begin{array}{l c l}
x_{\text{F}'}&=& \frac{5}{2}\\
y_{\text{F}'}&=&\frac{11}{2}
\end{array}\right.$

$\left\{\begin{array}{l c l}
x_{\text{G}'}&=&\frac{5}{4}\times (- 3) + \frac{3}{4}\times 3\\
y_{\text{G}'}&=&\frac{3}{4}\times (- 3) + \frac{5}{4}\times 3\\
\end{array}\right. \iff \left\{\begin{array}{l c l}
x_{\text{G}'}&=&- \frac{3}{2}\\
y_{\text{G}'}&=&\frac{3}{2}
\end{array}\right.$

b)
OE$^2 = 2^2 + 2^2 = 8$, donc OE $= 2\sqrt{2}$.

OE$'^2 	 = 4^2 + 4^2 = 32$, donc OE$' = 4\sqrt{2}$. Donc OE$' = 2 \text{OE}$.

OG$^2 = (- 3)^2 + 3^2 = 9 + 9 = 18$, donc OG $= 3\sqrt{2}$ ;

OG$'^2 = \left(- \frac{3}{2} \right)^2 + \left(\frac{3}{2} \right)^2 = \frac{18}{4}$, donc OG$' = \frac{3\sqrt{2}}{2}$. Donc OG
$' = \dfrac{1}{2}\text{OG}$.

On a $A = \begin{pmatrix}\frac{5}{4}&\frac{3}{4}\\\frac{3}{4}&\frac{5}{4} \end{pmatrix}$.

**Partie B**

1.

Il suffit d'écrire avant le FIN POUR : afficher $x$, afficher $y$

2.

Il semble que les cordonnées sont de plus en plus grandes tout en se rapprochant (les points images sont de plus en plus proches de la droite $y = x$.)

**Partie C**

1.

_Initialisation_ : pour $n = 1$, on a bien $A^1 = \begin{pmatrix}\frac{5}{4}&\frac{3}{4}\\\frac{3}{4}&\frac{5}{4} \end{pmatrix}$ et :

$\alpha_{1} = 2^0 + \frac{1}{2^2}$ et $\beta_{1} =  2^0 - \frac{1}{2^2}$.

_Hérédité_ : supposons que pour  tout  naturel $p$ tel que : $A^p = \begin{pmatrix}\alpha_{p}&\beta_{p}\\ \beta_{p}&\alpha_{p} \end{pmatrix}$ et

$$
\alpha_{p} = 2^{p-1}  + \dfrac{1}{2^{p+1}} \quad \text{et}\quad  \beta_{p} = 2^{p-1}  - \dfrac{1}{2^{p+1}}.
$$

La relation $A^{p+1} = A \times A^p$ entraîne que :

$\alpha_{p+1} = \frac{5}{4}\alpha_{p} + \frac{3}{4}\beta_{p}$ et

$\beta_{p+1} = \frac{3}{4}\alpha_{p} + \frac{5}{4}\beta_{p}$, soit en utilisant la relation de récurrence :

$\alpha_{p+1} = \frac{5}{4}\left(2^{p-1}  + \dfrac{1}{2^{p+1}}\right) + \frac{3}{4}\left(2^{p-1}  - \dfrac{1}{2^{p+1}} \right) = \frac{8}{4}2^{p-1} + \frac{2}{4}\dfrac{1}{2^{p+1}} = 2^p + \dfrac{1}{2^{p+2}}$.

De même :

$\beta_{p+1} = \frac{3}{4}\left(2^{p-1}  + \dfrac{1}{2^{p+1}}\right) + \frac{5}{4}\left(2^{p-1}  - \dfrac{1}{2^{p+1}} \right) = \dfrac{8}{4}2^{p-1} - \dfrac{2}{4}\dfrac{1}{2^{p+1}} = 2^p  - \dfrac{1}{2^{p+2}}$.

Donc les relations sont vraies au rang $p + 1$.

On a donc démontré par récurrence que pour tout entier naturel $n \geqslant 1$, on a :

$$
\alpha_{n} = 2^{n-1}  + \dfrac{1}{2^{n+1}} \quad \text{et}\quad  \beta_{n} = 2^{n-1}  - \dfrac{1}{2^{n+1}}.
$$

2.

a)

L'égalité

$$
\begin{pmatrix}x_{n}\\y_{n}\end{pmatrix} = A^n \begin{pmatrix}2\\2\end{pmatrix}.
$$

se traduit par :

$\left\{\begin{array}{l c l}
x_{n}&=&2\alpha_{n} + 2\beta_{n}\\
y_{n}&=&2\beta_{n} + 2\alpha_{n}
\end{array}\right.$

On a quel que soit le naturel $n$, \, $x_{n} = y_{n}$.

b)
OE$_{n}^2  = x_{n}^2 + y_{n}^2 = 2x_{n}^2$ ;

Avec $x_{n} = 2\alpha_{n} + 2\beta_{n} = 2\left(\alpha_{n} + \beta_{n} \right)$ et $\alpha_{n} + \beta_{n} = 2^n$, on obtient

OE$_{n}^2  = 2 \times 4 \left(2^n \right)^2 = 2^{2n + 3}$.

Or $\displaystyle\lim_{n \to + \infty}  2^{2n+3} = + \infty$, donc $\displaystyle\lim_{n \to + \infty} \text{OE}_{n} = + \infty$.

**Annexe**

**à rendre avec la copie**

**Exercice 2**

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