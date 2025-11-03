% bird_fly.pl

% --- Database of birds ---
can_fly(sparrow).
can_fly(pigeon).
can_fly(eagle).
can_fly(parrot).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

% --- Rule to check if a bird can fly ---
fly(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).

fly(Bird) :-
    cannot_fly(Bird),
    format('~w cannot fly.~n', [Bird]).

% --- Main program with example input ---
main :-
    Bird = penguin,
    fly(Bird).
