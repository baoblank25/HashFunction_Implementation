#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <limits>
#include <vector>
#include "../include/URLHashTable.h"

using namespace std;

//Structure to hold test results
struct TestResult {
    int tableSize;
    double loadFactor;
    double avgComparisons;
    int maxComparisons;
    double avgTime;
    int numQueries;
};

//Helper function
bool isValidURL(const string& url) {
    if(url.length() < 6) return false;
    
    if(url.length() >= 7 && url.substr(0, 7) == "http://") return true;
    if(url.length() >= 6 && url.substr(0, 6) == "http//") return true;
    if(url.length() >= 8 && url.substr(0, 8) == "https://") return true;
    if(url.length() >= 7 && url.substr(0, 7) == "https//") return true;
    
    return false;
}

//Function to load URLs from CSV file
vector<string> loadURLsFromFile(const string& filename, int& tableSize) {
    vector<string> urls;
    ifstream inputFile(filename);
    
    if(!inputFile.is_open()){
        cout << "Error opening file: " << filename << endl;
        return urls;
    }
    
    //Read table size from first line
    string line;
    if(getline(inputFile, line)){
        stringstream ss(line);
        ss >> tableSize;
    }
    
    //Read all URLs
    while(getline(inputFile, line)){
        stringstream ss(line);
        string url;
        
        while(getline(ss, url, ',')){
            size_t start = url.find_first_not_of(" \t\r\n");
            size_t end = url.find_last_not_of(" \t\r\n");
            
            if(start != string::npos && end != string::npos){
                url = url.substr(start, end - start + 1);
            }
            
            if(!url.empty() && isValidURL(url)){
                urls.push_back(url);
            }
        }
    }
    
    inputFile.close();
    return urls;
}

//Function to run a single test
TestResult runTest(int size, const vector<string>& urls, HashType hashType, ProbingMethod probingType) {
    URLHashTable* hashTable = new URLHashTable(size);
    hashTable->setHashFunction(hashType);
    hashTable->setProbingMethod(probingType);
    
    int counter = 0;
    
    //Insert all URLs
    for(const string& url : urls){
        if(hashTable->insertURL(url)){
            counter++;
        }
    }
    cout << "Table Size: " << size << endl;
    cout << "URLs Inserted: " << counter << endl;
    
    hashTable->displayStats();
    
    //Collect stats
    TestResult result;
    result.tableSize = size;
    result.loadFactor = hashTable->getLoadFactor();
    result.avgComparisons = hashTable->getStats().getAvgComparisons();
    result.maxComparisons = hashTable->getStats().getMaxComp();
    result.avgTime = hashTable->getStats().getAvgTime();
    result.numQueries = hashTable->getStats().getNumQueries();
    
    delete hashTable;
    return result;
}

int main(){
    string filename;
    int originalSize = 0;
    
    //Get CSV filename and load URLs
    cout << "Enter CSV filename: ";
    getline(cin, filename);
    
    vector<string> urls = loadURLsFromFile(filename, originalSize);
    
    if(urls.empty()){
        cout << "No valid URLs found in file. Exiting." << endl;
        return 1;
    }
    
    cout << "Loaded " << urls.size() << " URLs from file." << endl;
    cout << "Original table size from CSV: " << originalSize << endl;
    
    //Choose testing mode
    int mode;
    while(true){
        cout << "\nSelect mode:" << endl;
        cout << "1. Single table size test (interactive)" << endl;
        cout << "2. Multiple table size test (10 sizes)" << endl;
        cout << "Enter choice (1 or 2): ";
        
        if(cin >> mode){
            if(mode == 1 || mode == 2){
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                break;
            }
            else{
                cout << "Only enter 1 or 2." << endl;
            }
        }
        else{
            cout << "Only enter 1 or 2." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
    
    //Get hash function type
    int hashChoice;
    while(true){
        cout << "\nSelect hash function:" << endl;
        cout << "1. Bitwise Mixing Hash" << endl;
        cout << "2. Polynomial Rolling Hash" << endl;
        cout << "3. Universal Hashing" << endl;
        cout << "Enter choice (1, 2, or 3): ";
        
        if(cin >> hashChoice){
            if(hashChoice >= 1 && hashChoice <= 3){
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                break;
            }
            else{
                cout << "Only enter 1, 2, or 3." << endl;
            }
        }
        else{
            cout << "Only enter 1, 2, or 3." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
    
    HashType hashType;
    if(hashChoice == 1){
        hashType = BITWISE_HASH;
        cout << "Using Bitwise Mixing Hash" << endl;
    }
    else if(hashChoice == 2){
        hashType = POLYNOMIAL_HASH;
        cout << "Using Polynomial Rolling Hash" << endl;
    }
    else{
        hashType = UNIVERSAL_HASH;
        cout << "Using Universal Hashing" << endl;
    }
    
    //Get probing method
    int probingChoice;
    while(true){
        cout << "\nSelect probing method:" << endl;
        cout << "1. Linear Probing" << endl;
        cout << "2. Quadratic Probing" << endl;
        cout << "Enter choice (1 or 2): ";
        
        if(cin >> probingChoice){
            if(probingChoice == 1 || probingChoice == 2){
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                break;
            }
            else{
                cout << "Only enter 1 or 2." << endl;
            }
        }
        else{
            cout << "Only enter 1 or 2." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
    
    ProbingMethod probingType = (probingChoice == 1) ? LINEAR_PROBING : QUADRATIC_PROBING;
    cout << "Using " << (probingChoice == 1 ? "Linear" : "Quadratic") << " Probing" << endl;
    
    if(mode == 1){
        int size;
        cout << "\nEnter hash table size: ";
        cin >> size;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        
        URLHashTable* hashTable = new URLHashTable(size);
        hashTable->setHashFunction(hashType);
        hashTable->setProbingMethod(probingType);
        
        int counter = 0;
        
        //Insert URLs
        cout << "\nInserting URLs into hash table..." << endl;
        for(const string& url : urls){
            if(hashTable->insertURL(url)){
                counter++;
            }
        }
        
        cout << "\nHash table size is: " << size << endl;
        cout << "Total URLs inserted: " << counter << endl;
        
        // Interactive command loop
        do{
            cout << "\nAvailable Commands" << endl;
            cout << "hashSearch,<URL>" << endl;
            cout << "hashDelete,<URL>" << endl;
            cout << "hashDisplay" << endl;
            cout << "hashStats" << endl;
            cout << "hashReset" << endl;
            cout << "End" << endl;
            cout << "\nEnter command:" << endl;
            string cLine;
            getline(cin, cLine);
            
            if(cLine=="End"){
                break;
            }
            
            string delimiter = ",";
            size_t pos = cLine.find(delimiter);
            
            if(pos==string::npos){
                if(cLine=="hashDisplay"){
                    hashTable->displayTable();
                }
                else if(cLine=="hashStats"){
                    hashTable->displayStats();
                }
                else if(cLine=="hashReset"){
                    hashTable->resetStats();
                    cout << "Stats have been reset." << endl;
                }
                else{
                    cout << "Enter a valid command." << endl;
                }
            }
            else{
                string command = cLine.substr(0, pos);
                string url = cLine.substr(pos+delimiter.length());
                
                if(command=="hashSearch"){
                    if(!url.empty()){
                        hashTable->searchURL(url);
                    }
                    else{
                        cout << "Enter a valid URL." << endl;
                    }
                }
                else if(command=="hashDelete"){
                    if(!url.empty()){
                        bool found = hashTable->searchURL(url);
                        if(found){
                            hashTable->deleteURL(url);
                            counter--;
                        }
                    }
                    else{
                        cout << "Enter a valid URL." << endl;
                    }
                }
                else{
                    cout << "Enter a valid command." << endl;
                }
            }
        }while(true);
        
        cout << "\nFinal Stats" << endl;
        hashTable->displayStats();
        
        delete hashTable;
    }
    else{
        cout << "Testing same " << urls.size() << " URLs with different table sizes" << endl;
        
        //Generate at least 10 different table sizes
        vector<int> tableSizes;
        int numURLs = urls.size();
        
        //Calculate sizes for different load factors
        tableSizes.push_back(numURLs * 3);
        tableSizes.push_back(numURLs * 2);
        tableSizes.push_back((numURLs * 3) / 2);
        tableSizes.push_back((numURLs * 4) / 3); 
        tableSizes.push_back((numURLs * 5) / 4);
        tableSizes.push_back((numURLs * 10) / 9);
        tableSizes.push_back((numURLs * 20) / 19);
        tableSizes.push_back(numURLs + 100);
        tableSizes.push_back(numURLs + 50);
        tableSizes.push_back(numURLs + 10);
        
        //Store results for summary
        vector<TestResult> results;
        
        //Run tests for each table size
        for(int i = 0; i < tableSizes.size(); i++){
            int size = tableSizes[i];
            double expectedLoadFactor = (double)numURLs / size;
            
            cout << "TEST #" << (i+1) << " - Table Size: " << size << endl;
            cout << "Expected Load Factor: " << fixed << setprecision(4) << expectedLoadFactor << endl;
            
            TestResult result = runTest(size, urls, hashType, probingType);
            results.push_back(result);
            
            //Pause between tests
            if(i < tableSizes.size() - 1){
                cout << "\nPress Enter to continue to next test...";
                cin.get();
            }
        }
        
        //Display summary
        cout << "\n\n" << endl;
        cout << "BATCH TEST SUMMARY" << endl;
        
        //Find best and worst based on average comparisons
        int bestIdx = 0;
        int worstIdx = 0;
        
        for(int i = 1; i < results.size(); i++){
            if(results[i].avgComparisons < results[bestIdx].avgComparisons){
                bestIdx = i;
            }
            if(results[i].avgComparisons > results[worstIdx].avgComparisons){
                worstIdx = i;
            }
        }
        
        //Display all results in table format
        cout << "\nAll Test Results:" << endl;
        cout << fixed << setprecision(4);
        cout << left << setw(12) << "Table Size" 
             << setw(15) << "Load Factor" 
             << setw(18) << "Avg Comparisons"
             << setw(18) << "Max Comparisons"
             << setw(18) << "Avg Time (s)" << endl;
        cout << string(81, '-') << endl;
        
        for(int i = 0; i < results.size(); i++){
            cout << left << setw(12) << results[i].tableSize
                 << setw(15) << results[i].loadFactor
                 << setw(18) << results[i].avgComparisons
                 << setw(18) << results[i].maxComparisons
                 << fixed << setprecision(9) << setw(18) << results[i].avgTime
                 << endl;
        }
        
        //Display best performance
        cout << "BEST PERFORMANCE (Lowest Average Comparisons):" << endl;
        cout << fixed << setprecision(4);
        cout << "Table Size:           " << results[bestIdx].tableSize << endl;
        cout << "Load Factor:          " << results[bestIdx].loadFactor << endl;
        cout << "Avg Comparisons:      " << results[bestIdx].avgComparisons << endl;
        cout << "Max Comparisons:      " << results[bestIdx].maxComparisons << endl;
        cout << fixed << setprecision(9);
        cout << "Avg Time per Query:   " << results[bestIdx].avgTime << " seconds" << endl;
        cout << fixed << setprecision(2);
        cout << "Total Queries:        " << results[bestIdx].numQueries << endl;
        
        cout << "WORST PERFORMANCE (Highest Average Comparisons):" << endl;
        cout << fixed << setprecision(4);
        cout << "Table Size:           " << results[worstIdx].tableSize << endl;
        cout << "Load Factor:          " << results[worstIdx].loadFactor << endl;
        cout << "Avg Comparisons:      " << results[worstIdx].avgComparisons << endl;
        cout << "Max Comparisons:      " << results[worstIdx].maxComparisons << endl;
        cout << fixed << setprecision(9);
        cout << "Avg Time per Query:   " << results[worstIdx].avgTime << " seconds" << endl;
        cout << fixed << setprecision(2);
        cout << "Total Queries:        " << results[worstIdx].numQueries << endl;
        
        
    }
    
    return 0;
}
