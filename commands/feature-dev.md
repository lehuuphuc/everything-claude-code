---
description: Guided feature development with codebase understanding and architecture focus
---

A structured 7-phase feature development workflow that emphasizes understanding existing code before writing new code.

## Phases

### Phase 1: Discovery
- Read the user's feature request carefully
- Identify key requirements, constraints, and acceptance criteria
- Ask clarifying questions if the request is ambiguous

### Phase 2: Codebase Exploration
- Use the **code-explorer** agent to deeply analyze relevant existing code
- Trace execution paths and map architecture layers
- Understand existing patterns, abstractions, and conventions
- Document dependencies and integration points

### Phase 3: Clarifying Questions
- Present findings from exploration to the user
- Ask targeted questions about design decisions, edge cases, and preferences
- **Wait for user response before proceeding**

### Phase 4: Architecture Design
- Use the **code-architect** agent to design the feature architecture
- Provide implementation blueprint: files to create/modify, component designs, data flows
- Present the plan to the user for approval
- **Wait for user approval before implementing**

### Phase 5: Implementation
- Implement the feature following the approved architecture
- Use TDD approach: write tests first, then implementation
- Follow existing codebase patterns and conventions
- Make small, focused commits

### Phase 6: Quality Review
- Use the **code-reviewer** agent to review the implementation
- Address Critical and Important issues
- Verify test coverage meets requirements

### Phase 7: Summary
- Summarize what was built and how it integrates
- List any follow-up items or known limitations
- Provide testing instructions
