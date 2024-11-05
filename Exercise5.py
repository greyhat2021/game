class GameLevelDesignDocument: 
    def __init__(self, title, genre, storyline): 
        self.title = title 
        self.genre = genre 
        self.storyline = storyline 
        self.levels = [] 
 
    def add_level(self, level_name, theme, objectives, layout, mechanics, visual_design, 
sound_design, technical_requirements, progression, testing): 
        level = { 
            "Level Name": level_name, 
            "Theme": theme, 
            "Objectives": objectives, 
            "Layout": layout, 
            "Gameplay Mechanics": mechanics, 
            "Visual Design": visual_design, 
            "Sound Design": sound_design, 
            "Technical Requirements": technical_requirements, 
            "Level Progression": progression, 
            "Testing and Feedback": testing 
        } 
        self.levels.append(level) 
 
    def generate_document(self): 
        document = f"Game Title: {self.title}\nGenre: {self.genre}\nStoryline: {self.storyline}\n\n" 
        for i, level in enumerate(self.levels): 
            document += f"Level {i + 1}:\n" 
            for key, value in level.items(): 
                document += f"{key}: {value}\n" 
            document += "\n" 
        return document 
 
game_doc = GameLevelDesignDocument("Mystical Forest Adventure", "Action-Adventure", "You are lost in a mystical forest and must find your way home.") 
 
game_doc.add_level( 
    level_name="The Enchanted Grove", 
    theme="Mystical Forest", 
    objectives="Find the hidden crystal to unlock the next area.", 
    layout="A winding path with various checkpoints and a crystal at the end.", 
    mechanics="Player can jump, climb, and interact with objects.", 
    visual_design="Vibrant colors, lush greenery, and glowing crystals.", 
    sound_design="Calming background music and ambient forest sounds.", 
    technical_requirements="Developed in Unity for PC and console.", 
    progression="Increasing difficulty with more enemies and traps as you advance.", 
    testing="Playtesting sessions with feedback collection forms." 
) 
 
game_doc.add_level( 
    level_name="The Dark Cave", 
    theme="Dark Cave", 
    objectives="Navigate through the cave and escape before time runs out.", 
    layout="Linear path with branching paths leading to hidden treasures.", 
    mechanics="Stealth mechanics to avoid enemies and traps.", 
    visual_design="Dark tones with occasional bioluminescent plants.", 
    sound_design="Eerie sounds echoing through the cave.", 
    technical_requirements="Developed in Unity for PC and console.", 
    progression="More enemies and time constraints as the level progresses.", 
    testing="Playtesting sessions with a focus on timing challenges." 
) 
 
print(game_doc.generate_document()) 