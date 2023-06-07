# nanjing-lulc-modified-sankey

[![DOI](https://zenodo.org/badge/DOI/10.3390/rs13040580.svg)](https://doi.org/10.3390/rs13040580)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4131521.svg)](https://doi.org/10.5281/zenodo.4131521)

The modified Sankey chart to visualize the landuse/landcover change flow in Nanjing.

## Steps to create a M-Sankey chart

1. prepare the nodes file

	- Each node for a sub-column,

	- Edit by hand,

	- Start from 0.

1. prepare the links file

	- Calculated on EarthEngine/transitionMatrixCalculating3_featColl,

1. concatenate the links and nodes

	- [concatenate-links-notes-to-sankey-json.py](/concatenate-links-notes-to-sankey-json.py)

1. plot modified Sankey chart on [Observable]

    - <https://observablehq.com/@longavailable/the-modified-sankey-diagram-for-lulc-changes>

## How to cite

If this tool is useful to your research, cite the published article as below:

>Liu, X.; Fu, D.; Zevenbergen, C.; Busker, T.; Yu, M. Assessing Sponge Cities Performance at City Scale Using Remotely Sensed LULC Changes: Case Study Nanjing. Remote Sens. 2021, 13, 580. https://doi.org/10.3390/rs13040580.

Easily, you can import it to 
<a href="https://www.mendeley.com/import/?url=https://www.mdpi.com/989436"><i class="fa fa-external-link"></i> Mendeley</a>.

## Related repositories

- [longavailable/json-data-preparation-for-modified-sankey](https://github.com/longavailable/json-data-preparation-for-modified-sankey)

<!--links-->
[Observable]: observablehq.com
