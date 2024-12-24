def recommend_task(emotion):
    task_mapping = {
        "happy": ["Collaborative brainstorming", "Creative projects"],
        "sad": ["Low-stress tasks", "Personal development activities"],
        "angry": ["Independent work", "Tasks with clear outcomes"],
        "neutral": ["Regular workload", "Moderate complexity tasks"],
        "stressed": ["Light workload", "Take a break, or mindfulness activities"]
    }
    return task_mapping.get(emotion.lower(), ["General tasks"])