# Contributing to Project MRI

Contributions should make the governed-context boundary clearer, safer or more reproducible.

## Before opening a change

- run the unit suite;
- run the Northstar eval;
- add or update a negative case when changing diagnostics;
- preserve source paths and line-range evidence;
- keep fixture data synthetic or explicitly public;
- update the claim map when a public claim changes.

## Design constraints

- keep mutation proposal-only unless a separately authorized design adds a reversible write boundary;
- do not treat the newest source as authoritative without stating the uncertainty;
- do not add a model/provider dependency merely for appearance;
- keep provider operations downstream from MRI’s evidence and review model;
- preserve Apache-2.0 code / CC BY 4.0 documentation scope unless a file-level notice says otherwise.

## Pull requests

Describe the user-visible behavior, evidence/fixture changes, safety impact and claim impact. A green CI run is required for merge.
