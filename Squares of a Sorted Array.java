class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int [] res = new int[nums.length];
        int left =0;
        int right = nums.length -1;
        int currentIndex = right;
        while(left<=right){
            int num1 = Math.abs(nums[left]);
            int num2 = Math.abs(nums[right]);
            if (num1>=num2){
                res[currentIndex]=num1 * num1;
                left++;
            }else{
                res[currentIndex]=num2 * num2;
                right--;
            }
            currentIndex--;
        }
        return res;
    }
}
