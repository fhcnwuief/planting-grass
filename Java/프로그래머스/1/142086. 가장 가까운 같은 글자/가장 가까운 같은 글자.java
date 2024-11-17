class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        int[] alpha = new int[26]; //alphabet using asciicode
        int[] idx = new int[26]; //index saving
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            
            if(alpha[ch-'a'] == 0){
                answer[i] = -1;
                alpha[ch-'a']++;
            }
            else{
                answer[i] = i - idx[ch-'a'];
            }
            idx[ch-'a'] = i;
        }
        
        return answer;
    }
}