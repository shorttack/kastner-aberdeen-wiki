---
title: "CORBA (Common Object Request Broker Architecture)"
slug: corba
page_type: technology
category: protocol
vendor: "OMG"
era: "1991-2010"
lifecycle_at_study: "emerging"
lifecycle_current: "legacy-supported"
tier: 1
study_count: 13
obs_count: 21
aliases: ["CORBA (Common Object Request Broker Architecture)"]
tags: [type/technology, category/protocol, vendor/omg]
source_csv: known_technologies.csv
---

# CORBA (Common Object Request Broker Architecture)

CORBA (Common Object Request Broker Architecture) is a protocol from OMG (era 1991-2010). Current lifecycle: legacy-supported.

**Appears in 13 studies, 21 observations.**

## Studies citing this technology

- [[1999-aberdeengroup-newsletter-april-1999-d157ec|AberdeenGroup Newsletter Volume 1 Number 2 — April 1999]] (1999-04-01)
- [[intern~1-45df51|Internet Infrastructures: 1998 Practice Summary]] (1998-05-01)
- [[middle~1-a64fa0|Middleware Technology: 1998 Practice Summary]] (1998-05-01)
- [[1997-broadvision-dynamic-web-application-5f10bb|BroadVision Dynamic Web Applications Enhance Employees, Clinch Customers, and Pamper Partners]] (1997-07-07)
- [[1997-commerce-exchange-pvp-250db8|Commerce eXchange Answers The 'Show Me The Internet Money!' Challenge]] (1997-03-14)
- [[tool-vendors-neglect-intranet-computing--97bde3|Tool vendors neglect intranet needs (Kastner three-year IT predictions)]] (1996-10-30)
- [[aberdeen-1995-hp-softbench|Hewlett-Packard's C++ SoftBench 5.0 -- A Powerful Platform for Professional Developers]] (1995-12-01)
- [[nti-5-development-toolsets-0e71c5|Selecting and Using Advanced Software Toolsets]] (1993-04-01)
- [[nti-4-nextgen-os-timing-1993-a45049|Timing Your Move to Next Generation Operating Systems]] (1993-02-01)
- [[nti-2-open-systems-1dd3af|Open Systems: A Technology Status Report]] (1993-01-01)

## Top observations

- **1997** — BroadVision CORBA architecture scalability: CORBA-based system scales by replacing or adding servers; communicates with existing apps via screen scraping or other CORBA systems ([[1997-broadvision-dynamic-web-application-5f10bb]])
- **1997** — CORBA vs DCOM enterprise internet standards battle: Oracle, BroadVision promoting CORBA; Microsoft pushing DCOM; typical middleware translation gateways create performance hit; Oasis avoids this with neutral abstraction layer ([[1997-commerce-exchange-pvp-250db8]])
- **2005** — CORBA/DCOM enterprise internet standard outcome: CORBA and DCOM both largely obsolete by 2005; replaced by XML/SOAP web services and later REST/JSON APIs; the abstraction layer approach InterWorld championed proved correct but manifested differently than 1997 technology battle suggested ([[1997-commerce-exchange-pvp-250db8]])
- **1997** — CORBA as middleware integration standard: Emerging enterprise middleware; VISION should integrate with CORBA for object distribution ([[1997-unify-vision-8fcfc3]])
- **1999** — CORBA vs DCOM standards war outcome: Crucial to ISV strategies; outcome undetermined in 1999 ([[1999-aberdeengroup-newsletter-april-1999-d157ec]])
- **2003** — CORBA vs DCOM standards war — actual outcome: Both largely superseded by web services (SOAP/REST) and later microservices; neither CORBA nor DCOM won ([[1999-aberdeengroup-newsletter-april-1999-d157ec]])
- **1995** — Distributed objects market size: <$10 million ([[aberdeen-1995-commercial-messaging]])
- **1995** — CORBA Commercial Messaging readiness: will not provide Commercial Messaging capabilities in near future ([[aberdeen-1995-commercial-messaging]])
- **1995** — Microsoft distributed-object Commercial Messaging readiness: will not provide Commercial Messaging capabilities in near future ([[aberdeen-1995-commercial-messaging]])
- **2010** — CORBA Commercial Messaging outcome: CORBA became largely obsolete; never provided mainstream Commercial Messaging ([[aberdeen-1995-commercial-messaging]])
- **1995** — HP Distributed Smalltalk: HP Distributed Smalltalk (DST) allows building CORBA-compliant Smalltalk systems conforming to OMG CORBA specification using an object request broker ([[aberdeen-1995-hp-softbench]])
- **1996** — HP ORB Plus CORBA C++ rollout outcome: HP did ship ORB+ and CORBA tools for HP-UX in 1996; however HP-UX and SoftBench ecosystem declined through late 1990s as Java and web-based development supplanted C++ toolchain; SoftBench eventually discontinued ([[aberdeen-1995-hp-softbench]])
- **1996** — ICX / CORBA ORB role: Location-independent component invocation across platforms; bridges Oracle NCA to Microsoft COM ([[aberdeen-1996-oracle-network-computing-architecture]])
- **2005** — CORBA market outcome: CORBA declined rapidly by 2000s; superseded by XML web services and REST; Oracle shifted accordingly ([[aberdeen-1996-oracle-network-computing-architecture]])
- **1998** — CORBA role in Java interoperability: CORBA extends Java capabilities to legacy and disparate platforms; Aberdeen predicts CORBA will become lingua franca between different Java environments ([[intern~1-45df51]])
- **1998** — orb_interoperability_status: Major ORBs do not communicate with each other; CORBA and DCOM cannot interoperate ([[middle~1-a64fa0]])
- **1993** — Object-oriented standards status: Early stage; CORBA work beginning ([[nti-2-open-systems-1dd3af]])
- **1993** — Object-oriented systems mainstream impact timeline: Not until turn of the century (year 2000) ([[nti-4-nextgen-os-timing-1993-a45049]])
- **2000** — Object-oriented systems mainstream reality: [UNVERIFIED] ([[nti-4-nextgen-os-timing-1993-a45049]])
- **1993** — OMG standardization scope: Standardizing types of service requests objects universally provide; object behavior in distributed systems ([[nti-5-development-toolsets-0e71c5]])

## DuckDB query for full data

```sql
SELECT * FROM observations WHERE tech_id = 'corba';
```

