#################
Studied specimens
#################

openMINDS supports the representation of two explicit types of specimens: **subject** (referring to a whole organism) and **tissue sample** (referring to an extracted or artifically grown tissue). Moreover, openMINDS supports the additional or alternative representation of individual specimens as respective sets, referred to as **subject group** and **tissue sample collection**. 

Time dependencies of specimen properties
########################################

For each specimen (set), openMINDS distinguishes timepoint-independent from timepoint-dependent properties which are captured separately in a specimen (set) state. Each specimen (set) is therewith linked to at least one specimen (set) state.

Descendence of specimens
########################

openMINDS also supports you to identify if a specific state of a specimen (set) **descents from** a particular state of another specimen (set). For example, an unfixated state of a tissue sample can descent from an anaesthetized state of a subject as result of a biopsy, or an unmounted state of a tissue sample collection can descent from a fixated state of a tissue sample as result of a tissue slicing procedure.  
