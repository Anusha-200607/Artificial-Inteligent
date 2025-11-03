% person_db.pl
% --- Database of people ---
person('Anusha', '07/07/2006').
person('Saadhana', '13/10/2006').

% --- Rule to display DOB by name ---
find_dob(Name) :-
    person(Name, DOB),
    format('Date of Birth of ~w is ~w~n', [Name, DOB]).

% --- Main program with example query ---
main :-
    Name = 'Anusha',
    find_dob(Name).
