//Biên dịch gcc prufercode.c -o prufercode
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100000

// Hàm tính mã Prufer code
void prufer_code(int n, int m, int edges[][2]) {
    int degrees[n + 1];
    int prufer[n - 2];

    // Khởi tạo mảng tính bậc các đỉnh
    for (int i = 1; i <= n; i++) {
        degrees[i] = 0;
    }

    // Tính bậc đỉnh mới
    for (int i = 0; i < m; i++) {
        degrees[edges[i][0]]++;
        degrees[edges[i][1]]++;
    }

    // Tính mã Prufer code
    int j = 0;
    while (j < n - 2) {
        int min_leaf = -1;
        for (int i = 1; i <= n; i++) {
            if (degrees[i] == 1 && (min_leaf == -1 || i < min_leaf)) {
                min_leaf = i;
            }
        }

        int neighbor = -1;
        for (int i = 0; i < m; i++) {
            if (edges[i][0] == min_leaf) {
                neighbor = edges[i][1];
                break;
            }
            if (edges[i][1] == min_leaf) {
                neighbor = edges[i][0];
                break;
            }
        }

        prufer[j++] = neighbor;

        degrees[min_leaf] = 0; // Loai bo dinh la khoi danh sach
        degrees[neighbor]--; // Giam bac dinh ke
    }

    // In mã Prufer code
    printf("Prufer code: ");
    for (int i = 0; i < n - 2; i++) {
        printf("%d ", prufer[i]);
    }
    printf("\n");
}

// Hàm chính
int main() {
    // Nhập số lượng đỉnh và cạnh của cây
    int n, m;
    printf("NHập số lượng đỉnh của cây: ");
    scanf("%d", &n);
    printf("Nhập số lượng cạnh của cây: ");
    scanf("%d", &m);

    // Kiểm tra nếu số lượng đỉnh ko đủ tạo cây
    if (m != n - 1) {
        printf("Số lượng cạnh không hợp lệ! Mỗi cây có %d đỉnh sẽ có %d cạnh.\n", n, n - 1);
        return 1;
    }

    // NHập danh sách các cạnh
    int edges[MAX_VERTICES][2];
    printf("Nhập danh sách các cạnh (mỗi cạnh là 1 cặp số nguyên cách nhau 1 khoảng trắng):\n");
    for (int i = 0; i < m; i++) {
        printf("Canh %d: ", i + 1);
        scanf("%d %d", &edges[i][0], &edges[i][1]);
    }

    // Tính mã Prufer code
    prufer_code(n, m, edges);

    return 0;
}
