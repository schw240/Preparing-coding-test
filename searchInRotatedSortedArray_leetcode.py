class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target값의 인덱스 출력하기
        # 시간복잡도가 O(logN) -> 이진탐색

        # print(nums)
        # print(target)
        s, e = 0, len(nums)-1

        while s <= e:
            m = int((s+e) / 2)

            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m] >= nums[s]:
                    if nums[s] > target:
                        s = m+1
                    else:  # nums[s] < target
                        e = m-1
                else:  # nums[m] < nums[s] 5(S) 6 7 8 1 2(m) 3 4
                    e = m-1
            else:  # nums[m] < target
                if nums[m] >= nums[s]:
                    s = m+1
                else:  # nums[m] < nums[s]
                    if nums[e] >= target:
                        s = m+1
                    else:  # nums[e] < target
                        e = m-1
        return -1
