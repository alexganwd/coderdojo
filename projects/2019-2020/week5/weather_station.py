
def run(dry_run=False, display=False):
    if dry_run:
        import mock_bme280
    else:
        import smbus2
        from bme280 import BME280
        pass

    import time
    import sqlite3

    if display:
        import ST7735

        from PIL import Image
        from PIL import ImageDraw
        from PIL import ImageFont

        # Create LCD class instance.
        display_interface = ST7735.ST7735(
            port=0,
            cs=1,
            dc=9,
            backlight=12,
            rotation=270,
            spi_speed_hz=10000000
        )

        # Initialise the display
        display_interface.begin()

        # Width and height to calculate text position.
        WIDTH = display_interface.width
        HEIGHT = display_interface.height

        # New canvas to draw on.
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Text settings.
        # use a bitmap font
        font = ImageFont.load("arial.pil")
        font_size = 10
        font = ImageFont.truetype("arial.ttf", font_size)
        text_colour = (255, 255, 255)
        back_colour = (0, 170, 170)

        message = "Weather Station"
        size_x, size_y = draw.textsize(message, font)

        # Calculate text position
        x = (WIDTH - size_x) / 2
        y = (HEIGHT / 2) - (size_y / 2)

        # Draw background rectangle and write text.
        draw.rectangle((0, 0, 160, 80), back_colour)
        draw.text((x, y), message, font=font, fill=text_colour)
        display_interface.display(img)

    # Initialise the BME280
    if not dry_run:
        bus = smbus2.SMBus(1)
        bme280 = BME280(i2c_dev=bus)
        pass

    try:
        if dry_run:
            db_connection = sqlite3.connect('meassurements-test')
        else:
            db_connection = sqlite3.connect('meassurements')
    except sqlite3.Error as e:
        print("Database error: %s" % e)

    try:
        db_connection.execute('CREATE TABLE IF NOT EXISTS bme280 (id Integer primary key AUTOINCREMENT, temperature REAL, humidity REAL, pressure REAL);')
    except sqlite3.IntegrityError as e:
        print("Exception in _query %s" % e)

    while True:
        if dry_run:
            temperature = mock_bme280.get_temperature()
            pressure = mock_bme280.get_pressure()
            humidity = mock_bme280.get_humidity()
        else:
            temperature = bme280.get_temperature()
            pressure = bme280.get_pressure()
            humidity = bme280.get_humidity()

            if display:
                message = "Temperature: " + str(temperature) + "\n Pressure:" + str(pressure) + "\n Humidity: " + str(humidity)
                size_x, size_y = draw.textsize(message, font)
                # Calculate text position
                x = 0
                y = HEIGHT

                # Draw background rectangle and write text.
                draw.rectangle((0, 0, 160, 80), back_colour)
                draw.text((x, y), message, font=font, fill=text_colour)
                display_interface.display(img)

            print ("We use hardware")
        try:
            db_connection.execute('INSERT INTO bme280 (temperature, humidity, pressure) VALUES (?, ?, ?)',  (temperature, humidity, pressure))
            db_connection.commit()
        except sqlite3.IntegrityError as e:
            print("Exception in _query %s" % e)

        print ("Temperature " + str(temperature))
        print ("Humedity: " + str(humidity))
        print ("Pressure: " + str(pressure))
        time.sleep(5)
