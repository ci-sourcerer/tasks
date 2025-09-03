import logging

LOGGER = logging.getLogger(__name__)

def say_hello() -> None:
    print("Hello!")

async def some_task(a: int, b: int) -> int:
    LOGGER.info("Doin' some stuff")
    return a + b
