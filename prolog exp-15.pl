% pattern_match.pl
% Program to implement pattern matching

% --- Rule to match two lists (patterns) ---
match([], []).                             % empty pattern matches empty list
match([X|T1], [X|T2]) :- match(T1, T2).    % if heads match, check tails

% --- Main program example ---
main :-
    Pattern = [a, b, c],
    Text = [a, b, c],
    (   match(Pattern, Text)
    ->  writeln('Pattern found!')
    ;   writeln('Pattern not found.')
    ).
