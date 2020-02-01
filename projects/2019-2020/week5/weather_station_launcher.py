import argparse
import weather_station

parser = argparse.ArgumentParser(description="Short sample app")
parser.add_argument('--dry_run', action="store_true", default=False)
parser.add_argument('--display', action="store_true", default=False)


args = parser.parse_args()

if args.dry_run:
    weather_station.run(dry_run=True)
else:
    if args.dispay:
        weather_station.run(dry_run=False, display=True)
    else:
        weather_station.run(dry_run=False)
