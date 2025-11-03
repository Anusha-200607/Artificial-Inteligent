% planetsDB.pl
% --- Database of planets ---
planet('Mercury', 57.9, 0).      % Distance in million km
planet('Venus', 108.2, 0).
planet('Earth', 149.6, 1).
planet('Mars', 227.9, 2).
planet('Jupiter', 778.5, 79).
planet('Saturn', 1434, 83).
planet('Uranus', 2871, 27).
planet('Neptune', 4495, 14).

% --- Rules ---
has_moons(Planet) :-
    planet(Planet, _, Moons),
    Moons > 0.

farther_than(P1, P2) :-
    planet(P1, D1, _),
    planet(P2, D2, _),
    D1 > D2.

% --- Main program with example query ---
main :-
    Planet = 'Earth',
    planet(Planet, Distance, Moons),
    format('~w is ~w million km from the Sun and has ~w moon(s).~n', [Planet, Distance, Moons]).
