function solution(slice, n) {
    let pizzaBox = 1
    while ((pizzaBox * slice) < n) {
        pizzaBox += 1
    }
    
    return pizzaBox;
}