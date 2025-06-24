def convert_seconds(total_seconds):
    """Converts total seconds into hours, minutes, and seconds."""
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return hours, minutes, seconds

def main():
    print("Time Converter: Seconds → Hours : Minutes : Seconds")
    total_seconds = int(input("Enter time in seconds: "))

    hours, minutes, seconds = convert_seconds(total_seconds)

    print(f"{total_seconds} seconds = {hours}h:{minutes}m:{seconds}s")

if __name__ == "__main__":
    main()
