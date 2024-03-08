function recursiveBinarySearch(list, target) {
    console.log(list);
    if (list.length === 1 && list[0] !== target) {
        return false
    } else {
        var midpointIndex = Math.floor(list.length / 2);
        if (list[midpointIndex] == target) {
            return true
        } else {
            if (list[midpointIndex] < target) {
                return recursiveBinarySearch(list.slice(midpointIndex));
            } else {
                return recursiveBinarySearch(list.slice(0, midpointIndex));
            }
        }
    }
}


var numbers = [1,2,3,4,5,6,7,8];

console.log(recursiveBinarySearch(numbers, 7));