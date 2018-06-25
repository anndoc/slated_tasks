### Django Project

Create a small, working Django site that serves a simple activity feed list with 3 filters:
* My posts
* Me and the posts of everyone I’m tracking (note: use an asymmetric relationship, meaning, “Even if I track you, you may or may not track me”.)
* Everybody’s posts

### API endpoint

Get users posts

    `/?post=(my|all|tracking) (GET)`

Returns

    [
        {
        'pk': <int>,
        'content': <text>,
        'username': <text>
        }
    ]
