% family_tree.pl

male(ravi).
male(raj).
male(kumar).
female(anusha).
female(saadhana).
female(latha).

parent(ravi, raj).
parent(latha, raj).
parent(ravi, anusha).
parent(latha, anusha).
parent(raj, saadhana).
parent(kumar, saadhana).

father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
grandparent(G, C) :- parent(G, P), parent(P, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

main :-
    Child = anusha,
    father(F, Child),
    mother(M, Child),
    format('Father of ~w is ~w.~n', [Child, F]),
    format('Mother of ~w is ~w.~n', [Child, M]).

:- initialization(main).
