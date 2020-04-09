D2 Map Investigation
====================

## Exits in Act 1

Once you know the first three exits (*Rogue Encampment to Blood Moor, Blood Moor to Cold Plains, and Cold Plains to Stony Field*) the following overworld exits (*Dark Wood to Black Marsh, Black Marsh to Tamoe Highland, Outer Cloister to Barracks*) are fairly determined. **NOTE**: `TR` = Top Right, `BR` = Bottom Right, `BL` = Bottom Left, `TL` = Top Left

| RE->BM | BM->CP | CP->SF | DW->BM   | BM->TH | OC->B          |
| ------ | ------ | ------ | -------- | ------ | -------------- |
| **TR** | **TR** | **TL** | TR       | TL     | TL             |
| **TR** | **TL** | **TL** | TL       | TL     | TL             |
| **TR** | **TL** | **BL** | TL       | TL     | TR             |
| **BR** | **TR** | **BR** | TR       | BR     | TR             |
| **BR** | **TR** | **TL** | TR       | TL     | TL             |
| **BR** | **BL** | **BL** | BL       | TL     | TR             |
| **BR** | **BL** | **BR** | TR       | BR     | TR             |
| **BR** | **BL** | **TL** | BL       | TL     | TL             |
| **BL** | **BL** | **BL** | BL       | TL     | TR             |
| **BL** | **BL** | **BR** | TR       | BR     | TR             |
| **BL** | **BL** | **TL** | BL       | TL     | TL             |
| **BL** | **TL** | **TL** | TL       | TL     | TL             |
| **BL** | **TL** | **BL** | TL       | TL     | TR             |
| **TL** | **TL** | **TL** | TL       | TL     | TL             |
| **TL** | **TL** | **BL** | TL       | TL     | TR             |
| **TL** | **BL** | **BL** | BL       | TL     | TR             |
| **TL** | **BL** | **BR** | TR       | BR     | TR             |
| **TL** | **TR** | **BR** | TR       | BR     | TR             |
| **TL** | **TR** | **TL** | TR       | TL     | TL             |
| **BR** | **BR** | **BR** | BR       | BR     | TR \| TL       |
| **BR** | **BR** | **BL** | TR \| BL | TL     | TR             |
| **TR** | **TL** | **TR** | TL       | TR     | TR \| BR \| TL |
| **TR** | **TR** | **TR** | TR       | TR     | TR \| BR \| TL |
| **BR** | **BR** | **TR** | BR       | TR     | TR \| BR \| TL |
| **BR** | **TR** | **TR** | TR       | TR     | TR \| BR \| TL |
| **BL** | **TL** | **TR** | TL       | TR     | TR \| BR \| TL |
| **TL** | **TL** | **TR** | TL       | TR     | TR \| BR \| TL |
| **TL** | **TR** | **TR** | TR       | TR     | TR \| BR \| TL |

## Arcane Probabilty & Seed Parity

It appears some combinations of Act 1 maps may produce better Summoner direction odds if you know the seed's parity (Which can be determined by the Forgotten Tower position - courtesy of **evo_Demon**).

For instance, when Blood Moor to Cold Plains exits Top Right and Cold Plains to Stony Field exists Bottom Right (part of the Indrek seed):

**Even Seed** (Tower Top Right):

| Summoner Direction | Occurrences | %   |
| ------------------ | ----------- | --- |
| TR                 | 322         | 29% |
| BR                 | 269         | 24% |
| BL                 | 223         | 20% |
| TL                 | 275         | 25% |

**Odd Seed** (Tower Top Left):

| Summoner Direction | Occurrences | %   |
| ------------------ | ----------- | --- |
| TR                 | 274         | 20% |
| BR                 | 363         | 25% |
| BL                 | 434         | 30% |
| TL                 | 319         | 23% |

*Dataset of 17,386 seeds. Analysis over a larger dataset needed*

## Acknowledgements

Data produced with [d2-map-investigation](https://github.com/squeek502/d2-map-investigation/)
