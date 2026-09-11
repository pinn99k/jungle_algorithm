class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        
        // 1. 0부터 n까지의 인용 횟수를 카운트할 배열 생성 📊
        // (인덱스가 0부터 n까지 필요하므로 크기는 n + 1)
        int[] count = new int[n + 1];
        
        // 2. 각 논문의 인용 횟수를 count 배열에 기록 📝
        for (int c : citations) {
            if (c >= n) {
                count[n]++; // n번 이상 인용된 논문은 전부 n번 위치에 누적!
            } else {
                count[c]++;
            }
        }
        
        // 3. 뒤(n)에서부터 거꾸로 오며 누적합 계산 🔍
        int total = 0; // h번 이상 인용된 논문의 총 개수
        for (int h = n; h >= 0; h--) {
            total += count[h];
            
            // h번 이상 인용된 논문 수가 h편 이상이 되는 첫 순간! 🎯
            if (total >= h) {
                return h;
            }
        }
        
        return 0;
    }
}