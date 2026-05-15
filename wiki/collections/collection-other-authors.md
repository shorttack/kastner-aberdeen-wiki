                ---
                title: "Collection: other-authors"
                slug: collection-other-authors
                page_type: collection
                tier: 1
                tags: [type/collection]
                ---
                # other-authors

                Source rollup row from `_collection_stats.csv`:

                - **collection**: other-authors
- **study_id**: youtube-kastner-intel-vpro-tco-2008-cb1733
- **title**: Industry Analyst Discusses Impact of Intel vPro Technology
- **date**: 2008-09-23
- **author**: Intel Corporation (featuring Peter S. Kastner)
- **n_entities**: 3
- **n_technologies**: 4
- **n_observations**: 2
- **n_codes**: 26
- **importance**: medium
- **relevance**: medium
- **prescience**: low

                ```dataview
                TABLE date, importance, prescience
                FROM "studies"
                SORT date ASC
                ```
