##############
FileRepository
##############

:Semantic name: core:FileRepository

:Display as: Core:file repository


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `hostedBy <hostedBy_heading_>`_, `name <name_heading_>`_
:Optional: `contentTypePattern <contentTypePattern_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `storageSize <storageSize_heading_>`_, `structurePattern <structurePattern_heading_>`_, `type <type_heading_>`_

------------

.. _IRI_heading:

***
IRI
***

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _contentTypePattern_heading:

******************
contentTypePattern
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentTypePattern
   :value type: | linked object array \(1-N\) of type
                | core:ContentTypePattern \[TYPE_ERROR\]
   :instructions: Add all content type patterns that identify matching content types for files within this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | core:ContentType \[TYPE_ERROR\]
   :instructions: If the files and file bundles within this repository are organised and formatted according to a formal data structure, add the content type of this formal data structure. Leave blank if no formal data structure has been applied.

`BACK TO TOP <FileRepository_>`_

------------

.. _hash_heading:

****
hash
****

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | core:Hash \[TYPE_ERROR\]
   :instructions: Add the hash that was generated for this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _hostedBy_heading:

********
hostedBy
********

Reference to an organization that provides facilities and services for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hostedBy
   :value type: | linked object of type
                | core:Organization \[TYPE_ERROR\]
   :instructions: Add the host organization of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _storageSize_heading:

***********
storageSize
***********

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\]
   :instructions: Enter the storage size of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _structurePattern_heading:

****************
structurePattern
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/structurePattern
   :value type: | linked object of type
                | core:FileRepositoryStructure \[TYPE_ERROR\]
   :instructions: Add the file repository structure that identifies the file path patterns used in this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | controlledTerms:FileRepositoryType \[TYPE_ERROR\]
   :instructions: Add the type of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

