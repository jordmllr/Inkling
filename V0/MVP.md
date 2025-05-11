# Inkling MVP: Progressive Web App Architecture

## Overview

Inkling is a fiction writing tool that helps writers develop narratives through a structured approach to scene development, character motivation, and narrative flow. This MVP outlines the architecture for implementing Inkling as a progressive web app using htmx and Alpine.js.

## Core Philosophy

- **Progressive Enhancement**: Start with functional HTML, enhance with JavaScript
- **Server-driven UI**: Use htmx for server-side rendering and partial updates
- **Minimal Client-side State**: Leverage Alpine.js only where needed for UI interactions
- **Offline Capability**: Enable writers to work without constant internet connection
- **Graph-based Narrative Structure**: Implement scene graphs as the primary unit of narrative structure

## Technology Stack

### Frontend
- **HTML/CSS**: Semantic markup with responsive design
- **htmx**: For dynamic content loading and server interactions without full page refreshes
- **Alpine.js**: For lightweight client-side interactivity
- **Service Workers**: For offline capabilities and caching
- **LocalStorage/IndexedDB**: For client-side data persistence

### Backend
- **Python**: Core application logic
- **FastAPI**: API framework for serving htmx requests and JSON endpoints
- **SQLite/SQLAlchemy**: For data persistence with graph capabilities
- **Jinja2**: Server-side templating

## Key Features for MVP

1. **Scene Graph Management**
   - Create, edit, and connect scenes
   - Visualize narrative flow between scenes
   - Track character appearances across scenes

2. **Character Motivation System**
   - Define character motivations based on psychological models
   - Connect motivations to specific objects, people, or concepts
   - Track motivation evolution throughout the narrative

3. **Writing Interface**
   - Distraction-free writing environment
   - Context-aware sidebar with relevant scene/character information
   - Real-time saving and version history

4. **Offline Functionality**
   - Work without internet connection
   - Sync changes when connection is restored
   - Cache resources for improved performance

## Architecture Components

### 1. Data Layer

#### Core Entities
- **Scene**: The primary narrative unit
- **Character**: Active agents within scenes
- **Motivation**: Psychological drives that influence character behavior
- **Setting**: Locations where scenes take place
- **Object**: Items of significance within the narrative
- **Relationship**: Connections between entities (Character-Character, Character-Object, etc.)

#### Data Storage
- Server-side SQLite database with graph capabilities
- Client-side IndexedDB for offline data access and modifications

### 2. Server Layer

#### API Endpoints
- RESTful endpoints for CRUD operations on all entities
- Specialized endpoints for graph operations (connections, traversals)
- htmx-specific endpoints returning HTML fragments

#### Server Components
- Authentication service
- Data persistence service
- Template rendering service
- Sync service (for offline changes)

### 3. Client Layer

#### UI Components
- **Navigation**: htmx-powered navigation with minimal page refreshes
- **Editor**: Alpine.js enhanced writing interface
- **Graph Visualizer**: Interactive visualization of scene connections
- **Character Dashboard**: Overview of character motivations and appearances
- **Timeline View**: Chronological arrangement of scenes

#### Client Services
- Service worker for offline capabilities
- Sync manager for handling offline changes
- Local storage manager

## Implementation Approach

### Phase 1: Core Structure
1. Set up basic FastAPI application with Jinja2 templates
2. Implement data models for Scene, Character, and Motivation
3. Create basic CRUD operations for all entities
4. Develop simple UI with htmx for navigation and data manipulation

### Phase 2: Enhanced Functionality
1. Implement graph database capabilities for entity relationships
2. Develop the scene graph visualization
3. Create the motivation system with psychological models
4. Enhance the writing interface with Alpine.js

### Phase 3: Offline Capabilities
1. Implement service workers for offline access
2. Develop client-side storage with IndexedDB
3. Create sync mechanism for offline changes
4. Add progressive enhancement for network-constrained environments

## User Experience Flow

1. **Writer creates a new project**
   - Enters basic project information
   - System creates initial database structure

2. **Writer develops characters**
   - Defines character attributes
   - Establishes motivation patterns
   - Sets up character relationships

3. **Writer creates scene graph**
   - Defines scenes with goals
   - Connects scenes to form narrative flow
   - Assigns characters to scenes

4. **Writer develops scene content**
   - Writes scene content with context-aware sidebar
   - System tracks character motivations and goals
   - Changes automatically saved and versioned

5. **Writer reviews narrative structure**
   - Visualizes scene connections
   - Analyzes character arcs across scenes
   - Identifies gaps or inconsistencies

## Technical Implementation Details

### htmx Usage
- Navigation between views without full page reloads
- Form submissions with inline validation and feedback
- Partial updates of UI components (character lists, scene connections)
- Server-sent events for collaborative features (future enhancement)

### Alpine.js Integration
- Form validation and UI feedback
- Interactive components (dropdowns, tooltips)
- Managing small pieces of UI state
- Enhancing the writing interface with contextual tools

### Offline Strategy
- Service worker caches core application assets
- IndexedDB stores user data locally
- Changes tracked with timestamps for conflict resolution
- Background sync when connection is restored

## Metrics for Success

- **Usability**: Writers can create and connect scenes without friction
- **Performance**: Page load and interaction times below 300ms
- **Reliability**: App functions without internet connection
- **Engagement**: Time spent writing vs. time spent navigating UI

## Future Enhancements (Post-MVP)

- AI assistance for scene development and character motivation
- Collaborative writing capabilities
- Advanced visualization of narrative structures
- Export to various formats (PDF, EPUB, etc.)
- Integration with external writing tools

## Development Roadmap

### Week 1-2: Foundation
- Set up project structure
- Implement core data models
- Create basic API endpoints
- Develop initial UI templates

### Week 3-4: Core Functionality
- Implement scene graph management
- Develop character motivation system
- Create basic writing interface
- Set up authentication

### Week 5-6: Enhanced Features
- Implement visualization components
- Develop offline capabilities
- Create sync mechanism
- Polish UI/UX

### Week 7-8: Testing & Refinement
- User testing with writers
- Performance optimization
- Bug fixes and refinements
- Documentation
