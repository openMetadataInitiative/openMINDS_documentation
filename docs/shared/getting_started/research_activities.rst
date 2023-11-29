###################
Research activities
###################

In particular for dataset versions, openMINDS can capture the actual performed research activities producing respective data with different level of detail. 

Tagging a dataset version
#########################

For the most basic level to indicate what was done, a dataset version can be tagged with the studied specimen (cf. previous chapter), the used techniques, the study targets, as well as the used technical and behavioral protocols. 

Used **techniques** and **study targets** link to different types of controlled terms (e.g., analysis technique, stimulation technique, age category, anatomical entity, etc.). A well-defined selection of metadata instances of these controlled term types are provided through the openMINDS libraries or can be user-defined (in case of study targets).

.. note::
   For all controlled terms, openMINDS provides libraries of well-defined metadata instances that are linked to matching ontological terms where applicable. The instances of these libraries are maintained and extended together with the InterLex project and the Knowledge Space.

A **technical protocol** requires a user to name and describe the applied technical procedure in form of a generic recipe (should be reusable across dataset verions). In addition, the technical protocol should be tagged with the respectively used techniques. These techniques should be at least a subset of the techniques tagged onto the dataset version the technical protocol is linked to.

A **behavioural protocol** requires a user to name and describe the conducted behavioural task or paradigm in form of a generic recipe (should be reusable across dataset verions). When applicable, the behavioural protocol should be tagged with the respectively used stimulus types and stimulation techniques. These stimulation techniques should be at least a subset of the techniques tagged onto the dataset version the behavioural protocol is linked to.
