from nicegui import ui

def create() -> None:
    @ui.page('/counter')
    def page():
        # Initialize a Python variable for the counter
        count = 0

        ui.label('Counter:').classes('text-2xl')
        # Create a label to display the count and store a reference to it
        count_display = ui.label(str(count)).classes('text-4xl font-bold')

        def increment():
            nonlocal count
            count += 1
            count_display.set_text(str(count))

        def decrement():
            nonlocal count
            count -= 1
            count_display.set_text(str(count))

        with ui.row():
            ui.button('Increment', on_click=increment).mark('increment_button')
            ui.button('Decrement', on_click=decrement).mark('decrement_button')