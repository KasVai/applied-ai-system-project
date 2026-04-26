class AIInterpreter:
    """
    Specialized Model approach: Classifies text into structured Task data.
    This acts as the 'Natural Language' gateway for PawPal+.
    """
    
    def parse_input(self, user_text: str):
        """
        Simulates an LLM classification. 
        In a production environment, this would hit an OpenAI/Anthropic endpoint.
        """
        text = user_text.lower()
        
        # Priority 5: Critical/Emergency/Medical
        if any(word in text for word in ["med", "blood", "hurt", "vet", "emergency", "pill", "seizure"]):
            return {
                "desc": f"🚨 URGENT: {user_text}", 
                "time": 15, 
                "priority": 5, 
                "freq": "Once"
            }
        
        # Priority 4: Essential Care (Food/Water)
        elif any(word in text for word in ["feed", "food", "dinner", "breakfast", "water", "hungry"]):
            return {
                "desc": f"🍴 {user_text}", 
                "time": 10, 
                "priority": 4, 
                "freq": "Daily"
            }
            
        # Priority 3: Exercise & Engagement
        elif any(word in text for word in ["walk", "run", "play", "park", "fetch"]):
            return {
                "desc": f"🐕 {user_text}", 
                "time": 30, 
                "priority": 3, 
                "freq": "Daily"
            }
            
        # Priority 2: Grooming & Maintenance
        elif any(word in text for word in ["bath", "brush", "groom", "nails", "litter"]):
            return {
                "desc": f"🛁 {user_text}", 
                "time": 20, 
                "priority": 2, 
                "freq": "Weekly"
            }
            
        # Priority 1: Low Priority/Misc
        else:
            return {
                "desc": user_text, 
                "time": 15, 
                "priority": 1, 
                "freq": "Once"
            }