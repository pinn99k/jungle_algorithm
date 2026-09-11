class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 주식의 배열을 받는다
        # 차가 가장 큰 경우를 리턴한다
        # 가장 큰 인덱스를 temp 가장 작은 인덱스를 temp2 / 두 인덱스 값의 차이
        
        temp_max = 0
        min_price = prices[0]

        for i in prices:
            if min_price > i:
                min_price = i
                continue
            temp_max = max(temp_max, i - min_price)

        return temp_max