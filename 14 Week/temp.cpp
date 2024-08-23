// #include <bits/stdc++.h>

bool isSafe(int x, int y, int n, vector<vector<int>> visited, vector<vector<int>> &maze)
{

    if ((x >= 0 && x < n) && (y >= 0 && y < n) && visited[x][y] == 0 && maze[x][y] == 1)

        return true;

    else

        return false;
}

void solve(vector<vector<int>> &maze, int n, vector<vector<int>> &ans, int x, int y, vector<vector<int>> visited)
{

    // base case

    if (x == n - 1 && y == n - 1)
    {

        vector<int> temp;

        visited[x][y] = 1;

        for (int i = 0; i < n; i++)
        {

            for (int j = 0; j < n; j++)

                temp.push_back(visited[i][j]);
        }

        visited[x][y] = 0;

        ans.push_back(temp);

        return;
    }

    visited[x][y] = 1;

    // 4 choices - DOWN, LEFT, RIGHT, UP

    // down

    int newx = x + 1;

    int newy = y;

    if (isSafe(newx, newy, n, visited, maze))

        solve(maze, n, ans, newx, newy, visited);

    // left

    newx = x;

    newy = y - 1;

    if (isSafe(newx, newy, n, visited, maze))

        solve(maze, n, ans, newx, newy, visited);

    // right

    newx = x;

    newy = y + 1;

    if (isSafe(newx, newy, n, visited, maze))

        solve(maze, n, ans, newx, newy, visited);

    // up

    newx = x - 1;

    newy = y;

    if (isSafe(newx, newy, n, visited, maze))

        solve(maze, n, ans, newx, newy, visited);

    visited[x][y] = 0;
}

vector<vector<int>> ratInAMaze(vector<vector<int>> &maze, int n)
{

    vector<vector<int>> ans;

    if (maze[0][0] == 0)

        return ans;

    int srcx = 0;

    int srcy = 0;

    vector<vector<int>> visited = maze;

    // initialise with 0

    for (int i = 0; i < n; i++)
    {

        for (int j = 0; j < n; j++)

            visited[i][j] = 0;
    }

    solve(maze, n, ans, srcx, srcy, visited);

    return ans;
}