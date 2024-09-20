from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Represents the input model for wine data.

    Attributes:
        alcohol (float): The alcohol content of the wine.
        malic_acid (float): The malic acid content of the wine.
        ash (float): The ash content of the wine.
        alcalinity_of_ash (float): The alcalinity of ash in the wine.
        magnesium (float): The magnesium content of the wine.
        total_phenols (float): The total phenols content of the wine.
        flavanoids (float): The flavanoids content of the wine.
        nonflavanoid_phenols (float): The nonflavanoid phenols content of the wine.
        proanthocyanins (float): The proanthocyanins content of the wine.
        color_intensity (float): The color intensity of the wine.
        hue (float): The hue of the wine.
        od280_od315_of_diluted_wines (float): The OD280/OD315 of diluted wines.
        proline (float): The proline content of the wine.
    """

    alcohol: float = Field(default=13.199999809265137)
    malic_acid: float = Field(default=1.7799999713897705)
    ash: float = Field(default=2.140000104904175)
    alcalinity_of_ash: float = Field(default=11.199999809265137)
    magnesium: float = Field(default=100.0)
    total_phenols: float = Field(default=2.6500000953674316)
    flavanoids: float = Field(default=2.759999990463257)
    nonflavanoid_phenols: float = Field(default=0.25999999046325684)
    proanthocyanins: float = Field(default=1.2799999713897705)
    color_intensity: float = Field(default=4.380000114440918)
    hue: float = Field(default=1.0499999523162842)
    od280_od315_of_diluted_wines: float = Field(default=3.4000000953674316)
    proline: float = Field(default=1050.0)


class OutputModel(BaseModel):
    """
    Represents the output model for the wine prediction.

    Attributes:
        prediction (int): The predicted value for the wine.
    """
    prediction: int = Field(default=0)
