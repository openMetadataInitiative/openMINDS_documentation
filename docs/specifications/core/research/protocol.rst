########
Protocol
########

https://openminds.ebrains.eu/core/Protocol
------------------------------------------

Structured information on a research project.

------------

------------

**********
Properties
**********

:Required: `description <description_heading_>`_, `name <name_heading_>`_, `technique <technique_heading_>`_
:Optional: `behavioralTask <behavioralTask_heading_>`_, `studyOption <studyOption_heading_>`_

------------

.. _behavioralTask_heading:

behavioralTask
--------------

Specific set of defined activities (or their absence) that should be performed (or avoided) by a subject.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/behavioralTask
   :value type: | linked object array \(1-N\) of type
                | `BehavioralTask <https://openminds.ebrains.eu/controlledTerms/BehavioralTask>`_
   :instructions: Add all behavioral tasks that were executed as part of this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description of this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _studyOption_heading:

studyOption
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyOption
   :value type: | linked object array \(1-N\) of type
                | `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_, `CellType
                <https://openminds.ebrains.eu/controlledTerms/CellType>`_, `Disease <https://openminds.ebrains.eu/controlledTerms/Disease>`_, `DiseaseModel
                <https://openminds.ebrains.eu/controlledTerms/DiseaseModel>`_, `Handedness <https://openminds.ebrains.eu/controlledTerms/Handedness>`_, `Organ
                <https://openminds.ebrains.eu/controlledTerms/Organ>`_, `Phenotype <https://openminds.ebrains.eu/controlledTerms/Phenotype>`_, `Species
                <https://openminds.ebrains.eu/controlledTerms/Species>`_, `Strain <https://openminds.ebrains.eu/controlledTerms/Strain>`_, `TermSuggestion
                <https://openminds.ebrains.eu/controlledTerms/TermSuggestion>`_, `CustomAnatomicalEntity
                <https://openminds.ebrains.eu/sands/CustomAnatomicalEntity>`_ or `ParcellationEntity <https://openminds.ebrains.eu/sands/ParcellationEntity>`_
   :instructions: Add all study options this protocol offers.

`BACK TO TOP <Protocol_>`_

------------

.. _technique_heading:

technique
---------

Method of accomplishing a desired aim.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `Technique <https://openminds.ebrains.eu/controlledTerms/Technique>`_
   :instructions: Add all techniques that were used in this protocol.

`BACK TO TOP <Protocol_>`_

------------

