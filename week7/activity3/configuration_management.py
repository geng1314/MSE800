

class ConfigurationManagement:
    
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.system_name = "Smart Device System"
            cls._instance.version = "1.0"   
        return cls._instance
    
    def show_config(self):
        print(f"\n--- [{self.system_name} {self.version}] Config Loaded ---")