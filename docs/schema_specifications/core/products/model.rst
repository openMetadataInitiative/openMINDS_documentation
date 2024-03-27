#####
Model
#####

:Semantic name: https://openminds.ebrains.eu/core/Model

:Display as: Model

Structured information on a computational model (concept level).


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `fullName <fullName_heading_>`_, `shortName <shortName_heading_>`_
:Optional: `hasVersion <hasVersion_heading_>`_, `homepage <homepage_heading_>`_

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
   :instructions: Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references).

`BACK TO TOP <Model_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | `DigitalIdentifier <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/digitalIdentifier.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this research product.

`BACK TO TOP <Model_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name (title) for this research product.

`BACK TO TOP <Model_>`_

------------

.. _hasVersion_heading:

**********
hasVersion
**********

Reference to variants of an original.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hasVersion
   :value type: | linked object array \(1-N\) of type
                | `ModelVersion <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/products/modelVersion.html>`_
   :instructions: Add one or several versions of this computational model.

`BACK TO TOP <Model_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this research product.

`BACK TO TOP <Model_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (alias) for this research product (max. 30 characters; no space).

`BACK TO TOP <Model_>`_

------------

