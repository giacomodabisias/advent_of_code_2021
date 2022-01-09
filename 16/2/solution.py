import pprint
import math

INPUT_FILE = "input.txt"
base = 2
bin_2_hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def read_input() -> list[str]:
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse_literal_value(message: str) -> tuple[dict, int]:
    parsed_packet = {}
    keep_reading = True
    content = ""
    total_bits_read = 0
    while keep_reading:
        # 1 bit for reading continuation
        total_bits_read += 1
        keep_reading = int(message[:1], base)
        message = message[1:]
        # 4 bits for the literal value
        total_bits_read += 4
        content += message[:4]
        message = message[4:]
    parsed_packet["message"] = int(content, base)
    return parsed_packet, total_bits_read


def parse_operator_length(message: str) -> tuple[dict, int]:
    sub_package_length_header_length = 15
    parsed_packet = dict()
    parsed_packet["sub_packages"] = []
    sub_packets_length = int(message[:sub_package_length_header_length], base)
    parsed_packet["sub_packet_length"] = sub_packets_length
    sub_packets = message[sub_package_length_header_length:(sub_package_length_header_length + sub_packets_length)]
    total_parsed_length = 0
    while total_parsed_length != sub_packets_length:
        parsed_message, parsed_length = parse(sub_packets)
        sub_packets = sub_packets[parsed_length:]
        total_parsed_length += parsed_length
        parsed_packet["sub_packages"].append(parsed_message)
    return parsed_packet, sub_packets_length + sub_package_length_header_length


def parse_operator_multi(message: str) -> tuple[dict, int]:
    sub_package_length_header_length = 11
    parsed_packet = dict()
    parsed_packet["sub_packages"] = []
    number_of_sub_packets = int(message[:sub_package_length_header_length], base)
    parsed_packet["number_of_sub_packets"] = number_of_sub_packets
    content = message[sub_package_length_header_length:]
    total_parsed_length = 0
    for idx in range(0, number_of_sub_packets):
        parsed_message, parsed_length = parse(content)
        total_parsed_length += parsed_length
        parsed_packet["sub_packages"].append(parsed_message)
        content = content[parsed_length:]
    return parsed_packet, total_parsed_length + sub_package_length_header_length


def parse(packet: str) -> tuple[dict, int]:
    total_bits_read = 0
    parsed_packet = dict()
    version = int(packet[0:3], base)
    total_bits_read += 3
    parsed_packet["version"] = version
    type_id = int(packet[total_bits_read:6], base)
    total_bits_read += 3
    parsed_packet["type_id"] = type_id
    content = packet[total_bits_read:]

    # Parsing a literal value
    if type_id == 4:
        package_message, current_bits_read = parse_literal_value(content)
        parsed_packet.update(package_message)
    # Parsing Operator
    else:
        length_type_id = int(content[0], base)
        parsed_packet["length_type_id"] = length_type_id
        # Skip length id
        content = content[1:]
        total_bits_read += 1
        if length_type_id == 0:
            package_message, current_bits_read = parse_operator_length(content)
            parsed_packet.update(package_message)
        elif length_type_id == 1:
            package_message, current_bits_read = parse_operator_multi(content)
            parsed_packet.update(package_message)
        else:
            raise ValueError(f"Unhandled value: {length_type_id}")
    return parsed_packet, total_bits_read + current_bits_read


def compute_packet_value(packet: dict) -> int:
        if packet["type_id"] == 0:
            return sum([compute_packet_value(packet) for packet in packet["sub_packages"]])
        elif packet["type_id"] == 1:
            return math.prod([compute_packet_value(packet) for packet in packet["sub_packages"]])
        elif packet["type_id"] == 2:
            return min([compute_packet_value(packet) for packet in packet["sub_packages"]])
        elif packet["type_id"] == 3:
            return max([compute_packet_value(packet) for packet in packet["sub_packages"]])
        elif packet["type_id"] == 4:
            return packet["message"]
        elif packet["type_id"] == 5:
            return 1 if compute_packet_value(packet["sub_packages"][0]) > compute_packet_value(
                packet["sub_packages"][1]) else 0
        elif packet["type_id"] == 6:
            return 1 if compute_packet_value(packet["sub_packages"][0]) < compute_packet_value(
                packet["sub_packages"][1]) else 0
        elif packet["type_id"] == 7:
            return 1 if compute_packet_value(packet["sub_packages"][0]) == compute_packet_value(
                packet["sub_packages"][1]) else 0
        else:
            raise ValueError(f"Unrecognized packet type id {packet['type_id']}")


if __name__ == "__main__":
    packets = read_input()
    pp = pprint.PrettyPrinter(indent=4)
    parsed_packets = []
    packages_values = []
    for packet_to_parse in packets:
        print(f"Parsing {packet_to_parse}")
        bin_packet = "".join([bin_2_hex_map[value] for value in packet_to_parse])
        parsed_message, _ = parse(bin_packet)
        parsed_packets.append(parsed_message)
        package_value = compute_packet_value(parsed_message)
        packages_values.append(package_value)
        print(f"Package value: {package_value}")
        # pp.pprint(parsed_message)

    print(f"Total value: {sum(packages_values)}")


