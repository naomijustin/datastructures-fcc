function binarySearch(array, key) {
    let first = 0;
    let last = array.length - 1;

    while (first <= last) {
        const mid = first + Math.floor((last - first) / 2); // Find middle
        if (array[mid] === key) {
            return mid;
        }
        if (array[mid] < key) { // key is higher (to the right/last) - discard left/first half
            first = mid + 1;
        } else {
            last = mid - 1; // key is lower (to the left/first) - discard the right/last half
        }
    }
    return -1; // Not found
}

// === Verify Result ===
function verify(index) {
    if (index != -1) {
        console.log("Target found at index: " + index);
    } else {
        console.log("Target not found in list");
    }
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result;

result = binarySearch(numbers, 12);
verify(result);

result = binarySearch(numbers, 5);
verify(result);

// Logs the below:
// Target not found in list
// Target found at index: 4
