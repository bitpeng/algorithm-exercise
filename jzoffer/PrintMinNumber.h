class Solution {
public:
    bool num1Greatnum2(int num1, int num2){
        string str1 = to_string(num1) + to_string(num2);
        string str2 = to_string(num2) + to_string(num1);
        if(str1 >= str2){
            return true;
        }
        return false;
    }
    int partition(vector<int>& input, int begin, int end){
        if(begin == end){
            return begin;
        }
        if(begin == end - 1){
            if(num1Greatnum2(input[begin], input[end])){
                int temp = input[begin];
                input[begin] = input[end];
                input[end] = temp;
                return end;
            }
            return begin;
        }
        int i = begin+1;
        int j = end;
       // int keyval = input[begin];
        int key = begin;
        while(i < j){
             
            while(i < j && num1Greatnum2(input[j], input[key])){
                j--;
            }
            while(i < j && !num1Greatnum2(input[i], input[key])){
                i++;
            }
            if(i < j){
                int temp = input[i];
                input[i] = input[j];
                input[j] = temp;
                i++;
                j--;
            }
        }
        int temp = input[key];
        input[key] = input[j];
        input[j] = temp;
        return j;
    }
    void mysort(vector<int>& numbers, int begin, int end){
        if(end == begin){
            return;
        }
        int index = partition(numbers, begin, end);
        if(index > begin + 1){
            mysort(numbers, begin, index-1);
        }
        if(index < end - 1){
            mysort(numbers, index+1, end);
        }
    }
    string PrintMinNumber(vector<int> numbers) {
        string str = "";
        if(numbers.empty()){
            return str;
        }
        if(numbers.size() == 1){
            str = str + to_string(numbers[0]);
            return str;
        }
        mysort(numbers, 0, numbers.size()-1);
        for(int i = 0; i < numbers.size(); i++){
            str = str + to_string(numbers[i]);
        }
        return str;
    }
};