import java.util.*;

class Solution {
    public int solution(int[] nums) {
        /*
        
        입력으로 오는 nums 배열에 원소들의 값들이 있는데
        이 배열 중에서 최대 nums.length/2만큼의 원소를 선택할 수 있음
        단, 중복되는 원소는 선택하면 안됨

        1) nums = [3,1,2,3] 에서는
        nums.length/2 = 2(개)만 nums에서 고를 수 있음
        중복된 원소는 고를 필요 없으니 [1,2,3] 에서 최대 2개를 고를 수 있음

        2) nums = [3,3,3,2,2,2]에서는
        nums.length/2 = 3, 최대 3개만 nums에서 고를 수 있음
        중복된 원소는 고를 필요 없으니 [3,2] 에서 최대 3개를 고르면 되지만
        중복 원소를 제거하면 원소가 2개뿐이므로 nums에 남은 것을 모두 고르면 됨
        
        */
        
        int answer = 0;
        int len = nums.length/2;

        HashSet<Integer> set = new HashSet<>();

        for(int num : nums){
            //set = 중복제거
            set.add(num);
        }

        int size = set.size();

        if (size >= len) {
            return len;
        }
        else{
            return size;
        }
    }
}