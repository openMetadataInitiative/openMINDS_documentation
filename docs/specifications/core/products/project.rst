#######
Project
#######

*****************************************
https://openminds.ebrains.eu/core/Project
*****************************************

Structured information on a research project.

------------

------------

**********
Properties
**********

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasResearchProducts <hasResearchProducts_heading_>`_, `shortName
   <shortName_heading_>`_
:Optional: `homepage <homepage_heading_>`_, `projectLeader <projectLeader_heading_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description of this project.

`BACK TO TOP <Project_>`_

------------

.. _fullName_heading:

fullName
--------

Whole, non-abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name (title) for this project.

`BACK TO TOP <Project_>`_

------------

.. _hasResearchProducts_heading:

hasResearchProducts
-------------------

Reference to subsidiary research products.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasResearchProducts
   :value type: | linked object array \(2-N\) of type
                | `Dataset <https://openminds.ebrains.eu/core/Dataset>`_, `DatasetVersion <https://openminds.ebrains.eu/core/DatasetVersion>`_, `MetaDataModel
                <https://openminds.ebrains.eu/core/MetaDataModel>`_, `MetaDataModelVersion <https://openminds.ebrains.eu/core/MetaDataModelVersion>`_, `Model
                <https://openminds.ebrains.eu/core/Model>`_, `ModelVersion <https://openminds.ebrains.eu/core/ModelVersion>`_, `Software
                <https://openminds.ebrains.eu/core/Software>`_or `SoftwareVersion <https://openminds.ebrains.eu/core/SoftwareVersion>`_
   :instructions: Add all research products or research product versions that are part of this project.

`BACK TO TOP <Project_>`_

------------

.. _homepage_heading:

homepage
--------

Main website of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this model version.

`BACK TO TOP <Project_>`_

------------

.. _projectLeader_heading:

projectLeader
-------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/projectLeader
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds.ebrains.eu/core/Organization>`_or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add one or several project leader (person or organization).

`BACK TO TOP <Project_>`_

------------

.. _shortName_heading:

shortName
---------

Shortened or fully abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (alias) for this project.

`BACK TO TOP <Project_>`_

------------

