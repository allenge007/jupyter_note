## <center> Homework5</center>

<center> 23336003 陈政宇 </center>

### 1.

```cpp
class Graph {
public:
    Graph(int vertices) : adjList(vertices) {}

    void addEdge(int v, int w) {
        adjList[v].push_back(w);
        adjList[w].push_back(v); // 无向图
    }

    bool hasPathOfLengthK(int V0, int V1, int k) {
        unordered_set<int> visited;
        return dfs(V0, V1, k, visited);
    }

private:
    vector<vector<int>> adjList;

    bool dfs(int current, int target, int k, unordered_set<int>& visited) {
        if (k == 0) {
            return current == target;
        }

        visited.insert(current);

        for (int neighbor : adjList[current]) {
            if (visited.find(neighbor) == visited.end()) {
                if (dfs(neighbor, target, k - 1, visited)) {
                    return true;
                }
            }
        }

        visited.erase(current);
        return false;
    }
};
```

### 2.

最早发生时间（EET）计算

计算：

	1.	事件 1：
	•	最早发生时间 EET(1) = 0（起点）
	2.	事件 2：
	•	EET(2) = EET(1) + 工序时间(1→2) = 0 + 15 = 15
	3.	事件 3：
	•	EET(3) = EET(1) + 工序时间(1→3) = 0 + 10 = 10
	4.	事件 4：
	•	EET(4) = max{EET(2) + 工序时间(2→4), EET(3) + 工序时间(3→4)}
	•	EET(4) = max{15 + 50, 10 + 40} = max{65, 50} = 65
	5.	事件 5：
	•	EET(5) = EET(3) + 工序时间(3→5) = 10 + 40 = 50
	6.	事件 6：
	•	EET(6) = max{EET(4) + 工序时间(4→6), EET(5) + 工序时间(5→6)}
	•	EET(6) = max{65 + 15, 50 + 15} = max{80, 65} = 80
	7.	事件 7：
	•	EET(7) = EET(5) + 工序时间(5→7) = 50 + 120 = 170
	8.	事件 8：
	•	EET(8) = max{EET(6) + 工序时间(6→8), EET(7) + 工序时间(7→8)}
	•	EET(8) = max{80 + 300, 170 + 60} = max{380, 230} = 380
	9.	事件 9：
	•	EET(9) = max{EET(6) + 工序时间(6→9), EET(7) + 工序时间(7→9)}
	•	EET(9) = max{80 + 120, 170 + 15} = max{200, 185} = 200
	10.	事件 10：
	•	EET(10) = EET(9) + 工序时间(9→10) = 200 + 30 = 230
	11.	事件 11：
	•	EET(11) = max{EET(8) + 工序时间(8→11), EET(10) + 工序时间(10→11)}
	•	EET(11) = max{380 + 40, 230 + 20} = max{420, 250} = 420

结果：
	•	事件 1: 0
	•	事件 2: 15
	•	事件 3: 10
	•	事件 4: 65
	•	事件 5: 50
	•	事件 6: 80
	•	事件 7: 170
	•	事件 8: 380
	•	事件 9: 200
	•	事件 10: 230
	•	事件 11: 420

最迟发生时间（LET）计算

计算：

	1.	事件 11：
	•	最迟发生时间 LET(11) = EET(11) = 420（终点）
	2.	事件 10：
	•	LET(10) = LET(11) - 工序时间(10→11) = 420 - 20 = 400
	3.	事件 9：
	•	LET(9) = min{LET(10) - 工序时间(9→10), LET(11) - 工序时间(8→11)}
	•	LET(9) = min{400 - 30, 420 - 40} = min{370, 380} = 370
	4.	事件 8：
	•	LET(8) = LET(11) - 工序时间(8→11) = 420 - 40 = 380
	5.	事件 7：
	•	LET(7) = min{LET(8) - 工序时间(7→8), LET(9) - 工序时间(7→9)}
	•	LET(7) = min{380 - 60, 370 - 15} = min{320, 355} = 320
	6.	事件 6：
	•	LET(6) = min{LET(8) - 工序时间(6→8), LET(9) - 工序时间(6→9)}
	•	LET(6) = min{380 - 300, 370 - 120} = min{80, 250} = 80
	7.	事件 5：
	•	LET(5) = min{LET(6) - 工序时间(5→6), LET(7) - 工序时间(5→7)}
	•	LET(5) = min{80 - 15, 320 - 120} = min{65, 200} = 65
	8.	事件 4：
	•	LET(4) = LET(6) - 工序时间(4→6) = 80 - 15 = 65
	9.	事件 3：
	•	LET(3) = min{LET(4) - 工序时间(3→4), LET(5) - 工序时间(3→5)}
	•	LET(3) = min{65 - 40, 65 - 40} = min{25, 25} = 25
	10.	事件 2：
	•	LET(2) = LET(4) - 工序时间(2→4) = 65 - 50 = 15
	11.	事件 1：
	•	LET(1) = min{LET(2) - 工序时间(1→2), LET(3) - 工序时间(1→3)}
	•	LET(1) = min{15 - 15, 25 - 10} = min{0, 15} = 0

结果：
	•	事件 1: 0
	•	事件 2: 15
	•	事件 3: 25
	•	事件 4: 65
	•	事件 5: 65
	•	事件 6: 80
	•	事件 7: 320
	•	事件 8: 380
	•	事件 9: 370
	•	事件 10: 400
	•	事件 11: 420

关键路径与最短工期

关键路径：

1 → 2 → 4 → 6 → 8 → 11
最短工期：420