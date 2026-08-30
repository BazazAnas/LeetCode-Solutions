bool isVowel(char c) {
    c = (c >= 'A' && c <= 'Z') ? c + 32 : c;  // convert to lowercase
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

char* reverseVowels(char* s) {
    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        if (!isVowel(s[left])) {
            left++;
        } else if (!isVowel(s[right])) {
            right--;
        } else {
            // both are vowels, swap them
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    return s;
}