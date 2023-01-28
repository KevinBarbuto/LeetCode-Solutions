// The classic FizzBuzz problem

class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function fizzBuzz($n) {
        $ans = [];
        for ($i = 1; $i <= $n; $i++) {
            if ($i % 15 == 0) {
                array_push($ans, "FizzBuzz");
            } else if ($i % 3 == 0) {
                array_push($ans, "Fizz");
            } else if ($i % 5 == 0) {
                array_push($ans, "Buzz");
            } else {
                // strval function converts var to str
                array_push($ans, strval($i) );
            }
        }
        return $ans;
    }
}
