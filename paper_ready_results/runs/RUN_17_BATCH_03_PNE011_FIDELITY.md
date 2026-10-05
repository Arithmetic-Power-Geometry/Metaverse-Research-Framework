# PNE011 Fidelity Specification — Equations and Algorithms

## Source identity
Xinyu Zhou, Chang Liu, Jun Zhao. Resource Allocation of Federated Learning for the Metaverse With Mobile Augmented Reality. IEEE Transactions on Wireless Communications 24(8):6290-6305. DOI 10.1109/TWC.2023.3326884.

## Optimization
Decision variables per device n: bandwidth B_n, transmit power p_n, CPU frequency f_n, frame resolution s_n.

Objective:
min w1 E + w2 T - rho A

Constraints:
- sum_n B_n <= B and B_n >= 0
- p_min_n <= p_n <= p_max_n
- f_min_n <= f_n <= f_max_n
- s_n in {s_min, s_max}

Accuracy surrogate:
A_n(s_n) = 1 - 1.578 exp(-6.5e-3 s_n)

## Algorithm 1 fidelity
Newton-like optimization of (p,B) and auxiliary (nu,beta):
1. initialize i=0, xi in (0,1), epsilon in (0,1), feasible p^(0), B^(0)
2. calculate nu_n = w1 R_g / G_n(p_n,B_n)
3. calculate beta_n = p_n d_n / G_n(p_n,B_n)
4. solve SP2_v2 for next p,B with CVX for fixed nu,beta
5. backtracking selects smallest integer j satisfying the source norm-reduction inequality
6. update beta,nu using xi^j times Newton directions
7. stop when phi(beta,nu)=0 or iteration count reaches i0

## Algorithm 2 fidelity
Block-coordinate resource allocation:
1. initialize feasible sol^(0)=(p,B,f,s), k=1
2. solve Subproblem 1 / dual A.7 with CVX for fixed previous p,B
3. recover f,s from source equations (19),(20)
4. solve Subproblem 2 using Algorithm 1 to obtain p,B
5. update sol
6. stop when norm(sol^k-sol^(k-1)) <= epsilon0 or k reaches K

## Unresolved numerical controls
The source text expresses xi, epsilon, epsilon0, i0, K and CVX solution accuracy symbolically in the exposed algorithm/complexity text. No numerical values are admitted here unless separately source-verified.

## Scientific execution gate
BLOCKED. A runnable implementation must not invent unresolved numerical controls. Any future sensitivity experiment over those controls must be labeled a reconstruction/sensitivity analysis, not an exact reproduction.
