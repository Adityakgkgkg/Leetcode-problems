class Solution(object):
    def search(self, arr, key):
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid =(lo + hi) // 2
            if arr[mid] == key :
                return mid
            #left half is sorted
            if arr[lo] <= arr[mid]:
                if arr[lo] <= key < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            #right half is sorted
            else:
                if arr[mid] < key <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
        