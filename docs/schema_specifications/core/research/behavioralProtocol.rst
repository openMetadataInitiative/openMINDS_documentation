##################
BehavioralProtocol
##################

:Semantic name: core:BehavioralProtocol

:Display as: Core:behavioral protocol


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `name <name_heading_>`_
:Optional: `describedIn <describedIn_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `stimulation <stimulation_heading_>`_, `stimulusType <stimulusType_heading_>`_

------------

.. _describedIn_heading:

***********
describedIn
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/describedIn
   :value type: | linked object array \(1-N\) of type
                | core:DOI \[TYPE_ERROR\], core:File \[TYPE_ERROR\] or core:WebResource \[TYPE_ERROR\]
   :instructions: Add all sources in which this behavioral protocol is described in detail.

`BACK TO TOP <BehavioralProtocol_>`_

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
   :instructions: Enter a description of this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this behavioral protocol that is used within the corresponding data files to identify this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

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
   :instructions: Enter a descriptive name for this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _stimulation_heading:

***********
stimulation
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stimulation
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:StimulationApproach \[TYPE_ERROR\] or controlledTerms:StimulationTechnique \[TYPE_ERROR\]
   :instructions: Add all stimulation approaches and/or techniques used within this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _stimulusType_heading:

************
stimulusType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stimulusType
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:AuditoryStimulusType \[TYPE_ERROR\], controlledTerms:ElectricalStimulusType \[TYPE_ERROR\], controlledTerms:GustatoryStimulusType \[TYPE_ERROR\], controlledTerms:OlfactoryStimulusType \[TYPE_ERROR\], controlledTerms:OpticalStimulusType \[TYPE_ERROR\], controlledTerms:TactileStimulusType \[TYPE_ERROR\] or controlledTerms:VisualStimulusType \[TYPE_ERROR\]
   :instructions: Add all stimulus types used within this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

