class Box:
    def __init__(self, label: str, length: float, width: float, height: float):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        """Calculate the volume of the box."""
        # Multiply length, width, and height of the box
        return self.length * self.width * self.height


def pack_truck(boxes: list, truck_volume: float, truck_length: float, truck_width: float, truck_height: float) -> list:
    """Pack the truck using a greedy strategy based on box volumes and physical dimensions."""
    # 1. Sort boxes in descending order of volume to prioritize larger items
    boxes.sort(key=lambda box: box.volume(), reverse=True)
    
    # 2. Initialize packed_boxes list and used_volume counter
    packed_boxes = []
    used_volume = 0
    
    # 3. Iterate through sorted boxes
    for box in boxes:
        # Check if the box fits the remaining volume AND its individual dimensions fit the truck
        fits_volume = (used_volume + box.volume()) <= truck_volume
        fits_dimensions = (box.length <= truck_length and 
                           box.width <= truck_width and 
                           box.height <= truck_height)
        
        if fits_volume and fits_dimensions:
            packed_boxes.append(box)
            used_volume += box.volume()
            
    # 4. Return the list of packed boxes
    return packed_boxes


if __name__ == "__main__":
    print("Welcome to the Truck Cargo Calculator")
    print("This program helps you calculate how to pack your cargo efficiently using a greedy algorithm.\n")

    # 1. Prompt user for truck dimensions
    t_length = float(input("Enter truck length: "))
    t_width = float(input("Enter truck width: "))
    t_height = float(input("Enter truck height: "))
    
    # 2. Calculate and display truck volume
    truck_volume = t_length * t_width * t_height
    print(f"Total Truck volume available: {truck_volume:.2f}\n")

    boxes = []  # List to store box objects

    # Input boxes loop
    while True:
        label = input("Enter box label (or 'done' to finish): ")
        if label.lower() == 'done':
            break
        
        try:
            length = float(input(f"Enter length for {label}: "))
            width = float(input(f"Enter width for {label}: "))
            height = float(input(f"Enter height for {label}: "))
            
            # Create Box object and add to the list
            new_box = Box(label, length, width, height)
            boxes.append(new_box)
        except ValueError:
            print("Invalid input. Please enter numerical values for dimensions.")

    # Pack the truck
    packed_boxes = pack_truck(boxes, truck_volume, t_length, t_width, t_height)
    
    # Display results
    print("\n" + "="*30)
    print("PACKING RESULTS")
    print("="*30)
    
    if not packed_boxes:
        print("No boxes could be packed into the truck.")
    else:
        total_packed_volume = 0
        for box in packed_boxes:
            vol = box.volume()
            total_packed_volume += vol
            print(f"- {box.label}: Volume {vol:.2f} (Dims: {box.length}x{box.width}x{box.height})")
        
        print(f"\nTotal volume used: {total_packed_volume:.2f} / {truck_volume:.2f}")
        print(f"Utilization: {(total_packed_volume / truck_volume) * 100:.2f}%")

    print("\nThank you for using the Truck Cargo Calculator.")