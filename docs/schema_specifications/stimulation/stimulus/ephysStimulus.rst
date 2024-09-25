#############
EphysStimulus
#############

:Semantic name: stimulation:EphysStimulus

:Display as: Stimulation:ephys stimulus


------------

------------

Properties
##########

:Required: `internalIdentifier <internalIdentifier_heading_>`_
:Optional: `deliveredBy <deliveredBy_heading_>`_, `description <description_heading_>`_, `epoch <epoch_heading_>`_, `generatedBy <generatedBy_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `specification <specification_heading_>`_, `type <type_heading_>`_

------------

.. _deliveredBy_heading:

***********
deliveredBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/deliveredBy
   :value type: | linked object of type
                | ephys:ElectrodeArrayUsage \[TYPE_ERROR\], ephys:ElectrodeUsage \[TYPE_ERROR\], ephys:PipetteUsage \[TYPE_ERROR\] or specimenPrep:SlicingDeviceUsage \[TYPE_ERROR\]
   :instructions: Add the device used to deliver this stimulus.

`BACK TO TOP <EphysStimulus_>`_

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
   :instructions: Enter a short text describing this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _epoch_heading:

*****
epoch
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/epoch
   :value type: | embedded object of type
                | core:QuantitativeValue \[TYPE_ERROR\]
   :instructions: Enter the total epoch length of this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _generatedBy_heading:

***********
generatedBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/generatedBy
   :value type: | linked object of type
                | ephys:ElectrodeArrayUsage \[TYPE_ERROR\], ephys:ElectrodeUsage \[TYPE_ERROR\], ephys:PipetteUsage \[TYPE_ERROR\] or specimenPrep:SlicingDeviceUsage \[TYPE_ERROR\]
   :instructions: Add the device used to generate this stimulus.

`BACK TO TOP <EphysStimulus_>`_

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
   :instructions: Enter the identifier (or label) of this stimulus that is used within the corresponding data files to identify this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this stimulus that may help you to find this instance more easily.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _specification_heading:

*************
specification
*************

Detailed and precise presentation of, or proposal for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specification
   :value type: | linked object array \(1-N\) of type
                | core:Configuration \[TYPE_ERROR\], core:File \[TYPE_ERROR\], core:FileBundle \[TYPE_ERROR\] or core:PropertyValueList \[TYPE_ERROR\]
   :instructions: Add the specification information for this stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object of type
                | controlledTerms:ElectricalStimulusType \[TYPE_ERROR\]
   :instructions: Add the type that describe this electrical stimulus.

`BACK TO TOP <EphysStimulus_>`_

------------

