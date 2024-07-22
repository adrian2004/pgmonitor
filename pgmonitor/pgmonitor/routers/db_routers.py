class PrimaryRouter:
    """
    A router to control all database operations on models in the
    primary application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read primary models go to primary.
        """
        if model._meta.app_label == 'app_pgmonitor':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write primary models go to primary.
        """
        if model._meta.app_label == 'app_pgmonitor':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the primary app is involved.
        """
        if obj1._meta.app_label == 'app_pgmonitor' or \
           obj2._meta.app_label == 'app_pgmonitor':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the primary app only appears in the 'primary'
        database.
        """
        if app_label == 'app_pgmonitor':
            return db == 'default'
        return None

class SecondaryRouter:
    """
    A router to control all database operations on models in the
    secondary application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read secondary models go to secondary.
        """
        if model._meta.app_label == 'app_pgmonitor':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write secondary models go to secondary.
        """
        if model._meta.app_label == 'app_pgmonitor':
            return 'secondary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the secondary app is involved.
        """
        if obj1._meta.app_label == 'app_pgmonitor' or \
           obj2._meta.app_label == 'app_pgmonitor':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the secondary app only appears in the 'secondary'
        database.
        """
        if app_label == 'app_pgmonitor':
            return db == 'secondary'
        return None