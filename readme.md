# My Namaz Alert

My Namaz Alert is a custom component for Home Assistant that provides namaz (Islamic prayer) timing alerts based on the location coordinates obtained from an external API.

## Installation

Copy the `my_namaz_alert` directory to the `custom_components` directory in your Home Assistant configuration.

## Configuration

Add the following to your Home Assistant configuration:

```yaml
my_namaz_alert:
  interval: 60
```

- `interval` (optional): The interval in minutes between checks for namaz timing alerts. Default is 60 minutes.

## Usage

Once the component is installed and configured, it will automatically create persistent notifications for each namaz (Islamic prayer) timing for the day. The notifications will appear in the Home Assistant frontend.

## Dependencies

This component requires the following dependencies:

- `requests` library

Make sure to install the required dependencies by adding them to your Home Assistant environment or virtual environment.

## Support and Issues

For support or to report any issues, please open an issue on the [GitHub repository](https://github.com/danyalahmed/my-namaz-alert).

## Credits

This custom component is developed by [danyalahmed](https://github.com/danyalahmed).

## License

MIT License
