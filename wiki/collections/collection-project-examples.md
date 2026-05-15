                ---
                title: "Collection: Project Examples"
                slug: collection-project-examples
                page_type: collection
                tier: 1
                tags: [type/collection]
                ---
                # Project Examples

                Source rollup row from `_collection_stats.csv`:

                - **collection**: Project Examples
- **study_id**: world-it-spending-2002-2005-2265a2
- **title**: World IT Spending 2002-2005: Timing the Recovery
- **date**: 2002-04-01
- **author**: Aberdeen Group
- **n_entities**: 2
- **n_technologies**: 0
- **n_observations**: 27
- **n_codes**: 25
- **importance**: medium
- **relevance**: low
- **prescience**: medium

                ```dataview
                TABLE date, importance, prescience
                FROM "studies"
                SORT date ASC
                ```
