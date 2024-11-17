import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Stack<Integer> st = new Stack<>();
        
        for(int i = 0; i < arr.length; i++){
            if(st.isEmpty()){ st.push(arr[i]); }
            if(st.peek().equals(arr[i])) { continue;}
            else{ st.push(arr[i]); }
            
        }
        
        int[] answer = new int[st.size()];
        for(int i = answer.length -1 ; i >= 0; i--){
            answer[i] = st.pop();
        }
        return answer;
    }
}