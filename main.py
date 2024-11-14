"""
Main Module

This is the entry point of the Weather Data Application.
It handles the main program loop and user input processing.
"""

from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser
from user_interface import UserInterface


def main() -> None:
    """
    Main function to run the Weather Data Application.
    Handles user input and displays weather information.
    """
    weather_data_fetcher = WeatherDataFetcher()
    data_parser = DataParser()
    user_interface = UserInterface(weather_data_fetcher, data_parser)
    
    print("Welcome to the Weather Data Application!")
    print("Available cities: New York, London, Tokyo")
    
    while True:
        city = input("\nEnter the city to get the weather forecast or 'exit' to quit: ").strip()
        if city.lower() == 'exit':
            print("Thank you for using the Weather Data Application!")
            break
            
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower().strip()
        
        if detailed == 'yes':
            forecast = user_interface.get_detailed_forecast(city)
        else:
            forecast = user_interface.display_weather(city)
            
        print("\nForecast Results:")
        print("-" * 40)
        print(forecast)
        print("-" * 40)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please try again.")
