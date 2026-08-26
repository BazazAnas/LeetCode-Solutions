int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

char* gcdOfStrings(char* str1, char* str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    // Build str1+str2 and str2+str1, compare them
    int totalLen = len1 + len2;
    char* concat1 = (char*)malloc(totalLen + 1);
    char* concat2 = (char*)malloc(totalLen + 1);

    strcpy(concat1, str1);
    strcat(concat1, str2);

    strcpy(concat2, str2);
    strcat(concat2, str1);

    int equal = strcmp(concat1, concat2) == 0;

    free(concat1);
    free(concat2);

    if (!equal) {
        char* result = (char*)malloc(1);
        result[0] = '\0';
        return result;
    }

    int g = gcd(len1, len2);
    char* result = (char*)malloc(g + 1);
    strncpy(result, str1, g);
    result[g] = '\0';

    return result;
}
