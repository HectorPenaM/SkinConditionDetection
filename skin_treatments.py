def give_recommendation(condition):
    """
    Funcion that returns recommendations on how to 
    treat a skin condition 

    Args:
        condition: str 
    
    returns recommendation as list of str
    """

    recommendation_dict = dict()
    recommendation_dict["acne"] = ["Topical Treament: Over-the-counter treatments like" \
                                    "salicylic acid, benzoyl peroxide, and retinoids can be effective.",
                                    "Lifestyle Changes: Maintaining a healthy diet and regular exercise" \
                                    "can help manage acne.", 
                                    "Medical Treatments: If the aforementioned treatments are deemed uneffective" \
                                    "a healthcare provider might recommend prescription medications or therapies such" \
                                    "as antibiotics, hormonal therapies, or laser therapy."]
    
    recommendation_dict["eczema"] = ["Topical Treament: Over-the-counter treatments like" \
                                    "emollients and topical steroids can be effective. These work by" \
                                    "moisturizing the skin and reducing inflammation.",
                                    "Lifestyle Changes: Avoiding substances that trigger or worsen your symptoms can help manage eczema." \
                                    "Regularly moisturizing your skin and avoiding sudden changes in temperature or humidity can also be beneficial", 
                                    "Medical Treatments: If the aforementioned treatments are deemed uneffective" \
                                    "a healthcare provider might recommend prescription medications or therapies such" \
                                    "as antihistamines to help with sleeping, antibiotics to treat skin infections, or light therapy to treat rashes."]
    
    recommendation_dict["eczema"] = ["Surgical Treatments: The primary treatment for all stages of melanoma" \
                                    "often starts with surgery to remove the cancer",
                                    "Lifestyle Changes: Lifestyle Changes: While there are no foods proven to affect melanoma progression or to" \
                                    "prevent melanoma, a balanced diet is recommended1. Avoiding the sun during the middle of the day, wearing" \
                                    "sunscreen year-round, wearing protective clothing, and avoiding tanning lamps and beds can help prevent melanoma", 
                                    "Medical Treatments: Depending on the stage of your cancer, your overall health, and your own" \
                                    "preferences, treatment may include chemotherapy, radiation therapy, immunotherapy, or targeted therapy."]
    
    recommendation_dict["healthy skin"] = ["Topical Treatments: Regularly moisturize your skin to keep it hydrated." \
                                        "Use gentle cleansers that don’t strip your skin of its natural oils.",
                                        "Lifestyle Changes: Maintain a nutrient-dense diet that’s high in protein, healthy fats, and vitamins." \
                                        "Exercise moderation when eating processed foods and sugar. Stay hydrated and get plenty of high-quality sleep",
                                        "Preventive Measures: Protect your skin from harmful UV rays by wearing sunscreen and avoiding the sun during peak hours." \
                                        "Avoid substances that trigger or worsen your skin conditions."]

    if(not condition in recommendation_dict):
        return "No recommendations found for that condition."
    
    return recommendation_dict[condition]

