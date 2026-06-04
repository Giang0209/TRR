#include <stdio.h>

int MAX[3] = {10, 7, 4};

typedef struct
{
    int a[3];
} node;

int visited[11][8][5] = {0};

node pouring(node x, int i, int j);
void draw(node x, node y, FILE *file);
void highlight(node x, FILE *file);
void dfs(node x, FILE *file);

int main()
{
    node origin;

    scanf("%d %d %d",
          &origin.a[0],
          &origin.a[1],
          &origin.a[2]);

    FILE *file = fopen("dothi.dot", "w");

    if (file == NULL)
    {
        printf("Khong mo duoc file.\n");
        return 1;
    }

    fprintf(file, "digraph WaterJug {\n");

    dfs(origin, file);

    fprintf(file, "}\n");

    fclose(file);

    printf("Da tao file dothi.dot\n");

    return 0;
}

void dfs(node x, FILE *file)
{
    visited[x.a[0]][x.a[1]][x.a[2]] = 1;

    if (x.a[1] == 2 || x.a[2] == 2)
    {
        highlight(x, file);
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (i != j)
            {
                node tmp = pouring(x, i, j);

                if (tmp.a[0] == x.a[0] &&
                    tmp.a[1] == x.a[1] &&
                    tmp.a[2] == x.a[2])
                {
                    continue;
                }

                if (!visited[tmp.a[0]][tmp.a[1]][tmp.a[2]])
                {
                    draw(x, tmp, file);
                    dfs(tmp, file);
                }
            }
        }
    }
}

node pouring(node x, int i, int j)
{
    node tmp;

    for (int k = 0; k < 3; k++)
    {
        tmp.a[k] = x.a[k];
    }

    if (x.a[i] == 0 || x.a[j] == MAX[j])
    {
        return tmp;
    }

    int amount = MAX[j] - x.a[j];

    if (x.a[i] > amount)
    {
        tmp.a[i] -= amount;
        tmp.a[j] = MAX[j];
    }
    else
    {
        tmp.a[j] += tmp.a[i];
        tmp.a[i] = 0;
    }

    return tmp;
}

void draw(node x, node y, FILE *file)
{
    fprintf(file,
            "\"(%d,%d,%d)\" -> \"(%d,%d,%d)\";\n",
            x.a[0], x.a[1], x.a[2],
            y.a[0], y.a[1], y.a[2]);
}

void highlight(node x, FILE *file)
{
    fprintf(file,
            "\"(%d,%d,%d)\" [style=filled, fillcolor=red];\n",
            x.a[0], x.a[1], x.a[2]);
}
