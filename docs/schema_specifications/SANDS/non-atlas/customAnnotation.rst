################
CustomAnnotation
################

:Semantic name: https://openminds.ebrains.eu/sands/CustomAnnotation


------------

------------

Properties
##########

:Required: `coordinateSpace <coordinateSpace_heading_>`_, `criteriaQualityType <criteriaQualityType_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `visualizedIn <visualizedIn_heading_>`_
:Optional: `bestViewPoint <bestViewPoint_heading_>`_, `criteria <criteria_heading_>`_, `displayColor <displayColor_heading_>`_, `inspiredBy <inspiredBy_heading_>`_, `laterality <laterality_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `name <name_heading_>`_

------------

.. _bestViewPoint_heading:

*************
bestViewPoint
*************

Coordinate point from which you get the best view of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/bestViewPoint
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Add the coordinate point identifying the best view of this custom annotation in space.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _coordinateSpace_heading:

***************
coordinateSpace
***************

Two or three dimensional geometric setting.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinateSpace
   :value type: | linked object of type
                | `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/atlas/commonCoordinateSpace.html>`_ or `CustomCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/non-atlas/customCoordinateSpace.html>`_
   :instructions: Add the coordinate space in which this custom annotation exists.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _criteria_heading:

********
criteria
********

Aspects or standards on which a judgement or decision is based.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteria
   :value type: | linked object of type
                | `ProtocolExecution <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/research/protocolExecution.html>`_
   :instructions: Add the protocol execution defining the criteria that were applied to produce this custom annotation.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _criteriaQualityType_heading:

*******************
criteriaQualityType
*******************

Distinct class that defines how the judgement or decision was made for a particular criteria.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteriaQualityType
   :value type: | linked object of type
                | `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/controlledTerms/criteriaQualityType.html>`_
   :instructions: Add the quality type of the stated criteria used to define this custom annotation.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _displayColor_heading:

************
displayColor
************

Preferred coloring.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/displayColor
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the preferred display color (HEX) for this custom annotation.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _inspiredBy_heading:

**********
inspiredBy
**********

Reference to an inspiring element.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inspiredBy
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/data/file.html>`_
   :instructions: Add one or several (source) files that inspired the definition of this custom annotation.

`BACK TO TOP <CustomAnnotation_>`_

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
   :instructions: Enter the identifier used for this custom annotation within the file it is stored in.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _laterality_heading:

**********
laterality
**********

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/controlledTerms/laterality.html>`_
   :instructions: Add one or both sides of the body, bilateral organ or bilateral organ part that this custom annotation is defined in.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this custom annotation that may help you to more easily find it again.

`BACK TO TOP <CustomAnnotation_>`_

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
   :instructions: Enter a descriptive name for this custom annotation.

`BACK TO TOP <CustomAnnotation_>`_

------------

.. _visualizedIn_heading:

************
visualizedIn
************

Reference to an image in which something is visible.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/visualizedIn
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/data/file.html>`_
   :instructions: Add the (source) image file in which this custom annotation is visualized in.

`BACK TO TOP <CustomAnnotation_>`_

------------

