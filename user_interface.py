"""
User Interface Module

This module handles the user interaction and display of weather information.
"""

from typing import Optional
from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser


class UserInterface:
    """A class to handle user interaction and weather information display."""

    def __init__(self, weather_data_fetcher: WeatherDataFetcher, data_parser: DataParser):
        """
        Initialize UserInterface with required components.

        Args:
            weather_data_fetcher (WeatherDataFetcher): Instance of WeatherDataFetcher
            data_parser (DataParser): Instance of DataParser
        """
        self.weather_data_fetcher = weather_data_fetcher
        self.data_parser = data_parser

    def get_detailed_forecast(self, city: str) -> str:
        """
        Get detailed weather forecast for a city.

        Args:
            city (str): Name of the city to get forecast for

        Returns:
            str: Detailed weather forecast
        """
        data = self.weather_data_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def display_weather(self, city: str) -> Optional[str]:
        """
        Display basic weather information for a city.

        Args:
            city (str): Name of the city to display weather for

        Returns:
            Optional[str]: Weather information if available, None otherwise
        """
        data = self.weather_data_fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        return self.data_parser.parse_weather_data(data)
