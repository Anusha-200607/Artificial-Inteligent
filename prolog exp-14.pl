% easiest_backward_chaining.pl
% Absolutely simple Backward Chaining demo

% --- Facts (known truths) ---
raining.
cloudy.

% --- Rules ---
wet_ground :- raining.
carry_umbrella :- raining, cloudy.

% --- Start program ---
start :-
    writeln('Checking if you should carry an umbrella...'),
    (carry_umbrella ->
        writeln('Yes, you should carry an umbrella!')
    ;
        writeln('No need for an umbrella.')
    ),

    writeln('Checking if the ground is wet...'),
    (wet_ground ->
        writeln('Yes, the ground is wet!')
    ;
        writeln('No, the ground is dry.')
    ).
