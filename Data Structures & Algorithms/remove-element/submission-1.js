class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let l = 0
        let r = nums.length

        for (;l < r;) {
            if (nums[l] == val) {
                r--
                nums[l] = nums[r]
            } else {
                l++
            }
        }

        return l

    }
}
