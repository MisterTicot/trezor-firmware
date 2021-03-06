# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEMMosaicLevy = Literal[1, 2]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEMMosaicLevy = None  # type: ignore


class NEMMosaicDefinition(p.MessageType):

    def __init__(
        self,
        name: str = None,
        ticker: str = None,
        namespace: str = None,
        mosaic: str = None,
        divisibility: int = None,
        levy: EnumTypeNEMMosaicLevy = None,
        fee: int = None,
        levy_address: str = None,
        levy_namespace: str = None,
        levy_mosaic: str = None,
        supply: int = None,
        mutable_supply: bool = None,
        transferable: bool = None,
        description: str = None,
        networks: List[int] = None,
    ) -> None:
        self.name = name
        self.ticker = ticker
        self.namespace = namespace
        self.mosaic = mosaic
        self.divisibility = divisibility
        self.levy = levy
        self.fee = fee
        self.levy_address = levy_address
        self.levy_namespace = levy_namespace
        self.levy_mosaic = levy_mosaic
        self.supply = supply
        self.mutable_supply = mutable_supply
        self.transferable = transferable
        self.description = description
        self.networks = networks if networks is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('name', p.UnicodeType, 0),
            2: ('ticker', p.UnicodeType, 0),
            3: ('namespace', p.UnicodeType, 0),
            4: ('mosaic', p.UnicodeType, 0),
            5: ('divisibility', p.UVarintType, 0),
            6: ('levy', p.EnumType("NEMMosaicLevy", (1, 2)), 0),
            7: ('fee', p.UVarintType, 0),
            8: ('levy_address', p.UnicodeType, 0),
            9: ('levy_namespace', p.UnicodeType, 0),
            10: ('levy_mosaic', p.UnicodeType, 0),
            11: ('supply', p.UVarintType, 0),
            12: ('mutable_supply', p.BoolType, 0),
            13: ('transferable', p.BoolType, 0),
            14: ('description', p.UnicodeType, 0),
            15: ('networks', p.UVarintType, p.FLAG_REPEATED),
        }
