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
:Optional: `describedIn <describedIn_heading_>`_, `stimulusType <stimulusType_heading_>`_

------------

.. _describedIn_heading:

describedIn
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/describedIn
   :value type: | linked object of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_, `File <https://openminds.ebrains.eu/core/File>`_ or `WebResource
                <https://openminds.ebrains.eu/core/WebResource>`_
   :instructions: Add a publication or file in which this behavioral protocol is (originally) described in detail.

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

.. _stimulusType_heading:

stimulusType
------------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stimulusType
   :value type: | linked object array \(1-N\) of type
                | `AuditoryStimulusType <https://openminds.ebrains.eu/controlledTerms/AuditoryStimulusType>`_, `ElectricalStimulusType
                <https://openminds.ebrains.eu/controlledTerms/ElectricalStimulusType>`_, `GustatoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/GustatoryStimulusType>`_, `OlfactoryStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OlfactoryStimulusType>`_, `OpticalStimulusType
                <https://openminds.ebrains.eu/controlledTerms/OpticalStimulusType>`_, `TactileStimulusType
                <https://openminds.ebrains.eu/controlledTerms/TactileStimulusType>`_ or `VisualStimulusType
                <https://openminds.ebrains.eu/controlledTerms/VisualStimulusType>`_
   :instructions: Add all stimulus types used with this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _technique_heading:

technique
---------

Method of accomplishing a desired aim.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds.ebrains.eu/controlledTerms/AnalysisTechnique>`_, `StimulationApproach
                <https://openminds.ebrains.eu/controlledTerms/StimulationApproach>`_, `StimulationTechnique
                <https://openminds.ebrains.eu/controlledTerms/StimulationTechnique>`_ or `Technique <https://openminds.ebrains.eu/controlledTerms/Technique>`_
   :instructions: Add all techniques (including stimulation approaches and/or techniques) that were used in this protocol.

`BACK TO TOP <Protocol_>`_

------------

