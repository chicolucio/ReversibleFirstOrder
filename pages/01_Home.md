### Brief explanation

For a reversible reaction $A \rightleftarrows B$ the rate law is of the form

$$
v = - \frac{d[A]}{dt} = k_f [A] - k_b [B]
$$

where $k_f$ is the rate constant of the forward reaction and $k_b$ is the rate constant of the backward reaction.

If both A and B are present initially, $[A]_0 = [A]$ and $[B]_0 = [B]$ then $[B] = [A]_0 + [B]_0 - [A]$ is a boundary condition:

$$
- \frac{d[A]}{dt} = (k_f + k_b) \left( [A] - \frac{k_b}{k_f + k_b} ([A]_0 + [B]_0) \right)
$$

Integrating and isolating $[A]$:

$$
[A] = -\frac{(k_b [B]_0 - k_f [A]_0) \exp(-t(k_f + k_b)) - k_b([A]_0 + [B]_0 }{k_f + k_b}
$$

The reactions of the mutual conversion of isomers, for example $d$-menthone
$\rightleftarrows$ $l$-menthone or ammonium thiocyanate $\rightleftarrows$ thiocarbamide
can serve as examples of reversible reactions.
