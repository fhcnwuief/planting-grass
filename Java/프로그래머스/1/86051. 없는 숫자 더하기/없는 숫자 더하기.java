class Solution {
    public int solution(int[] numbers) {
        int answer = -1;
        
        int num = 45;
        for (int i : numbers) {
            num -= i;
        }
        return num;
    }
}