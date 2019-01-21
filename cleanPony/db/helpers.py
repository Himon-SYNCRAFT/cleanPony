from pony.orm import db_session, commit, rollback


def execute_in_transaction(f):
    def wrapped_f(*args):
        with db_session:
            try:
                rv = f(*args)
                commit()
                return rv
            except Exception:
                rollback()
                raise

    return wrapped_f
