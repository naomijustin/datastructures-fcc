function linearSearch(array, target) {
    // Returns the position of the target if found, else returns -1
    for (let i = 0; i < array.length; i++) {
        if (array[i] === target) {
            return i // once we hit the return we terminate our function
        } 
    }
    return -1; // if we don't terminate, we will return -1
}

function verify(index) {
    if (index != -1) {
        console.log("Target found at index: " + index);
    } else {
        console.log("Target not found in list");
    }
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result = linearSearch(numbers, 1);

verify(result);