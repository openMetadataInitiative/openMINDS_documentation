#################
Research products
#################

openMINDS supports the representation of various research products (e.g., datasets from human, animal or simulation studies, computational models, software tools). All research products are versioned, have a common set of bibliographic properties, and (typically) link to a file repository pointing to the stored data.

Understanding research product versioning
#########################################

openMINDS distinguishes between a conceptual (version-independent) research product and it's respective research product version(s). Both entities, research product and research product version, can be assigned with a unique, persistent digital identifier (e.g., a digital object identifier; DOI) which enables the citation of the overall concept (including all versions) or a specific version.  

A **research product** is composed of properties that are typically valid across all versions (e.g., title, abstract, homepage) and has to link to at least one research product version.  

A **research product version** can inherit or overwrite all version-independent properties. Additionally, it includes properties that are (usually) version-specific (e.g., studied specimen, used technique). If a research product is composed of multiple versions, these versions can refer to each other as updates or alternatives:

If the usage of version **B** should be preferred over version A, version B **is the new version of** version A. For example, a software version could be preferred over another, because it includes more application features, or a dataset version could be preferred over another, because it studied a larger cohort.

If the usage of version A and B depends on the users preference, the versions should reference each other as **alternative version of**. For example, two model versions describe the same computational model, but using different model description languages, or two dataset versions could present the same data content, but using different data formats. 

Registration of file repositories
#################################

openMINDS allows to register data from a file repository in three levels of detail: 

**Level-01:** Registration of a general pointer to a file repository.  

**Level-02:** Registration of a general pointer to a file repository, and individual pointers to all data files within this repository.  

**Level-03:** Registration of a general pointer to a file repository, individual pointers to all data files within this repository, and grouping of those data files into customized file bundles. 


Making use of research projects
###############################

openMINDS supports the grouping of different research products into a joint research project (e.g. to capture collaborative work).  
