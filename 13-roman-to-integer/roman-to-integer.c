int romanToInt(char* s) {
    int total = 0;
    int len = strlen(s);

    for (int i = 0; i < len; i++) {
        int val;
        switch (s[i]) {
        case 'I':
            val = 1;
            break;
        case 'V':
            val = 5;
            break;
        case 'X':
            val = 10;
            break;
        case 'L':
            val = 50;
            break;
        case 'C':
            val = 100;
            break;
        case 'D':
            val = 500;
            break;
        case 'M':
            val = 1000;
            break;
        default:
            val = 0;
            break; // invalid character
        }

        int next_val = 0;
        if (i + 1 < len) {
            switch (s[i + 1]) {
            case 'I':
                next_val = 1;
                break;
            case 'V':
                next_val = 5;
                break;
            case 'X':
                next_val = 10;
                break;
            case 'L':
                next_val = 50;
                break;
            case 'C':
                next_val = 100;
                break;
            case 'D':
                next_val = 500;
                break;
            case 'M':
                next_val = 1000;
                break;
            default:
                next_val = 0;
                break;
            }
        }

        if (val < next_val)
            total -= val;
        else
            total += val;
    }

    return total;
}
