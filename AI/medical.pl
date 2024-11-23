dise(heart_attack, "heart").
dise(fever, "hot").
dise(cold, "runny_nose").
dise(diabetes, "sugar").
dise(allergy, "itchy").
dise(migraine, "headache").
dise(stomach_ache, "pain").
dise(arthritis, "joint_pain").
diet("heart", "Avoid oily food").
diet("hot", "Avoid cool food").
diet("runny_nose", "Avoid cold food").
diet("sugar", "Avoid sugary food").
diet("itchy", "Avoid allergens").
diet("headache", "Stay hydrated and avoid caffeine").
diet("pain", "Avoid spicy food").
diet("joint_pain", "Avoid heavy lifting").
food(Dise, Diet) :-
    dise(Dise, Symptom),
    diet(Symptom, Diet).

