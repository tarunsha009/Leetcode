/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        
        ListNode head1 = l1;
        ListNode head2 = l2;
        ListNode tempHead = null;
        
        if(head1 ==null)
            return head2;
        if(head2==null)
            return head1;
        
        if(head1.val <head2.val){
            tempHead = head1;
            head1 = head1.next;
        }
        else{
            tempHead = head2;
            head2 = head2.next;
        }
        
        ListNode templast = tempHead;
        
        
        while(head1!=null && head2!=null){
            
            ListNode temp = null;            
            if(head1.val <head2.val){
            temp = head1;
            head1 = head1.next;
            }
            else{
            temp = head2;
            head2 = head2.next;
            }
            
            templast.next = temp;
            templast = temp;       
    }
        
        if(head1!=null){
            templast.next = head1;
        }
        else
            templast.next = head2;
        
        return tempHead;
    }
}