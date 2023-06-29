##################
BehavioralProtocol
##################

****************************************************
https://openminds.ebrains.eu/core/BehavioralProtocol
****************************************************

Structured information about a protocol used in an experiment studying human or animal behavior.

------------

------------

**********
Properties
**********

:Required: `description <description_heading_>`_, `name <name_heading_>`_
:Optional: `describedIn <describedIn_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `stimulation <stimulation_heading_>`_, `stimulusType
   <stimulusType_heading_>`_

------------

.. _describedIn_heading:

describedIn
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/describedIn
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds.ebrains.eu/core/DOI>`_, `File <https://openminds.ebrains.eu/core/File>`_or `WebResource
                <https://openminds.ebrains.eu/core/WebResource>`_
   :instructions: Add all sources in which this behavioral protocol is described in detail.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _description_heading:

description
-----------

Longer statement or account giving the characteristics of someone or something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a description of this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this behavioral protocol that is used within the corresponding data files to identify this behavioral
      protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _name_heading:

name
----

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive name for this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _stimulation_heading:

stimulation
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stimulation
   :value type: | linked object array \(1-N\) of type
                | `StimulationApproach <https://openminds.ebrains.eu/controlledTerms/StimulationApproach>`_or `StimulationTechnique
                <https://openminds.ebrains.eu/controlledTerms/StimulationTechnique>`_
   :instructions: Add all stimulation approaches and/or techniques used within this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

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
                <https://openminds.ebrains.eu/controlledTerms/TactileStimulusType>`_or `VisualStimulusType
                <https://openminds.ebrains.eu/controlledTerms/VisualStimulusType>`_
   :instructions: Add all stimulus types used within this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

