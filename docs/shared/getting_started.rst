###############
Getting started
###############

This chapter offers an overview of the openMINDS metadata models from a practical perspective. 
Please note that this overview will by no means cover all annotation options the openMINDS metadata models offer.
However, we hope we can provide you with a good starting point to create an openMINDS metadata collection for your data.


******
Basics
******

openMINDS provides specifications of schemas that build interlinked metadata models which are tailored for data representations in graph databases.
Each openMINDS schema within in a metadata model constraints for the properties and edges (links) of a node (metadata instance) within a graph databases.

Currently, openMINDS assumes that the metadata instances within a graph database are encoded as `JSON-LD <https://json-ld.org/>`_ \(JavaScript Object Notation for Linked Data\), a recommended format for linked data by the World Wide Web Consortium (W3C). The metadata instances of the openMINDS libraries for serviceable, well-defined terms and constructs are also encoded in JSON-LD.


.. toctree::
   getting_started/matlab
   getting_started/python
