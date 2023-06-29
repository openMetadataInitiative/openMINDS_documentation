#######
Project
#######

https://openminds.ebrains.eu/core/Project
-----------------------------------------

Structured information on a research project.

------------

------------

**********
Properties
**********

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasPart <hasPart_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `coordinator <coordinator_heading_>`_, `homepage <homepage_heading_>`_

------------

.. _coordinator_heading:

coordinator
-----------

Legal person who organizes the collaborative work of people or groups.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinator
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds.ebrains.eu/core/Consortium>`_, `Organization <https://openminds.ebrains.eu/core/Organization>`_or `Person
                <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add all parties that coordinate this project.

`BACK TO TOP <Project_>`_

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
   :instructions: Enter a descriptive full name (or title) for this project.

`BACK TO TOP <Project_>`_

------------

.. _hasPart_heading:

hasPart
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasPart
   :value type: | linked object array \(2-N\) of type
                | `ValidationTest <https://openminds.ebrains.eu/computation/ValidationTest>`_, `ValidationTestVersion
                <https://openminds.ebrains.eu/computation/ValidationTestVersion>`_, `WorkflowRecipe <https://openminds.ebrains.eu/computation/WorkflowRecipe>`_,
                `WorkflowRecipeVersion <https://openminds.ebrains.eu/computation/WorkflowRecipeVersion>`_, `Dataset
                <https://openminds.ebrains.eu/core/Dataset>`_, `DatasetVersion <https://openminds.ebrains.eu/core/DatasetVersion>`_, `MetaDataModel
                <https://openminds.ebrains.eu/core/MetaDataModel>`_, `MetaDataModelVersion <https://openminds.ebrains.eu/core/MetaDataModelVersion>`_, `Model
                <https://openminds.ebrains.eu/core/Model>`_, `ModelVersion <https://openminds.ebrains.eu/core/ModelVersion>`_, `Software
                <https://openminds.ebrains.eu/core/Software>`_, `SoftwareVersion <https://openminds.ebrains.eu/core/SoftwareVersion>`_, `WebService
                <https://openminds.ebrains.eu/core/WebService>`_, `WebServiceVersion <https://openminds.ebrains.eu/core/WebServiceVersion>`_, `LivePaper
                <https://openminds.ebrains.eu/publications/LivePaper>`_, `LivePaperVersion <https://openminds.ebrains.eu/publications/LivePaperVersion>`_,
                `BrainAtlas <https://openminds.ebrains.eu/sands/BrainAtlas>`_, `BrainAtlasVersion <https://openminds.ebrains.eu/sands/BrainAtlasVersion>`_,
                `CommonCoordinateSpace <https://openminds.ebrains.eu/sands/CommonCoordinateSpace>`_or `CommonCoordinateSpaceVersion
                <https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion>`_
   :instructions: Add all research product (versions) that are part of this project.

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
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this project.

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
   :instructions: Enter a short name (or alias) for this project that could be used as a shortened display title (e.g., for web services with too little space
      to display the full name).

`BACK TO TOP <Project_>`_

------------

