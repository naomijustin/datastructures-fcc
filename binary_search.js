function binarySearch(array, key) {
    let left = 0;
    let right = array.length - 1;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2); // Find middle
        if (array[mid] === key) {
            return mid;
        }
        if (array[mid] < key) { // key is higher (to the right) - discard left half
            left = mid + 1;
        } else {
            right = mid - 1; // key is lower (to the left) - discard the right half
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
