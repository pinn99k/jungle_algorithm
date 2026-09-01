class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // 해쉬 셋을 써서 해당 char에 count ++ 
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        // 정렬된 값은 key에 원본 값은 val에 추가
        for (int i = 0; i < strs.length; i ++){
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);
            String k = new String(charArray);
            map.computeIfAbsent(k, key -> new ArrayList<>()).add(strs[i]);
        }
        for(List<String> group : map.values()){
            result.add(group);
        }
        return result;
    }
}