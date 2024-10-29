#include <iostream>
#include <list>
#include <map>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

class graph
{
       map<string, list<string>> vertices;

public:
       void addVertex(string newVertex)
       {
              this->vertices[newVertex] = list<string>();
       }

       bool HasThisVertex(string Node)
       {
              return this->vertices.find(Node) != vertices.end();
       }

       void addEdge(string startNode, string endNode)
       {
              if (HasThisVertex(startNode) && HasThisVertex(endNode))
              {
                     this->vertices[startNode].push_back(endNode);
              }
       }
       void PrintGraph()
       {
              for (auto keyValue : this->vertices)
              {
                     cout << keyValue.first << "->" << "[ ";
                     for (auto listItem : keyValue.second)
                     {
                            cout << listItem << " ";
                     }
                     cout << " ]\n";
              }
       }
       void DFS(string curNode, map<string, bool> &visited)
       {
              visited[curNode] = true;
              cout << curNode << " ";
              for (auto NodesListItems : this->vertices[curNode])
              {
                     if (not visited[NodesListItems])
                     {
                            DFS(NodesListItems, visited);
                     }
              }
       }
       void iterativeDFS(string curNode)
       {
              map<string, bool> visited;
              stack<string> st;
              st.push(curNode);
              while (not st.empty())
              {
                     string topNode = st.top();
                     st.pop();
                     cout << topNode << " ";
                     for (auto it = this->vertices[topNode].rbegin(); it != this->vertices[topNode].rend(); it++)
                     {
                            if (not visited[*it])
                            {
                                   visited[topNode] = true;
                                   st.push(*it);
                            }
                     }
              }
       }

       void BFS(string start)
       {
              map<string, bool> visited;
              queue<string> q;
              q.push(start);
              while (not q.empty())
              {
                     string front = q.front();
                     q.pop();
                     cout << front << " ";
                     for (auto it = vertices[front].begin(); it != vertices[front].end(); it++)
                     {
                            if (not visited[*it])
                            {
                                   visited[front] = true;
                                   q.push(*it);
                            }
                     }
              }
       }
       void RecursiveBFS(queue<string> &q, map<string, bool> &visited)
       {
              if (q.empty())
                     return;
              string front = q.front();
              q.pop();
              cout << front << " ";
              for (const auto &neighbor : vertices[front])
              {
                     if (!visited[neighbor])
                     {
                            visited[front] = true;
                            q.push(neighbor);
                     }
              }
              RecursiveBFS(q, visited);
       }
};

signed main()
{

       graph g;
       g.addVertex("A");
       g.addVertex("B");
       g.addVertex("C");
       g.addVertex("D");
       g.addVertex("E");
       g.addVertex("F");

       g.addEdge("A", "B");
       g.addEdge("A", "C");
       g.addEdge("B", "D");
       g.addEdge("B", "E");
       g.addEdge("A", "F");
       g.addEdge("C", "B");

       g.PrintGraph();
       map<string, bool> mp;
       g.DFS("A", mp);
       cout << "\n";
       g.iterativeDFS("A");
       cout << "\n";
       g.BFS("A");
       cout << "\n";

       queue<string> q;
       q.push("A");
       mp.clear();
       g.RecursiveBFS(q, mp);
}