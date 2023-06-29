#######
Comment
#######

https://openminds.ebrains.eu/core/Comment
-----------------------------------------

Structured information about a short text expressing an opinion on, or giving information about some entity.

------------

------------

**********
Properties
**********

:Required: `about <about_heading_>`_, `comment <comment_heading_>`_, `commenter <commenter_heading_>`_, `timestamp <timestamp_heading_>`_
:Optional:

------------

.. _about_heading:

about
-----

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/about
   :value type: | linked object of type
                | `ValidationTest <https://openminds.ebrains.eu/computation/ValidationTest>`_, `ValidationTestVersion
                <https://openminds.ebrains.eu/computation/ValidationTestVersion>`_, `WorkflowRecipe <https://openminds.ebrains.eu/computation/WorkflowRecipe>`_,
                `WorkflowRecipeVersion <https://openminds.ebrains.eu/computation/WorkflowRecipeVersion>`_, `Dataset
                <https://openminds.ebrains.eu/core/Dataset>`_, `DatasetVersion <https://openminds.ebrains.eu/core/DatasetVersion>`_, `MetaDataModel
                <https://openminds.ebrains.eu/core/MetaDataModel>`_, `MetaDataModelVersion <https://openminds.ebrains.eu/core/MetaDataModelVersion>`_, `Model
                <https://openminds.ebrains.eu/core/Model>`_, `ModelVersion <https://openminds.ebrains.eu/core/ModelVersion>`_, `Software
                <https://openminds.ebrains.eu/core/Software>`_, `SoftwareVersion <https://openminds.ebrains.eu/core/SoftwareVersion>`_, `WebService
                <https://openminds.ebrains.eu/core/WebService>`_, `WebServiceVersion <https://openminds.ebrains.eu/core/WebServiceVersion>`_, `LivePaper
                <https://openminds.ebrains.eu/publications/LivePaper>`_, `LivePaperVersion <https://openminds.ebrains.eu/publications/LivePaperVersion>`_,
                `BrainAtlas <https://openminds.ebrains.eu/sands/BrainAtlas>`_, `BrainAtlasVersion <https://openminds.ebrains.eu/sands/BrainAtlasVersion>`_,
                `CommonCoordinateSpace <https://openminds.ebrains.eu/sands/CommonCoordinateSpace>`_ or `CommonCoordinateSpaceVersion
                <https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion>`_
   :instructions: Add the research product (version) that this comment is about.

`BACK TO TOP <Comment_>`_

------------

.. _comment_heading:

comment
-------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/comment
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the comment about the research product (version) stated under 'about'.

`BACK TO TOP <Comment_>`_

------------

.. _commenter_heading:

commenter
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/commenter
   :value type: | linked object of type
                | `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the person that created this comment.

`BACK TO TOP <Comment_>`_

------------

.. _timestamp_heading:

timestamp
---------

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/timestamp
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time on which this comment was made, formatted as '2023-02-07T16:00:00+00:00'.

`BACK TO TOP <Comment_>`_

------------

