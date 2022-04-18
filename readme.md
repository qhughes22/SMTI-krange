# Super Stable Matching and K-Range
Codebase for my senior honors project on super-stable matching and k-range preferences.

This is the code I used for the honors project I submitted to Amherst College on 4/18/22.

If you want to use these functions to run stable matching algorithms, I suggest you look to this repo instead. It contains the scripts that might be useful without files specific to my project.

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
