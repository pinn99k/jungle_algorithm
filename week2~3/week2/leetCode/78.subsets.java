class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        
        backtrack(0, temp, result, nums);
        
        return result;
    }

    public void backtrack(int start, List<Integer> temp, List<List<Integer>> result, int[] nums) {
        result.add(new ArrayList<>(temp));


        for (int i = start; i < nums.length; i++) {
            temp.add(nums[i]);

            backtrack(i + 1, temp, result, nums);

            temp.remove(temp.size() - 1);
        }
    }
}