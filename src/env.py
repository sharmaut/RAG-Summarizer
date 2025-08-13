import asyncio

async def do_migrations():
    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)

asyncio.run(do_migrations())

