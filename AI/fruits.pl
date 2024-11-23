fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(cherry, red).
find_fruits_by_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
