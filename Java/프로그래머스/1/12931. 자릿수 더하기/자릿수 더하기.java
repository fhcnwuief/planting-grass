import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int d = 0;
        while (n>0){
            d = n%10;
            n /= 10;
            answer+= d;
        }
        return answer;
    }
}