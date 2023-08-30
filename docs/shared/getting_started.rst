###############
Getting started
###############

This chapter offers an overview of the openMINDS metadata framework from a practical perspective. 
Please note that this overview will by no means cover the complete power of openMINDS.
However, we hope we can provide you with a good starting point to use openMINDS for your data.


******
Basics
******

openMINDS provides specifications of schemas that build interlinked metadata models which are specifically tailored for data representations in graph databases. A graph database consists of nodes (or instances) and edges (links), where the nodes represent concepts and the edges represent relationships between these concepts \(`Wood 2009 <https://doi.org/10.1007/978-0-387-39940-9_183>`_\).
The schemas of the openMINDS metadata models provide constraints for the properties and relations of these concepts.

There are various file formats for defining the linked instances of a graph database. openMINDS currently assumes that instances are stored as `JSON-LD <https://json-ld.org/>`_ files. Consequently, the metadata instances of the openMINDS libraries for serviceable, well-defined terms and constructs are also encoded as JSON-LDs.

.. toctree::
   getting_started/matlab
   getting_started/python
