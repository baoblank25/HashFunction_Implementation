// ASU CSE310 Hash Table Assignment
// File: Statistics.cpp
// Description: Implementation of statistics tracking


#include "../include/Statistics.h"


Statistics::Statistics(){
    numComp = 0;
    maxComp = 0;
    numQueries = 0;
    totalTime = 0;
}


void Statistics::recordQuery(int comp, clock_t time){
    numComp += comp;
    numQueries++;
    totalTime += time;
    
    if(comp>maxComp){
        maxComp = comp;
    }
}


void Statistics::reset(){
    numComp = 0;
    maxComp = 0;
    numQueries = 0;
    totalTime = 0;
}


void Statistics::display(int tableSize, int numElements, double loadFactor){
    cout << "\nHash Table Stats" << endl;
    cout << fixed << setprecision(4);
    cout << "Table Size: " << tableSize << endl;
    cout << "Number of Elements: " << numElements << endl;
    cout << "Load Factor: " << loadFactor << endl;
    cout << "Total Queries: " << numQueries << endl;
    
    if(numQueries>0){
        double avgComp = (double)numComp/numQueries;
        double avgTime = ((double)totalTime/CLOCKS_PER_SEC)/numQueries;
        double performanceRatio = avgComp/(1+loadFactor);
        
        cout << "Average Comparisons per Query: " << avgComp << endl;
        cout << "Maximum Comparisons: " << maxComp << endl;
        cout << fixed << setprecision(8);
        cout << "Average Time: " << avgTime << " seconds" << endl;
        cout << fixed << setprecision(2);
        cout << "Performance Ratio: " << performanceRatio << endl;
    }
}


int Statistics::getTotalComp() const{
    return numComp;
}


int Statistics::getMaxComp() const{
    return maxComp;
}


int Statistics::getNumQueries() const{
    return numQueries;
}
