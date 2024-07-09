# Oriole - Sub-graph Partitioning Algorithm 
<!-- # Standard Readme -->

<!--[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
-->

## Table of Contents

- [Overview](#overview)
- [Install](#install)
- [Usage](#usage)
	- [Small Graph Benchmarks](#small)
    - [Regular Electronic Circuit Benchmarks](#regular)
    - [Big circuit Benchmarks](#big)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
    - [Contributors](#contributors)
- [License](#license)

## Overview
Synthetic consortia represent an emerging research area in synthetic biology, promising to solve various industrial challenges through the metabolic diversity, division of labor, and spatial organization inherent in microbial consortia. As synthetic biology advances into multi-cellular systems, new design strategies are essential for engineering distributed functions across networks of cells. However, existing strategies either lack scalability or require extensive reformulation, limiting their usage to various applications. In this work, we propose an application-agnostic approach to partitioning networks of interacting biological components using graph-based algorithms. We developed a three-stage algorithm, named Oriole, that verifies and optimizes the subgroup distribution of all entities within a network, considering constraints, objectives, and other biological considerations essential for engineering these systems. We validated our algorithm on three types of networks, including 30 small-graph benchmarks, 537 regular electronic circuit designs, and 43 large circuit benchmarks. One large circuit benchmark was recently implemented in the wet lab. Compared with the published sub-graph partitioning solution, the results generated by our new algorithm reduced design time from days to hours and decreased the total number of cells required for the multi-cellular system by 3\%. This case study demonstrates that our algorithm provides a more efficient approach to designing multi-cellular systems.

## Install

Download the repository from GitHub, create a venv environment, and install the necessary packages. Here we use python3.8 as the python interpreter.

```sh
$ git clone https://github.com/CIDARLAB/Oriole.git
$ cd algorithm
$ python3 -m venv venv/
$ venv/bin/pip3 install -r requirements.txt
```

After you install all the packages, you are able to run the algorithm.

## Usage


### Verification for Small Graph Benchmarks
You can run the first stage of our algorithm to verify the small graph benchmarks with the following command. 
Don't forget to comment the command "Merge()" in Merging.py and command "EdgeColoring()" in EdgeColoring.py.
```sh
$ venv/bin/python3 verification.py
```

If you want to generate random benchmarks by your self, you can use this command to generate random designs:
```sh
$ venv/bin/python3 RandomCaseGenerator.py
```

If it is the first time to test the random benchmarks, this command can automatically generate random Constraints by calling [ConstraintMaker.py](ConstraintMaker.py) and save it for the next time:
```sh
$ venv/bin/python3 TestAlgorithm.py
```

All Experiment objectives for Random Constraints are set to ['F1', 'F2']. User can edit it in [TestAlgorithm.py](TestAlgorithm.py).

### Literature Benchmarks
You can run this algorithm to test the given literature review benchmarks with this command:
```sh
$ venv/bin/python3 lrbtest.py
```

You can also create your own biochip design by editing [LRB_new.py](Literature_Review_Benchmarks_Generator/LRB_new.py).
And Create Constraint and Experiment objectives in [Constraint_UR_lrb_new.csv](TestCaseFiles/lrb/URC/Constraint_UR_lrb_new.csv).

## Maintainers

[@zyrrron](https://github.com/zyrrron).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/zyrrron/VeSpA-Algorithm/issues/new) or submit PRs.

### Contributors

This project exists thanks to all the people who contribute. 

## License

Parameters for verification, merging, EdgeColoring:
-settings
../settings.txt
-samples
test0