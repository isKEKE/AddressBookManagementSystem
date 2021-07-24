#include "library.h"
#include "info.h"

void serverInfoOutput()
{
    cout << "*****************************" << endl;
    cout << "*****\t1、添加联系人\t*****" << endl;
    cout << "*****\t2、显示联系人\t*****" << endl;
    cout << "*****\t3、删除联系人\t*****" << endl;
    cout << "*****\t4、查找联系人\t*****" << endl;
    cout << "*****\t5、修改联系人\t*****" << endl;
    cout << "*****\t6、清空联系人\t*****" << endl;
    cout << "*****\t0、退出通讯录\t*****" << endl;
    cout << "*****************************" << endl;
}

int userInput()
{
    int tmp;
    cout << ">>>";
    cin >> tmp;
    return tmp;
}

void test(struct People *p_people)
{
    cout << p_people[0].name << endl;
}


void write(struct People *p_people, const int *p_index)
{
    cout << "姓名:\t";
    cin >> p_people[*p_index].name;
    cout << "性别:\t";
    cin >> p_people[*p_index].gender;
    cout << "年龄:\t\t";
    cin >> p_people[*p_index].age;
    cout << "电话:\t\t";
    cin >> p_people[*p_index].phone;
    cout << "地址:\t";
    cin >> p_people[*p_index].address;
}

void addContactPerson(struct People *p_people, int *p_count) // 添加联系人
{
    write(p_people, p_count);
    *p_count += 1;
}

void show(const struct People *p_people, int i)
{
    cout << "姓名: " << p_people[i].name
         << "\t性别: " << p_people[i].gender
         << "\t年龄: " << p_people[i].age
         << "\t电话: " << p_people[i].phone
         << "\t地址: " << p_people[i].address
         << endl;
}

void showContactPerson(const struct People *p_people, const int *p_count) // 显示联系人
{
    for (int i = 0; i < *p_count; i++)
    {
        show(p_people, i);
    }
}

int findContactPerson(struct People *p_people, const int *p_count, bool trace=true) // 查找联系人
{
    string keyword;
    cout << "请输入关键字(姓名):\t";
    cin >> keyword;
    for (int i = 0; i < *p_count; i++)
    {
        if (keyword == p_people[i].name)
        {
            // 打印
            if (trace)
            {
                show(p_people, i);
            }
            return i;
        }
    }
    return -1;
}

void delContactPerson(struct People *p_people, int *p_count) // 删除联系人
{
    int tmp_index = findContactPerson(p_people, p_count, false);
    if (tmp_index != -1)
    {
        string flag;
        cout << "请问确定要删除" << p_people[tmp_index].name << "联系人吗？y/n ";
        cin >> flag;
        if ((flag == "y") || (flag == "Y"))
        {
            for (int i = tmp_index; i < *p_count; i++)
            {
                p_people[i] = p_people[(i + 1)];
            }
            *p_count -= 1;
            cout << "删除成功" << endl;
        }
    }
    else
    {
        cout << "删除失败" << endl;
    }
}


void updateContactPerson(struct People *p_people, const int *p_count) // 修改联系人
{
    int tmp_index = findContactPerson(p_people, p_count, false);
    if (tmp_index != -1)
    {
        write(p_people, &tmp_index);
        cout << "修改成功" << endl;
    }
}

void clearContactPerson(int *p_count) // 清空联系人
{
    *p_count = 0;
}

void getBranch(struct People *p_people, int *p_count, int length)
{
    /*
        *p_people: 表示要存放数据至结构体列表，是个指针；
        *p_count : 表示当前存放在结构体列表中数量，是个指针；
        length   : 表示最大可存放数据大小。 
    */
    int reply;
    while (true)
    {
        serverInfoOutput();
        // 获得用户输入
        reply = userInput();
        if (!reply)
        {
            break;
        }
        // 根据用户输入选择进入分支语句
        switch(reply)
        {
            case 1:
                addContactPerson(p_people, p_count);
                break;
            case 2:
                showContactPerson(p_people, p_count);
                break;
            case 3:
                delContactPerson(p_people, p_count);
                break;
            case 4:
                findContactPerson(p_people, p_count);
                break;
            case 5:
                updateContactPerson(p_people, p_count);
                break;
            case 6:
                clearContactPerson(p_count);
                break;
            default:
                break;
        }
        // 测试函数，类断点作用，可删
        // test(p_people);

        // 用户操作完成阻塞，并清除界面内容。
        system("pause");
        system("cls");
    }
    
}