#########
LocalFile
#########

:Semantic name: computation:LocalFile

:Display as: Computation:local file


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `path <path_heading_>`_
:Optional: `contentDescription <contentDescription_heading_>`_, `copyOf <copyOf_heading_>`_, `dataType <dataType_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `specialUsageRole <specialUsageRole_heading_>`_, `storageSize <storageSize_heading_>`_

------------

.. _contentDescription_heading:

******************
contentDescription
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentDescription
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter a short content description for this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

.. _copyOf_heading:

******
copyOf
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/copyOf
   :value type: | linked object of type
                | core:File \[TYPE_ERROR\]
   :instructions: Add the file of which this is a copy.

`BACK TO TOP <LocalFile_>`_

------------

.. _dataType_heading:

********
dataType
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataType
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:DataType \[TYPE_ERROR\]
   :instructions: Add all data types that are specifically represented in this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Add the content type of this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Add the hash that was generated for this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Enter the name of this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

.. _path_heading:

****
path
****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/path
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the file system path (absolute path or relative to the working directory) to this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

.. _specialUsageRole_heading:

****************
specialUsageRole
****************

Particular function of something when it is used.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specialUsageRole
   :value type: | linked object of type
                | controlledTerms:FileUsageRole \[TYPE_ERROR\]
   :instructions: Add the special usage role of this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Enter the storage size of this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

