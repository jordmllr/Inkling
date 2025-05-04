import kuzu

# Initialize Kuzu database
db_path = "./story_graph_db"
db = kuzu.Database(db_path)
conn = kuzu.Connection(db)

# Create schema for our narrative graph
def create_schema():
    # Create node tables for core entities
    conn.execute("CREATE NODE TABLE Character(name STRING, description STRING, background STRING, memory STRING)")
    conn.execute("CREATE NODE TABLE Setting(name STRING, description STRING, physical_attributes STRING[], emotional_atmosphere STRING)")
    conn.execute("CREATE NODE TABLE Scene(name STRING, goals STRING[], emotional_opening STRING, emotional_closing STRING)")
    conn.execute("CREATE NODE TABLE Event(name STRING, description STRING, event_type STRING)")
    conn.execute("CREATE NODE TABLE Theme(name STRING, description STRING)")
    conn.execute("CREATE NODE TABLE Object(name STRING, description STRING, object_type STRING)")

    # Create node tables for scene graph components
    conn.execute("CREATE NODE TABLE Motivation(type STRING, state STRING, description STRING)")
    conn.execute("CREATE NODE TABLE Goal(description STRING, goal_type STRING, timeframe STRING)")
    conn.execute("CREATE NODE TABLE Action(description STRING, action_type STRING)")
    conn.execute("CREATE NODE TABLE Outcome(description STRING, significance STRING)")

    # Create relationship tables for scene connections
    conn.execute("CREATE REL TABLE LEADS_TO(FROM Scene TO Scene, transition_type STRING, tension_state STRING)")

    # Create relationship tables for character connections
    conn.execute("CREATE REL TABLE APPEARS_IN(FROM Character TO Scene, role STRING)")
    conn.execute("CREATE REL TABLE RELATED_TO(FROM Character TO Character, relationship STRING, power_dynamic STRING, emotional_bond STRING)")

    # Create relationship tables for scene settings
    conn.execute("CREATE REL TABLE LOCATED_IN(FROM Scene TO Setting, description STRING)")
    conn.execute("CREATE REL TABLE CONTAINS_EVENT(FROM Scene TO Event, importance STRING)")
    conn.execute("CREATE REL TABLE EXPLORES_THEME(FROM Scene TO Theme, strength STRING)")
    conn.execute("CREATE REL TABLE CONTAINS_OBJECT(FROM Scene TO Object, significance STRING)")

    # Create relationship tables for causal flow
    conn.execute("CREATE REL TABLE HAS_MOTIVATION(FROM Character TO Motivation, strength STRING, awareness STRING, target STRING)")
    conn.execute("CREATE REL TABLE DRIVES(FROM Motivation TO Goal, intensity STRING)")
    conn.execute("CREATE REL TABLE PURSUES(FROM Character TO Goal, commitment STRING, progress STRING)")
    conn.execute("CREATE REL TABLE NECESSITATES(FROM Goal TO Action, urgency STRING)")
    conn.execute("CREATE REL TABLE PERFORMS(FROM Character TO Action, intent STRING, skill STRING)")
    conn.execute("CREATE REL TABLE PRODUCES(FROM Action TO Outcome, causality STRING, predictability STRING)")
    conn.execute("CREATE REL TABLE AFFECTS(FROM Outcome TO Motivation, impact STRING)")

    # Create relationship tables for character-location interactions
    conn.execute("CREATE REL TABLE INTERACTS_WITH(FROM Character TO Setting, familiarity STRING, control STRING, comfort STRING)")

# Load initial data from your story files
def load_initial_data():
    # Add characters
    conn.execute("INSERT INTO Character (name, description, background, memory) VALUES ('Franklyn', 'Protagonist, master gardener of the plantation with no memory before the plantation', 'Unknown past before arriving at plantation', 'First memory is stumbling out of the woods onto plantation grounds')")
    conn.execute("INSERT INTO Character (name, description, background, memory) VALUES ('Baron', 'Antagonist, cruel plantation owner', 'Founded the plantation, eccentric billionaire', 'Complete memory and awareness of his actions')")
    conn.execute("INSERT INTO Character (name, description, background, memory) VALUES ('Chef', 'New chef who teaches Franklyn and plots against the Baron', 'Comes from Yoruba with secret mission', 'Remembers injustices of the Baron')")

    # Add settings
    conn.execute("INSERT INTO Setting (name, description, physical_attributes, emotional_atmosphere) VALUES ('Plantation', 'Main setting, founded by eccentric billionaire', ['Large estate', 'Isolated', 'Self-sufficient'], 'Oppressive')")
    conn.execute("INSERT INTO Setting (name, description, physical_attributes, emotional_atmosphere) VALUES ('Kitchen', 'Franklyns primary workspace', ['Hot', 'Busy', 'Confined'], 'Tense but creative')")
    conn.execute("INSERT INTO Setting (name, description, physical_attributes, emotional_atmosphere) VALUES ('Garden', 'Beautiful but oppressive space where spices grow', ['Colorful', 'Fragrant', 'Carefully maintained'], 'Deceptively peaceful')")
    conn.execute("INSERT INTO Setting (name, description, physical_attributes, emotional_atmosphere) VALUES ('Yoruba', 'External location visited during the story', ['Coastal', 'Vibrant', 'Free'], 'Liberating')")

    # Add motivations
    conn.execute("INSERT INTO Motivation (type, state, description) VALUES ('Power', 'Active', 'Desire to control others')")
    conn.execute("INSERT INTO Motivation (type, state, description) VALUES ('Security', 'Active', 'Need for safety and stability')")
    conn.execute("INSERT INTO Motivation (type, state, description) VALUES ('Freedom', 'Dormant', 'Desire for autonomy and self-determination')")
    conn.execute("INSERT INTO Motivation (type, state, description) VALUES ('Revenge', 'Active', 'Desire to punish those who have caused harm')")

    # Add goals
    conn.execute("INSERT INTO Goal (description, goal_type, timeframe) VALUES ('Maintain control of plantation', 'Explicit', 'Long-term')")
    conn.execute("INSERT INTO Goal (description, goal_type, timeframe) VALUES ('Survive daily life', 'Explicit', 'Short-term')")
    conn.execute("INSERT INTO Goal (description, goal_type, timeframe) VALUES ('Find meaning in existence', 'Implicit', 'Long-term')")
    conn.execute("INSERT INTO Goal (description, goal_type, timeframe) VALUES ('Overthrow the Baron', 'Explicit', 'Long-term')")

    # Add scenes
    conn.execute("INSERT INTO Scene (name, goals, emotional_opening, emotional_closing) VALUES ('Execution Day', ['Show execution of old chef', 'Establish oppressive atmosphere', 'Introduce Franklyn', 'Reveal Barons cruelty'], 'Tense', 'Fearful')")
    conn.execute("INSERT INTO Scene (name, goals, emotional_opening, emotional_closing) VALUES ('Daily Life', ['Show Franklyns routine', 'Establish hopelessness', 'Introduce supporting characters', 'Demonstrate Barons control'], 'Resigned', 'Curious')")
    conn.execute("INSERT INTO Scene (name, goals, emotional_opening, emotional_closing) VALUES ('New Chef Arrival', ['Introduce the new chef', 'Show first signs of resistance', 'Plant seeds of hope', 'Establish chef-Franklyn relationship'], 'Curious', 'Hopeful')")

    # Add actions
    conn.execute("INSERT INTO Action (description, action_type) VALUES ('Execute the old chef', 'Physical')")
    conn.execute("INSERT INTO Action (description, action_type) VALUES ('Prepare meals', 'Physical')")
    conn.execute("INSERT INTO Action (description, action_type) VALUES ('Teach Franklyn to read', 'Verbal')")

    # Add outcomes
    conn.execute("INSERT INTO Outcome (description, significance) VALUES ('Fear instilled in workers', 'High')")
    conn.execute("INSERT INTO Outcome (description, significance) VALUES ('Baron pleased with meal', 'Medium')")
    conn.execute("INSERT INTO Outcome (description, significance) VALUES ('Franklyn gains knowledge', 'High')")

    # Connect characters to motivations
    conn.execute("INSERT INTO HAS_MOTIVATION (FROM, TO, strength, awareness, target) VALUES ('Baron', 'Power', 'Strong', 'Conscious', 'Plantation workers')")
    conn.execute("INSERT INTO HAS_MOTIVATION (FROM, TO, strength, awareness, target) VALUES ('Franklyn', 'Security', 'Strong', 'Conscious', 'Self')")
    conn.execute("INSERT INTO HAS_MOTIVATION (FROM, TO, strength, awareness, target) VALUES ('Franklyn', 'Freedom', 'Medium', 'Unconscious', 'Self')")
    conn.execute("INSERT INTO HAS_MOTIVATION (FROM, TO, strength, awareness, target) VALUES ('Chef', 'Revenge', 'Strong', 'Conscious', 'Baron')")

    # Connect motivations to goals
    conn.execute("INSERT INTO DRIVES (FROM, TO, intensity) VALUES ('Power', 'Maintain control of plantation', 'High')")
    conn.execute("INSERT INTO DRIVES (FROM, TO, intensity) VALUES ('Security', 'Survive daily life', 'High')")
    conn.execute("INSERT INTO DRIVES (FROM, TO, intensity) VALUES ('Freedom', 'Find meaning in existence', 'Medium')")
    conn.execute("INSERT INTO DRIVES (FROM, TO, intensity) VALUES ('Revenge', 'Overthrow the Baron', 'High')")

    # Connect characters to goals
    conn.execute("INSERT INTO PURSUES (FROM, TO, commitment, progress) VALUES ('Baron', 'Maintain control of plantation', 'High', 'Ongoing')")
    conn.execute("INSERT INTO PURSUES (FROM, TO, commitment, progress) VALUES ('Franklyn', 'Survive daily life', 'High', 'Ongoing')")
    conn.execute("INSERT INTO PURSUES (FROM, TO, commitment, progress) VALUES ('Franklyn', 'Find meaning in existence', 'Low', 'Beginning')")
    conn.execute("INSERT INTO PURSUES (FROM, TO, commitment, progress) VALUES ('Chef', 'Overthrow the Baron', 'High', 'Planning')")

    # Connect goals to actions
    conn.execute("INSERT INTO NECESSITATES (FROM, TO, urgency) VALUES ('Maintain control of plantation', 'Execute the old chef', 'High')")
    conn.execute("INSERT INTO NECESSITATES (FROM, TO, urgency) VALUES ('Survive daily life', 'Prepare meals', 'High')")
    conn.execute("INSERT INTO NECESSITATES (FROM, TO, urgency) VALUES ('Overthrow the Baron', 'Teach Franklyn to read', 'Medium')")

    # Connect characters to actions
    conn.execute("INSERT INTO PERFORMS (FROM, TO, intent, skill) VALUES ('Baron', 'Execute the old chef', 'Intimidate others', 'High')")
    conn.execute("INSERT INTO PERFORMS (FROM, TO, intent, skill) VALUES ('Franklyn', 'Prepare meals', 'Survive', 'Medium')")
    conn.execute("INSERT INTO PERFORMS (FROM, TO, intent, skill) VALUES ('Chef', 'Teach Franklyn to read', 'Empower ally', 'High')")

    # Connect actions to outcomes
    conn.execute("INSERT INTO PRODUCES (FROM, TO, causality, predictability) VALUES ('Execute the old chef', 'Fear instilled in workers', 'Direct', 'Expected')")
    conn.execute("INSERT INTO PRODUCES (FROM, TO, causality, predictability) VALUES ('Prepare meals', 'Baron pleased with meal', 'Direct', 'Expected')")
    conn.execute("INSERT INTO PRODUCES (FROM, TO, causality, predictability) VALUES ('Teach Franklyn to read', 'Franklyn gains knowledge', 'Direct', 'Expected')")

    # Connect outcomes back to motivations (completing the cycle)
    conn.execute("INSERT INTO AFFECTS (FROM, TO, impact) VALUES ('Fear instilled in workers', 'Security', 'Strengthens')")
    conn.execute("INSERT INTO AFFECTS (FROM, TO, impact) VALUES ('Baron pleased with meal', 'Security', 'Maintains')")
    conn.execute("INSERT INTO AFFECTS (FROM, TO, impact) VALUES ('Franklyn gains knowledge', 'Freedom', 'Awakens')")

    # Connect scenes in sequence
    conn.execute("INSERT INTO LEADS_TO (FROM, TO, transition_type, tension_state) VALUES ('Execution Day', 'Daily Life', 'Temporal', 'Decreasing')")
    conn.execute("INSERT INTO LEADS_TO (FROM, TO, transition_type, tension_state) VALUES ('Daily Life', 'New Chef Arrival', 'Causal', 'Increasing')")

    # Add character appearances in scenes
    conn.execute("INSERT INTO APPEARS_IN (FROM, TO, role) VALUES ('Franklyn', 'Execution Day', 'Witness')")
    conn.execute("INSERT INTO APPEARS_IN (FROM, TO, role) VALUES ('Baron', 'Execution Day', 'Antagonist')")
    conn.execute("INSERT INTO APPEARS_IN (FROM, TO, role) VALUES ('Franklyn', 'Daily Life', 'Protagonist')")
    conn.execute("INSERT INTO APPEARS_IN (FROM, TO, role) VALUES ('Baron', 'Daily Life', 'Background')")
    conn.execute("INSERT INTO APPEARS_IN (FROM, TO, role) VALUES ('Franklyn', 'New Chef Arrival', 'Protagonist')")
    conn.execute("INSERT INTO APPEARS_IN (FROM, TO, role) VALUES ('Chef', 'New Chef Arrival', 'Mentor')")

    # Add scene locations
    conn.execute("INSERT INTO LOCATED_IN (FROM, TO, description) VALUES ('Execution Day', 'Plantation', 'Courtyard')")
    conn.execute("INSERT INTO LOCATED_IN (FROM, TO, description) VALUES ('Daily Life', 'Kitchen', 'Main workspace')")
    conn.execute("INSERT INTO LOCATED_IN (FROM, TO, description) VALUES ('New Chef Arrival', 'Kitchen', 'Introduction space')")

# Query function examples
def query_character_scenes(character_name):
    query = f"""
    MATCH (c:Character)-[r:APPEARS_IN]->(s:Scene)
    WHERE c.name = '{character_name}'
    RETURN s.name, r.role
    """
    return conn.execute(query).get_as_df()

def query_scene_details(scene_name):
    query = f"""
    MATCH (s:Scene)
    WHERE s.name = '{scene_name}'
    RETURN s.name, s.goals, s.emotional_opening, s.emotional_closing
    """
    return conn.execute(query).get_as_df()

def query_scene_sequence():
    query = """
    MATCH (s1:Scene)-[r:LEADS_TO]->(s2:Scene)
    RETURN s1.name AS from_scene, s2.name AS to_scene, r.transition_type, r.tension_state
    """
    return conn.execute(query).get_as_df()

def query_character_motivations(character_name):
    query = f"""
    MATCH (c:Character)-[r:HAS_MOTIVATION]->(m:Motivation)
    WHERE c.name = '{character_name}'
    RETURN m.type, m.state, r.strength, r.awareness, r.target
    """
    return conn.execute(query).get_as_df()

def query_causal_flow_in_scene(scene_name):
    query = f"""
    MATCH (s:Scene)<-[:APPEARS_IN]-(c:Character)-[:HAS_MOTIVATION]->(m:Motivation)-[:DRIVES]->(g:Goal)
    -[:NECESSITATES]->(a:Action)<-[:PERFORMS]-(c2:Character)-[:APPEARS_IN]->(s)
    WHERE s.name = '{scene_name}'
    RETURN c.name AS character, m.type AS motivation, g.description AS goal,
           a.description AS action, c2.name AS actor
    """
    return conn.execute(query).get_as_df()

def query_character_arc(character_name):
    query = f"""
    MATCH path = (c:Character)-[:APPEARS_IN]->(s1:Scene)-[:LEADS_TO*]->(s2:Scene)<-[:APPEARS_IN]-(c)
    WHERE c.name = '{character_name}'
    RETURN [node IN nodes(path) WHERE node:Scene | node.name] AS scene_sequence
    """
    return conn.execute(query).get_as_df()

def query_motivation_to_outcome(motivation_type):
    query = f"""
    MATCH (m:Motivation)-[:DRIVES]->(g:Goal)-[:NECESSITATES]->(a:Action)-[:PRODUCES]->(o:Outcome)
    WHERE m.type = '{motivation_type}'
    RETURN m.type AS motivation, g.description AS goal, a.description AS action, o.description AS outcome
    """
    return conn.execute(query).get_as_df()

if __name__ == "__main__":
    create_schema()
    load_initial_data()
    print("Knowledge graph initialized with scene graph elements")

    # Example queries
    print("\nScenes featuring Franklyn:")
    print(query_character_scenes("Franklyn"))

    print("\nDetails for Execution Day scene:")
    print(query_scene_details("Execution Day"))

    print("\nScene sequence in the narrative:")
    print(query_scene_sequence())

    print("\nFranklyn's motivations:")
    print(query_character_motivations("Franklyn"))

    print("\nCausal flow in 'New Chef Arrival' scene:")
    print(query_causal_flow_in_scene("New Chef Arrival"))