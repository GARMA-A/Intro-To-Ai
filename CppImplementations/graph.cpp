#include <iostream>
#include <list>
#include <map>
#include <vector>
using namespace std;

class graph
{
       map<string, list<string>> verteces;

public:
       void addVertex(string newVertex)
       {
              this->verteces[newVertex] = list<string>();
       }

       bool HasThisVertex(string Node)
       {
              return this->verteces.find(Node) != verteces.end();
       }

       void addEdge(string startNode, string endNode)
       {
              if (HasThisVertex(startNode) && HasThisVertex(endNode))
              {
                     this->verteces[startNode].push_back(endNode);
              }
       }
       void PrintGraph()
       {
              for (auto keyValue : this->verteces)
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
              for (auto NodesListItems : this->verteces[curNode])
              {
                     if (not visited[NodesListItems])
                     {
                            DFS(NodesListItems, visited);
                     }
              }
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
}