#!/usr/bin/env python3
#!/usr/bin/env python3
#!/usr/bin/env python3
#!/usr/bin/env python3
import asyncio

async def my_function():
    print("wzza")
    task = asyncio.create_task(wal())
    
    print("waaaa")

async def wal():
    await asyncio.sleep(3)
    print("wa")

asyncio.run(my_function())
