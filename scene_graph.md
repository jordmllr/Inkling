# Scene Graph

A scene graph is the causal flow graph of a scene. It represents how character X does action Y in an attempt to accomplish Z, driven by motivation M, within context C, resulting in outcome O.

## Nodes

### Characters
Characters are the active agents within a scene. Each character should have:

#### Identity
- **Name**: The character's identifier
- **Description**: Brief character description
- **Background**: Relevant history that influences current behavior
- **Memory**: What the character remembers and forgets (influences perception)

#### Motivation Patterns
Motivation patterns represent the psychological drives that influence character behavior and can be modeled as nodes that connect to specific objects, people, or concepts within the scene.

##### Core Motivation Types
- **Achievement**: Desire to accomplish difficult tasks, overcome obstacles, attain high standards
- **Affiliation**: Need for close relationships and belonging
- **Power**: Desire to influence, control, or impact others
- **Meaning**: Search for purpose and significance
- **Autonomy**: Need for self-determination and independence
- **Competence**: Desire to be effective in dealing with the environment
- **Security**: Need for safety and stability
- **Recognition**: Desire for acknowledgment and appreciation

##### Motivation States
- **Active**: Currently driving behavior
- **Dormant**: Present but not currently influential
- **Conflicting**: When two motivation nodes pull a character in opposite directions
- **Reinforcing**: When multiple motivation nodes align toward the same goal
- **Thwarted**: When a character's core motivation is repeatedly blocked
- **Unconscious**: Drives that influence behavior without the character's awareness

#### Goals
Each character has specific goals in the scene. These are what they are trying to accomplish, derived from their motivation patterns.
- **Explicit Goals**: What the character consciously wants
- **Implicit Goals**: What the character unconsciously seeks
- **Short-term Goals**: Immediate objectives within the scene
- **Long-term Goals**: Objectives that extend beyond the current scene

#### Actions
Actions are how characters pursue their goals, influenced by their motivations.

##### Verbal Actions
People say things verbally to accomplish something. Communication is a tool that can be:
- **Direct**: Explicitly stating intentions or requests
- **Indirect**: Implying intentions through subtext
- **Truthful**: Honest communication of facts or feelings
- **Deceptive**: Deliberately misleading or withholding information
- **Emotional**: Expressing feelings or triggering emotions in others
- **Rational**: Appealing to logic or reason
- **Persuasive**: Attempting to change another's beliefs or actions
- **Informative**: Sharing knowledge or information

##### Physical Actions
Physical movements and behaviors that characters perform:
- **Deliberate**: Conscious, intentional actions
- **Reactive**: Responses to external stimuli
- **Habitual**: Unconscious patterns of behavior
- **Symbolic**: Actions with deeper meaning beyond the physical act

##### Internal Actions
Mental processes that influence external behavior:
- **Decision-making**: Choosing between options
- **Perception**: How characters interpret events and others' actions
- **Emotional processing**: How characters handle feelings
- **Memory recall**: Accessing past experiences

### Events
Events are occurrences that happen beyond the characters' direct control. They can be:
- **External**: Environmental changes, natural phenomena, actions by off-scene characters
- **Coincidental**: Random occurrences that impact the scene
- **Consequential**: Results of previous actions or decisions
- **Transformative**: Events that fundamentally change the scene dynamics

### Objects
Physical or conceptual items that characters interact with:
- **Tools**: Items used to accomplish goals
- **Symbols**: Objects with significance beyond their physical properties
- **Barriers**: Objects that impede character goals
- **Resources**: Objects that facilitate character goals

### Locations
The physical or virtual spaces where the scene takes place:
- **Physical attributes**: Sensory details of the environment
- **Emotional atmosphere**: The mood or feeling of the space
- **Constraints**: How the location limits character actions
- **Opportunities**: How the location enables character actions
- **Symbolic meaning**: What the location represents thematically

## Edges (Relationships)

### Character-to-Character
- **Power dynamics**: Authority, submission, equality
- **Emotional bonds**: Love, hate, trust, suspicion
- **History**: Shared past experiences, conflicts, alliances
- **Knowledge asymmetry**: What one knows that the other doesn't
- **Interdependence**: How characters rely on each other

### Character-to-Motivation
- **Strength**: How powerful the motivation is
- **Awareness**: Whether the character is conscious of the motivation
- **Target**: What object/person/concept the motivation is directed toward

### Character-to-Goal
- **Commitment**: How dedicated the character is to the goal
- **Progress**: How close the character is to achieving the goal
- **Obstacles**: What stands in the way of the goal

### Character-to-Action
- **Intent**: What the character hopes to accomplish
- **Skill**: How effectively the character can perform the action
- **Consequence**: What results from the action

### Character-to-Location
- **Familiarity**: How well the character knows the location
- **Control**: How much influence the character has over the space
- **Comfort**: How at ease the character feels in the location

### Action-to-Outcome
- **Causality**: How directly the action leads to the outcome
- **Predictability**: How expected the outcome was
- **Significance**: How important the outcome is to the scene

## Scene Structure

### Scene Goals
What the scene needs to accomplish in the narrative:
- **Plot advancement**: Moving the story forward
- **Character development**: Revealing or changing character traits
- **World-building**: Expanding the setting or context
- **Theme exploration**: Developing thematic elements
- **Emotional impact**: Creating specific feelings in the audience

### Tension Dynamics
How conflict and resolution operate within the scene:
- **Rising action**: Building complications and stakes
- **Climax**: Point of highest tension or decision
- **Resolution**: How tensions are resolved or transformed
- **Unresolved elements**: Tensions that carry forward

### Causal Flow
The chain of cause and effect that drives the scene:
1. **Motivation** → Drives → **Goal**
2. **Goal** → Necessitates → **Action**
3. **Action** → Produces → **Reaction/Outcome**
4. **Outcome** → Affects → **Motivation** (creating a cycle)

### Emotional Arc
The emotional journey of characters and audience:
- **Opening state**: Initial emotional conditions
- **Emotional shifts**: Changes in feeling throughout the scene
- **Closing state**: Final emotional conditions
- **Emotional contrast**: Differences between characters' emotions

## Implementation Guidelines

When generating a scene graph:

1. Start with character motivations as the primary drivers
2. Ensure all actions logically flow from motivations and goals
3. Create meaningful conflicts through opposing character goals
4. Balance external events with character agency
5. Maintain causal connections between all elements
6. Ensure the location meaningfully impacts character options
7. Track emotional states throughout the scene
8. Create resolution that feels both surprising and inevitable

A scene is considered complete when there has been an interaction between character, motivation, internal state, goal, action, event, and outcome.