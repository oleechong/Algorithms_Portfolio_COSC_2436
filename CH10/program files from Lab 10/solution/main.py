class Box:
    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


def pack_truck(boxes, truck_volume):
    # Sorts the list of boxes in descending order based on their volume
    boxes_sorted = sorted(boxes, key=lambda x: x.volume(), reverse=True)

    packed_boxes = []  # List to store boxes that will be packed into the truck
    used_volume = 0  # Keep track of the volume used so far

    # Iterate through sorted boxes and pack them if they fit
    for box in boxes_sorted:
        if used_volume + box.volume() <= truck_volume:
            packed_boxes.append(box)
            used_volume += box.volume()

    return packed_boxes


if __name__ == "__main__":
    # Truck dimensions input with added instructions
    truck_length = float(input("Enter the truck's length (in units): "))
    truck_width = float(input("Enter the truck's width (in units): "))
    truck_height = float(input("Enter the truck's height (in units): "))
    truck_volume = truck_length * truck_width * truck_height

    boxes = []  # List to store box objects

    while True:
        box_label = input("Enter box label (or type 'done' to finish): ")
        if box_label.lower() == 'done':
            break

        box_length = float(input(f"Enter length for box '{box_label}' (in units): "))
        box_width = float(input(f"Enter width for box '{box_label}' (in units): "))
        box_height = float(input(f"Enter height for box '{box_label}' (in units): "))
        new_box = Box(box_label, box_length, box_width, box_height)
        boxes.append(new_box)

    # Packing and results display section with added UI elements
    packed_boxes = pack_truck(boxes, truck_volume)
    print(f"Total boxes packed: {len(packed_boxes)}")
    for box in packed_boxes:
        print(f"Box '{box.label}': Volume {box.volume()} cubic units")

    total_volume_used = sum(box.volume() for box in packed_boxes)
    print(f"Total volume used: {total_volume_used} cubic units")
    print(f"Remaining volume: {truck_volume - total_volume_used} cubic units")
