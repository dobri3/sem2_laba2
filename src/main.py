from asyncio import Task


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    task = Task("обработать заказ", 1, "new")
    print(task.id)
    print(task.description)
    print(task.is_ready)
    
    task.status = "done"
    print(task.is_ready)
    
    task.priority = 30 #упадет


if __name__ == "__main__":
    main()
