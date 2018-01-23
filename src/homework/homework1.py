def get_hours_since_midnight(total_seconds):
   return seconds // 3600
def get_minutes(total_seconds): 
  return (seconds % 3600) * 60 
def get_seconds(total_seconds): 
   return (seconds % 3600) % 60
