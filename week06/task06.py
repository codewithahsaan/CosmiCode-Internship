import asyncio
import random

# Simulate an asynchronous I/O task (e.g., fetching data from an API)
async def fetch_data(source):
    print(f"📡 Fetching data from {source}...")
    await asyncio.sleep(random.randint(1, 3))  # simulate network delay
    print(f"✅ Done fetching from {source}")
    return f"Data from {source}"

# Main async function
async def main():
    # Create tasks (concurrent execution)
    task1 = asyncio.create_task(fetch_data("Server 1"))
    task2 = asyncio.create_task(fetch_data("Server 2"))
    task3 = asyncio.create_task(fetch_data("Server 3"))

    # Wait until all tasks are completed
    results = await asyncio.gather(task1, task2, task3)

    print("\n📊 Results collected:")
    for res in results:
        print(res)

# Run the asyncio program
asyncio.run(main())
