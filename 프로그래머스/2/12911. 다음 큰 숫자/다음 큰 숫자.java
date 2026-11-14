class Solution {
    public int solution(int n) {
        int target = binaryOneNum(n);
        int nextNum = n+1;
        while(target!=binaryOneNum(nextNum)){
            nextNum++;
        }
        return nextNum;
    }
    
    private int binaryOneNum(int n){
        int count = 0;
        while(n!=0){
            if(n%2==1){
                count++;
            }
            n=n/2;
        }
        return count;
    }
}