% best_first_search_easy.pl
% Simple Best First Search Program

% --- Facts: graph connections ---
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).
edge(e, f).

% --- Heuristic values (smaller = closer to goal) ---
h(a, 5).
h(b, 4).
h(c, 2).
h(d, 1).
h(e, 0).   % goal node
h(f, 0).   % goal node

% --- Best First Search rule ---
best_first(Start, Goal) :-
    h(Start, H),
    format('Start at ~w (Heuristic: ~w)~n', [Start, H]),
    travel(Start, Goal, []).

travel(Node, Goal, _) :-
    Node = Goal,
    format('Reached the goal: ~w~n', [Goal]), !.

travel(Node, Goal, Visited) :-
    edge(Node, Next),
    \+ member(Next, Visited),
    h(Next, H),
    format('Move from ~w to ~w (Heuristic: ~w)~n', [Node, Next, H]),
    travel(Next, Goal, [Node | Visited]).

% --- Main program ---
main :-
    writeln('--- Best First Search ---'),
    best_first(a, f).
