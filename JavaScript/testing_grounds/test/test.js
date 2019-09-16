for (i in Range(0, 15)) {
    if (i % 3 == 0 && i % 5 ==0) {
        console.log("FizzBuzz");
    }
    if (i % 3 == 0) {
        console.log("Fizz");
    }
    if (i % 5 == 0) {
        console.log("Buzz");
    }
}