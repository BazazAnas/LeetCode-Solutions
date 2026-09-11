typedef struct {
    int* requests;
    int size;
    int head;
} RecentCounter;


RecentCounter* recentCounterCreate() {
    RecentCounter* obj = (RecentCounter*)malloc(sizeof(RecentCounter));
    obj->requests = (int*)malloc(10000 * sizeof(int));
    obj->size = 0;
    obj->head = 0;
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj->requests[obj->size] = t;
    obj->size++;

    while (obj->requests[obj->head] < t - 3000) {
        obj->head++;
    }

    return obj->size - obj->head;
}

void recentCounterFree(RecentCounter* obj) {
    free(obj->requests);
    free(obj);
}

/**
 * Your RecentCounter struct will be instantiated and called as such:
 * RecentCounter* obj = recentCounterCreate();
 * int param_1 = recentCounterPing(obj, t);
 
 * recentCounterFree(obj);
*/