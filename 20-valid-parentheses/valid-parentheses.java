class Solution {
    public int top = -1;
    public char[] stack;
    public boolean isValid(String s) {
        top=-1;
        if(s.isEmpty())
            return true;
        if(isValidParenthese(s))
            return true;
        else
            return false;
    }

    public boolean matchingPair(char a,char b){
        if(a=='[' && b == ']')
            return true;
        else if(a=='{' && b == '}')
            return true;
        else if(a=='(' && b == ')')
            return true;
        else
            return false;
    }

    public boolean isValidParenthese(String str){

        stack = new char[str.length()];

        for(int i = 0;i<str.length();i++){
            if(str.charAt(i) == '[' || str.charAt(i) == '{' || str.charAt(i) == '('){
                //push
                push(str.charAt(i));
                // return true;
            }
            else if(str.charAt(i) == ']' || str.charAt(i) == '}' || str.charAt(i) == ')'){
                //char removeItem =  get the remove item
                if(isEmpty()){
                    return false;
                }
                else if (!matchingPair(pop(),str.charAt(i)))
                    return false;
            }

        }
        if(isEmpty()){
            return true;
        }
        else
            return false;

    }

    public void push(char c){
        if(isFull()){
            System.out.println("Stack is already full. Please pop item to Push new one!");
        }
        else {
            top++;
            stack[top] = c;
        }

    }

    public char pop(){
        if(isEmpty()){
            System.out.println("Your Stack is empty. Please enter element to pop!");
            return '?';
        }
        else {
            int temp = top;
            top--;
            return stack[temp];
        }
    }

    public boolean isEmpty(){
        return top ==-1;
    }

    public boolean isFull(){
        return stack.length-1 == top;
    }
    
}