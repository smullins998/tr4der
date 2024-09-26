import yfinance as yf
from pandas import DataFrame
import pandas as pd
from datetime import date
import openai
from typing import Dict, Any
import os
from tqdm import tqdm
from tr4der.utils.data_loader import DataLoader
from tr4der.strategies.simple_strategies import SimpleStrategies
from tr4der.strategies.technical_strategies import TechnicalAnalysisStrategies
from tr4der.strategies.machine_learning_strategies import MachineLearningStrategies


class Tr4der:

    def __str__(self) -> str:
        return "Object to load data from Yahoo Finance"

    def __init__(self, data_prompt: str):

        if not data_prompt:
            raise ValueError("Data prompt is required")

        # Load the data
        self._data_loader = DataLoader(data_prompt)
        self._data_loader.execute_code()

        # Allow flexibility to explore different strategies with different parameters.
        # Ultimately the user could pass in a strategy object and then we can call the execute method.
        self.SimpleStrategies = SimpleStrategies()
        self.TechnicalAnalysisStrategies = TechnicalAnalysisStrategies()
        self.MachineLearningStrategies = MachineLearningStrategies()

    @property
    def strategy_data(self) -> DataFrame:
        df = self._data_loader.strategy_data
        df = df[
            [ticker for ticker in df.columns if ticker != "Date" and "_" not in ticker]
        ]
        return df
