########
Protocol
########

:Semantic name: https://openminds.ebrains.eu/core/Protocol

:Display as: Protocol

Structured information on a research project.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `name <name_heading_>`_, `technique <technique_heading_>`_
:Optional: `describedIn <describedIn_heading_>`_, `stimulusType <stimulusType_heading_>`_

------------

.. _describedIn_heading:

***********
describedIn
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/describedIn
   :value type: | linked object of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add a publication or file in which this protocol is (originally) described in detail.

`BACK TO TOP <Protocol_>`_

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
   :instructions: Enter a description of this protocol.

`BACK TO TOP <Protocol_>`_

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
   :instructions: Enter a descriptive name for this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _stimulusType_heading:

************
stimulusType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/stimulusType
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:AuditoryStimulusType \[TYPE_ERROR\], controlledTerms:ElectricalStimulusType \[TYPE_ERROR\], controlledTerms:GustatoryStimulusType \[TYPE_ERROR\], controlledTerms:OlfactoryStimulusType \[TYPE_ERROR\], controlledTerms:OpticalStimulusType \[TYPE_ERROR\], controlledTerms:TactileStimulusType \[TYPE_ERROR\] or controlledTerms:VisualStimulusType \[TYPE_ERROR\]
   :instructions: Add all stimulus types used with this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:AnalysisTechnique \[TYPE_ERROR\], controlledTerms:MRIPulseSequence \[TYPE_ERROR\], controlledTerms:MRIWeighting \[TYPE_ERROR\], controlledTerms:StimulationApproach \[TYPE_ERROR\], controlledTerms:StimulationTechnique \[TYPE_ERROR\] or controlledTerms:Technique \[TYPE_ERROR\]
   :instructions: Add all techniques (including stimulation approaches and/or techniques) that were used in this protocol.

`BACK TO TOP <Protocol_>`_

------------

