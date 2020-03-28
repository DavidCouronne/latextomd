:::exercice Exercice 1: Pondichéry 2019

**[Exercice 2]{.smallcaps} points**

**Commun à tous les candidats**

Le but de cet exercice est d'étudier la suite $\left(u_n\right)$ définie
par la donnée de son premier terme $u_1$ et, pour tout entier naturel
$n$ supérieur ou égal à 1, par la relation :

$$u_{n+1} = (n + 1)u_n - 1.$$

**Partie A**

**1.** Vérifier, en détaillant le calcul, que si $u_1 = 0$ alors
$u_4 = - 17$.

**2.** Recopier et compléter l'algorithme ci-dessous pour qu'en
saisissant préalablement dans $U$ une valeur de $u_1$ il calcule les
termes de la suite $\left(u_n\right)$ de $u_2$ à $u_{13}$.

  ---------------------------
  Pour $N$ allant de 1 à 12
  $U \gets$
  Fin Pour
  ---------------------------

**3.** On a exécuté cet algorithme pour $u_1 = 0,7$ puis pour
$u_1 = 0,8$.

Voici les valeurs obtenues.

  ------------ -----------
  0,4          0,6
  0,2          0,8
  $- 0,2$      2,2
  $- 2$        10
  $- 13$       59
  $- 92$       412
  $- 737$      3295
  -6634        29654
  -66341       296539
  -729752      3261928
  -8757025     39143135
  -113841326   508860754
  ------------ -----------

Quelle semble être la limite de cette suite si $u_1 = 0,7$ ? Et si
$u_1 = 0,8$ ?

**Partie B**

On considère la suite $\left(I_n\right)$ définie pour tout entier
naturel $n$, supérieur ou égal à 1, par :

$$I_n = \displaystyle\int_0^1 x^n \text{e}^{1 - x}\:\text{d}x.$$

On rappelle que le nombre e est la valeur de la fonction exponentielle
en 1, c'est-à-dire que e $= \text{e}^1$.

**1.** Prouver que la fonction $F$ définie sur l'intervalle \[0 ; 1\]
par $F(x)=(- 1 - x)\text{e}^{1 - x}$ est une primitive sur l'intervalle
\[0 ; 1\] de la fonction $f$ définie sur l'intervalle \[0 ; 1\] par
$f(x) = x \text{e}^{1 - x}$.

**2.** En déduire que $I_1 = \text{e} - 2$.

**3.** On admet que, pour tout entier naturel $n$ supérieur ou égal à 1,
on a :

$$I_{n+1} =  (n+1)I_{n} - 1.$$

Utiliser cette formule pour calculer $I_2$.

**4.**

**4.a)** Justifier que, pour tout nombre réel $x$ de l'intervalle
\[0 ; 1\] et pour tout entier naturel $n$ supérieur ou égal à 1, on a :
$0 \leqslant x^n \text{e}^{1-x} \leqslant  x^n \text{e}$.

**4.b)** Justifier que :
$\displaystyle\int_0^1 x^n\text{e}\:\text{d}x = \dfrac{\text{e}}{n+ 1}$.

**4.c)** En déduire que, pour tout entier naturel $n$ supérieur ou égal
à 1, on a : $0 \leqslant I_n \leqslant \dfrac{\text{e}}{n+ 1}$.

**4.d)** Déterminer $\displaystyle\lim_{n \to + \infty} I_n$.

**Partie C**

Dans cette partie, on note $n$! le nombre défini, pour tout entier
naturel n supérieur ou égal à 1, par : 1!=1

2!$=2 \times 1$

et si $n \geqslant 3$ : $n$!
$= n \times  (n-1) \times  \ldots  \times 1$

On a ainsi par exemple

3! $= 3\times 2\times 1 = 3\times(2 \times 1) = 3\times 2$!

4!
$= 4\times 3\times 2\times 1 = 4\times (3\times 2\times 1) = 4\times 3$!

8!
$= 8\times 7\times 6\times 5\times 4\times 3\times 2\times 1 = 8\times(7\times 6\times 5\times 4\times 3\times 2\times 1) = 8\times 7$!

Et, plus généralement :

$$(n+1)\text{!} = (n+1)  \times n\text{!}$$

**1.** Démontrer par récurrence que, pour tout entier naturel $n$
supérieur ou égal à 1, on a :

$$u_n =n\text{!}\left(u_1 - \text{e} + 2\right)+ I_n.$$

On rappelle que, pour tout entier naturel $n$ supérieur ou égal à 1, on
a :

$$u_{n+1} = (n+1)u_{n} - 1\quad \text{ et } I_{n+1} = (n+1)I_{n} - 1.$$

**2.** On admet que :
$\displaystyle\lim_{n \to + \infty} n\text{!} = + \infty$.

**2.a)** Déterminer la limite de la suite $\left(u_n\right)$ lorsque
$u_1 = 0,7$.

**2.b)** Déterminer la limite de la suite $\left(u_n\right)$ lorsque
$u_1 = 0,8$.

:::

:::exercice Exercice 2: Polynésie 2019

**Exercice 3 points**

**Commun à tous les candidats**

On considère la suite $\left(I_n\right)$ définie par
$I_0 = \displaystyle\int_0^{\frac{1}{2}}\dfrac{1}{1 - x}\:\text{d}x$ et
pour tout entier naturel $n$ non nul

$$I_n = \displaystyle\int_0^{\frac{1}{2}}\dfrac{x^n}{1 - x}\:\text{d}x.$$

**1.** Montrer que $I_0 = \ln (2)$.

**2.**

**2.a)** Calculer $I_0 - I_1$.

**2.b)** En déduire $I_1$.

**3.**

**3.a)** Montrer que, pour tout entier naturel
$n,\: I_n - I_{n+1} = \dfrac{\left(\frac{1}{2} \right)^{n+1}}{n+1}$.

**3.b)** Proposer un algorithme permettant de déterminer, pour un entier
naturel $n$ donné, la valeur de $I_n$.

**4.** Soit $n$ un entier naturel non nul.

On admet que si $x$ appartient à l'intervalle
$\left[0~;~\frac{1}{2}\right]$ alors
$0 \leqslant \dfrac{x^n}{1 - x} \leqslant \dfrac{1}{2^{n-1}}$.

**4.a)** Montrer que pour tout entier naturel $n$ non nul,
$0 \leqslant  I_n \leqslant \dfrac{1}{2^n}$.

**4.b)** En déduire la limite de la suite $\left(I_n\right)$ lorsque $n$
tend vers $+\infty$.

**5.** Pour tout entier naturel $n$ non nul, on pose

$$S_n = \dfrac{1}{2} + \dfrac{\left(\frac{1}{2} \right)^2}{2} + \dfrac{\left(\frac{1}{2} \right)^3}{3} + \ldots +\dfrac{\left( \frac{1}{2}\right)^n}{n}.$$

**5.a)** Montrer que pour tout entier naturel $n$ non nul,
$S_n = I_0 - I_n$.

**5.b)** Déterminer la limite de $S_n$ lorsque $n$ tend vers $+\infty$.

:::

:::exercice Exercice 3: Liban 2019

**Exercice 1 points**

**Commun à tous les candidats**

Le plan est muni d'un repère orthogonal (O, I, J).

**1.** On considère la fonction $f$ définie sur l'intervalle \]0 ; 1\]
par

$$f(x) = x(1 - \ln x)^2.$$

**1.a)** Déterminer une expression de la fonction dérivée de $f$ et
vérifier que pour tout $x \in ]0~;~1]$,
$f'(x) = (\ln x + 1)(\ln x - 1)$.

**1.b)** Étudier les variations de la fonction $f$ et dresser son
tableau de variations sur l'intervalle \]0 ; 1\] (on admettra que la
limite de la fonction $f$ en 0 est nulle).

On note $\Gamma$ la courbe représentative de la fonction $g$ définie sur
l'intervalle \]0 ; 1\] par $g(x) = \ln x$.

Soit $a$ un réel de l'intervalle \]0 ; 1\]. On note $M_a$ le point de la
courbe $\Gamma$ d'abscisse $a$ et $d_a$ la tangente à la courbe $\Gamma$
au point $M_a$. Cette droite $d_a$ coupe l'axe des abscisses au point
$N_a$ et l'axe des ordonnées au point $P_a$ .

On s'intéresse à l'aire du triangle O$N_aP_a$ quand le réel $a$ varie
dans l'intervalle \]0 ; 1\].

**1.** Dans cette question, on étudie le cas particulier où $a = 0,2$ et
on donne la figure ci-dessous.

**1.a)** Déterminer graphiquement une estimation de l'aire du triangle
O$N_{0,2}P_{0,2}$ en unités d'aire.

**1.b)** Déterminer une équation de la tangente $d_{0,2}$.

**1.c)** Calculer la valeur exacte de l'aire du triangle
O$N_{0,2}P_{0,2}$ .

Dans ce qui suit, on admet que, pour tout réel $a$ de l'intervalle
\]0 ; 1\], l'aire du triangle O$N_aP_a$ en unités d'aire est donnée par
$\mathcal{A}(a) = \dfrac{1}{2}a (1 - \ln a)^2$.

**2.** À l'aide des questions précédentes, déterminer pour quelle valeur
de $a$ l'aire $\mathcal{A}(a)$ est maximale. Déterminer cette aire
maximale.

:::

:::exercice Exercice 4: Antilles Guyanne 2019

**[Exercice 1]{.smallcaps} points**

[Commun à tous les candidats]{.smallcaps}

**Partie A**

Soit $a$ et $b$ des nombres réels. On considère une fonction $f$ définie
sur $[0~;~+\infty[$ par

$$f(x) = \dfrac{a}{1 + \text{e}^{-bx}}.$$

La courbe $\mathcal{C}_f$ représentant la fonction $f$ dans un repère
orthogonal est donnée ci-dessous.

La courbe $\mathcal{C}_f$ passe par le point A(0 ; 0,5). La tangente à
la courbe $\mathcal{C}_f$ au point A passe par le point B(10 ; 1).

![image](./TS-integrales-1)

**1.** Justifier que $a = 1$.

On obtient alors, pour tout réel $x \geqslant 0$,

$$f(x) = \dfrac{1}{1 + \text{e}^{-bx}}.$$

**2.** On admet que la fonction $f$ est dérivable sur $[0~;~+\infty[$ et
on note $f'$ sa fonction dérivée.

Vérifier que, pour tout réel $x \geqslant 0$

$$f'(x) = \dfrac{b\text{e}^{-bx}}{\left(1 + \text{e}^{-bx}\right)^2}.$$

**3.** En utilisant les données de l'énoncé, déterminer $b$.

**Partie B**

La proportion d'individus qui possèdent un certain type d'équipement
dans une population est modélisée par la fonction $p$ définie sur
$[0~;~+\infty[$ par

$$p(x) = \dfrac{1}{1 + \text{e}^{-0,2x}}.$$

Le réel $x$ représente le temps écoulé, en année, depuis le 1 janvier
2000.

Le nombre $p(x)$ modélise la proportion d'individus équipés après $x$
années.

Ainsi, pour ce modèle, $p(0)$ est la proportion d'individus équipés au 1
janvier 2000 et $p(3,5)$ est la proportion d'individus équipés au milieu
de l'année 2003.

**1.** Quelle est, pour ce modèle, la proportion d'individus équipés au
1er janvier 2010? On en donnera une valeur arrondie au centième.

**2.**

**2.a)** Déterminer le sens de variation de la fonction $p$ sur
$[0~;~+\infty[$.

**2.b)** Calculer la limite de la fonction $p$ en $+\infty$.

**2.c)** Interpréter cette limite dans le contexte de l'exercice.

**3.** On considère que, lorsque la proportion d'individus équipés
dépasse 95 %, le marché est saturé.

Déterminer, en expliquant la démarche, l'année au cours de laquelle cela
se produit.

**4.** On définit la proportion moyenne d'individus équipés entre 2008
et 2010 par

$$m = \dfrac{1}{2}\displaystyle\int_8^{10} p(x)\:\text{d}x.$$

**4.a)** Vérifier que, pour tout réel $x \geqslant 0$,

$$p(x) = \dfrac{\text{e}^{0,2x}}{1 + \text{e}^{0,2x}}.$$

**4.b)** En déduire une primitive de la fonction $p$ sur
$[0~;~+\infty[$.

**4.c)** Déterminer la valeur exacte de $m$ et son arrondi au centième.

:::

:::exercice Exercice 5: Métropole juin 2019

**Exercice 1 points**

**Commun à tous les candidats**

**Partie A**

On considère la fonction $f$ définie sur l'ensemble $\R$ des nombres
réels par :

$$f(x)=\dfrac{7}{2}-\dfrac{1}{2}\left(\text{e}^x+\text{e}^{-x}\right)$$

**1.**

**1.a)** Déterminer la limite de la fonction $f$ en $+\infty$.

**1.b)** Montrer que la fonction $f$ est strictement décroissante sur
l'intervalle $[0~;~+\infty[$.

**1.c)** Montrer que l'équation $f(x) = 0$ admet, sur l'intervalle
$[0~;~+\infty[$, une unique solution, que l'on note $\alpha$.

**2.** En remarquant que, pour tout réel $x$, $f(-x) = f(x)$, justifier
que l'équation $f(x)=0$ admet exactement deux solutions dans $\R$ et
qu'elles sont opposées.

**Partie B**

Les **serres en forme de tunnel** sont fréquemment utilisées pour la
culture des plantes fragiles; elles limitent les effets des intempéries
ou des variations de température.

Elles sont construites à partir de plusieurs arceaux métalliques
identiques qui sont ancrés au sol et supportent une bâche en plastique.

Le plan est rapporté à un repère orthonormé d'unité 1 mètre. La fonction
$f$ et le réel $\alpha$ sont définis dans la **partie A**. Dans la suite
de l'exercice, on modélise un arceau de serre par la courbe
$\mathcal{C}$ de la fonction $f$ sur l'intervalle $[-\alpha~;~+\alpha]$.

On a représenté ci-dessous la courbe $\mathcal{C}$ sur l'intervalle
$[-\alpha~;~+\alpha]$.

![image](./TS-integrales-2)

On admettra que la courbe $\mathcal{C}$ admet l'axe des ordonnées pour
axe de symétrie.

**1.** Calculer la hauteur d'un arceau.

**2.**

**2.a)** Dans cette question, on se propose de calculer la valeur exacte
de la longueur de la courbe $\mathcal{C}$ sur l'intervalle
$[0~;~\alpha]$. On admet que cette longueur est donnée, en mètre, par
l'intégrale :

$$I=\displaystyle\int_0^{\alpha}\sqrt{1+(f'(x))^2}\ dx$$

Montrer que, pour tout réel $x$, on a :
$1+(f'(x))^2=\dfrac{1}{4}(\text{e}^x+\text{e}^{-x})^2$

**2.b)** En déduire la valeur de l'intégrale $I$ en fonction de
$\alpha$.

Justifier que la longueur d'un arceau, en mètre, est égale à :
$\text{e}^{\alpha}-\text{e}^{-\alpha}$.

**Partie C**

On souhaite construire une serre de jardin en forme de tunnel.

On fixe au sol quatre arceaux métalliques, dont la forme est celle
décrite dans la partie précédente, espacés de 1,5 mètre, comme indiqué
sur le schéma ci-dessous.

Sur la façade sud, on prévoit une ouverture modélisée sur le schéma par
le rectangle $ABCD$ de largeur 1 mètre et de longueur 2 mètres.

![image](./TS-integrales-3)

On souhaite connaître la quantité, exprimée en m$^2$, de bâche plastique
nécessaire pour réaliser cette serre.

Cette bâche est constituée de trois parties, l'une recouvrant la façade
nord, l'autre la façade sud (sauf l'ouverture), la troisième partie de
forme rectangulaire recouvrant le toit de la serre.

**1.** Montrer que la quantité de bâche nécéssaire pour recouvrir les
façades sud et nord est donnée, en m$^2$, par :
$$\mathcal{A}=4\int_0^{\alpha}f(x)\ dx-2$$

**2.** On prend $1,92$ pour valeur approchée de $\alpha$. Déterminer, au
m$^2$ près, l'aire totale de la bâche plastique nécessaire pour réaliser
cette serre.

:::

:::exercice Exercice 6: Antilles Guyane spetembre 2019

**[Exercice 3]{.smallcaps} points**

**Commun à tous les candidats**

Soit $g$ la fonction définie sur $]0~;~+\infty[$ par

$$g(x) = 4x - x \ln x.$$

On admet que la fonction $g$ est dérivable sur $]0~;~ +\infty[$ et on
note $g'$ sa dérivée.

**Partie A**

Le graphique ci-contre représente une partie de la courbe représentative
de la fonction $g$ obtenue par un élève sur sa calculatrice. Cet élève
émet les deux conjectures suivantes :

-   il semble que la fonction $g$ soit positive ;

-   il semble que la fonction $g$ soit strictement croissante.

![image](./TS-integrales-4)

L'objectif de cette partie est de valider ou d'invalider chacune de ces
conjectures.

**1.** Résoudre l'équation $g(x) = 0$ sur l'intervalle $]0~;~ +\infty[$.

**2.** Déterminer le signe de $g(x)$ sur l'intervalle $]0~;~ +\infty[$.

**3.** Les conjectures de l'élève sont-elles vérifiées ?

**Partie B**

Dans cette partie, on poursuit l'étude de la fonction $g$.

**1.**

**1.a)** On rappelle que

$$\displaystyle\lim_{t \to + \infty} \dfrac{\ln t}{t} = 0.$$

En déduire que

$$\displaystyle\lim_{x \to 0} x \ln x = 0.$$

**1.b)** Calculer la limite de $g(x)$ lorsque $x$ tend vers $0$.

**2.**

**2.a)** Démontrer que, pour tout réel $x$ strictement positif,
$g'(x) = 3 - \ln x$.

**2.b)** Dresser le tableau de variations de la fonction $g$.

**3.** On désigne par $G$ la fonction définie sur $]0~;~ +\infty[$ par

$$G(x) = \dfrac{1}{4}x^2(9 - 2\ln x).$$

On admet que la fonction $G$ est dérivable sur $]0~;~ +\infty[$.

**3.a)** Démontrer que la fonction $G$ est une primitive de la fonction
$g$ sur $]0~;~ +\infty[$.

**3.b)** L'affirmation suivante est-elle vraie ?

Il n'existe aucun réel $\alpha$ strictement supérieur à 1 tel que
$\displaystyle\int_1^{\alpha} g(x) \:\text{d}x = 0$.

:::