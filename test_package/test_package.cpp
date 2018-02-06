#include "sqlite_orm/sqlite_orm.h"

int main(int, char* [])
{
    auto storage = sqlite_orm::make_storage(":memory:");
}
