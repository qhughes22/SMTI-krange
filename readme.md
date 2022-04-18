# Super Stable Matching and K-Range
Tools I created as part of my senior honors project on super-stable matching and k-range preferences. Implementations of algorithms related to super-stable matchings can be found here, along with scripts to generate preferences restricted in either a tiered model or a k-range model.

The full codebase for my project can be found at https://github.com/qhughes22/super-stable-matching-thesis. This repo contains the code that may be useful to anyone trying to study the stable matching problem.

## Setup

Clone the repo, and run `pip install -r requirements.txt` to install necessary packages.

## Usage

SuperStableMatchingInstance is the class which stores an instance of SMTI and has methods implemented to find the woman/man-optimal super-stable matchings, check for weak stability, strong stability, and super-stability, and find the super-stable rotation poset and all super-stable matchings for the instance.

Instances are created using pairs of sets of preferences, where each element in the set is a list of lists denoting a single agent's preferences. generate_prefs_with_indifference.py includes functions to generate preferences in that format, either under the k-range model or with a tiered model. There is also a function to randomly insert indifference into lists.

The exact processes used are outlined in my thesis paper, found here (insert link).

## Files
1. SuperStableMatchingInstance.py: This class includes stable matching algorithms. It includes functions to find the super-stable matching poset for any SMTI instance and to find all super-stable matchings.
2. test.py: This file includes tests for the functions in SuperStableMatchingInstance.py.
3. util.py: This file includes helper functions used in SuperStableMatchingInstance.py
4. GraphVisualization.py: This file includes the Digraph class, a wrapper class around NetworkX's DiGraph. Mostly used for easier visualization of digraphs for debugging SuperStableMatchingInstance.py.
5. generate_prefs_with_indifference.py: This file provides functions for generating random k-range preferences through a method of iterative adjacent swaps. It also provides functions for generating tiered preferences and adding indifference to existing lists.
