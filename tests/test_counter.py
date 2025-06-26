from nicegui.testing import User
from nicegui import ui

async def test_counter_initial_value(user: User) -> None:
    await user.open('/counter')
    await user.should_see('0')

async def test_counter_increment(user: User) -> None:
    await user.open('/counter')
    increment_button = user.find(marker='increment_button')
    increment_button.click()
    await user.should_see('1')
    increment_button.click()
    await user.should_see('2')

async def test_counter_decrement(user: User) -> None:
    await user.open('/counter')
    decrement_button = user.find(marker='decrement_button')
    decrement_button.click()
    await user.should_see('-1')
    decrement_button.click()
    await user.should_see('-2')

async def test_counter_increment_and_decrement(user: User) -> None:
    await user.open('/counter')
    increment_button = user.find(marker='increment_button')
    decrement_button = user.find(marker='decrement_button')

    increment_button.click() # 1
    increment_button.click() # 2
    decrement_button.click() # 1
    await user.should_see('1')

    decrement_button.click() # 0
    decrement_button.click() # -1
    increment_button.click() # 0
    await user.should_see('0')