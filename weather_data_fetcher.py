"""
Weather Data Fetcher Module

This module provides functionality to fetch weather data for different cities.
It currently uses mock data but can be extended to use real API services.
"""

from typing import Dict, Optional


class WeatherDataFetcher:
    """A class to handle weather data retrieval operations."""

    def __init__(self):
        """Initialize the WeatherDataFetcher with mock weather data."""
        self.weather_data: Dict[str, Dict[str, any]] = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_weather_data(self, city: str) -> Dict[str, any]:
        """
        Fetch weather data for a given city.

        Args:
            city (str): The name of the city to fetch weather data for.

        Returns:
            Dict[str, any]: A dictionary containing weather data for the city.
                          Returns an empty dict if the city is not found.
        """
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})
