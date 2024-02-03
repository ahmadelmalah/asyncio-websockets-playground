import asyncio, time

async def some_background_tasks(num):
    for i in range(num):
        print(f'Task {i} is running...')
        await asyncio.sleep(1)

async def corountine_delay(delay):
    print(f'Waiting for {delay} seconds...')
    await asyncio.sleep(delay)
    return delay

async def main():
    asyncio.create_task(some_background_tasks(10))
    print(f'{time.ctime()} Hello!')
    await corountine_delay(3)
    print(f'{time.ctime()} Goodbye!')

# loop = asyncio.get_event_loop()
# task = loop.create_task(main())
# loop.run_until_complete(task)
# pending = asyncio.all_tasks(loop=loop)
# for task in pending:
#     task.cancel()
# group = asyncio.gather(*pending, return_exceptions=True)
# loop.run_until_complete(group)
# loop.close
asyncio.run(main())
print('Done!')