#######
Project
#######

:Semantic name: core:Project

:Display as: Core:project


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `fullName <fullName_heading_>`_, `hasPart <hasPart_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `coordinator <coordinator_heading_>`_, `homepage <homepage_heading_>`_

------------

.. _coordinator_heading:

***********
coordinator
***********

Legal person who organizes the collaborative work of people or groups.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinator
   :value type: | linked object array \(1-N\) of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all parties that coordinate this project.

`BACK TO TOP <Project_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of this project.

`BACK TO TOP <Project_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name (or title) for this project.

`BACK TO TOP <Project_>`_

------------

.. _hasPart_heading:

*******
hasPart
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasPart
   :value type: | linked object array \(2-N\) of type
                | computation:ValidationTest \[TYPE_ERROR\], computation:ValidationTestVersion \[TYPE_ERROR\], computation:WorkflowRecipe \[TYPE_ERROR\], computation:WorkflowRecipeVersion \[TYPE_ERROR\], core:Dataset \[TYPE_ERROR\], core:DatasetVersion \[TYPE_ERROR\], core:MetaDataModel \[TYPE_ERROR\], core:MetaDataModelVersion \[TYPE_ERROR\], core:Model \[TYPE_ERROR\], core:ModelVersion \[TYPE_ERROR\], core:Software \[TYPE_ERROR\], core:SoftwareVersion \[TYPE_ERROR\], core:WebService \[TYPE_ERROR\], core:WebServiceVersion \[TYPE_ERROR\], publications:LivePaper \[TYPE_ERROR\], publications:LivePaperVersion \[TYPE_ERROR\], sands:BrainAtlas \[TYPE_ERROR\], sands:BrainAtlasVersion \[TYPE_ERROR\], sands:CommonCoordinateSpace \[TYPE_ERROR\] or sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\]
   :instructions: Add all research product (versions) that are part of this project.

`BACK TO TOP <Project_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this project.

`BACK TO TOP <Project_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this project that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <Project_>`_

------------

