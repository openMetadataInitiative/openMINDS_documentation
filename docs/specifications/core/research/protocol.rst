########
Protocol
########

:Semantic name: https://openminds.ebrains.eu/core/Protocol

Structured information on a research project.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `name <name_heading_>`_, `technique <technique_heading_>`_
:Optional: `behavioralTask <behavioralTask_heading_>`_, `studyTarget <studyTarget_heading_>`_

------------

.. _behavioralTask_heading:

**************
behavioralTask
**************

Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/behavioralTask
   :value type: | linked object array \(1-N\) of type
                | `BehavioralTask <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/behavioralTask.html>`_
   :instructions: Add all behavioral tasks that were executed as part of this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _studyTarget_heading:

***********
studyTarget
***********

Structure or function that was targeted within a study.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyTarget
   :value type: | linked object array \(1-N\) of type
                | `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/biologicalSex.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/disease.html>`_, `Genotype <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/genotype.html>`_, `Phenotype <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/phenotype.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/species.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/termSuggestion.html>`_ or `AnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/anatomicalEntity.html>`_
   :instructions: Add all study targets of this model version.

`BACK TO TOP <Protocol_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `Technique <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/technique.html>`_
   :instructions: Add all techniques that were used in this protocol.

`BACK TO TOP <Protocol_>`_

------------

