class Solution {
    
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int highestCount = 0;
        int currentCount = 0;
        
        for (int i = 0; i < nums.length; i++) {
            
            if (nums[i] > 0) {
                
                currentCount++;
                
            } else {
                
                if (currentCount >= highestCount) highestCount = currentCount;
                
                currentCount = 0;
            }

            // if highest possible number is found before end of array, return
            if (currentCount < 1 && highestCount > (nums.length - i)) return highestCount;
                
        }
        
        if (currentCount > highestCount) return currentCount;
        
        return highestCount;
    }
}
