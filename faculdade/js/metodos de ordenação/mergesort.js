function mergeSort (arr) {
    if (arr.length < 2) return arr;
    var mid = Math.floor(arr.length /2);
    var subLeft = mergeSort(arr.slice(0,mid));
    var subRight = mergeSort(arr.slice(mid));
    return merge(subLeft, subRight);
  }


