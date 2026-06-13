# Quick Start

## Choose a command

```text
/github    clone, create, or push a research repository
/code-idea extract candidate research ideas from existing code
/idea      refine a raw research idea
/lit       search literature and closest work
/gap       assess novelty and decide go/pivot/stop
/frame     design the research framework
/exp       plan experiments
/paper     create the paper core or write sections
/method    write and audit a Method section against code
/review    run adversarial review
/submit    check submission readiness
/project   manage project state
/log       maintain research logs
```

## Start from existing code

```text
/github clone OWNER/REPO with --depth=1
/code-idea inspect the repository and extract candidate ideas
/lit find closest work and method citations
/gap decide go, pivot, stop, or search more
/frame define the defensible framework
/exp plan evidence for each claim
/method write the Method section with a method-to-code map
/review audit novelty, implementation alignment, and evidence
```

For a private repository, prefer:

```bash
gh repo clone OWNER/REPO DEST -- --depth=1
```

## Start from a raw idea

```text
/idea <raw idea>
/lit search current and foundational literature
/gap assess the gap
/frame design the framework
/exp plan experiments
/paper create the paper core
```

Every workflow must separate facts, hypotheses, and plans; name evidence gaps; save a concrete artifact; and end with the next smallest useful action.
