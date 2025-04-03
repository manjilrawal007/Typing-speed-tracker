#include <iostream>
#include <chrono>
#include <cstdint>

int main() {
    using namespace std;
    using namespace std::chrono;

    volatile int32_t a = 1, b = 2, c = 3; // use volatile to avoid optimization

    auto start = high_resolution_clock::now();

    // 10^10 additions
    for (uint64_t i = 0; i < 1000000000ULL; ++i) {
        a = a + b;
    }

    // 5 * 10^9 multiplications
    for (uint64_t i = 0; i < 500000000ULL; ++i) {
        b = b * c;
    }

    // 2 * 10^9 divisions
    for (uint64_t i = 0; i < 200000000ULL; ++i) {
        if (c != 0) a = a / c;
    }

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(end - start);

    cout << "Total execution time for 32-bit Integer Benchmark: "
         << duration.count() << " seconds" << endl;

    // Use result to avoid optimization
    cout << "Final value of a: " << a << endl;

    return 0;
}

