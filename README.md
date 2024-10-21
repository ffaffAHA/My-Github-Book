# 目录  

1 first 1.1和差化积 1.2 Qsome easy replace 2线性表出2.1 线性相关 3两个方程同解  

3.1 已知特征值，求特征向量（  

3.2 [分析]矩阵的对角化:  

4A;特征值；求可逆矩阵P，相应的对角矩阵Λ LO  

4.1实对称矩阵A（含参数），求可逆矩阵P，求对角矩阵A4.2实对称矩阵的正交规范化 4.3  $f(A)$  的特征值及对应的特征向量 11 4.3.1实对称矩阵必可对角化  

5 最最最易错的分解  

5.1  $\frac{x^{2}+c}{(x+a)(x+b)^{2}}$  2 5.2arccos的区间 15 6A的行列变换 18 7方程组同解 19 8函数极限218.1复合函数219数列极限 22 9.1极限存在证明2210连续与可导 23 11  A| 23 11.1克拉默法则 24 12方程实根数 24 12.1 分情况讨论 25 12.2参数分离 25 13 绝对值[X| 27 14中值定理 27 15已知两个方程组的通解，求公共解。2816 sinx与cosx  29 17微分方程 29 17.1二阶，少y 30 17.2  $y(x)\!=\!u(x)g(x)$  的二阶微分方程 30 17.3一个简单的倒带换3117.4高阶K重根 32 18 定积分应用3218.1旋转体体积，非  $y$  轴,  $V=V_{1}-V_{2}$  32 18.2积分比大小 32 19重积分 33 19.1 分段区间3319.2区间相同，二重积分保序性 34 19.3二重积分存在3520积分表  
# 1 first  

题目]设 $n$ 阶可逆矩阵 $A$ 有特征值 $\lambda$ ，对应的特征向量为 $_{\alpha}$ ，证明 $_{\alpha}$ 也是 $A^{-}1$ 对应于 $\cdot\lambda^{-1}$ 的特征向量  
[证明]由题设  $A\,\pmb{\alpha}\,{=}\,\lambda\,\pmb{\alpha}$  ，两边同乘  $A^{-}1$  则  

$\left(A^{-1}\,A\right)\alpha=\lambda\left(A^{-1}\,\alpha\right)\Rightarrow E\,\alpha=\lambda\left(A^{-1}\,\alpha\right)\Rightarrow\alpha=\lambda\left(A^{-1}\,\alpha\right)$ 因为 $A$ 可逆，则 $|A|\!\neq\!0$ .由 $|A|$ 等于特征值之积，故 $\lambda\!\neq\!0$ .综上， $A^{-1}{\pmb\alpha}\!=\!\frac{1}{\lambda}{\pmb\alpha}$ .故 $\cdot_{\alpha}$ 也是 $A^{-}1$ 对应于 $\lambda^{-1}$ 的特征向量。 $A^{-1}\alpha\!=\!\frac{1}{\lambda}\alpha$  

$$
{\cal A}\!=\!\alpha\alpha^{T}\qquad{\cal A}\alpha\!=\!\alpha(\alpha^{T}\!\alpha)
$$  

$$
\alpha\alpha^{t}\!=\!k
$$  

# 1.1和差化积  

和差化积公式： $\sin(\alpha)+\sin{(\beta)}=2\sin\left({\frac{\alpha+\beta}{2}}\right)\cos\left({\frac{\alpha-\beta}{2}}\right)$  

$$
\begin{array}{c}{{\sin{\left(\alpha\right)}+\sin{\left(\beta\right)}\!=\!2\sin\left(\displaystyle\frac{\alpha+\beta}{2}\right)\cos\left(\displaystyle\frac{\alpha-\beta}{2}\right)}}\\ {{\sin{\left(\alpha\right)}-\sin{\left(\beta\right)}\!=\!2\cos\left(\displaystyle\frac{\alpha+\beta}{2}\right)\sin\left(\displaystyle\frac{\alpha-\beta}{2}\right)\!\cos\left(\alpha\right)}+\cos{\left(\beta\right)}\!=\!2\cos\left(\displaystyle\frac{\alpha+\beta}{2}\right)\cos\left(\displaystyle\frac{\alpha-\beta}{2}\right)}}\\ {{\cos{\left(\alpha\right)}-\cos{\left(\beta\right)}\!=\!-2\sin\left(\displaystyle\frac{\alpha+\beta}{2}\right)\sin\left(\displaystyle\frac{\alpha-\beta}{2}\right)}}\end{array}
$$  

[帮助记忆]  

方法1.可以只记第一个公式，将其它公式用诱导公式化成 $\sin\left(\alpha\right)\!+\!\sin\left(\beta\right)$ 的形式。方法 2.找规律。前两个公式是 sin和cos异名函数乘积，后两个公式是同名函数乘积。  

口诀：  

正加正，正在前，  
余加余，余并肩。正减正，余在前，余减余，负正弦。  

1.2 some easy replace  

(%i14） tm_plot2d([log(1+t),t/(1+t)],[t,0,0.5])  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/bc74f1899d1a513c387eb1514e877a2fa7fed3aab8075cc674ccda815ed22162.jpg)  

(%014) true  

# 2线性表出  

[2003年真题]设向量组 $I{:}\alpha_{1},\alpha_{2},.\,.\,.\,.\,.\,,\alpha_{t}$ 可由向量组 $I I\colon\beta_{1},\beta_{2},.\,.\,.\,.\,.\,\beta_{s}$ 线性表示，则

 $\mathcal{A}$  .当  $t<s$  时，向量组  $I I$  必线性相关 B.当  $t>s$  时，向量组  $I I$  必线性相关  
$\mathbb{C}$ 当 $t<s$ 时，向量组 $I$ 必线性相关  

D.当 $t>s$ 时，向量组 $I$ 必线性相关  

[简解］根据定理："若  $\alpha_{1},\alpha_{2},\cdot\cdot\cdot,\alpha_{t}$  可有  $\beta_{1},\beta_{2},\cdots,\beta_{s}$  线性表出，且  $t>s$  则  $\alpha_{1},\alpha_{2},\cdot\cdot\cdot$   $\alpha_{t}$  必线性相关  

即若多数向量可以由少数向量线性表出，则此多数向量必线性相关，故选D 若 $A$ 为 $m\times n$ 矩阵，则以下哪个选项是正确的？  

A.若 $n\!>\!m$ ,由 $A$ 的行秩是行极大线性无关组的向量个数≤行向量组的总向量个数 $=m$ 则 $r(A)\!=\!m$ B.由 $A$ 的行秩是行极大线性无关组的向量个数 $\c=$ 行向量组的总向量个数 $\scriptstyle{\dot{=}}m$ 则  $r(A)\leq m\ \mathbb{C}.\ A$  的列秩是列极大线性无关组的向量个数  $=$  列向量组的总向量个数  $=\!n$  ，则  $r(A)\!=\!n$  D.  $A$  的列秩是列极大线性无关组的向量个数≤列向量组的总向量个数  $\scriptstyle{:=n}$  则  $r(A)\!\leq$   $n$  

因为 $r(A)\!=\!A$ 的行秩 ${=}A$ 的列秩，而 $A$ 的列秩是列极大线性无关组的向量个数 $\leq$ 列向量组的总向量个数  $\scriptstyle{:=n}$  .同理  $A$  的行秩是行极大线性无关组的向量个数  $\leq$  行向量组的总向量个 数 $\scriptstyle{:=m}$ .综上， $r(A)\!\leq\ \!\operatorname*{min}\,\left(m,n\right)$ 即有 $r(A)\leq n$ .选D  

其余选项：  

A:只能得出 $r(A)\!\leq\!m$  

B：A的行秩是行极大线性无关组的向量个数<行向量组的总向量个数 $\mathrm{=}m$  

# 2.1线性相关  

由特征值的定义  
有 $\left[A\left(\lambda_{2}\,\alpha_{1}\right)\!,A\left(\lambda_{1}\,\alpha_{2}\right)\right]\!=\!\left[\lambda_{1}\,\lambda_{2}\,\alpha_{1},\lambda_{1}\,\lambda_{2}\,\alpha_{2}\right]$ 极大线性无关组中所含向量的个数 $r$ 称为向量组的秩，因此需判定 $[\lambda_{1}\,\lambda_{2}\,\alpha_{1},\lambda_{1}\,\lambda_{2}\,\alpha_{2}]$ 中的线性无关向量。  

由互不相同的特征值对应的特征向量线性无关，则 $\alpha_{1}$ 与 $\alpha_{2}$ 线性无关  

当 $\lambda_{1}\!\neq\!0,\lambda_{2}\!\neq\!0\!\Rightarrow\!\lambda_{1}\,\lambda_{2}\!\neq\!0.$ 则 $\lambda_{1}\,\lambda_{2}\,\alpha_{1}\!\neq\!0,\lambda_{1}\,\lambda_{2}\,\alpha_{2}\!\neq\!0$ 故 $\cdot\lambda_{1}\lambda_{3}\alpha_{1}$ 与 $\lambda_{1}\lambda_{3}\alpha_{3}$ 线性无关向量组  $A\left(\lambda_{2}\alpha_{1}\right)\!,A\left(\lambda_{1}\,\alpha_{3}\right)$  的秩为2.  

${\heartsuit}\alpha_{1}$ 和 $A\left(\alpha_{1}\!+\!\alpha_{2}\right)$ 线性无关 ${\Leftrightarrow}r(\alpha_{1},\lambda_{1}\,\alpha_{1}+\lambda_{2}\,\alpha_{2})\,=2{\circ}$ 这是因为 $\alpha_{1}$ 和 $\alpha_{2}$ 是不同特征值的特征向量，所以它们线性无关，即 $r(\alpha_{1},\alpha_{2})\!=\!2c$ ，要使 $r(\alpha_{1},\lambda_{1}\,\alpha_{1}+\lambda_{2}\,\alpha_{2})\!=\!2$ ，必须保证  $\lambda_{2}\!\neq\!0$  ，这样矩阵  $\left[\begin{array}{l l}{1}&{\lambda_{1}}\\ {0}&{\lambda_{2}}\end{array}\right]$  的秩才能为  $2\circ$  Z  

$\heartsuit$ 设 $A\!=\!(\alpha_{1},\alpha_{2},\alpha_{3})$ 是三阶矩阵， $A^{*}$ 为 $A$ 的伴随矩阵，若 $(0,2,1)^{\mathrm{T}}$ 是方程组 $A\mathbf{x}\!=\!0$ 的一个基础解系，则 $A^{*}\mathbf{x}=0$ 的基础解系可为  

A.  $\alpha_{1}\textit{B.}\alpha_{1},\alpha_{2}\textit{C.}\alpha_{2},\alpha_{3}\textit{D.}\alpha_{1},\alpha_{2},\alpha_{3}$  

[分析]没有具体的线性方程组，先用秩来决定线性无关解的个数，再用 $A\,B=O$ 来得到解向量。  

[解答］用秩来决定线性无关解的个数：因为  $A\mathbf{x}\!=\!0$  只有1个线性无关的解，即  $n-$   $r(A)\!=\!1,n\!=\!3.$ 从而 $r(A)\!=\!2$ .由 $r(A)\!=\!2\!=\!n-1$ 则 $r(A^{*})\!=\!1$ .有 $\begin{array}{r}{n-r(A^{*})\!=\!3-1\!=\!2.}\end{array}$ 故 $A^{*}\mathbf{x}=0$ 的基础解系中有2个线性无关的解向量。  

用  $A\,B=O$  来得到解向量：由  $A\mathbf{x}\!=\!0$  有非零解，则  $|A|\!=\!0$  由  $A^{*}\,A\!=\!\left|A\right|E$  及  $|A|\!=\!0$  有 $A^{*}\,A\!=\!O$ ,则 $A$ 的列向量全是 $A^{*}\mathbf{x}=0$ 的解。  

而秩 $r(A)\!=\!2$ 故 $A$ 的列向量中必有2个线性无关。需找到这2个线性无关的列向量：  

$$
\begin{array}{r}{!A\!\left[\begin{array}{l}{0}\\ {2}\\ {1}\end{array}\right]\!=\!0,\sharp\!\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\!\!\left[\begin{array}{l}{0}\\ {2}\\ {1}\end{array}\right]\!=\!0,}\end{array}
$$  

综上， $\alpha_{1},\alpha_{2}$ 无关， $\alpha_{1},\alpha_{3}$ 无关。选B  
M[2011年真题)设 $A\!=\!(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4})$ 是四阶矩阵， $A^{*}$ 为 $A$ 的伴随矩阵，若 $(1,0,1,0)^{\mathrm{T}}$ 是方程组 $A\mathbf{x}\!=\!0$ 的一个基础解系，则  

$A^{*}\mathbf{x}=0$ 的基础解系可为  

$$
A.~\alpha_{1},\alpha_{3}~~B.~~\alpha_{1},\alpha_{2}~~~C.~~\alpha_{1},\alpha_{2},\alpha_{3}~~\mathcal{D}.~\alpha_{2},\alpha_{3},\alpha_{4}
$$  

[分析]没有具体的线性方程组，先用秩来决定线性无关解的个数，再用 $A\,B=O$ 来得到解向量。  

[解答］用秩来决定线性无关解的个数：因为  $A\mathbf{x}\!=\!\mathbf{0}$  只有1个线性无关的解，即  $\mathbfit{n}-$   $r(A)\!=\!1,n\!=\!4,$ 从而 $r(A)\!=\!3$ 由 $r(A)\!=\!3\!=\!n-\!1,$ 则 $r(A^{*})\!=\!1$ 有 $\scriptstyle n\,-\,r\left(A^{*}\right)\,=\,4\,-\,1\,=\,3$ 故 $A^{*}\mathbf{x}\!=\!0$ 的基础解系中有3个线性无关的解向量。用 $A B\!=\!O$ 来得到解向量：由 $A\mathbf{x}\!=\!0$ 有非零解，则 $|A|\!=\!0$ .由 $A^{*}A\!=\!\left|A\right|E$ 及 $|A|\!=\!0$ 有 $A^{*}A\!=\!O$ 则 $A$ 的列向量全是 $A^{*}\mathbf{x}\!=\!0$ 的解。而秩 $r(A)\!=\!3$ 故 $A$ 的列向量中必有3个线性无关。  

需找到这3个线性无关的列向量！由 $A{\left[\begin{array}{l}{1}\\ {0}\\ {1}\\ {0}\end{array}\right]}\,{=}\,0.$ 即 $\begin{array}{r}{\left(\alpha_{1},\alpha_{2},\alpha_{3},\alpha_{4}\right)\left[\begin{array}{l}{1}\\ {0}\\ {1}\\ {0}\end{array}\right]=0,}\end{array}$ 则 $\alpha_{1}+\alpha_{3}\!=\!0$ ，即 $\alpha_{1},\alpha_{3}$ 相关。综上  

综上， $\alpha_{2},\alpha_{3},\alpha_{4}$ 无关。  

选D.  

# 3两个方程同解  

线性无关的解的个数相同  $=>$  系数矩阵的秩相同  

基础解系相同  

$$
\begin{array}{r l}&{\left(\!\!\!\begin{array}{c}{\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!
$$  
由方程组同解，则 $n-r(B)\!=$ 方程 (1I)线性无关解的个数 $=$ 方程 (1)线性无关解的个数  $=$  方程(1)线性无关解的个数  $=\!n-r(A)$  ，即  $r(B)\!=\!r(A)$  .因 为 $r(B)\!\le\!2$ 则 $r(A)\leq2$ 即 $|A|\!=\!0$ ，有  

$\begin{array}{l l l}{{1}}&{{3}}&{{3}}\\ {{2}}&{{4}}&{{6}}\\ {{1}}&{{a}}&{{1}}\end{array}=\left|\begin{array}{l l l}{{1}}&{{3}}&{{3}}\\ {{0}}&{{-2}}&{{-4}}\\ {{0}}&{{-1}}&{{0}}\end{array}\right|=4\left(a-1\right)=0.$  则  $a\!=\!1$  

$$
A\mathrm{B}\!=\!O\qquad r(A)+r(B)\!\leqslant\!\operatorname*{min}\left\{r(A),r(B)\right\}
$$  

由于 $A,B$ 均非零，故 $r(A)\!>\!0$ 且 $r(B)\!>\!0$ 即 $r(A)\!\ge\!1,r(B)\!\ge\!1$ 由于 $A B\!=\!O$ 且 $A$ 是 $5\times4,B$ 是 $4\times6$ 矩阵，则 $r(A)\!+\!r(B)\!\leq\!4.$ 代入 $r(A)\!\ge\!1$ 有 $r(B)\!\leq\!4\!-\!r(A)\!\leq\!3.$ 因为已得出 $r(B)\!\ge\!1$ 则  $1\leq r(B)\leq3$  

过  $D$  

$\mathrm{AB}{=}\mathrm{O}$ 时的秩:若 A是 $\mathrm{m}\!\times\!\mathrm{n}$ 矩阵,B是 $\mathrm{n\timess}$ 矩阵， $\mathrm{AB}{=}\mathrm{O}$ ,则 $\mathrm{r(A){+}r(B){\leq}n}$  

已知 $\upalpha_{1},\upalpha_{2},\upalpha_{3}$ 线性无关，则 $[\alpha_{1},\alpha_{2},\alpha_{3}]$ 可逆，又有 $\mathrm{A}\upalpha_{1}$ ， $\mathrm{A}\upalpha_{2}$  $\mathrm{A}\upalpha_{3}$ 的表达式，想到相似，即 $\scriptstyle\mathrm{AP=PB}\Leftrightarrow\mathrm{P^{-1}A P=B}$  

1  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/573a36ce7b46c63b8e6f2718dbabf3617e614baf31b32f6d7ba589900e2f360d.jpg)  

列向量线性无关，可逆， $\mathrm{AP}\,{=}\,\mathrm{PB}\,{\Leftrightarrow}\,P^{-1}\mathrm{AP}\,{=}\,B$  

$$
A\!\sim\!B;A_{\lambda}\!=\!B_{\lambda}
$$  

$$
|\lambda E-A|\!=\!O
$$  
# 3.1已知特征值，求特征向量 $\heartsuit$  

A系数矩阵，行最简形矩阵，自由未知量 $x_{x}$ 0；得到基础解系即属于特征值 $\lambda_{x}$ 的特征向量-代入每个 $\rangle_{\mathrm{i}}$ ，得到线性方程组 $(\mathrm{\lambda_{i}E_{-}A})\mathbf{x}{=}0.$ 通解即对应 $\rangle_{\mathrm{i}}$ 的全体特征向量（除去0向量）  

1.当 $\lambda_{1}\!=\!\lambda_{2}\!=\!1$ 时，由 $(E-B){\bf x}\!=\!0$ ,系数矩阵 $E-B\!=\!\!\left[\begin{array}{c c c}{{0}}&{{0}}&{{0}}\\ {{-1}}&{{-1}}&{{-2}}\\ {{-1}}&{{-1}}&{{-2}}\end{array}\right]\!\rightarrow\!\!\left[\begin{array}{c c c}{{1}}&{{1}}&{{2}}\\ {{0}}&{{0}}&{{0}}\\ {{0}}&{{0}}&{{0}}\end{array}\right]$ 令 $x_{2},x_{3}$ 为自由未知量， $x_{1}$ 为独立未知量。令 $x_{2},x_{3}$ 为自由未知量， $x_{1}$ 为独立未知量。令 $x_{2}\!=\!1,x_{3}\!=\!0.$ 则 $x_{1}\!=\!-1$ .令 $x_{2}\!=\!0,x_{3}\!=\!1$ 则 $x_{1}\!=\!-2$ .故 $\eta_{1}\!=\!(-1,1,$  $))^{T},\eta_{2}\!=\!(-2,0,1)^{T}$ 是一个基础解系，即属于特征值 $\lambda_{1}\!=\!\lambda_{2}\!=\!1$ 的两个线性无关的特征向量。2.当 $\lambda_{3}\!=\!4$ 时，由 $(4\,E-B){\bf x}\!=\!0$ ,系数矩阵 $4E-B\!=\!\!\left[\begin{array}{c c c}{{3}}&{{0}}&{{0}}\\ {{-1}}&{{2}}&{{-2}}\\ {{-1}}&{{-1}}&{{1}}\end{array}\right]\!\to\!\!\left[\begin{array}{c c c}{{1}}&{{0}}&{{0}}\\ {{0}}&{{1}}&{{-1}}\\ {{0}}&{{0}}&{{0}}\end{array}\right]$ 令 $x_{3}$ 为自由未知量， $x_{1},x_{2}$ 为独立未知量。令 $x_{3}\!=\!1$ ，则 $x_{2}\!=\!1,x_{1}\!=\!0.$ 故 $\eta_{3}\!=\!(0,1,1)^{\mathrm{T}}$ 是一个基础解系，即属于特征值 $\lambda_{\mathrm{3}}\,{=}\,4$ 的一个特征向量。综上， $\eta_{1},\eta_{2},\eta_{3}$ 为三个线性无关的特征向量。选 $D$  

# 3.2「分析]矩阵的对角化：  

令 $A$ 的特征值为 $\lambda_{1},\lambda_{2},\cdot\cdot\cdot,\lambda_{n}$ 设 $A$ 有 $n$ 个线性无关的特征向量 $\alpha_{\mathrm{1}},\alpha_{\mathrm{2}},\cdot\cdot\cdot,\alpha_{n}$ ，  
取 $P=[\alpha_{1},\alpha_{2},\cdot\cdot\cdot,\alpha_{n}].$ 则有 $P^{-1}A\,P\!=\!\Lambda$ ,其中 $\Lambda\,{=}\,\left[\begin{array}{c c c c c}{{\lambda_{1}}}&{{}}&{{}}&{{}}&{{}}\\ {{}}&{{\lambda_{2}}}&{{}}&{{}}&{{}}\\ {{}}&{{}}&{{\ddots}}&{{}}&{{}}\\ {{}}&{{}}&{{}}&{{}}&{{\lambda_{n}}}\end{array}\right].$  

[解答注意 $P$ 的每一列为一个特征向量，且 $P$ 中 $\alpha_{1},\alpha_{2}$ ,(cdotp)(cdotp)(cdotp), $\alpha_{n}$ 排列次序应与 $\Lambda$ 中 $\lambda_{1},\lambda_{2}$ (cdotp)(cdotp)(cdotp), $\lambda_{n}$ 的排列次序一致。  

<with|color|red|[解答]>  

# 4A：特征值；求可逆矩阵P，相应的对角矩阵  $\Lambda$  

[1999年真题]设矩阵 $A\!=\!\!{\left[\begin{array}{l l l}{3}&{2}&{\!\!-2}\\ {0}&{\!\!-1}&{0}\\ {4}&{2}&{\!\!-3}\end{array}\right]},$ 已知 $A$ 的特征值  

为1，-1,-1.求可逆矩阵 $P$ ，使得 $P^{-1}\,\mathrm{AP}\,{=}\,\Lambda$ 为对角矩阵？  

并求出相应的对角矩阵。  

# 4.1实对称矩阵 $\mathbf{A}$ （含参数），求可逆矩阵 $\mathbf{P}$ ，求对角矩阵 $\Lambda$  

[2002年真题设实对称矩阵 $A\,{=}\,{\left|\begin{array}{l l l}{a}&{1}&{1}\\ {1}&{a}&{-1}\\ {1}&{-1}&{a}\end{array}\right|}.$ 求可逆矩阵 $P$ ，使 $P^{-1}A\,P$ 为对角阵。  

$|\lambda E-A|\!=\!O$  ；求特征值  $\lambda_{n}$   $\Lambda\,\,\checkmark$  ;代入A，化最简阶梯形矩阵，自由未知数  $X_{n}{:}{\mathrm{q1}}{\rightarrow}$  得 到基础解系(特征向量)  $P$  

1.求特征值：  

$$
\begin{array}{r l}&{\quad\frac{\operatorname{\lambda}}{\operatorname{\lambda}}\ddag\hat{\mathbb{H}}\ddot{\mathcal{H}}\ddot{\mathcal{H}}\ddag\hat{\mathbb{H}}\ddot{\mathcal{H}}\ddag\hat{\mathbb{H}}\cdot\left|\lambda\,E-A\right|=\left|\begin{array}{c c c}{\lambda-a}&{-1}&{-1}\\ {-1}&{\lambda-a}&{1}\\ {-1}&{1}&{\lambda-a}\end{array}\right|=\left|\begin{array}{c c c}{\lambda-a-1}&{\lambda-a-1}&{0}\\ {-1}&{\lambda-a}&{1}\\ {0}&{a+1-\lambda}&{\lambda-a-1}\end{array}\right|}\\ &{=\!(\lambda-a-1)^{2}\left|\begin{array}{c c c}{1}&{1}&{0}\\ {-1}&{\lambda-a}&{1}\\ {0}&{-1}&{1}\end{array}\right|=\!(\lambda-a-1)^{2}\left|\begin{array}{c c c}{1}&{1}&{0}\\ {0}&{\lambda-a+1}&{1}\\ {0}&{-1}&{1}\end{array}\right|}\\ &{=\!(\lambda-a-1)^{2}\left(\lambda-a+2\right)}\end{array}
$$  
# 4.2实对称矩阵的正交规范化  

对矩阵 $A$ 执行特征值分解。  

-将得到的特征向量作为矩阵 $Q$ 的列。  

$Q$  $q_{i}$  $q_{i}\!=\!\frac{q_{i}}{\lVert q_{i}\rVert}$ 其中 $\lVert q_{i}\rVert$ 是向量 $q_{i}$ 的欧几里得范数。  

# 4.3 $\pmb{f}(\pmb{A})$ 的特征值及对应的特征向量  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/f65ca5e3139a4e715061ce40f449f763b2cd2c102838f057a99d99a9ca12d060.jpg)  

$A$ 的特征值已知？ $f(A)$ 的特征值是?对应的特征向量变了吗？/  

相似矩阵的性质对应的特征向量是变的  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/57cd04809c36f66290478124fbfd987a74454087447ad6f9d59172f1297a1dd0.jpg)  

# 4.3.1实对称矩阵必可对角化  

注意：特征值相同是任意矩阵相似的必要条件，但只当矩阵实对称时，才是充分条件。即：矩阵相似 $\Rightarrow$ 特征值相同  
特征值相同  $\Rightarrow$ 矩阵相似.实对称矩阵  

$A$ 与 $B$ (实对称矩阵)相似的充分必要条件is $A$ 和 $B$ 的特征值相同 $\rightarrow|\lambda_{b_{n}}E-A|\,{=}\,O$  

# 5最最最易错的分解  

5.1  $\frac{x^{2}+c}{(x+a)(x+b)^{2}}$   $\frac{x^{2}+5}{(x-2)\left(x+1\right)^{2}}\!=\!\frac{A}{x-2}\!+\!\frac{B}{x+1}\!+\!\frac{C}{(x+1)^{2}}.$ （）注意拆项时要写成 $\frac{B}{x+1}\!+\!\frac{C}{(x+1)^{2}}$  $\frac{B}{x+1}$ ,可能不存在满足条件的 $B$  $x^{2}+5=A\,(x+1)^{2}+B\,(x-2)\,(x+1)+C\,(x-2)$  使用留数法：令 $\cdot x=2$ 得 $A\!=\!1$ 同理，令 $x=-1$ ，可得 $C=-2$ 使用赋值法：令 $x\!=\!0$ ,解得 $B\!=\!0$ 即  ${\frac{x^{2}+5}{(x-2)\,(x+1)^{2}}}\!=\!{\frac{1}{x-2}}-{\frac{2}{(x+1)^{2}}}.$  

有理分式：分母能因式分解，含二次式的高次幂，则拆成分子为一次式的项  

$$
\frac{x^{2}-2\,x+2}{(2+x^{2})^{2}}{=}\frac{A\,x+B}{2+x^{2}}{+}\frac{C\,x+D}{(2+x^{2})^{2}}.
$$  

$$
\int\!\mathrm{e^{x.}\frac{x^{2}\!\!-\!\!2x\!+\!2}{(2\!+\!x^{2})^{2}}d x}
$$  

(dbm:17.) kill(all)  

done  

(dbm:18.) eql:  ${\frac{x^{2}-2\,x+2}{(2+x^{2})^{2}}};$  x2.-2.x+2.  $\overline{{(x^{2}.+2.)^{2}}}$  
$$
\begin{array}{l}{{(\mathsf{d b m}\!:\!18\,.)\;\;\mathrm{eq2}\!:\!\displaystyle\frac{a\,x+b}{2+x^{2}}\!+\!\displaystyle\frac{c\,x+d}{(2+x^{2})^{2}}}}\\ {{\displaystyle\frac{a\,x+b}{x^{2}\!-\!2.}\!+\!\displaystyle\frac{c\,x+d}{(x^{2}\!-\!2.)^{2}}}.}\end{array}
$$  

$\mathrm{solve}(\mathrm{eq1}-\mathrm{eq2}\!=\!0,\!\left[a\!=\!-\!\frac{2}{3},b,c,d\right]\!)

$   $\begin{array}{r l}&{\left[\left[a=-\bigg(\cfrac{2.}{3.}\bigg)=\%R26,b=\%R28,c=\%R27,d=-\big(a\,x^{3}.\big)+\big(1.-\%R28\big)\,x^{2}.+\big(-(2.\,a)-\%R28\big)\,x^{3}\right]\right.}\\ &{\left.\%R27-2.\big)\,x-2.\%R28+2.\right]\bigg]}\end{array}

$  

(dbm:18.） eq1:'frac $(\mathbf{x}\mathbf{\hat{\Sigma}}2\mathbf{\Sigma}\mathbf{-}\mathbf{\Sigma}2\mathbf{*}\mathbf{x}\mathbf{\hat{\Sigma}}+\mathbf{\Sigma}2$ ， $(2\ +\ \mathtt{x}\hat{\ }2)\hat{\ }2)$ ·

 $\operatorname{frac}(x^{2}.-2.\,x+2.,(x^{2}.+2.)^{2}.)

$  

(dbm:18.) eq2: 'frac(ax + b,  $\smash{2\ +\ \mathbf{x}\widehat{\mathbf{\omega}}^{2}}.$   $^+$  'frac(  $\mathsf{c x\ +\ d}$  ，  $(2\ +\ \mathtt{x}\hat{\ }2)\hat{\ }2)

$   $\operatorname{frac}(d+\operatorname{ex},(x^{2}.+2.)^{2}.)+\operatorname{frac}(b+\operatorname{ex},x^{2}.+2.)

$  

(dbm:18.） sol: linsolve([eq1 - eq2]，[a,b,C，d]);  

$\heartsuit$ 含 $\sqrt{\frac{\mathrm{ax+b}}{\mathrm{cx+d}}}$ 的积分，命 $\sqrt{\frac{\mathrm{ax+b}}{\mathrm{cx+d}}}{=}\mathrm{t}$ 原式 $\mathrm{\Gamma=\!\int_{2}^{8}\!\sqrt{\frac{x{-}2}{3x}}\ d x=\int_{0}^{\frac{1}{2}}\!\frac{12t^{2}}{(3t^{2}\!{-}1)^{2}}\ d t.}

$  $\frac{t^{2}}{(3\,t^{2}-1)^{2}}=\frac{t^{2}}{(\sqrt{3}\,t-1)^{2}\,(1+\sqrt{3}\,t)^{2}}$ 是有理分式,分母能因式分解 $:\!\frac{t^{2}}{(3\,t^{2}-1)^{2}}=\frac{A}{\sqrt{3}\,t-1}\;+

$  ${\frac{B}{({\sqrt{3}}\,t-1)^{2}}}+{\frac{C}{{\sqrt{3}}\,t+1}}\,+\,{\frac{D}{({\sqrt{3}}\,t+1)^{2}}}.

$  

(dbm:3.) f(a):=sqrt((a-2)/(3\*a))  $f(a)\mathrel{\mathop:}=\sqrt{\frac{a-2.}{3.\,a}}

$  

$(\mathtt{d b m}\!:\!3\,.\,)\,\,\,\operatorname{jf}(a)\!:=\!\,\operatorname{integrate}(\,f(a),a,2,8)

$   $\operatorname{jf}(a)\!:=\!\operatorname{iint}(a),a,2.,8.)$  
(dbm:3.) jf(a)

  ${\frac{-\log\left({\sqrt{2.}}\,{\sqrt{6.}}+4.\right)+\log\left({\sqrt{2.}}\,{\sqrt{6.}}-4.\right)-\log\left(-1.\right)+2.^{\frac{3.}{2.}}{\sqrt{6.}}}{\sqrt{3.}}}

$  

(dbm:3.） zk(a):  $=$  integrate(f(a),a)  

$$
\mathrm{zk}(a)\!:=\!\mathrm{iint}_{}\!\!\!(f(a),a)
$$  

(dbm:3.) expand(zk(a))

  ${\frac{\sqrt{1.-{\frac{2.}{a}}}\,a}{\sqrt{3.}}}-{\frac{\log\left({\sqrt{1.-{\frac{2.}{a}}}}+1.\right)}{\sqrt{3.}}}+{\frac{\log\left({\sqrt{1.-{\frac{2.}{a}}}}-1.\right)}{\sqrt{3.}}}

$  

(dbm:3.) factor(zk(a))

  ${\frac{\sqrt{\frac{a-2.}{a}}\,a-\log\left({\sqrt{\frac{a-2.}{a}}}+1.\right)+\log\left({\sqrt{\frac{a-2.}{a}}}-1.\right)}{\sqrt{3}.}}

$  

(dbm:3.) fullratsimp(zk(a))  

$$
{\frac{\sqrt{\frac{a-2.}{a}}\,a-\log\left({\sqrt{\frac{a-2.}{a}}}+1.\right)+\log\left({\sqrt{\frac{a-2.}{a}}}-1.\right)}{\sqrt{3}.}}
$$  

(dbm:3.） \int_0\~{\frac{1}{2}}\frac{12t\~2}{\left(3t\~2-1\right)\~2} mathrm{d}t.  

incorrect syntax: { is not an infix operator \int_O\~{\frac{  

$$
(\mathrm{d bm:3\,.})\,\,\,\mathrm{hy}(t){\mathrel{:=}}\frac{12\,t^{2}}{(3\,t^{2}-1)^{2}}
$$  
$$
\mathrm{jf}(t)\!:=\!\mathrm{integrate}\bigg(\mathrm{hy}(t),t,0.,\frac{1.}{2.}\bigg)
$$  

(dbm:3.）1 fullratsimp(jf(t))

  $\frac{{\sqrt{3.}}\log\left({7.}-{4.}\,{\sqrt{3.}}\right)+12.}{3.}

$  

(dbm:3.) trace(hy(t)) trace: argument is apparently not a function or operator: hy(t) 一  

(dbm:3.) step(hy(t))  

incorrect syntax:; is an unknown keyword in a do statement. step(hy(t) ) ;  

求系数  $A,B,C,D.$  (1)两侧同乘  $({\sqrt{3}}\,t-1)^{2}\,({\sqrt{3}}\,t+1)^{2}$  ，得 t  $\begin{array}{r}{\mathrm{\Sigma}^{2}\!=\!A\cdot\!\left(\sqrt{3}\,t-1\right)\!\left(\sqrt{3}\,t+1\right)^{2}\!+\!B\cdot\!\left(\sqrt{3}\,t+1\right)^{2}\!+C\cdot\!\left(\sqrt{3}\,t+1\right)\!\left(\sqrt{3}\,t-1\right)^{2}\!+D\cdot\!\left(\sqrt{3}\,t-1\right)^{2}\!.}\end{array}$   $t\!=\!\frac{\sqrt{3}}{3}$ 可得 $B\!=\!\frac{1}{12}$  $t\!=\!-\frac{\sqrt{3}}{3}$ 可得 $D\!=\!\frac{1}{12}$ 使用赋值法：分别令 $t\!=\!0$ 和 $t\,{=}\,\sqrt{3}$   $B$   $D$   $A\!=\!{\frac{1}{12}},C\!=\!-{\frac{1}{12}}

$  

# 5.2arccos的区间  

(dbm:5)  $\operatorname{ac}(x)\!:=\!\operatorname{acos}(\cos(x))$   $\operatorname{as}(x)\!:=\!\operatorname{asin}(\sin(x))

$  

$$
\begin{array}{l}{{\mathrm{ac}(x):=\operatorname{arccos}\left(\cos\left(x\right)\right)}}\\ {{\ }}\\ {{(\mathrm{d bm}\!:\!5)\ \ \mathrm{tm\_plot2}d([\mathrm{ac}(x),\mathrm{as}(x),\sin(x),\cos(x)],[x,\frac{7\,\pi}{2},4\,\pi],[y,-2,3])}}\end{array}
$$  

<image|<tuple|<raw-data>|pdf>[0.618par[l>true  
(dbm:5) tm_plot2d([ac(α),as(c),sin(),cos(c)], [,-3π,3π],[y,-3,4]  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/e274c57a01c039abbf94d71d1e2ef951e23af566f8af703e8aef212cf713e112.jpg)  
true  

(dbm:5) tm_plot2d([ac(α),as(c),acos(c),asin(c)], [,-1,1],[y,-π,π])  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/c9d47bc2ccdf801a99756bb0b41cab9a2882a04df1f007a101c2b00eabf8957b.jpg)  
true  

(dbm:5)  $\operatorname{as}(x)\!:=\!\operatorname{asin}(\sin(x))$  

$$
\displaystyle\mathrm{as}(x)\!:=\!\arcsin{(\sin{(x)})}
$$  

# (dbm:5)  

arcsin的性质:(  $\arcsin\left(\sin x\right))=\left(2\,k-1\right)\pi-x$  , arcsin  $(\sin\left(x\right))=x-2\,k\,\pi$  arcsin  $x$  的值域是  $\left[-{\frac{\pi}{2}},{\frac{\pi}{2}}\right]\arcsin\left(\sin x\right)$   $\left[-{\frac{\pi}{2}},{\frac{\pi}{2}}\right]$   $x_{0}$   $\scriptstyle1\,x_{0}\,=\,\sin x$   $\frac{\pi}{2}+2\,\mathrm{km}\!\le\!x\!\le\!\frac{3\,\pi}{2}+2\,k\,\pi\left(k\in\pi\right)$   $\arcsin\left(\sin\left(x\right)\right)=(2\,k+1)\,\pi-x$   $-{\frac{\pi}{2}}+2\,k\,\pi\leq x\leq$   ${\frac{\pi}{2}}+2\,k\,\pi\left(k\in\mathbb{Z}\right)$   $\arcsin\left(\sin\left(x\right)\right)=x-2\,k\,\pi$  
$x\in\left[-{\frac{\pi}{2}},{\frac{\pi}{2}}\right]\arcsin\left(\sin x\right)=x.$  

类似的  $\operatorname{arccos}x$  的值域是  $[0,\pi]$  对  $-\pi+2\,k\,\pi\leq x\leq2\,k\,\pi\,(k\in\mathbb{Z})$  有arccos  $\left(\cos\left(x\right)\right)\,=\,2\,k\,\pi\,-$   $x$ 对 $2\,k\,\pi\leq x\leq\pi+2\,k\,\pi\,(k\in\mathbb{Z})$ 有  

arccos $\left(\cos\,(x)\right)=x-2\,\pi(x$ 特别的,对于 $x\in[0,\pi]$ 对于 $x\in[0,\pi]$ 的,对于 $x\in[0,\pi]$ 的,有arccos $\left(\cos\left(x\right)\right)=2\,k\,\pi-x$ 对 $2\,k\,\pi\leq x\leq\pi+2\,k\,\pi\,(k\in\mathbb{Z})$ 有  

二重积分 $\int_{\frac{5\pi}{2}}^{\frac{8\pi}{3}}\!\mathrm{d}x\int_{-\frac{1}{2}}^{\cos x}\!f(x,y)\mathrm{d}y$ 对应的积分区域为 $D=\left\{(x,y)|\,\frac{5\,\pi}{2}\!\leq\!x\leq\!\frac{8}{3}\,\pi,\,-\frac{1}{2}\!\leq$  $y\!\leq\!\cos x\!\right\}$  $y\,{=}\,-{\frac{1}{2}}$ 上方， $y\,{=}\,\cos\,x$ 下方， $x\!=\!\frac{5\pi}{2}$ 序，将区域 $D$ 写为 $a\!\le\!y\!\le\!b,\varphi_{1}(y)\!\le\!x\!\le\!\varphi_{2}(y)$ 的形式：求 $x$ 右边界.在边界上 $y\!=\!\cos x$ 因 $\frac{5\,\pi}{2}\!\le\!x\!\le\!\frac{8}{3}\pi$   $\left(\cos\,{(x)}\right)=x-2\,\pi.$   $\pmb{x}=\mathbf{arccos}\,\left(\pmb{y}\right)+2\,\pi$  

$$
D=\left\{(x,y)\mid{\frac{5\,\pi}{2}}\!\leq\!x\!\leq\!\operatorname{arccos}{\bigl(}y\bigr)+2\,\pi,\ -\ {\frac{1}{2}}\!\leq\!y\!\leq\!0\,\right\}
$$  

因为 $B$ 可以由 $A$ 经行变换得到， $B=$ （矩阵左乘 $A$ 已知 $A$ 为 $n\left(n\geq2\right)$ 阶可逆矩阵，为书写简洁，不妨设 $A$ 为三阶矩阵。  

根据题设：将 $A$ 的第1 行加到第 2 行得矩阵 $B$ ,则 $B\,{=}\,\left[\begin{array}{l l l}{1}&{0}&{0}\\ {1}&{1}&{0}\\ {0}&{0}&{1}\end{array}\right]A\,{=}\,E_{21}(1)\,A.$ 因此 $B^{-1}\!=\!A^{-1}\,E_{21}(1)^{-1}$ 其中 $E_{2}\,1(1)$ 为倍加初等矩阵。利用倍加初等矩阵的逆矩阵，有 $E_{2}\,1(1)^{-1}\!=\!E_{21}(-1)$ 则 $B^{-}\,1\!=\!A^{-1}\,E_{21}\,(-1)$ 根据定义，有 $A^{-}\,1\!=\!\frac{A^{*}}{|A|},B^{-1}\!=\!\frac{B^{*}}{|B|}$ 从而 $\frac{B^{*}}{|B|}\!=\!\frac{A^{*}}{|A|}\!\;E_{21}(-1)$ 因为将一行（或列）的 $k$ 倍加到另一行 (或列),行列式的值不变，则 $|B|\!=\!|A|$ 故 $B^{*}\!=\!A^{*}\,E_{21}\left(-1\right)$ 即将 $A^{*}$ 的第 2 列从第 1 列中减去得 $B^{*}$ ，答案选D  
[分析]因为所求行列式中含 $\beta_{1}+\beta_{2}.$ 想到 $\vert\alpha_{3},\alpha_{2},\alpha_{1},\beta_{1}+\beta_{2}\vert\!=\!\!\left\vert\alpha_{3},\alpha_{2},\alpha_{1},\beta_{1}\right\vert\!+\!\left\vert\alpha_{3},\alpha_{2},\alpha_{1},\right.$  

$\beta_{2}|$ ．试着将题设转化成等式右边的两项。  

# 6方程组同解  

[2005年真题】已知齐次线性方程组  

(1  $){\left\{\begin{array}{l l}{x_{1}+2\,x_{2}+3\,x_{3}\!=\!0}\\ {2\,x_{1}+3\,x_{2}+5\,x_{3}\!=\!0,\mp\!\mathbb{H}(11){\left\{\begin{array}{l l}{x_{1}+b\,x_{2}+c\,x_{3}\!=\!0}\\ {2\,x_{1}+b^{2}\,x_{2}+(c+1)\,x_{3}\!=\!0}\end{array}\right.}}\end{array}\right.}$  同解, 则  $a+b+c\!=$  

$A.\;3\;\;B.\;5\;\;\mathrm{C.\;3}$ 或5D.2或5  

[分析]方程组同解，则1.线性无关解的个数相同  $\Rightarrow$  系数矩阵的秩相同；2.基础解系相 同[解答令方程组 $(\mathrm{l})$ 的系数矩阵为 $A\!=\!\left[{\begin{array}{l l l}{1}&{2}&{3}\\ {2}&{3}&{5}\\ {1}&{1}&{a}\end{array}}\right]\!.$  

令方程组 (II)的系数矩阵为 $\boldsymbol{B}\!=\!\left[\begin{array}{c c c}{1}&{b}&{c}\\ {2}&{b^{2}}&{c+1}\end{array}\right]$ 中十印如同知则的 $\mathbf{\Psi}(x)=(x,y)=(x,y)$  

由方程组同解，则 $n\!-\!r(B)\!=$ 方程 (II)线性无关解的个数 $=$ 方程 (II)线性无关解的个数 $=\!n-r(A)$ ，即 $r(B)\!=\!r(A)$ .因为 $r(B)\leq2$ 则 $r(A)\leq2.$ 即 $|A|\!=\!0$ 有 $\begin{array}{r}{\begin{array}{c c c}{1}&{2}&{3}\\ {2}&{3}&{5}\\ {1}&{1}&{a}\end{array}=\left|\begin{array}{c c c}{1}&{2}&{3}\\ {0}&{-1}&{-1}\\ {0}&{0}&{a-2}\end{array}\right|=2-a=0,}\end{array}$  则  $a\!=\!2$  

代入 $a\!=\!2$ ,则可以求方程组(1)的解。对 $A$ 高斯消元： ${\left[\begin{array}{l l l}{1}&{2}&{3}\\ {2}&{3}&{5}\\ {1}&{1}&{2}\end{array}\right]}{\rightarrow}{\left[\begin{array}{l l l}{1}&{0}&{1}\\ {0}&{1}&{1}\\ {0}&{0}&{0}\end{array}\right]}$ 则令 $\cdot x_{1}$  $x_{2}$ 为独立未知量， $x_{3}$ 为自由未知量。  

$x_{3}\!=\!1$  ,解得  $x_{2}\!=\!-1,x_{1}\!=\!-1$  

则方程组 $(\mathrm{l})$ 的通解是 $k(-1,-1,1)^{\top},k$ 为任意常数。  

以下由方程组(II)的通解也是 $k(-1,-1,1)^{\top}$ ，求出 $b$ 和 $c$  
注意有两部分：  

$1.\,(-1,-1,1)^{\mathrm{T}}$ 是方程组(II)的解；2.方程组 (II）只有1个线性无关解，即 $r(B)\!=\!2$ 第1部分：  

因为 $(-1,\,\,\,-1,\,\,\,1)^{\top}$ 应当是方程组 (II)的解，代入则得到b， $c$ 的方程组： $\left\{{\begin{array}{l}{-1-b+c\!=\!0}\\ {-2-b^{2}+c\!+\!1\!=\!0}\end{array}}\right.$ 解得 $b\,{=}\,1,c\,{=}\,2$ 或 $b\!=\!0,c\!=\!1$  

第2部分：  

情况一：当 $b\,{=}\,0,c\,{=}\,1$ ,方程组 (Il)为 $\left\{\begin{array}{l}{x_{1}+x_{3}\,{=}\,0}\\ {2\,x_{1}+2\,x_{3}\,{=}\,0}\end{array}\right.$ 有 $r(B)=1$ 从而 $\mathrm{(I)}$ 与 (II)不同解，故 $b\!=\!0,c\!=\!1$ 应舍去。情况二：当 $b\!=\!1,c\!=\!2$ 时，方程组 $\Big(|\mathrm{l}\Big)$ 为 $\left\{\begin{array}{l}{{x_{1}+x_{2}+2\,x_{3}\!=\!0}}\\ {{2\,x_{1}+x_{2}+3\,x_{3}\!=\!0}}\end{array}\right.$ 有 $r(B)\!=\!2$ 从而方程组（II）只有1个线性无关解，即通解是 $k(-1,-1,1)^{\top},$  $k$ 为任意常数(I)与(II)同解。  

故  $a+b+c\!=\!2+1+2\!=\!5.$  选B  

# 7函数极限  

设 $\operatorname*{lim}_{n\to\infty}x_{n}$ 存在,则下列选项哪个是律误的？  

$\operatorname{A}\operatorname*{lim}_{n\to\infty}{\frac{x_{n+1}}{x_{n}}}$ 可能为1B. lim $\frac{x_{n+1}}{x_{n}}$ 可能小于1n—0 C $:\operatorname*{lim}_{n\to\infty}{\frac{x_{n+1}}{x_{n}}}$ 可能大于1  

由lim $x_{n}\!=\!0$ 时, $\frac{0}{0}$ 为不定式,则 $\operatorname*{lim}_{n\to\infty}{\frac{x_{n+1}}{x_{n}}}$  $D$  $n{\longrightarrow}\infty$  

令 $\operatorname*{lim}_{n\to\infty}x_{n}\!=\!a$ ，当 $a\!\neq\!0$ 时,则 $\operatorname*{lim}_{n\to\infty}{\frac{x_{n+1}}{x_{n}}}\!=\!{\frac{x_{n\to\infty}}{\operatorname*{lim}_{n\to\infty}x_{n}}}\!=\!{\frac{a}{a}}\!=\!1$ 故 $A$ 正确。令  $\cdot_{x_{n}=a^{n},\left(|a|<1\right)}$  则  $\operatorname*{lim}_{n\to\infty}x_{n}\!=\!0$  而  $\operatorname*{lim}_{\imath\to\infty}\frac{x_{n+1}}{x_{n}}\!=\!a<\!1$  .故  $B$  正确 7  

【证明 $C$ 错误】  

反证:若 $\left|\operatorname*{lim}_{n\to\infty}\frac{x_{n+1}}{x_{n}}\right|>1.$ ,由保号性,存在 $N$ 使得当 $n>N$ 时 $\left|\frac{x_{n+1}}{x_{n}}\right|>1$ 故 $\operatorname*{lim}_{n\to\infty}x_{n}\!=\!\infty$ 极限不存在，与条件矛盾。  
$$
\mathrm{\operatorname*{lim}_{x\to0^{-}}\frac{\int_{0}^{1}\!\sqrt{2\!\cdot\!2\!\cos\big(2\!\mathrm{xt}\big)}\ \mathrm{dt}}{x}}
$$  

则左导数 $\varphi_{-}^{\prime}(0)=\operatorname*{lim}_{x\to0^{-}}-{\frac{\int_{0}^{1}{\sqrt{2-2\cos\left(2\,\mathrm{x}t\right)}}\,\mathrm{d}t}{x}}=\operatorname*{lim}_{x\to0^{-}}-{\frac{\int_{0}^{2x}{\sqrt{2-2\cos u}}\,\mathrm{d}u}{2\,x^{2}}}=\operatorname*{lim}_{x\to0^{-}}-{\frac{\int_{0}^{1}{\sqrt{2-2\cos u}}\,\mathrm{d}u}{2\,x^{2}}}=0$  ${\frac{2\cdot{\sqrt{2-2\cos\left(2\,x\right)}}}{4\,x}}=\operatorname*{lim}_{x\to0^{-}}-{\frac{2\cdot{\sqrt{4\sin^{2}x}}}{4\,x}}$   $=\operatorname*{lim}_{x\to0^{-}}-{\frac{|\sin x|}{x}}\!=\operatorname*{lim}_{x\to0^{-}}{\frac{\sin x}{x}}\!=\!1$  其中倒数第一个等号使用了 $\sin x$ 的等价无穷小。  

2[2022年真题]当 $x\!\xrightarrow{}\!0$ 时， $\alpha(x),\beta(x)$ 是非零无穷小量，给出以下四个命题  

(1)若  $\alpha(x)\sim\beta(x)$  ,则  $|\alpha^{2}(x)\sim\beta^{2}(x)$  

(2)若  $\alpha^{2}(x)\sim\beta^{2}(x)$  ,则  $\alpha(x)\sim\beta(x)$  (3)若  $\alpha(x)\sim\beta(x)$  ,则  $\alpha(x)-\beta(x)\!=\!o(\alpha(x))$  (4)若  $\alpha(x)-\beta(x)\!=\!o(\alpha(x))$  ，则  $\alpha(x)\sim\beta(x)$   ${\begin{array}{l l}{1.{\cfrac{\alpha}{\beta}}\!=\!1,{\cfrac{\alpha^{2}}{\beta^{2}}}\!=\!1\times\!1\!=\!1}\\ {2.{\begin{array}{l l}{{\cfrac{\alpha^{2}}{\beta^{2}}}\!=\!1}&{{\cfrac{\alpha}{\beta}}\!=\!\pm1}\\ {3}&{{\cfrac{\alpha}{\beta}}\!=\!1}&{{\cfrac{a-\beta}{\alpha}}\!=\!1\!-{\cfrac{\beta}{\alpha}}\!=\!0}\end{array}}}&{{\mathrm{by~}}}\\ {4}&{{\cfrac{\alpha-\beta}{\alpha}}\!=\!0}&{1\!-\!{\cfrac{1}{\cfrac{\alpha}{\beta}}}\!=\!0}&{{\cfrac{\alpha}{\beta}}\!=\!1}\end{array}}$  

$\heartsuit$  wrong usually  

$$
\begin{array}{r l}&{\underset{x\rightarrow+\infty}{\operatorname*{lim}}\frac{\int_{1}^{x}2\,t^{2}\left(\sqrt{1+\frac{1}{t}}-1\right)-t\,\mathrm{d}t}{\int_{1}^{x^{2}}\arcsin\frac{1}{\sqrt{t}}\,\mathrm{d}t}}\\ &{=\underset{x\rightarrow+\infty}{\operatorname*{lim}}\frac{2\,x^{2}\left(\sqrt{1+\frac{1}{x}}-1\right)-x}{2\,x\cdot\arcsin\frac{1}{x}}}\\ &{=\underset{x\rightarrow+\infty}{\operatorname*{lim}}\frac{2\,x^{2}\left(\sqrt{1+\frac{1}{x}}-1\right)-x}{2\,x\cdot\frac{1}{x}}}\end{array}
$$  
$$
\begin{array}{l}{\displaystyle=\operatorname*{lim}_{x\to+\infty}\frac{1}{2}\!\left[2\,x^{2}\!\left(\frac{1}{2\,x}+\frac{\frac{1}{2}\left(-\frac{1}{2}\right)}{2\,x^{2}}+o\!\left(\frac{1}{x^{2}}\right)\right)\!-x\right]}\\ {\displaystyle=\operatorname*{lim}_{x\to+\infty}\frac{1}{2}\!\left[x-\frac{1}{4}+o(1)-x\right]}\\ {\displaystyle=\!-\frac{1}{8}}\end{array}
$$  

# 7.1复合函数  

因为 $\ln{\biggl[}\cos{\biggl(}{\frac{1}{x}}{\biggr)}+2{\biggr]};$ 是复合函数，故利用复合函数的单调性质，“同增异减”。[解答]  

又因为 $x+2$ 单调增加，故cos(1)  

因为 $\frac{1}{x}$ 在 $(1,+\infty)$ 上单调减少，其值域范围是 $(0,1)$ ,且cos $x$ 在 $(0,1)$ 上单调减少，故 $\cos\left({\frac{1}{x}}\right)$   $\left(1,+\infty\right)$  

$+2$ 单调增加；因为 $\ln x$ 单调增加，故 $\ln{\biggl[}\cos{\biggl(}{\frac{1}{x}}{\biggr)}+2{\biggr]}.$ 单调增加。  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/3e6081a5a0ce2f515d67949752f3bcbdf0a962dca3aac69e06fd67866397e692.jpg)  
true  

# 8数列极限  

下列条件中有几个是 $\operatorname*{lim}\to\infty\,x_{n}\!=\!A$ 的充分条件，几个是必要条件？  
$$
\begin{array}{r l}&{(1)\,*l\,i\,m_{n\to\infty}\,\,x_{2n}=\,*l\,i\,m_{n\to\infty}\,\,x_{2n-1}=A.}\\ &{(2)\,*l\,i\,m_{n\to\infty}\,\,x_{3n}\,=\,*l\,i\,m_{n\to\infty}\,\,x_{3n+1}=\,*l\,i\,m_{n\to\infty}\,\,x_{3n-1}=A.}\\ &{(3)\,*l\,i\,m_{n\to\infty}\,\,x_{4n}=\,*l\,i\,m_{n\to\infty}\,\,x_{4n-1}=\,A.}\\ &{(4)\,*l\,i\,m_{n\to\infty}\,\,x_{4n}=\,*l\,i\,m_{n\to\infty}\,\,x_{4n-1}=\,*l\,i\,m_{n\to\infty}\,\,x_{4n-2}=A.}\end{array}
$$  

(1)(2)是充要条件,包含了全部子数列，命题 (4)中,未出现的子数列 $\left\{\mathrm{x_{4n-3}}\right\}$ 可能发散，故原数列可能发散。故不是充分条件。  

8.1极限存在证明设 $f(x)$ 是区间 $\scriptstyle[0,\ +\infty)$ 上单调减少且非负的连续函数， $a_{n}\,=

$  ${\sum_{k}}=1^{n}f(k)-{\int_{1}}^{n}f(x)\ \mathrm{d}x(n\!=\!1,2,\cdots)$ 证明数列 $\left\{a_{n}\right\}$ 的极限存在。「解析]1.证明极限存在，想到用单调有界定理，需要证明 $\{x_{n}\}$ 单调且有界。2.证明数列 $\{x_{n}\}$ 的单调性，需证明对于任意 $n$ ,都有 $x_{n}\!\geq\!x_{n+1}$ 或 $x_{n}\!\leq\!x_{n+1}.\;3.\;f(x)$ 单调减，则有 $f\left(k+1\right)\leq\int_{k}^{k}+1\,f(x)\mathrm{d}x\leq$  $f(k)$  

# 9连续与可导  

cOS，0≤<π, 设函数f(x)=<1，C=π $F(x)\!=\!\int_{0}^{x}\!f(t)\mathrm{d}t$ 则-1， $\pi<x\leqslant2\,\pi$ A. $x=\pi$ 是函数 $F(x)$ 的跳跃间断点A. $x=\pi$ 是函数 $F(x)$ 的跳跃间断点 $B$  $x=\pi$ 是函数 $F(x)$ 的可去间断点 $C$  $F(x)$ 在 $x=\pi$ 处连续但不可导 $D$  $F(x)$ 在 $x=\pi$ 处可导[分析]  $\int_{0}^{x}\!f(t)\ \mathrm{d}t$  是变上限积分,利用变上限积分的性质判断。【知个] [解  

判断连续性：因为 $f(x)$ 除有限个第一类间断点 $(x=\pi)$ ）外处处连续，故 $f(x)$ 可积则 $\int_{0}^{x}\!f(t)\ \mathrm{d}t$ 为连续函数  

判断可导性：变上限积分 $F(x)=\int_{0}^{x}f(t)\mathrm{d}t$ 在某一点的左右导数等于被积函数 $f(x)$ 在这一点的左右极限。由于 $\ \operatorname*{lim}\rightarrow\pi^{-}\ f(x)=\cos\,\pi=-1\ *l\,i\,m_{x\rightarrow\pi^{+}}\,f(x)=-1$ 即 $\operatorname*{lim}_{x}\to$  $\pi^{-}\;f(x)=\operatorname*{lim}_{x\rightarrow\pi^{+}}\,f(x)$  故  $F_{\pi^{-1}}^{'}(x)=F_{\pi^{+}}^{\prime}(x)$  .左右导数相等，故  $F(x)$  在  $x=\pi$  处可导。综 上， $F(x)$ 在 $x=\pi$ 处连续可导，故选 $D$  
10 |A|  

[2013年真题 $]A=\left(\begin{array}{l}{a_{i j}}\end{array}\right)$ 是三阶非零矩阵， $|A|$ 为 $A$ 的行列式 $A_{i j}$ 为 $a_{i}j$ 的代数余子式，若 $a_{i}\,j+A_{i j}\!=\!0\,\;(i,j=1,2,3)$  则  $|A|=$  

$$
a_{\mathrm{ij}}+A_{\mathrm{ij}}=O,a_{\mathrm{ij}}=-A_{\mathrm{ij}},|A|=0,-1;A\neq O;|A|=-1.
$$  

# 10.1 克拉默法则  

设 $n$ 元线性方程组 $A\mathbf{x}=\mathbf{b}$ .其中 $A\,{=}\,\left[\begin{array}{c c c c c c}{4}&{1}&&&\\ {4}&{4}&{1}&&&&&\\ &{4}&{4}&{1}&&&&&\\ &&{\ddots}&{\ddots}&{\ddots}&{\ddots}&\\ &&&{4}&{4}&{1}\\ &&&&{4}&{4}\end{array}\right],\mathbf{x}\,{=}\,\left[\begin{array}{c}{x_{1}}\\ {x_{2}}\\ {\vdots}\\ {x_{n}}\end{array}\right],\mathbf{b}\,{=}\,\left[\begin{array}{c}{1}\\ {0}\\ {\vdots}\\ {0}\end{array}\right]$  已知行列式 $\left|A\right|=\left(n+1\right)2^{n}$ 则 $x_{1}\!=\!\frac{n}{2\left(n+1\right)}$  B.方程组有一解,且  $x_{1}\!=\!\frac{n}{n+1}$  C.方程组有无穷解,且 $\mathbf{x}\!=\!k(1,0,0,...,0)^{\top}$ ,其中 $k$ 为任意常数D.方程组有无穷解,且 $\mathbf{x}\!=\!k(0,1,0,...,0)^{\top}$ ,其中 $k$ 为任意常数由克拉默法则, $|A|\!\neq\!0$ 时 $,\!n$ 元线性方程组有唯一解。由题这 $\left|A\right|=\left(n+1\right)\cdot2^{n},$ ,故方程组有唯-解。又由ke拉默法则,将 $A$ 的第一列替换为 $\mathbf{b}$ ，有1 1 4 1 0 4 4 0 4 4  $x_{1}\!=\!\frac{|a|}{|A|}$  令 $\cdot n$ 阶行列式 $D_{n}\!=\!|A|=\!(n+1)\cdot2^{n}$ ,则按第1列展开: $\begin{array}{r l}&{\begin{array}{c c c c c}{1}&{1}&&&\\ {0}&{4}&{1}&&\\ {0}&{4}&{4}&{\ddots}&\\ {\vdots}&&{\ddots}&{\ddots}&{1}\\ {0}&&&{4}&{4}\end{array}\end{array}=1\cdot D_{n-1}\!=n\cdot2^{n-1}.$  

$\mathrm{x_{1}{=}\frac{n{\cdot}2^{n{\cdot}1}}{(n{+}1){\cdot}2^{n}}{=}\frac{n}{2(n{+}1)}}$  
# 11方程实根数  

[2011年真题]设 $k$ 为参数，则关于方程 $k$ arctan $x-x\!=\!0$ 不同实根的个数，说法正确的是：  

（注：考试中本题型为证明题，选择正确后需要对比详细过程）  

A.若 $k>0$ 则方程有2个实根；若 $k\leq0.$ 则方程有1个实根  

B.若 $k\geq0.$ 则方程有1个实根；若 $k<0$ 则方程有2个实根  

C.若  $k>1$  ,则方程有3个实根；若  $k\le1$  ,则方程有1个实根  

D.若  $k\geq1$  ，则方程有1个实根；若  $k<1$  则方程有3个实根  

[分析]  

判定方程根的个数，一般通过求导判断函数形态，利用单调性和介值定理判定。题目中函数的单调性受到k的影响。此类问题有两种解法：1.分情况讨论：对于不同的 $k$ 判断单调区间的情况；2.分离参数法：先将方程化为 $g(x)=k$ 的形式，再讨论 $g(x)$ 的形态。如果可以分离参数，则尝试分离参数法。如果不能分离参数，或分离参数后 $g(x)$ 的导数不易分析，则使用分情况讨论的方法。本题参数可以分离，得到 $g(x)=k$ 的形式但 $g^{\prime}(x)$ 不容易分析，故建议分情况讨论。  

# 11.1 分情况讨论  

$f(x)$ 的无定义点, $+f^{\prime}(x)$ 的无定义点 ${}+f^{\prime}(x)\!=\!0$ 的点(驻点)  

$f(x)$ 是否为奇函数,偶函数,对称区间， $f(0)\!=\!0?$  

实数解 $\to x=g(k)\to$ 划分单调区间 $\longrightarrow$  

通过单调区间判断函数零点  

先考察各单调区间的端点是否为零点，再考察每个区间内部的零点：  
# 11.2参数分离  

$g(x)\!=\!k$ 的根个数 $\longrightarrow$ 对 $g(x)$ 求导 $\longrightarrow$ 大致绘制 $g(x)$ 的图像(主要 $g(x)$ 在区间的单调情况)和 $g(x)_{\mathrm{min}}$ 和 $g(x)_{\mathrm{max}}$ 或者 $\operatorname*{lim}_{x\rightarrow?}g(x)=$  

$$
\begin{array}{r}{\displaystyle\operatorname*{lim}_{x\to2}f(x)=5}\\ {\quad\quad\quad\quad\quad\quad\quad\sum_{i=1}^{n}\operatorname*{lim}_{x\to x\to\infty}}\\ {\quad\quad\quad\quad\quad\quad\quad\quad\sum_{i=1}^{n}\operatorname*{lim}_{x\to x\to\infty}}\end{array}
$$  

# 12绝对值  $|\mathbf{X}|$  

判断绝对值函数在一点是否可导，有两个重要推论，做选择题时可以直接应用：1. $\varphi(x_{0})\!=\!0$ 且 $\varphi^{\prime}(x_{0})\!\neq\!0\!\Leftrightarrow\!x_{0}$ 是 $|\varphi(x)|$ 的不可导点；  

2. $f(x)=|\varphi(x)|\ g(x),|\varphi(x)|$ 在 $x=x_{0}$ 处不可导但 $\varphi(x)$ 可导，且 $g(x)$ 在 $x=x_{0}$ 处连续，则综上，令 $\cdot\varphi(x)=x^{2}-1,\,g(x)=\sqrt[3]{(x^{2}-1)\,(x-3)}$ 找 $f(x)$ 的不可导点，即1.找 $\varphi(x)=0$  $\varphi^{\prime}(x)\neq0$ 且 $g(x)\neq0$ 的点。2.找 $g(x)\!=\!0$ ， $g^{\prime}(x)\neq0$ 且 $\varphi(x)\neq0$ 的点。 $f(x)$ 在 $x=x_{0}$ 处可导的充要条件是  $g(x_{0})\!=\!0$  

loadfile: 1oading C:\Program Files\XmacsLabs\MoganResearch-1.2.9.5\plugins maxima\lisp\texmacs-maxima.lisp. Loading C: /Users/admin/maxima/maxima-init.mac  

Maxima 5.47.0 https://maxima.sourceforge.ic usingLispSBCL2.3.2 Distributed under the GNU Public License. See the file COPYING. Dedicated to the memory of William Schelter. The function bug-report() provides bug reporting information.  
(%i12) h:sin(x);

 (%012)  sin (c)  

(%i13) h_abs:abs(h);  

(%013) [sin (∞)|  

(%i20) g: x2+  

(%021)  $x^{2}+x

$  

(%i22) ）f:g\*h_abs;  

(%022) (x²+α)|sin()  

(%i28) tm_plot2d([f,h_abs],[x,-4,7])  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/8c8fa9deb0bab79799ba495f7e07e612aa091437a570d0b7cfd8ddc2068bafc1.jpg)  

(%028) true  

(dbm:4) kill(all) done  

$({\sf d b m}\!:\!4)\ \ f\!:\!{\mathrm{abs}}(x^{2}-1)\,\sqrt[3]{(x^{2}-1)\,(x-3)}

$   $(x-3)^{\frac{1}{3}}(x^{2}-1)^{\frac{1}{3}}|x^{2}-1|$  
(dbm:4) tm_plot2d(f,[c,-3,3])  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/06eea0090d9ba0d1fdb4f4d851d8edd83d5f8ee1158ecb0095653750029fd17f.jpg)  

(dbm:4)  

# 13中值定理  

$f(x)$   $f(0)\!=\!3,f(2)\!=\!\frac{3}{2},\operatorname*{min}_{[0,2]}f(x)\!=\!1.$  可以证明存在 $\xi\in(0,2)$ ，使得 $f^{\prime\prime}(\xi)\!\le\!c,(c$ 为常数)求 $c$ 的最小值，使不等式对任意满足条件的 $f(x)$ 都成立。  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/14f395ccfa098404cdfe40ab74aa76ee04096d1eee7a7c8e38929bf8645aca8a.jpg)  
true  

# 14已知两个方程组的通解，求公共解。  

则令通解相等，解关于常数 $k_{1},k_{2},l_{1},l_{2}$ 的新方程组  

[解答]  
设  $\eta$  是方程组(1)与 (ⅡI)的非零公共解，则  

$$
\eta\,{=}\,k_{1}\,\beta_{1}+k_{2}\,\beta_{2}\,{=}\,l_{1}\,\alpha_{1}+l_{2}\,\alpha_{2}.
$$  

那么 $k_{1}\,\beta_{1}+k_{2}\,\beta_{2}-l_{1}\,\alpha_{1}-l_{2}\,\alpha_{2}\!=\!0$ 再代入题设给出的 $\beta_{1},\beta_{2},\alpha_{1},\alpha_{2}$ 由此得齐次方程组(III) $(-k_{2}+l_{2}\!=\!0\ |k_{2}-l_{1}+l_{2}\!=\!0$ 对系数矩阵高斯消元  

$$
k_{1}-l_{1}\!=\!0
$$  

$$
(~k_{2}-l_{2}\!=\!0
$$  

$$
A\!=\!\left[\begin{array}{c c c c}{{0}}&{{-1}}&{{0}}&{{1}}\\ {{0}}&{{1}}&{{-1}}&{{1}}\\ {{1}}&{{0}}&{{-1}}&{{0}}\\ {{0}}&{{1}}&{{0}}&{{-1}}\end{array}\right]\!\to\!\left[\begin{array}{c c c c}{{1}}&{{0}}&{{-1}}&{{0}}\\ {{0}}&{{-1}}&{{0}}&{{1}}\\ {{0}}&{{0}}&{{-1}}&{{2}}\\ {{0}}&{{0}}&{{0}}&{{0}}\end{array}\right]
$$  

则令 $k_{1}\cdot k_{2}\cdot l_{1}$ ·为独立已知 $l_{2}$ ·为自由未知令 ${\cdot}l_{2}\!=\!1$ 则 $(l_{1}\!=\!2,k_{1}\!=\!2,k_{2}\!=\!1$ ，即通解为 $h\left(2,1,2,1\right)^{\top},h$ 为任意常数。  

$$
\mathbb{I}{\left[\begin{array}{l}{k_{1}}\\ {k_{2}}\\ {l_{1}}\\ {l_{2}}\end{array}\right]}={\left[\begin{array}{l}{2\,h}\\ {h}\\ {2\,h}\\ {h}\end{array}\right]}.
$$  

则方程组的公共解为 $\eta=l_{1}\,\alpha_{1}+l_{2}\,\alpha_{2}=2\,h\,\alpha_{1}+h\,\alpha_{2}=h\,(2\,\alpha_{1}+\alpha_{2})=h\,(-1,1,2,1)^{\top},h$ 为任意常数。  

# 15 sinx与cosx  

$n$ 项同类函数乘积，分母包含 $2^{n}$ ，添起始项，来达到连锁消项的目的。  

使用公式：2sin $x$ COS $x\!=\!\sin\,2\,x$  

[解答令 $A\,=\cos{(x)}\cos{(2\,x)}\cdot\cdot\cdot\cos{(2^{n}\,x)}.$  

1.若sin  $x\!\neq\!0$  ,添一项sin  $x$  ，则  

$$
\begin{array}{l}{\sin\left(x\right)A}\\ {=\sin\left(x\right)\cos\left(x\right)\cos\left(2\,x\right)\cdot\cdot\cdot\cos\left(2^{n}\,x\right)}\\ {=\displaystyle\frac{1}{2}\sin\left(2\,x\right)\cos\left(2\,x\right)\cdot\cdot\cdot\cos\left(2^{n}\,x\right)}\end{array}
$$  
$$
\begin{array}{l}{{\displaystyle=\!\frac{1}{2^{2}}\sin\left(4\,x\right)\cdot\cdot\cdot\cos\left(2^{n}\,x\right)}}\\ {{\displaystyle=\!\frac{1}{2^{n+1}}\sin\left(2^{n+1}\,x\right)}}\end{array}
$$  

$n\!\longrightarrow\!\infty$ 时， $\sin\left(2^{n}\!+\!1\,x\right)$ 振荡但有界，即 $-1\!\le\!\sin\left(2^{n+1}x\right)\!\le\!1$ 又 $\operatorname*{lim}_{n\rightarrow\infty}\frac{1}{\gamma^{n+1}}\!=\!0$ ,而sin $x\!\neq\!0$ 为常数  

故  $\operatorname*{lim}_{.}A\,{=}\,0.$  n→8 2.若sin $x\!=\!0$ ,分两种情况， $x\!=\!2\,k\,\pi$ 或 $x\!=\!(2\,k+1)\,\pi.$ 其中 $k\!=\!0,1,2,\cdot\cdot\cdot$ 若 $x\!=\!2\,k\,\pi$ 则lim  $\cdot\,A\,{=}\,\cos\,(2\,k\,\pi)\cos\,(2\,k\,\pi)\cdot\cdot\cdot\cdot\cos\,(2\,k\,\pi)\,{=}\,1\cdot1\cdot\cdot\cdot\cdot\,1\,{=}\,1.$   $n\!\longrightarrow\!\infty$  若 $x=(2\,k+1)\,\pi$ 则 lin  ${\frac{1}{\alpha}}\cdot A=\cos\left(\pi\right)\cos\left(2\,k\,\pi\right)\cdot\cdot\cdot\cdot\cos\left(2\,k\,\pi\right)=(-1)\cdot1\cdot\cdot\cdot\cdot1=-1.$   $n{\longrightarrow}\infty$   $n\!\longrightarrow\!\infty$  

综上，极限存在，可能为 0,1 或-1  

# 16微分方程  

16.1 二阶，少y  

$y^{\prime\prime}\,{-}\,\frac{x+3}{x+1}\,y^{\prime}\,{=}\,0$   $t\,{=}\,y^{\prime}$  

【解答答】  

令 $t\,{=}\,y^{\prime}$ ,有 $y^{\prime\prime}\!=\!\frac{\mathrm{d}y^{\prime}}{\mathrm{d}x}\!=\!\frac{\mathrm{d}t}{\mathrm{d}x}\!=\!t^{\prime}.$  $t^{\prime}\!-\!\frac{x+3}{x+1}\,t\!=\!0$  $\frac{\mathrm{d}t}{\mathrm{d}x}\!=\!\frac{x+3}{x+1}\,t.$  $\frac{\mathrm{d}t}{\mathrm{d}x}\!=\!\frac{x+3}{x+1}t$ 满足 $\frac{\mathrm{d}t}{\mathrm{d}x}\!=f(x)\,g(t)$ 的形式,是可分离变量的一阶微分方程。分离变量,两边积分求解。  
# 16.2 ${\pmb y}({\pmb x})\!={\pmb u}({\pmb x}){\pmb g}({\pmb x})$ 的二阶微分方程  

[2016年真题 $|_{i}$ 设 $\boldsymbol{y}(\boldsymbol{x})\!=\!\boldsymbol{u}(\boldsymbol{x})\,e^{\boldsymbol{x}}$ 是二阶微分方程 $\left(2\,x-1\right)y^{\prime}\prime-\left(2\,x+1\right)y^{\prime}+2\,y=0$ 的解， $u\left(-1\right)\!=\!e,u(0)\!=-1$   $y(1)\,{=}\,a\,e+{\frac{b}{e}}\,{+}\,c,$   $a,b,c$   $a-b+c$  

[分析]将 $y(x)\!=\!u(x)\,e^{x}$ 代入微分方程，得到关于 $u(x)$ 的关系式，由此求出 $u(x)$ 的表达式。  

[解答]由  $y(x)\!=\!u(x)\,e^{x}$  得  $y^{\prime}(x)=u^{\prime}(x)\,e^{x}+u(x)\,e^{x}\!=\!\left[u^{\prime}(x)+u(x)\right]e^{x}.$  

$\heartsuit$ 得到 $\left(2\,x-1\right)u^{\prime\prime}(x)+\left(2\,x-3\right)u^{\prime}(x)\,{=}\,0$ 为不显含 $u$ 的微分方程令 $t\!=\!u^{\prime}(x)$ ,有 $u^{\prime\prime}(x)\!=\!\frac{\mathrm{d}u^{\prime}(x)}{\mathrm{d}x}\!=\!\frac{\mathrm{d}t}{\mathrm{d}x}\!=\!t^{\prime}.$ 原方程化为 $\left(2\,x-1\right)t^{\prime}+\left(2\,x-3\right)t\,{=}\,0$  

化为标准形式，除以 $t^{\prime}$ 的系数 $(2\,x-1)$ 得 $t^{\prime}\!+\!\frac{2\,x-3}{2\,x-1}\,t\!=\!0\!\Rightarrow\!\frac{\mathrm{d}t}{\mathrm{d}x}\!=\!-\frac{2\,x-3}{2\,x-1}\,t$  

# 16.3一个简单的倒带换  

[2007年真题]令微分方程 $y^{\prime\prime}(x+y^{\prime2})\!=\!y^{\prime}$ 满足初始条件 $y(1)\!=\!y^{\prime}(1)\!=\!1$ 的特解为 $y(x)$ ，求 $y(4)$ 的值  

[分析]不显含 $y$ 的微分方程，令 $\scriptstyle t\=y^{\prime}(x)$ ,将 $y$ 的二阶微分方程转化为 $t$ 的一阶微分方程。 $t\!=\!y^{\prime}\!(x)$   $y^{\prime\prime}(x)\!=\!\frac{\mathrm{d}y^{\prime}(x)}{\mathrm{d}x}\!=\!\frac{\mathrm{d}t}{\mathrm{d}x}\!=\!t^{\prime}.$   ${t^{\prime}}(x\!+\!t^{2})\!=\!t$   ${\frac{\mathrm{d}t}{\mathrm{d}x}}(x+$   $t^{2})=t.$  

$t$  $x$  ${\frac{\mathrm{d}t}{\mathrm{d}x}}={\frac{t}{(x+t^{2})}}$ ，不便于求解。故将  $x$  作为未知函数，将上式转化为  $\frac{\mathrm{d}x}{\mathrm{d}t}\!=\!\frac{x}{t}+t.$  即  $|{\frac{\mathrm{d}x}{\mathrm{d}t}}-{\frac{x}{t}}=t$   $x^{\prime}+p(t)\,x=q(t)$   $p(t)\!=\!-\frac{1}{t},q(t)\!=\!t.$   $\!\!\!\overline{{\mathrm{1.~x=e^{-\int p(t)dt}*}\Bigg|\int}}\mathrm{q(t)^{*}e^{\int p(t)dt}d t+C_{1}}\!\!\Bigg|$  
# 16.4高阶K重根  

$k$ 重复数根：通解中的 $2\,k$ 项  

$e^{\alpha}\,x\,[(A_{1}+A_{2}\,x+\cdot\cdot\cdot+A_{k}\,x^{k-1})\cos\,\beta\,x+(B_{1}+B_{2}\,x+\cdot\cdot\cdot+B_{k}\,x^{k-1})\sin\,\beta\,x]$  若 $\lambda_{1,2}\!=\!\alpha\pm\beta\,i,\beta\!>\!0$ 为特征方程 $r^{n}+a_{1}\,r^{n-1}+\cdot\cdot\cdot+a_{n-1}\,r+a_{n}\!=\!0$ 的 $k$ 重复数根，  

则对应的齐次方程通解中的 $2k$ 项  

$$
e^{\alpha}\,x[(A_{1}+A_{2}\,x\ +\cdot\cdot\cdot+A_{k}\,x^{k-1})\mathrm{cos}\ \beta\,x+(B_{1}+B_{2}\,x+\cdot\cdot\cdot+B_{k}\,x^{k-1})\,\mathrm{sin}\ \beta\,x]
$$  

求高阶齐次方程的通解：将 $n$ 个特征根对应的项相加得到通解  

求 $n$ 阶常系数线性齐次微分方程 $y^{(}\,n)+a_{1}(x)\,y^{(n-1)}+\cdots+a_{n-1}(x)\,y^{\prime}+a_{n}(x)\,y\!=\!0$ 的通解：  

1 写出特征方程 $r^{n}+a_{1}\,r^{n-1}+\cdot\cdot\cdot+a_{n-1}\,r+a_{n}\!=\!0.$ 求出其特征根 $r_{i}(i\!=\!1,2,...,n)$ 2 对每一个根，判断对应形式：单重实根 $r$ ，对应一项 $C e^{\alpha}x$  $\heartsuit k$  重实根  $r$  对应  $k$  项  $\left(C_{1}+C_{2}\,x+\cdot\cdot\cdot+C_{k}\,x^{k-1}\right)e^{\alpha x_{1}}$   $\heartsuit$ 单重复数根 $r_{1}.\,2\,{=}\,\alpha\pm\beta\,i,\beta\,{>}\,0$ 对应两项 $e^{\alpha}\,x\left(C_{1}\cos\,\beta\,x+C_{2}\sin\,\beta\,x\right)$  

$\heartsuit k$ 重复数根 $r_{1}$  $.\,2\,{=}\,\alpha\pm\beta\,i,\beta>0$ 对应 $2\,k$ 项 $e^{\alpha}\,x\,[(A_{1}+A_{2}\,x+\cdot\cdot\cdot+A_{k}\,x^{k-1})\cos\,\beta\,x+$  $(B_{1}+B_{2}\,x+\cdot\cdot\cdot+B_{k}\,x^{k-1})\sin\,\beta\,x].$  

例1.K重  

已知以 $\mathrm{y=(C_{1}x+C_{2})c o s\ 2x+(C_{3}x+C_{4})s i n\ 2x,}$  $\mathrm{(C_{1},C_{2},C_{3},C_{4}}$ 为任意常数)为通解的微分方程是 $\mathrm{y}^{\prime\prime\prime\prime}\mathrm{+}\mathrm{ay}^{\prime\prime\prime}\mathrm{+}\mathrm{by}^{\prime\prime}\mathrm{+}\mathrm{cy}^{\prime}\mathrm{+}\mathrm{dy}\mathrm{=0}$ 求 $\mathrm{a+b+c+d}$  

3将 $n$ 个根对应的所有项相加便得通解，其中 $C,C_{i},A_{i},B_{i}$ 为任意常数。  
# 17定积分应用  

# 17.1 旋转体体积，非  $\pmb{y}$  轴,  $V\!=\!V_{1}\!-\!V_{2}$  

# 17.2积分比大小  

$\mathrm{I_{1}\!\!=\!\int_{0}^{\frac{\pi}{4}}\!\!\ln\left(1\!+\!2\!\sin\mathrm{x}\right)\!\cot\mathrm{x}\ \mathrm{d\mathrm{x,I_{2}\!\!=\!\int_{0}^{\frac{\pi}{4}}\!2\!\cos\mathrm{x}\ \mathrm{cot\mathrm{x}\ \mathrm{d\mathrm{x,I_{3}\!\!=\!\int_{0}^{\frac{\pi}{4}}\!\frac{\cos\mathrm{x}}{1+\mathrm{x}}}\mathrm{d\mathrm{x},\phantom{\frac{\pi}{4}}}}}}}}$   $x\in(0,\ +\infty)$ 时有 $\frac{x}{1+x}\!<\!\ln\left(1+x\right)\!<\!x$ 对 $\displaystyle{\mathrm{\Omega}^{\cdot}x\in\left(0,\frac{\pi}{4}\right)}$ 有(1)  $0<\sin{x}<x$  即  $\frac{\sin x}{1+x}<\frac{\sin x}{1+\sin x}<\ln\left(1+\sin x\right)<\ln\big(1+2\sin x\big).$   $\left(0,{\frac{\pi}{4}}\right)$   $\sin x>0,\cos x>0$  则  $\frac{\sin x}{1+x}\!\cdot\!\frac{\cos x}{\sin x}\!<\!\ln\left(1+2\sin x\right)\!\cdot\!\frac{\cos x}{\sin x},$   $\frac{\cos x}{1+x}\!<\!\ln\left(1+2\sin x\right)\!\cot\!x$   $\left(0,\frac{\pi}{4}\right)$   $\cos x>\sin x$   $\ln\left(1+2\sin x\right)<2\sin x<2\cos x,$  即  $\begin{array}{r}{\ln{\left(\dot{1}+\bar{2}\sin x\right)}\mathrm{cot}x<2\cos x\cot x.}\end{array}$  根据积分的保序性，有： $\int_{0}^{\frac{\pi}{4}}\!\!\frac{\cos x}{1+x}\mathrm{d}x\,<\,\int_{0}^{\frac{\pi}{4}}\!\!\ln\left(1+2\sin x\right)\cot x\,\mathrm{d}x\,<\,\int_{0}^{\frac{\pi}{4}}\!2\cos x\cot x\,\mathrm{d}x,$  即  $I_{3}<I_{1}<I_{2}$  

# 18重积分  

[2003年真题设 $f(x)=g(x)={\left\{\begin{array}{l l}{3}\\ {0}\end{array}\right.}$  $0\!\le\!x\!\le\!1$  $D$  $\iint_{D}\!f(\boldsymbol{x})\,\boldsymbol{g}\left(\boldsymbol{y}-\right.$ ，其他， $x)\mathrm{d}x\mathrm{d}y=$  

[分析]由于 $f(x)$ 和 $g(x)$ 为分段函数，所以被积函数 $f(x)\,g\left(y-x\right)$ 为分块函数，将积分区域按照被积函数拆分，分别积分。  

[解答] 又在  $0\!\le\!x\!\le\!1$  时  $f(x)\!=\!3$  仅在  $0\!\le\!y-x\!\le\!1$  时  $g\left(y-x\right)\!=\!3.$  则仅当  $0\!\le\!x\!\le\!1,0\!\le$   $y-x\!\le\!1$ 时，被积函数不为0.令此区域为 $D_{1}$ 则 $D_{1}\!=\!\{(x,y)|\,0\!\leq\!x\!\leq\!1,0\!\leq\!y-x\!\leq\!1\}\!=\!\{(x,$  $y)|\,0\!\le\!x\le\!1,x\le\!y\le\!1+x\,\}.\ \,|$  

$f(x)\,g\left(y-x\right)\!=\!\left\{\begin{array}{l l}{{3\cdot3,}}&{{(x,y)\in D_{1}}}\\ {{0,}}&{{\#1\!\!\!/\mathbb{H}.}}\end{array}\right.$  
# 18.1分段区间  

$$
A=\iint_{D}\!\operatorname*{max}\left(\frac{1}{x^{2}\,y+2\,x},\frac{1}{3\,x}\right)
$$  

drdy,其中 $D=\{(x,y)|\,1\!\le\!x\!\le\!2,0\le y\le\!1\}$ .已知 $A\!=\!a+b\ln\,2+c\ln\,3,$ 其中 $a,b,c$  

为有理数，求 $a+b+c$  

[分析 被积函数中 $\operatorname*{max}{\left({\frac{1}{x^{2}\,y+2\,x}},{\frac{1}{3\,x}}\right)}$ 是分块函数，先将积分区域拆分，去掉 max符号。[解答]  

被积函数在区域 $D$ 的分界线为 $\frac{1}{x^{2}\,y+2\,x}\!=\!\frac{1}{3\,x}$  $y=\frac{1}{x}$ 将 $D$ 拆分为 $D_{1}\cup D_{2}$ 如图所示。 $y\!=\!\frac{1}{x}$  $x\!=\!2$  $\left(2,{\frac{1}{2}}\right)$ 与 $y\!=\!1$ 相交于  

(1,1).  

$$
D_{1}\!=\!\left\{(x,y)|\,1\!\leq\!x\leq\!2,0\leq y\leq\!1,\frac{}{}y\geq\!\frac{1}{x}\right\}
$$  

$$
D_{2}\!=\!\left\{(x,y)|\,1\!\leq\!x\leq\!2,0\leq y\leq\!1,0\leq y\leq\!\frac{1}{x}\right\}
$$  

区域 $D_{1}$ 中 $\operatorname*{max}{\biggl(\frac{1}{x^{2}\,y+2\,x},\frac{1}{3\,x}\biggr)}\!=\!\frac{1}{3\,x},D_{2}$ 中 $\operatorname*{max}\biggl(\frac{1}{x^{2}\,y+2\,x},\frac{1}{3\,x}\biggr)\!=\!\frac{1}{x^{2}\,y+2\,x}.$  

# 18.2区间相同，二重积分保序性  

已知 $f(x,y)\!=\!x+y,g(x,y)\!=\!x-y.$ 区域 $D\!=\!\{0\!\leq\!y\!\leq\!3,h(y)\!\leq\!x\!\leq\!h(y)\!+\!1\}$ 其中 $h(x)$ 为某函数。以下选项正确的是：  

$\mathbf{A}.\langle\mathrm{init}\rangle_{D}f(x,y)\,\mathrm{d}\sigma>\langle\mathrm{init}\rangle_{D}g(x,y)\,\mathrm{d}\sigma$  B.可能有 $\langle\mathrm{init}\rangle_{D}f(x,y)\,\mathrm{d}\sigma=\langle\mathrm{init}\rangle_{D}g(x,y)\,\mathrm{d}\sigma$  $\mathrm{C.}\langle\mathrm{init}\rangle_{D}f(x,y)\,\mathrm{d}\sigma<\langle\mathrm{init}\rangle_{D}g(x,y)\,\mathrm{d}\sigma+3$   $.\langle\mathrm{init}\rangle_{D}f(x,y)\,\mathrm{d}\sigma\leq\langle\mathrm{init}\rangle_{D}g(x,y)\,\mathrm{d}\sigma$  
在积分区域 $D$ 上有 $y\geq0.$ 故 $f(x,y)\geq g(x,y)$  

$f(x,y)\!=\!x+y$ 和 $g(x,y)\!=\!x-y$ 在积分区域 $D$ 上连续，且不恒相等，所以 $\iint_{D}f(x,y)\,\mathrm{~d}\sigma>\iint_{D}g(x,y)\,\mathrm{~d}\sigma$  

综上选  $A$  

eg二重积分保序性： $f(x,y)\geq g(x,y)\Rightarrow\iint_{D}f(x,y)\,\mathrm{d}\sigma\geq\iint_{D}g(x,y)\,\mathrm{d}\sigma.$ 若在区域 $D$ 内 $f(x,y)\geq g(x,y),$ 则 $\iint_{D}f(x,y)\,\mathrm{d}\sigma\geq\iint_{D}g(x,y)\,\mathrm{d}\sigma.$  

【证明】  

令  $h(x,y)\!=f(x,y)-g(x,y)$  则有  $h(x,y)\!\ge\!0$  则  $\iint_{D}f(x,y)-g(x,y)\,\mathrm{d}\sigma=\iint_{D}h(x,y)\,\mathrm{d}\sigma\geq0.$  即  $\iint_{D}f(x,y)\,\mathrm{d}\sigma\geq\iint_{D}g(x,y)\,\mathrm{d}\sigma.$  

$$
\begin{array}{r l}&{I_{3}\!=\!\displaystyle\iint_{D}\!\cos{(x^{2}+y^{2})^{2}}\,\mathrm{d}\sigma,}\\ &{A.I_{3}\!>\!I_{2}\!>\!I_{1}\!\heartsuit}\\ &{\textrm{B.}I_{1}\!>\!I_{2}\!>\!I_{3}}\\ &{\mathbb{C}.I_{2}\!>\!I_{1}\!>\!I_{3}}\\ &{D.I_{3}\!>\!I_{1}\!>\!I_{2}}\end{array}
$$  

# 18.3二重积分存在  

$\heartsuit$  设二元函数  $f(\mathrm{x,y){=}x y^{\frac{3}{2}}l n(x^{4}{+}y^{6})}$  ，则  $\scriptstyle\operatorname*{lim}_{(\mathrm{x,y})\to(0,0)}f(\mathrm{x,y})=$  

[分析]二重极限存在，需证明点 $(x,y)$ 以任何方式趋于点 $(x_{0},y_{0})$ 时，函数 $f(x,y)$ 都无限趋近于同一常数 $A$ ：.运用 $\left|{\frac{2x y}{x^{2}+y^{2}}}\right|\leq1.$ 来证明对任何 $(x,y)$ ,不等式都成立;  

常用方法：2.夹逼定理；3．将重极限转化为一元函数极限。这里用1,2,3.  

[解答 由 $\left|{\frac{2\,x^{2}\,y^{3}}{x^{4}+y^{6}}}\right|\leq1$ 有 $|x^{2}\,y^{3}|\leq\frac{x^{4}+y^{6}}{2}$ 则  

$$
0\leq\bigg|x\,y^{\frac{3}{2}}\mathrm{ln}\,(x^{4}+y^{6})\bigg|\leq\sqrt{\frac{x^{4}+y^{6}}{2}}\bigg|\mathrm{ln}\,(x^{4}+y^{6})\bigg|.
$$  

令 $t\!=\!x^{4}\!+y^{6}$ 则 $(x,y)\!\to\!(0,0)$ 时， $t\!\xrightarrow{}\!0^{+}$ ，有  
$0\leq\operatorname*{lim}_{(x,y)\to(0,0)}|f(x,y)|\leq\operatorname*{lim}_{t\to0^{+}}\sqrt{\frac{t}{2}}|\ln t|=0,$  最后一个等式用了 $\operatorname*{lim}\rightarrow0^{+}\,x^{\delta}(\ln\,x)^{k}\!=\!0$ （常数 $\delta\,{>}\,0,k\,{>}\,0)$  

故由夹逼定理 $\operatorname*{lim}_{\prime}(x,y)\!\rightarrow\!(0,0)\:\mid f(x,y)\!\mid\!=\!0,\exists!\!\!\mid\!\operatorname*{lim}_{(}x,y)\!\rightarrow(0,0)^{\prime}\:f(x,y)\!=\!0$  

（分析 判断二重极限是否存在，关键在于构建不同路径，看是否存在：1.两种不同路径，点 $(x,y)$ 沿不同路径趋向于点 $(x_{0},y_{0})$ 时， $f(x,y)$ 趋于不同常数，2.某一路径，点 $(x,y)$ 沿此路径趋于 $(x_{0},y_{0})$ 时， $f(x,y)$ 的极限不存在，若1或2成立，则极限不存在。  

构建路径的常用方法：  

1.常见函数： $f(x,y)\!=\!\frac{x^{n}y^{m}}{x^{2n}\!+y^{2m}}.$  $y^{m}\!=\!k\,x^{n}$  $k$ 向：令 $y=y_{0}$ 或 $x=x_{0}$ 即沿平行于 $x$ 轴或 $y$ 轴的方向趋于 $(x_{0},y_{0})$ ,得到一个极限；3.归零：分子分母有相同项，则构建路径使分子分母上的其他项为0；4.分子低阶：构建路径使分母只余一项，如 $x^{k}$ 选择 $k$ 使分子为 $x^{k}$ 的低阶无穷小，则极限为 $\infty$  

这里用4即可.  

# 19积分表  

$$
\begin{array}{l}{{\displaystyle\int x^{n}\ln\left(x\right)\,d\,x\!=\!\frac{x^{n+1}}{n+1}\left(\ln\left(x\right)-\frac{x^{n+1}}{\left(n+1\right)}\right.}}\\ {~~}\\ {{\displaystyle\int\!\ln\,\left(\sin\mathrm{\,x\right)\,d x\!=\!x\!\ln\,\left(\sin\mathrm{\,x\right)\!-\!\ln\,\left(\cos\mathrm{\,x\right)\!+\!C}}}}}\end{array}
$$  

平方根函数积分：  

$$
\begin{array}{l}{\displaystyle\bullet\int\sqrt{a^{2}-x^{2}}\,\ d\,x\!=\!\frac{x}{2}\,\sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2}\sin^{-1}\!\left(\frac{x}{a}\right)+C}\\ {\displaystyle\bullet\int\sqrt{x^{2}\!\pm a^{2}}\,\ d\,x\!=\!\frac{x}{2}\,\sqrt{x^{2}\!\pm a^{2}}\pm\frac{a^{2}}{2}\ln\left|x+\sqrt{x^{2}\!\pm a^{2}}\right|+C}\end{array}
$$  
2.立方根函数积分：  

$$
\int\!\sqrt[3]{x}\,\ d\,x\!=\!\frac{3}{4}\,x^{4/3}+C
$$  

3.其他根号函数积分：  

$$
\begin{array}{c}{{\bullet\displaystyle\int\!\sqrt{x^{2}+a^{2}}\ d x\!=\!\frac{x}{2}\,\sqrt{x^{2}+a^{2}}+\frac{a^{2}}{2}\ln\left|x+\sqrt{x^{2}+a^{2}}\right|+C}}\\ {{\displaystyle\int\sqrt{x^{2}-a^{2}}\ d x\!=\!\frac{x}{2}\,\sqrt{x^{2}-a^{2}}-\frac{a^{2}}{2}\ln\left|x+\sqrt{x^{2}-a^{2}}\right|+C}}\end{array}
$$  

4.含有根号的三角函数积分：  

$$
\bullet\int{\sqrt{1-\sin^{2}x}}\,\ d\,x=\int\cos x\,\ d\,x=\sin x+C
$$  

$$
\bullet\int{\sqrt{1-\cos^{2}x}}\,\ d\,x=\int\sin x\,\ d\,x=-\cos x+C
$$  

5.含有根号和指数的函数积分：  

$\int\!\,e^{x}\,{\sqrt{1+e^{x}}}\,d\,x$ (这类积分通常需要换元法）  

6.含有根号和有理函数的积分：  

$\int\!{\frac{\sqrt{x}}{x^{2}+1}}\,d\,x$  (可能需要分部积分法)  

1.有理函数积分(部分分式分解)  

$$
\int\!{\frac{1}{\left(x-a\right)\left(x-b\right)}}\,d\,x\!=\!{\frac{1}{b-a}}\ln\left|{\frac{x-a}{x-b}}\right|+C
$$  

2.根式函数积分：  

$$
\int\!{\frac{1}{\sqrt{a^{2}-x^{2}}}}\,d\,x\!=\!\arcsin{\frac{x}{a}}+C
$$  

$$
\int\!{\frac{1}{\sqrt{a^{2}+x^{2}}}}\,d\,x\!=\!\ln\left(x+{\sqrt{a^{2}+x^{2}}}\right)\!+C
$$  
3.指数函数与三角函数的积分：  

$$
{\begin{array}{l c r}{\displaystyle\int e^{a x}\sin b\,x\ d\,x\!=\!\frac{e^{a x}}{a^{2}+b^{2}}\left(a\sin b\,x-b\cos b\,x\right)\!+\!C}\\ {\displaystyle\int e^{a x}\cos b\,x\ d\,x\!=\!\frac{e^{a x}}{a^{2}+b^{2}}\left(a\cos b\,x+b\sin b\,x\right)\!+\!C}\end{array}}
$$  

三角函数的分式，按顺序思考：  

1.凑微分,  

2.化简成一次式，或可以直接积分/凑微分积分的形式  

3.拆项,  

4.和差化积,  

5.万能代换。  

$\imath\left({\frac{x}{2}}\right)\!=\!t$  

[解答]原式 $\,=\!\int\!{\frac{\mathrm{d}}{x}}\sin\left(2\,x\right)+2\sin\,x=\int\!{\frac{\mathrm{d}x}{2\sin x\left(\cos x+1\right)}}

$  

(%011)  

(%i12) tm_plot2d(ds, [c,-0.5,3.5])  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/d3d6caa8-31a1-4b94-92b9-d0e20f8d3f5d.pdf/441b1bc39be3bf06621fae6a087ec589f66d4c2e1c501af932d9b2932247ed29.jpg)  

(%012) true  
