#######################
ParcellationTerminology
#######################

https://openminds.ebrains.eu/sands/ParcellationTerminology
----------------------------------------------------------

------------

------------

**********
Properties
**********

:Required: `fullName <fullName_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `definedIn <definedIn_heading_>`_, `isAlternativeVersionOf <isAlternativeVersionOf_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _definedIn_heading:

definedIn
---------

Reference to a file instance in which something is stored.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/definedIn
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds.ebrains.eu/core/File>`_
   :instructions: Add one or several files in which this parcellation terminology is stored in.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _fullName_heading:

fullName
--------

Whole, non-abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name for this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _isAlternativeVersionOf_heading:

isAlternativeVersionOf
----------------------

Reference to an original form where the essence was preserved, but presented in an alternative form.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isAlternativeVersionOf
   :value type: | linked object array \(1-N\) of type
                | `BrainAtlasVersion <https://openminds.ebrains.eu/sands/BrainAtlasVersion>`_
   :instructions: Add one or several alternative versions to this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _isNewVersionOf_heading:

isNewVersionOf
--------------

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `BrainAtlasVersion <https://openminds.ebrains.eu/sands/BrainAtlasVersion>`_
   :instructions: Add the earlier version of this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _ontologyIdentifier_heading:

ontologyIdentifier
------------------

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (IRI) of the related ontological term matching this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _shortName_heading:

shortName
---------

Shortened or fully abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive short name for this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _versionIdentifier_heading:

versionIdentifier
-----------------

Term or code used to identify the version of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

.. _versionInnovation_heading:

versionInnovation
-----------------

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short description of the novelties/peculiarities of this parcellation terminology.

`BACK TO TOP <ParcellationTerminology_>`_

------------

