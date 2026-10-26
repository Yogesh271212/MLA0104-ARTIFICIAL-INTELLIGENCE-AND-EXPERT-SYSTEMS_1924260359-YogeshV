def forward_chaining(facts, rules):
    inferred = set(facts)
    added = True

    while added:
        added = False
        for conditions, conclusion in rules:
            if conditions.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                print(f"Derived new fact: {conclusion}")
                added = True

    return inferred

initial_facts = {'power_light_off', 'wall_outlet_working'}
diagnostic_rules = [
    ({'power_light_off', 'wall_outlet_working'}, 'power_supply_faulty'),
    ({'power_supply_faulty'}, 'replace_power_supply'),
    ({'no_display', 'power_light_on'}, 'monitor_cable_loose')
]

print("Initial Facts:", initial_facts)
final_facts = forward_chaining(initial_facts, diagnostic_rules)
print("Final Derived Conclusions:", final_facts)
