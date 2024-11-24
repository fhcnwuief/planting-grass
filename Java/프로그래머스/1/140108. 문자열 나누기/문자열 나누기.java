class Solution {
    public int solution(String s) {
        char first = s.charAt(0);
        //count = x 문자 횟수
        //num = x가 아닌 문자 횟수
        //answer = 분해된 횟수
        int count = 0;
        int num = 0;
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            //x와 x가 아닌 글자들이 나온 횟수가 같아짐
            if (count == num) {
                answer++;
                first = s.charAt(i);
            }
            //x의 횟수 세기
            if (first == s.charAt(i)) {
                count++;
            }
            //x가 아닐 글자들 세기
            else {
                num++;
            }
        }
        return answer;
    }
}