// Automated Test Runner for Report Data Collection
// Runs all 6 configurations and exports results to CSV

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include "include/URLHashTable.h"

using namespace std;

struct TestResult {
    int tableSize;
    double loadFactor;
    double avgComparisons;
    int maxComparisons;
    double avgTime;
    int numQueries;
    string hashFunction;
    string probingMethod;
};

bool isValidURL(const string& url) {
    if(url.length() < 6) return false;
    if(url.length() >= 7 && url.substr(0, 7) == "http://") return true;
    if(url.length() >= 6 && url.substr(0, 6) == "http//") return true;
    if(url.length() >= 8 && url.substr(0, 8) == "https://") return true;
    if(url.length() >= 7 && url.substr(0, 7) == "https//") return true;
    return false;
}

vector<string> loadURLsFromFile(const string& filename, int& tableSize) {
    vector<string> urls;
    ifstream inputFile(filename);
    
    if(!inputFile.is_open()){
        cout << "Error opening file: " << filename << endl;
        return urls;
    }
    
    string line;
    if(getline(inputFile, line)){
        stringstream ss(line);
        ss >> tableSize;
    }
    
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

TestResult runTest(int size, const vector<string>& urls, HashType hashType, ProbingMethod probingType, 
                   const string& hashName, const string& probeName) {
    URLHashTable* hashTable = new URLHashTable(size);
    hashTable->setHashFunction(hashType);
    hashTable->setProbingMethod(probingType);
    
    int counter = 0;
    for(const string& url : urls){
        if(hashTable->insertURL(url)){
            counter++;
        }
    }
    
    TestResult result;
    result.tableSize = size;
    result.loadFactor = hashTable->getLoadFactor();
    result.avgComparisons = hashTable->getStats().getAvgComparisons();
    result.maxComparisons = hashTable->getStats().getMaxComp();
    result.avgTime = hashTable->getStats().getAvgTime();
    result.numQueries = hashTable->getStats().getNumQueries();
    result.hashFunction = hashName;
    result.probingMethod = probeName;
    
    delete hashTable;
    return result;
}

int main(){
    string filename = "test1.txt";
    int originalSize = 0;
    
    cout << "Loading URLs from " << filename << "..." << endl;
    vector<string> urls = loadURLsFromFile(filename, originalSize);
    
    if(urls.empty()){
        cout << "No valid URLs found. Exiting." << endl;
        return 1;
    }
    
    cout << "Loaded " << urls.size() << " URLs." << endl;
    cout << "\nRunning all configurations (this will take a few minutes)...\n" << endl;
    
    int numURLs = urls.size();
    vector<int> tableSizes;
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
    
    vector<TestResult> allResults;
    
    // Test all 6 configurations
    struct Config {
        HashType hashType;
        string hashName;
        ProbingMethod probingType;
        string probeName;
    };
    
    Config configs[] = {
        {BITWISE_HASH, "Bitwise", LINEAR_PROBING, "Linear"},
        {BITWISE_HASH, "Bitwise", QUADRATIC_PROBING, "Quadratic"},
        {POLYNOMIAL_HASH, "Polynomial", LINEAR_PROBING, "Linear"},
        {POLYNOMIAL_HASH, "Polynomial", QUADRATIC_PROBING, "Quadratic"},
        {UNIVERSAL_HASH, "Universal", LINEAR_PROBING, "Linear"},
        {UNIVERSAL_HASH, "Universal", QUADRATIC_PROBING, "Quadratic"}
    };
    
    int totalTests = 6 * tableSizes.size();
    int currentTest = 0;
    
    for(const auto& config : configs){
        cout << "\n========================================" << endl;
        cout << "Testing: " << config.hashName << " + " << config.probeName << endl;
        cout << "========================================" << endl;
        
        for(size_t i = 0; i < tableSizes.size(); i++){
            currentTest++;
            int size = tableSizes[i];
            double expectedLoadFactor = (double)numURLs / size;
            
            cout << "Progress: " << currentTest << "/" << totalTests 
                 << " - Size: " << size << " (α=" << fixed << setprecision(2) 
                 << expectedLoadFactor << ")..." << flush;
            
            TestResult result = runTest(size, urls, config.hashType, config.probingType, 
                                       config.hashName, config.probeName);
            allResults.push_back(result);
            
            cout << " Done!" << endl;
        }
    }
    
    // Export to CSV
    ofstream csvFile("test_results.csv");
    csvFile << "HashFunction,ProbingMethod,TableSize,LoadFactor,AvgComparisons,MaxComparisons,AvgTime,NumQueries\n";
    
    for(const auto& result : allResults){
        csvFile << result.hashFunction << ","
                << result.probingMethod << ","
                << result.tableSize << ","
                << fixed << setprecision(6) << result.loadFactor << ","
                << result.avgComparisons << ","
                << result.maxComparisons << ","
                << scientific << setprecision(9) << result.avgTime << ","
                << result.numQueries << "\n";
    }
    csvFile.close();
    
    // Also create Python-ready data file
    ofstream pyFile("test_data.py");
    pyFile << "# Test results collected on " << __DATE__ << "\n\n";
    pyFile << "data = {\n";
    pyFile << "    'load_factors': [";
    
    // Get load factors from first configuration
    for(size_t i = 0; i < 10; i++){
        pyFile << fixed << setprecision(4) << allResults[i].loadFactor;
        if(i < 9) pyFile << ", ";
    }
    pyFile << "],\n\n";
    
    // Export each configuration
    string configNames[] = {
        "bitwise_linear", "bitwise_quad",
        "poly_linear", "poly_quad",
        "universal_linear", "universal_quad"
    };
    
    for(int c = 0; c < 6; c++){
        pyFile << "    '" << configNames[c] << "_avg': [";
        for(int i = 0; i < 10; i++){
            pyFile << fixed << setprecision(6) << allResults[c*10 + i].avgComparisons;
            if(i < 9) pyFile << ", ";
        }
        pyFile << "],\n";
        
        pyFile << "    '" << configNames[c] << "_max': [";
        for(int i = 0; i < 10; i++){
            pyFile << allResults[c*10 + i].maxComparisons;
            if(i < 9) pyFile << ", ";
        }
        pyFile << "],\n";
        
        pyFile << "    '" << configNames[c] << "_time': [";
        for(int i = 0; i < 10; i++){
            pyFile << scientific << setprecision(9) << allResults[c*10 + i].avgTime;
            if(i < 9) pyFile << ", ";
        }
        pyFile << "],\n\n";
    }
    
    pyFile << "}\n";
    pyFile.close();
    
    cout << "\n\n========================================" << endl;
    cout << "ALL TESTS COMPLETED!" << endl;
    cout << "========================================" << endl;
    cout << "Total tests run: " << totalTests << endl;
    cout << "\nOutput files created:" << endl;
    cout << "  1. test_results.csv - Raw data in CSV format" << endl;
    cout << "  2. test_data.py - Python data ready for graphing" << endl;
    cout << "\nNext steps:" << endl;
    cout << "  1. Copy test_data.py contents into generate_graphs.py" << endl;
    cout << "  2. Run: python generate_graphs.py" << endl;
    cout << "  3. Check graphs/ folder for PNG images" << endl;
    cout << "========================================" << endl;
    
    return 0;
}
