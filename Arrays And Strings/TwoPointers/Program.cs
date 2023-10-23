// See https://aka.ms/new-console-template for more information

class Program
{
    static void Main(string[] args) {
        bool checkIfPalindrome(string word) {
            int left = 0;
            int right = word.Length - 1;
            while (left < right) {
                if (word[left] != word[right]) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }
        Console.WriteLine(Convert.ToString(checkIfPalindrome("racecar")));
    }
}