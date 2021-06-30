function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheese = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
console.log(pizzaOven("deep dish", "traditional",["mozzarella"], ["pepperoni", "sausage"]));
pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "pineapple"]);
pizzaOven("deep dish", "marinara", ["mozzarella"], ["beef", "chicken"]);