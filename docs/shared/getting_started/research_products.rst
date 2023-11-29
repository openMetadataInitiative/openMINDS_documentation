#################
Research products
#################

openMINDS supports the representation of various research products (e.g., datasets from human, animal or simulation studies, computational models, software tools). All research products are versioned, have a common set of bibliographic properties, and (typically) link to a file repository pointing to the stored data.

Versioning of research products 
###############################

openMINDS distinguishes between a conceptual (version-independent) research product and it's respective research product version(s). Both entities, research product and research product version, can be assigned with a unique, persistent digital identifier (e.g., a digital object identifier; DOI) which enables the citation of the overall concept (referring to all versions at once) or the explicit citation of a specific version.  

A **research product** is composed of properties that are typically valid across all versions (e.g., title, abstract, homepage) and has to link to at least one research product version.  

A **research product version** can inherit or overwrite all version-independent properties. Additionally, it includes properties that are (usually) version-specific (e.g., studied specimen, used technique). If a research product is composed of multiple versions, these versions can refer to each other as updates or alternatives:

If the usage of version **B** should be preferred over version **A**, version **B** **is** (the) **new version of** version **A**. For example, a software version could be preferred over another, because it includes more application features, or a dataset version could be preferred over another, because it studied a larger cohort.

If the usage of version **A** and **B** depends on the users preference, the versions should reference each other as **alternative version of**. For example, two model versions describe the same computational model, but using different model description languages, or two dataset versions could present the same data content, but using different data formats. 

Registration of data
####################

openMINDS allows to register data at three levels of detail: 

**Level-01:** Registration of a file repository with generic properties (e.g., storage size, name, hosted by) and a pointer (internationalized resource identifier; IRI) to the main data folder.    

**Level-02:** Registration of a file repository (cf. level-01) including the indexing of all data files that are part of this repository with individual file properties (e.g., storage size, name, format) and a specific file pointer (IRI).  

**Level-03:** Registration of a general pointer to a file repository, individual pointers to all data files within this repository, and grouping of those data files into customized file bundles. 

Grouping of research products
#############################

openMINDS supports the grouping of different research products into a joint research project (e.g. to capture collaborative work).  
