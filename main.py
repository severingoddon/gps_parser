def ascii_converter(numbers):
    ascii_chars = []
    for num in numbers:
        ascii_char = chr(num)
        ascii_chars.append(ascii_char)
    return ''.join(ascii_chars)

# received NMEA message directly from GPS Module in ASCII
numbers = [36, 71, 78, 71, 71, 65, 44, 49, 54, 50, 57, 53, 53, 46, 48, 48, 48, 44, 52, 54, 53, 54, 46, 56, 57, 48, 55, 51, 44, 78, 44, 48, 48, 55, 50, 53, 46, 57, 56, 48, 54, 54, 44, 69, 44, 49, 44, 48, 52, 44, 53, 46, 49, 44, 45, 49, 53, 46, 50, 44, 77, 44, 52, 57, 46, 53, 44, 77, 44, 44, 42, 53, 56, 13, 10, 36, 71, 78, 71, 76, 76, 44, 52, 54, 53, 54, 46, 56, 57, 48, 55, 51, 44, 78, 44, 48, 48, 55, 50, 53, 46, 57, 56, 48, 54, 54, 44, 69, 44, 49, 54, 50, 57, 53, 53, 46, 48, 48, 48, 44, 65, 44, 65, 42, 52, 69, 13, 10, 36, 71, 78, 71, 83, 65, 44, 65, 44, 51, 44, 48, 50, 44, 48, 56, 44, 51, 50, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 49, 53, 46, 49, 44, 53, 46, 49, 44, 49, 52, 46, 50, 44, 49, 42, 51, 67, 13, 10, 36, 71, 78, 71, 83, 65, 44, 65, 44, 51, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 49, 53, 46, 49, 44, 53, 46, 49, 44, 49, 52, 46, 50, 44, 52, 42, 51, 50, 13, 10, 36, 71, 78, 71, 83, 65, 44, 65, 44, 51, 44, 56, 53, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 49, 53, 46, 49, 44, 53, 46, 49, 44, 49, 52, 46, 50, 44, 50, 42, 51, 57, 13, 10, 36, 71, 80, 71, 83, 86, 44, 51, 44, 49, 44, 48, 57, 44, 48, 49, 44, 55, 53, 44, 51, 51, 48, 44, 44, 48, 50, 44, 49, 53, 44, 49, 49, 48, 44, 50, 54, 44, 48, 51, 44, 52, 56, 44, 50, 52, 52, 44, 48, 54, 44, 48, 56, 44, 50, 57, 44, 49, 55, 50, 44, 50, 54, 44, 48, 42, 54, 55, 13, 10, 36, 71, 80, 71, 83, 86, 44, 51, 44, 50, 44, 48, 57, 44, 49, 52, 44, 49, 55, 44, 50, 55, 53, 44, 44, 49, 55, 44, 50, 51, 44, 51, 49, 53, 44, 44, 50, 49, 44, 55, 51, 44, 48, 57, 52, 44, 44, 50, 56, 44, 48, 54, 44, 48, 57, 53, 44, 44, 48, 42, 54, 52, 13, 10, 36, 71, 80, 71, 83, 86, 44, 51, 44, 51, 44, 48, 57, 44, 51, 50, 44, 51, 50, 44, 48, 53, 52, 44, 48, 57, 44, 48, 42, 53, 52, 13, 10, 36, 66, 68, 71, 83, 86, 44, 49, 44, 49, 44, 48, 51, 44, 49, 49, 44, 55, 57, 44, 50, 56, 48, 44, 44, 50, 49, 44, 55, 49, 44, 48, 55, 55, 44, 44, 51, 52, 44, 55, 50, 44, 49, 54, 55, 44, 44, 48, 42, 52, 52, 13, 10, 36, 71, 76, 71, 83, 86, 44, 50, 44, 49, 44, 48, 53, 44, 55, 48, 44, 44, 44, 51, 54, 44, 56, 54, 44, 55, 57, 44, 48, 49, 57, 44, 51, 53, 44, 56, 55, 44, 50, 53, 44, 51, 49, 55, 44, 44, 56, 53, 44, 52, 50, 44, 49, 50, 50, 44, 50, 56, 44, 48, 42, 52, 69, 13, 10, 36, 71, 76, 71, 83, 86, 44, 50, 44, 50, 44, 48, 53, 44, 55, 49, 44, 55, 50, 44, 49, 55, 53, 44, 44, 48, 42, 52, 67, 13, 10, 36, 71, 78, 82, 77, 67, 44, 49, 54, 50, 57, 53, 53, 46, 48, 48, 48, 44, 65, 44, 52, 54, 53, 54, 46, 56, 57, 48, 55, 51, 44, 78, 44, 48, 48, 55, 50, 53, 46, 57, 56, 48, 54, 54, 44, 69, 44, 51, 46, 53, 51, 44, 49, 50, 54, 46, 56, 55, 44, 49, 53, 48, 53, 50, 51, 44, 44, 44, 65, 44, 86, 42, 48, 67, 13, 10, 36, 71, 78, 86, 84, 71, 44, 49, 50, 54, 46, 56, 55, 44, 84, 44, 44, 77, 44, 51, 46, 53, 51, 44, 78, 44, 54, 46, 53, 51, 44, 75, 44, 65, 42, 50, 67, 13, 10, 36, 71, 78, 90, 68, 65, 44, 49, 54, 50, 57, 53, 53, 46, 48, 48, 48, 44, 49, 53, 44, 48, 53, 44, 50, 48, 50, 51, 44, 48, 48, 44, 48, 48, 42, 52, 54, 13, 10, 36, 71, 80, 84, 88, 84, 44, 48, 49, 44, 48, 49, 44, 48, 49, 44, 65, 78, 84, 69, 78, 78, 65, 32, 79, 75, 42, 51, 53, 13, 10]
result = ascii_converter(numbers)
print("NMEA Message:")
print(result)
print(" ")
print("----------------------------------------")
print(" ")
print("Parsed NMEA message:")
print(" ")


def parse_nmea(nmea_string):
    nmea_messages = nmea_string.split('$')
    parsed_messages = []
    for message in nmea_messages:
        if message:
            message_parts = message.split(',')
            message_type = message_parts[0]
            if message_type == 'GNGGA':
                parsed_message = parse_gngga(message_parts)
            elif message_type == 'GNGLL':
                parsed_message = parse_gngll(message_parts)
            elif message_type == 'GNGSA':
                parsed_message = parse_gngsa(message_parts)
            elif message_type == 'GPGSV':
                parsed_message = parse_gpgsv(message_parts)
            else:
                parsed_message = {'Nachrichtentyp': message_type}
            parsed_messages.append(parsed_message)
    return parsed_messages


def parse_gngga(message_parts):
    time = message_parts[1][:2] + ':' + message_parts[1][2:4] + ':' + message_parts[1][4:]
    lat_degrees = int(float(message_parts[2]) // 100)
    lat_minutes = float(message_parts[2]) % 100
    lat_direction = message_parts[3]
    latitude = f"{lat_degrees}°{lat_minutes:.5f}'{lat_direction}"
    lon_degrees = int(float(message_parts[4]) // 100)
    lon_minutes = float(message_parts[4]) % 100
    lon_direction = message_parts[5]
    longitude = f"{lon_degrees}°{lon_minutes:.5f}'{lon_direction}"
    gps_quality_map = {'0': 'Ungültige Daten', '1': 'Gültige GPS-Daten', '2': 'Gültige DGPS-Daten', '6': 'Schätzung'}
    gps_quality = gps_quality_map.get(message_parts[6], 'Unbekannt')
    num_satellites = int(message_parts[7])
    altitude = float(message_parts[9])
    geoid_height = float(message_parts[11])

    parsed_message = {
        'Nachrichtentyp': 'GNGGA',
        'Zeit': time,
        'Breitengrad': latitude,
        'Längengrad': longitude,
        'GPS-Qualität': gps_quality,
        'Anzahl der verwendeten Satelliten': num_satellites,
        'Höhe über dem Meeresspiegel': altitude,
        'Geoid-Höhe': geoid_height,
    }

    return parsed_message


def parse_gpgsv(message_parts):
    total_messages = int(message_parts[1])
    current_message = int(message_parts[2])
    num_satellites = int(message_parts[3])
    satellite_info = []
    num_satellite_info = (len(message_parts) - 4) // 4
    for i in range(num_satellite_info):
        prn = message_parts[4 + i * 4]
        elevation = message_parts[5 + i * 4]
        azimuth = message_parts[6 + i * 4]
        snr = message_parts[7 + i * 4] + ' dB' if message_parts[7 + i * 4] else ''
        satellite_info.append({
            'PRN': prn,
            'Elevationswinkel': elevation,
            'Azimut': azimuth,
            'Signalstärke': snr
        })
    parsed_message = {
        'Nachrichtentyp': 'GPGSV',
        'Gesamtzahl der GSV-Nachrichten': total_messages,
        'Nummer der aktuellen GSV-Nachricht': current_message,
        'Anzahl der Satelliten in dieser GSV-Nachricht': num_satellites,
        'Satelliteninformationen': satellite_info,
    }

    return parsed_message


def parse_gngll(message_parts):
    lat_degrees = int(float(message_parts[1]) // 100)
    lat_minutes = float(message_parts[1]) % 100
    lat_direction = message_parts[2]
    latitude = f"{lat_degrees}°{lat_minutes:.5f}'{lat_direction}"
    lon_degrees = int(float(message_parts[3]) // 100)
    lon_minutes = float(message_parts[3]) % 100
    lon_direction = message_parts[4]
    longitude = f"{lon_degrees}°{lon_minutes:.5f}'{lon_direction}"
    time = message_parts[5][:2] + ':' + message_parts[5][2:4] + ':' + message_parts[5][4:]
    status_map = {'A': 'Gültige Daten', 'V': 'Ungültige Daten'}
    status = status_map.get(message_parts[6], 'Unbekannt')
    position_mode_map = {'A': 'Automatisch ermittelt', 'M': 'Manuell eingegeben'}
    position_mode = position_mode_map.get(message_parts[7], 'Unbekannt')

    parsed_message = {
        'Nachrichtentyp': 'GNGLL',
        'Breitengrad': latitude,
        'Längengrad': longitude,
        'Zeit': time,
        'Status': status,
        'Positionsfeld': position_mode
    }

    return parsed_message


def parse_gngsa(message_parts):
    fix_type_map = {'A': 'Automatic 2D/3D', 'M': 'Manual 2D/3D'}
    fix_type = fix_type_map.get(message_parts[1], '')
    operation_mode_map = {'1': 'Fix not available', '2': '2D', '3': '3D'}
    operation_mode = operation_mode_map.get(message_parts[2], '')
    satellite_prns = message_parts[3:15]
    pdop = message_parts[15]
    hdop = message_parts[16]
    vdop = message_parts[17]

    parsed_message = {
        'Message type': 'GNGSA',
        'Fix type': fix_type,
        'Operation mode': operation_mode,
        'PRN numbers of satellites used': satellite_prns,
        'PDOP': pdop,
        'HDOP': hdop,
        'VDOP': vdop,
    }

    return parsed_message



parsed_data = parse_nmea(result)
for d in parsed_data:
    if d:
        if len(d)>1:
            for field, value in d.items():
                print(f"{field}: {value}")
            print("----------------------------------------------------")

