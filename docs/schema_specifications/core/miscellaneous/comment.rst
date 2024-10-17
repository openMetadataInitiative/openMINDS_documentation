#######
Comment
#######

:Semantic name: core:Comment

:Display as: Core:comment


------------

------------

Properties
##########

:Required: `about <about_heading_>`_, `comment <comment_heading_>`_, `commenter <commenter_heading_>`_, `timestamp <timestamp_heading_>`_
:Optional:

------------

.. _about_heading:

*****
about
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/about
   :value type: | linked object of type
                | computation:ValidationTest \[TYPE_ERROR\], computation:ValidationTestVersion \[TYPE_ERROR\], computation:WorkflowRecipe \[TYPE_ERROR\], computation:WorkflowRecipeVersion \[TYPE_ERROR\], core:Dataset \[TYPE_ERROR\], core:DatasetVersion \[TYPE_ERROR\], core:MetaDataModel \[TYPE_ERROR\], core:MetaDataModelVersion \[TYPE_ERROR\], core:Model \[TYPE_ERROR\], core:ModelVersion \[TYPE_ERROR\], core:Software \[TYPE_ERROR\], core:SoftwareVersion \[TYPE_ERROR\], core:WebService \[TYPE_ERROR\], core:WebServiceVersion \[TYPE_ERROR\], publications:LivePaper \[TYPE_ERROR\], publications:LivePaperVersion \[TYPE_ERROR\], sands:BrainAtlas \[TYPE_ERROR\], sands:BrainAtlasVersion \[TYPE_ERROR\], sands:CommonCoordinateSpace \[TYPE_ERROR\] or sands:CommonCoordinateSpaceVersion \[TYPE_ERROR\]
   :instructions: Add the research product (version) that this comment is about.

`BACK TO TOP <Comment_>`_

------------

.. _comment_heading:

*******
comment
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/comment
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter the comment about the research product (version) stated under 'about'.

`BACK TO TOP <Comment_>`_

------------

.. _commenter_heading:

*********
commenter
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/commenter
   :value type: | linked object of type
                | core:Person \[TYPE_ERROR\]
   :instructions: Add the person that created this comment.

`BACK TO TOP <Comment_>`_

------------

.. _timestamp_heading:

*********
timestamp
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/timestamp
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time on which this comment was made, formatted as '2023-02-07T16:00:00+00:00'.

`BACK TO TOP <Comment_>`_

------------

