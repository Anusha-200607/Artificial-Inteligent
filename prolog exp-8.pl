% dieting_system.pl

% --- Facts: Basic food suggestions based on goal ---
diet(gain_weight, 'Eat protein-rich foods, nuts, milk, and rice.').
diet(lose_weight, 'Eat vegetables, fruits, oats, and avoid junk food.').
diet(maintain_weight, 'Eat balanced meals with fruits, veggies, and lean protein.').

% --- Rule to calculate BMI and give suggestion ---
bmi(Weight, Height, BMI) :-
    BMI is Weight / (Height * Height).

diet_plan(Weight, Height, Plan) :-
    bmi(Weight, Height, BMI),
    (   BMI < 18.5 -> Goal = gain_weight
    ;   BMI >= 18.5, BMI < 25 -> Goal = maintain_weight
    ;   Goal = lose_weight
    ),
    diet(Goal, Plan),
    format('Your BMI is ~2f. Recommended goal: ~w~n', [BMI, Goal]),
    format('Diet suggestion: ~w~n', [Plan]).

% --- Main program with example input ---
main :-
    Weight = 52,    % in kilograms
    Height = 1.65,  % in meters
    diet_plan(Weight, Height, _).
