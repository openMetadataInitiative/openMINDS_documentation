#######
Subject
#######

*****************************************
https://openminds.ebrains.eu/core/Subject
*****************************************

Structured information on a subject.

------------

------------

**********
Properties
**********

:Required: `species <species_heading_>`_, `studiedState <studiedState_heading_>`_
:Optional: `biologicalSex <biologicalSex_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `isPartOf <isPartOf_heading_>`_, `lookupLabel
   <lookupLabel_heading_>`_

------------

.. _biologicalSex_heading:

biologicalSex
-------------

Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/biologicalSex
   :value type: | linked object of type
                | `BiologicalSex <https://openminds.ebrains.eu/controlledTerms/BiologicalSex>`_
   :instructions: Add the biological sex of this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _internalIdentifier_heading:

internalIdentifier
------------------

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this specimen that is used within the corresponding data files to identify this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _isPartOf_heading:

isPartOf
--------

Reference to the ensemble of multiple things or beings.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `SubjectGroup <https://openminds.ebrains.eu/core/SubjectGroup>`_
   :instructions: Add all subject groups of which this subject is a member.

`BACK TO TOP <Subject_>`_

------------

.. _lookupLabel_heading:

lookupLabel
-----------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this specimen that may help you to find this instance more easily.

`BACK TO TOP <Subject_>`_

------------

.. _species_heading:

species
-------

Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that
consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/species
   :value type: | linked object of type
                | `Species <https://openminds.ebrains.eu/controlledTerms/Species>`_or `Strain <https://openminds.ebrains.eu/core/Strain>`_
   :instructions: Add the species or strain (a sub-type of a genetic variant of species) of this specimen.

`BACK TO TOP <Subject_>`_

------------

.. _studiedState_heading:

studiedState
------------

Reference to a point in time at which something or someone was studied in a particular mode or condition.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studiedState
   :value type: | linked object array \(1-N\) of type
                | `SubjectState <https://openminds.ebrains.eu/core/SubjectState>`_
   :instructions: Add all states in which this subject was studied.

`BACK TO TOP <Subject_>`_

------------

