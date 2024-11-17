import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {

        Set<Integer> intHashSet1 = new HashSet<>();
        
        for(int i = 0; i < numbers.length;i++){
            for(int j = i+1;j < numbers.length;j++){
                intHashSet1.add(numbers[i] + numbers[j]);
            }
        }
        
        int[] answer = new int[intHashSet1.size()];
 
        int index = 0;
        for (int i : intHashSet1) {
            answer[index++] = i;
        }                
        Arrays.sort(answer);
        
        return answer;
    }
}