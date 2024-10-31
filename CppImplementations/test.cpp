#include <iostream>
#include <map>
#include <list>
#include <stack>
#include <queue>

using namespace std;

class graph
{
       map<string, list<string>> verteces;

public:
       void addVertex(string edge)
       {
              if (this->verteces.find(edge) == this->verteces.end())
                     this->verteces[edge] = list<string>();
       }

       void addEdge(string start, string end)
       {

              if (this->verteces.find(start) != this->verteces.end() && this->verteces.find(end) != this->verteces.end())
              {
                     verteces[start].push_back(end);
              }
       }

       void DFS(string start, map<string, bool> &visited)
       {
              visited[start] = true;
              cout << start << " ";
              for (auto NodeListItem : this->verteces[start])
              {
                     if (not visited[NodeListItem])
                            DFS(NodeListItem, visited);
              }
       }

       void DFSIterative(string start)
       {
              map<string, bool> visited;
              stack<string> st;
              st.push(start);
              visited[start] = true;
              while (!st.empty())
              {
                     string top = st.top();
                     st.pop();
                     cout << top << " ";
                     for (auto it = this->verteces[top].rbegin(); it != this->verteces[top].rend(); it++)
                     {
                            if (not visited[*it])
                            {
                                   visited[*it] = true;
                                   st.push(*it);
                            }
                     }
              }
       }

       void BFSiterative(string start)
       {
              map<string, bool> visited;
              queue<string> q;
              q.push(start);
              visited[start] = true;
              while (not q.empty())
              {
                     string front = q.front();
                     q.pop();
                     cout << front << " ";
                     for (auto it = this->verteces[front].begin(); it != this->verteces[front].end(); it++)
                     {

                            if (not visited[*it])
                            {
                                   visited[*it] = true;
                                   q.push(*it);
                            }
                     }
              }
       }

       void BFS(queue<string>&q, map<string,bool>&visited){
              while(not q.empty()){
                     string front = q.front();
                     q.pop();
                     cout << front << " ";
                     for (auto it = this->verteces[front].begin(); it != this->verteces[front].end(); it++){
                            if(not visited[*it]){
                                   visited[*it] = true;
                                   q.push(*it);
                            }
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
       g.addEdge("E", "F");
       g.addEdge("F", "B");

       g.DFSIterative("A");
       map<string, bool> mp;
       cout << "\n";
       g.DFS("A", mp);
       cout << "\n";
       g.BFSiterative("A");
       queue<string>q;
       q.push("A");
       mp.clear();
       cout << "\n";
       g.BFS(q, mp);
}