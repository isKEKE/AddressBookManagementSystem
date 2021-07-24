#include "apps.h"

int main()
{
    int length = 1000;
    // 存放数据 - 结构体列表
    struct People contactPersons[length] = {
        {"A", "男", 1, 100, "北京"},
        {"B", "女", 1, 200, "上海"}
    };
    // 当前类db存放数据数量
    int count = 2;
    // 条件判断函数
    getBranch(contactPersons, &count, length);
    system("pause");
    return 0;
}

