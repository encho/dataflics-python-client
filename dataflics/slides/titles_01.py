from dataclasses import dataclass, asdict
from typing import Literal, Dict, Any

# Nested types that match the TypeScript schema for stillProps, animationProps, and dataflicsProps

@dataclass
class StillProps:
    fontSize: Literal["S", "M", "L", "XL", "XXL"]
    title: str

@dataclass
class AnimationProps:
    # Represents a strict empty object.
    pass

@dataclass
class DataflicsProps:
    durationInFrames: int

# These types remain unchanged.
@dataclass
class ColorPalettes:
    main: str

@dataclass
class Typographies:
    main: str

@dataclass
class Screens:
    main: str

class DataflicsTitles01:
    slideKey: Literal["dataflics/titles/01"] = "dataflics/titles/01"
    
    def __init__(
        self,
        id: str,
        fontSize: Literal["S", "M", "L", "XL", "XXL"],
        title: str,
        durationInFrames: int,
        colorPalettes: ColorPalettes,
        typographies: Typographies,
        screens: Screens,
    ) -> None:
        self.id = id
        # Build the nested objects from flattened parameters.
        self.stillProps = StillProps(fontSize=fontSize, title=title)
        self.animationProps = AnimationProps()  # always an empty object
        self.dataflicsProps = DataflicsProps(durationInFrames=durationInFrames)
        self.colorPalettes = colorPalettes
        self.typographies = typographies
        self.screens = screens

    def unflatten_props(self) -> Dict[str, Any]:
        """
        Merges stillProps, animationProps, and dataflicsProps into a single 'props' dictionary.
        """
        # Convert each nested object to a dict and merge them
        props: Dict[str, Any] = {
            **asdict(self.stillProps),
            **asdict(self.animationProps),  # will be empty
            **asdict(self.dataflicsProps)
        }
        # Build the final payload, keeping colorPalettes, typographies, and screens as-is.
        return {
            "id": self.id,
            "slideKey": self.slideKey,
            "props": props,
            "colorPalettes": asdict(self.colorPalettes),
            "typographies": asdict(self.typographies),
            "screens": asdict(self.screens),
        }

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the object using the original nested structure.
        """
        return {
            "id": self.id,
            "slideKey": self.slideKey,
            "stillProps": asdict(self.stillProps),
            "animationProps": asdict(self.animationProps),
            "dataflicsProps": asdict(self.dataflicsProps),
            "colorPalettes": asdict(self.colorPalettes),
            "typographies": asdict(self.typographies),
            "screens": asdict(self.screens),
        }


# if __name__ == "__main__":
#     # Create the supporting objects for the unchanged fields
#     color_palettes = ColorPalettes(main="palette123")
#     typographies = Typographies(main="typography123")
#     screens = Screens(main="screen123")
    
#     # Instantiate DataflicsTitles01 with flattened properties
#     slide = DataflicsTitles01(
#         id="slide_001",
#         fontSize="M",
#         title="Welcome to Dataflics!",
#         durationInFrames=120,
#         colorPalettes=color_palettes,
#         typographies=typographies,
#         screens=screens,
#     )
    
#     # Convert the slide instance to the API-ready payload with flattened 'props'
#     api_payload = slide.unflatten_props()
#     print("API Payload:")
#     print(api_payload)
    
#     # Optionally, convert to the original nested structure
#     nested_payload = slide.to_dict()
#     print("\nNested Payload:")
#     print(nested_payload)