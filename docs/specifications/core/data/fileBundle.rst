##########
FileBundle
##########

https://openminds.ebrains.eu/core/FileBundle
--------------------------------------------

Structured information on a bundle of file instances.

------------

------------

**********
Properties
**********

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional: `format <format_heading_>`_, `groupedBy <groupedBy_heading_>`_, `hash <hash_heading_>`_, `patternOfFilenames <patternOfFilenames_heading_>`_,
   `storageSize <storageSize_heading_>`_

------------

.. _format_heading:

format
------

Method of digitally organizing and structuring data or information.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds.ebrains.eu/core/ContentType>`_
   :instructions: If file instances within this bundle are organized and formatted according to a formal data structure use the appropriate contentType. Leave
      blank otherwise.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupedBy_heading:

groupedBy
---------

Reference to the aspect used to group something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupedBy
   :value type: | linked object of type
                | `FileBundleGrouping <https://openminds.ebrains.eu/controlledTerms/FileBundleGrouping>`_
   :instructions: Add the concept which was used to group file instances into this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _hash_heading:

hash
----

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | `Hash <https://openminds.ebrains.eu/core/Hash>`_
   :instructions: Add the hash that was generated for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `FileBundle <https://openminds.ebrains.eu/core/FileBundle>`_ or `FileRepository <https://openminds.ebrains.eu/core/FileRepository>`_
   :instructions: Add the file bundle or file repository this file bundle is a part of.

`BACK TO TOP <FileBundle_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _patternOfFilenames_heading:

patternOfFilenames
------------------

Reliable sample / structure of characters valid for all names in a particular collection of files.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/patternOfFilenames
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a regular expression (syntax: ECMA 262) which is valid for all filenames of the file instances that should be grouped into this file
      bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _storageSize_heading:

storageSize
-----------

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds.ebrains.eu/core/QuantitativeValue>`_
   :instructions: Enter the storage size this file bundle allocates.

`BACK TO TOP <FileBundle_>`_

------------

