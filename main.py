def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_uart_data_received():
    global data
    data = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    basic.show_string(data)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

data = ""
basic.show_icon(IconNames.HEART)
bluetooth.start_uart_service()