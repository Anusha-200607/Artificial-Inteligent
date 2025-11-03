% fruit_color.pl
% Demonstration of fruit and color using backtracking

% --- Facts ---
color(apple, red).
color(banana, yellow).
color(grapes, green).
color(orange, orange).
color(blueberry, blue).
color(watermelon, green).

% --- Rule to find fruit color ---
find_color(Fruit) :-
    color(Fruit, Colour),
    format('The color of ~w is ~w.~n', [Fruit, Colour]).

% --- Rule to find fruits of a given color ---
find_fruit_by_color(Colour) :-
    color(Fruit, Colour),
    format('~w is ~w in color.~n', [Fruit, Colour]).

% --- Main program example ---
main :-
    writeln('--- Fruit and Color Program ---'),
    find_color(apple),
    writeln('Now showing fruits that are green:'),
    find_fruit_by_color(green).
