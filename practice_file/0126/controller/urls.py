from controller import user, board, root

def urls():
    return [root.router, user.router, board.router]