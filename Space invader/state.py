class BulletState():
    INVISIBLE = 'invisible'
    FLYING = 'flying'
    COOLDOWN = 'cooldown'

class RocketState():
    READY = 'ready'
    FIRE = 'fire'
    EXPLODE = 'explode'
    RELOADING = 'reloading'


class EnemyState():
    ALIVE = 'alive'
    DEAD = 'dead'

ROCKET_MOVING_TIME = 5