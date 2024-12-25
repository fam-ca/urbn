import asyncio


async def start_strongman(name, power):
    total_number = 5
    print(f'Силач {name} начал соревнования.')
    for i in range(total_number):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_for_silach_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_for_silach_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_for_silach_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_for_silach_1
    await task_for_silach_2
    await task_for_silach_3

if __name__ == "__main__":
    asyncio.run(start_tournament())
