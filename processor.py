from collections import defaultdict


def group_posts_by_user(posts):
    posts_by_user = defaultdict(list)

    for post in posts:
        user_id = post['userId']
        posts_by_user[user_id].append(post)

    return dict(posts_by_user)


def calculate_average_characters(users, posts_by_user):
    report = []
    for user in users:
        user_id = user['id']
        name = user['name']
        posts = posts_by_user.get(user_id, [])
        total_characters = sum(len(post['body']) for post in posts)
        average_characters = total_characters / len(posts) if posts else 0

        report.append({
            'user_id': user_id,
            'user': name,
            'total_posts': len(posts),
            'average_characters': average_characters
        })
    for item in report:
        item['average_characters'] = round(item['average_characters'], 2)

    return report
