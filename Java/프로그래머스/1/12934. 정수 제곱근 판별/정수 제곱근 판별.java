import java.util.*;
import java.lang.*;
import java.io.*;


class Solution{
    public long solution(long n){
        if(Math.sqrt(n) == (int)Math.sqrt(n)){
            return (long)Math.pow(Math.sqrt(n)+1,2);
        }
        return -1;
    }
}