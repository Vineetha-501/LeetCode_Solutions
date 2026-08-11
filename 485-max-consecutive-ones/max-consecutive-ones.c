int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int max=0;
    for(int i=0,temp=0;i<numsSize;i++){
        if(nums[i]==1){
            temp++;
            if(temp>max) max=temp;
        }else{
            temp=0;
        }
    }
    return max;
}