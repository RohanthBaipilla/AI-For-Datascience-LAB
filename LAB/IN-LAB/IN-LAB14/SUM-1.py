def unify_interests(alice_interests, bob_interests):
    common_interests = []
    for interest in alice_interests:
        if interest in bob_interests:
            common_interests.append(interest)
    return common_interests

alice_interests = ['reading', 'traveling', 'cooking']
bob_interests = ['hiking', 'cooking', 'photography']

print(unify_interests(alice_interests, bob_interests))
