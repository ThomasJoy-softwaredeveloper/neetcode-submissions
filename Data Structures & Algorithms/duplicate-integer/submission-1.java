class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> elements = new HashSet<Integer>();

        for(int num : nums) {
            if (elements.contains(num))
                return true;
            else 
                elements.add(num);
        }
    
        return false;
    }

   
}
