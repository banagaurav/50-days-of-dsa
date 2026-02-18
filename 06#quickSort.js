function partition (array, low, high){
    pivot = array[high];
    i = low-1;

    for(j=i; j<high; j++){
        if(array[j]<=pivot){
            i++;
            [array[i],array[j]] = [array[j],array[i]]
        }
    }
    [array[i+1],array[high]]=[array[high],array[i+1]]
    return i+1;
}

function quickSort(array, low=0, high= null){
    if(high == null){
        high = array.length - 1;
    }

    if(low<high){
        pivot_index = partition(array,low,high);
        quickSort(array,pivot_index+1,high);
        quickSort(array,low,pivot_index-1);
    }
}

myArray = [12,2,125,5,65,78]
quickSort(myArray)
console.log(myArray)