bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
     int count = 0;

    for (int i = 0; i < flowerbedSize; i++) {
        if (flowerbed[i] == 0) {
            int leftEmpty = (i == 0) || (flowerbed[i - 1] == 0);
            int rightEmpty = (i == flowerbedSize - 1) || (flowerbed[i + 1] == 0);

            if (leftEmpty && rightEmpty) {
                flowerbed[i] = 1;  // plant a flower
                count++;

                if (count >= n) {
                    return true;
                }
            }
        }
    }

    return count >= n;
}