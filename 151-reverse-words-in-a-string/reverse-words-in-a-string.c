char* reverseWords(char* s) {
    int len = strlen(s);
    char* result = (char*)malloc(len + 1);
    int resultIndex = 0;

    int i = len - 1;

    while (i >= 0) {
        while (i >= 0 && s[i] == ' ') {
            i--;
        }

        if (i < 0) {
            break; 
        }
        int end = i;
        while (i >= 0 && s[i] != ' ') {
            i--;
        }
        int start = i + 1;
        if (resultIndex > 0) {
            result[resultIndex++] = ' ';
        }
        for (int j = start; j <= end; j++) {
            result[resultIndex++] = s[j];
        }
    }

    result[resultIndex] = '\0';
    return result;
}