// Objective: Create a list of numbers that prints out "fizz" if the number is divisible by 3, 
// "buzz" if the number is divisible by 5, and "fizzbuzz" if the number is divisible by both.

/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    result = [];

    for (i=1; i<=n; i++) {
        // Check for case where it's divisible by 3 and 5
        if (i%15 == 0) {
            result.push('FizzBuzz')
        } else if (i%3 == 0) {
            result.push('Fizz')
        } else if (i%5 == 0) {
            result.push('Buzz')
        } else {
            result.push( i.toString() ) // Convert to string
        }
    }

    return result;
};
