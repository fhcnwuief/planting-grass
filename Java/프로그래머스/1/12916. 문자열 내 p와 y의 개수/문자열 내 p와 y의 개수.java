class Solution {
    boolean solution(String s) {
        int p_c = 0 ,y_c = 0;
        s = s.toUpperCase();
        for(int i = 0; i < s.length();i++){
            if((s.charAt(i) + "").equals("P"))  p_c++;
            else if ((s.charAt(i) + "").equals("Y")) y_c++;
        }
        return (p_c == y_c);
    }
}