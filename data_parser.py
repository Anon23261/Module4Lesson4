"""
Data Parser Module

This module handles the parsing and formatting of weather data into human-readable format.
"""

from typing import Dict, Union


class DataParser:
    """A class to parse and format weather data."""

    @staticmethod
    def parse_weather_data(data: Dict[str, Union[str, int]]) -> str:
        """
        Parse weather data into a human-readable format.

        Args:
            data (Dict[str, Union[str, int]]): Dictionary containing weather data with keys:
                - city (str): Name of the city
                - temperature (int): Temperature in Fahrenheit
                - condition (str): Weather condition description
                - humidity (int): Humidity percentage

        Returns:
            str: Formatted weather information string
        """
        if not data:
            return "Weather data not available"
            
        city = data.get("city", "Unknown")
        temperature = data.get("temperature", "N/A")
        condition = data.get("condition", "Unknown")
        humidity = data.get("humidity", "N/A")
        
        return f"Weather in {city}: {temperature}°F, {condition}, Humidity: {humidity}%"
