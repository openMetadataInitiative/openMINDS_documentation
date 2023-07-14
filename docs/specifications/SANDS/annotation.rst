##########
Annotation
##########

:Semantic name: https://openminds.ebrains.eu/sands/Annotation

Structured information on an image annotation.


------------

------------

Properties
##########

:Required: `criteriaQualityType <criteriaQualityType_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `laterality <laterality_heading_>`_, `namingTerm <namingTerm_heading_>`_
:Optional: `bestViewPoint <bestViewPoint_heading_>`_, `criteria <criteria_heading_>`_, `displayColor <displayColor_heading_>`_, `inspiredBy <inspiredBy_heading_>`_, `relatedAtlasTerm <relatedAtlasTerm_heading_>`_, `visualizedIn <visualizedIn_heading_>`_

------------

.. _bestViewPoint_heading:

*************
bestViewPoint
*************

Coordinate point from which you get the best view of something.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/bestViewPoint
   :value type: | linked object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/coordinatePoint.html>`_
   :instructions: Add the coordinate point identifying the best view of this annotation in space.

`BACK TO TOP <Annotation_>`_

------------

.. _criteria_heading:

********
criteria
********

Aspects or standards on which a judgement or decision is based.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteria
   :value type: | linked object of type
                | `ProtocolExecution <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/core/research/protocolExecution.html>`_
   :instructions: Add the protocol execution defining the criteria that were applied to produce this annotation.

`BACK TO TOP <Annotation_>`_

------------

.. _criteriaQualityType_heading:

*******************
criteriaQualityType
*******************

Distinct class that defines how the judgement or decision was made for a particular criteria.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/criteriaQualityType
   :value type: | linked object of type
                | `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/criteriaQualityType.html>`_
   :instructions: Add the quality type of the stated criteria used to define this annotation.

`BACK TO TOP <Annotation_>`_

------------

.. _displayColor_heading:

************
displayColor
************

Preferred coloring.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/displayColor
   :value type: integer array \(3-3\)
   :instructions: Enter the preferred display color (RGB) for this annotation.

`BACK TO TOP <Annotation_>`_

------------

.. _inspiredBy_heading:

**********
inspiredBy
**********

Reference to an inspiring element.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/inspiredBy
   :value type: | linked object array \(1-N\) of type
                | `Image <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/image.html>`_
   :instructions: Add one or several (source) images that inspired the definition of this annotation.

`BACK TO TOP <Annotation_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier used for this annotation within the file it is stored in.

`BACK TO TOP <Annotation_>`_

------------

.. _laterality_heading:

**********
laterality
**********

Differentiation between a pair of lateral homologous parts of the body.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/laterality
   :value type: | linked object array \(1-2\) of type
                | `Laterality <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/controlledTerms/laterality.html>`_
   :instructions: Add one or both sides of the body or bilateral organ that this annotation is defined in.

`BACK TO TOP <Annotation_>`_

------------

.. _namingTerm_heading:

**********
namingTerm
**********

Word or expression that has a precise meaning within a science, art, profession, or subject.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/namingTerm
   :value type: | linked object array \(1-N\) of type
                | `AnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/anatomicalEntity.html>`_
   :instructions: Add one or several anatomical entities that name this annotation.

`BACK TO TOP <Annotation_>`_

------------

.. _relatedAtlasTerm_heading:

****************
relatedAtlasTerm
****************

Reference to a related naming term of an anatomical structure that is defined in a particular brain atlas.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedAtlasTerm
   :value type: | linked object array \(1-N\) of type
                | `AnatomicalEntity <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/anatomicalEntity.html>`_
   :instructions: Add one or several anatomical entities of registered brain atlas annotations to which this annotation is related to.

`BACK TO TOP <Annotation_>`_

------------

.. _visualizedIn_heading:

************
visualizedIn
************

Reference to an image in which something is visible.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/visualizedIn
   :value type: | linked object of type
                | `Image <https://openminds-documentation.readthedocs.io/en/v1.0/specifications/SANDS/image.html>`_
   :instructions: Add the image in which this annotation is visualized in.

`BACK TO TOP <Annotation_>`_

------------

