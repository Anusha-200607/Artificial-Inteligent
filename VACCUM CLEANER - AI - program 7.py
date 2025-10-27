def vacuum_cleaner_problem():
    # initial state: [A, Dirty, Dirty]
    state = {'A': 'Dirty', 'B': 'Dirty'}
    actions = []

    print("Initial State:", state)

    # Simple reflex agent
    for room in ['A', 'B']:
        if state[room] == 'Dirty':
            actions.append(f"Suck in {room}")
            state[room] = 'Clean'
        actions.append(f"Move to {'B' if room == 'A' else 'A'}")

    print("Actions taken:", " -> ".join(actions))
    print("Final State:", state)


print("\nVacuum Cleaner Problem")
print("----------------------")
vacuum_cleaner_problem()
