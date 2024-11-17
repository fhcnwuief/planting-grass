import java.util.*;

class Solution {
    public int solution(String s) {
        
        String result = "";
        String nword = "";
        
        Map<String, Integer> hashmap = new HashMap<>();
        
        hashmap.put("zero",0);
        hashmap.put("one",1);
        hashmap.put("two",2);
        hashmap.put("three",3);
        hashmap.put("four",4);
        hashmap.put("five",5);
        hashmap.put("six",6);
        hashmap.put("seven",7);
        hashmap.put("eight",8);
        hashmap.put("nine",9);
        
        for(int i=0; i<s.length();i++){
            String current = String.valueOf(s.charAt(i));

            if (current.matches("[+-]?\\d*(\\.\\d+)?")){
                result += current;
            }
            else{
                nword += current;
                if(hashmap.containsKey(nword)){ 

                    result += hashmap.get(nword);

                    nword = "";   
                }
            }
        }
        
        return Integer.parseInt(result);
    }
}