function linearSearch(array, target) {
    // Returns the position of the target if found, else returns -1
    for (let i = 0; i < array.length; i++) {
        if (array[i] === target) {
            return i // once we hit the return we terminate our function
        } 
    }
    return -1; // if we don't terminate, we will return -1
}

console.log(linearSearch([1,2,3,4,5], 5));
