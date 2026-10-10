class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        bucket = []
        counter=0
        for i in range(len(nums) + 1):
            bucket.append([])
            
        freq=defaultdict(int)

        for num in nums:
            freq[num]+=1

        for num, count in freq.items():
            bucket[count].append(num) #index => frequency, key-> value bucket[9]=[5]-> 5 sayisi 9 tane var, 9.sirada
            

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]: 
                result.append(num) # Sayıyı result listesine ekle
                
                if len(result)==k:
                    return result
                
                # result uzunluğu k'ye ulaştıysa
                # result listesini döndür

        #result= sorted(freq,key=freq.get, reverse=True) #dictte slice olmaz, sorted list verir slice onda yapilir
        #return result[:k]