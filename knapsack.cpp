#include<iostream>

using namespace std;

int main(){
    int weights[] = {0, 8, 2, 6, 1};
    int profit[] = {0, 50, 150, 210, 30};

    int data[5][11];

    const int n = 4;
    const int maxCapacity = 10;

    for (int itemNum = 0; itemNum <= n; itemNum++){
        for (int capacity = 0; capacity <= maxCapacity; capacity++){
            if (itemNum == 0 || capacity == 0)
            {
                data[itemNum][capacity] = 0;
            }
            else if(weights[itemNum] <= capacity)
            {
                data[itemNum][capacity] = std::max(profit[itemNum] + data[itemNum - 1][capacity - weights[itemNum]],
                                                data[itemNum - 1][ capacity]);
            }
            else
            {
                data[itemNum][capacity] = data[itemNum - 1][ capacity];
            }
        }
    }
    std::cout<<"Max value of the items included: "<<data[n][ maxCapacity]<<endl;
}
