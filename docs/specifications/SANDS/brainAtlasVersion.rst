#################
BrainAtlasVersion
#################

:Semantic name: https://openminds.ebrains.eu/sands/BrainAtlasVersion

Structured information on a brain atlas (version level).


------------

------------

Properties
##########

:Required: `annotationSet <annotationSet_heading_>`_, `coordinateSpace <coordinateSpace_heading_>`_, `fullName <fullName_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `terminology <terminology_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_, `versionInnovation <versionInnovation_heading_>`_
:Optional: `digitalIdentifier <digitalIdentifier_heading_>`_, `hasAlternativeVersion <hasAlternativeVersion_heading_>`_, `homepage <homepage_heading_>`_, `isNewVersionOf <isNewVersionOf_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _annotationSet_heading:

*************
annotationSet
*************

Collection of notes or markings, each added by way of comment or explanation.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/annotationSet
   :value type: | linked object array \(1-N\) of type
                | `Annotation <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/annotation.html>`_
   :instructions: Add all annotations that belong to this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _coordinateSpace_heading:

***************
coordinateSpace
***************

Two or three dimensional geometric setting.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinateSpace
   :value type: | linked object of type
                | `CoordinateSpace <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/coordinateSpace.html>`_
   :instructions: Add the coordinate space in which this brain atlas version exists in.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DigitalIdentifier <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/miscellaneous/digitalIdentifier.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name for this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _hasAlternativeVersion_heading:

*********************
hasAlternativeVersion
*********************

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasAlternativeVersion
   :value type: | linked object array \(1-N\) of type
                | `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/brainAtlasVersion.html>`_
   :instructions: Add one or several alternative versions to this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this brain atlas.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _isNewVersionOf_heading:

**************
isNewVersionOf
**************

Reference to a previous (potentially outdated) particular form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isNewVersionOf
   :value type: | linked object of type
                | `BrainAtlasVersion <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/brainAtlasVersion.html>`_
   :instructions: Add the earlier version of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (IRI) of the related ontological term matching this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date of first publication of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive short name for this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _terminology_heading:

***********
terminology
***********

Nomenclature for a particular field of study.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/terminology
   :value type: | linked object of type
                | `AtlasTerminology <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/atlasTerminology.html>`_
   :instructions: Add the terminology used for this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

.. _versionInnovation_heading:

*****************
versionInnovation
*****************

Documentation on what changed in comparison to a previously published form of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionInnovation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short description of the novelties/peculiarities of this brain atlas version.

`BACK TO TOP <BrainAtlasVersion_>`_

------------

