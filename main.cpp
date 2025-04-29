#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <thread>

int main() {
    std::srand(static_cast<unsigned>(std::time(nullptr)));
    std::vector<char*> blocks;
    const size_t max_block_size = 1024 * 1024;
    const size_t max_blocks = 5000;

    while (true) {
        int action = std::rand() % 2;

        if (action == 0 || blocks.empty()) {
            size_t size = 1024 + std::rand() % max_block_size;
            char* memory = new(std::nothrow) char[size];
            if (memory)
                blocks.push_back(memory);
        } else {
            size_t index = std::rand() % blocks.size();
            delete[] blocks[index];
            blocks.erase(blocks.begin() + index);
        }

        if (blocks.size() > max_blocks) {
            delete[] blocks.front();
            blocks.erase(blocks.begin());
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }

    return 0;
}
