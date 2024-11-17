class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int idx = 0;
        for(int i:absolutes){
            answer += (signs[idx] ? i : (-1) * i);
            idx++;   
        }
        return answer;
    }
}