class AuthRouter:
    """
    Um roteador para controlar todas as operações de banco de dados em modelos no
    aplicativos de autenticação e contenttypes.
    """

    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de ler os modelos auth e contenttypes vão para projeto05.
        """
        if model._meta.app_label in self.route_app_labels:
            return "projeto05"
        return None

    def db_for_write(self, model, **hints):
        """
        As tentativas de escrever modelos auth e contenttypes vão para projeto05.
        """
        if model._meta.app_label in self.route_app_labels:
            return "projeto05"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permitir relações se um modelo nos aplicativos auth ou contenttypes estiver envolvido.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Certifique-se de que os aplicativos auth e contenttypes apareçam apenas no banco de dados 'projeto05'.
        """
        if app_label in self.route_app_labels:
            return db == "projeto05"
        return None
    
class Blue:
    """
    Um roteador para controlar todas as operações de banco de dados em modelos no
    aplicativos de autenticação e contenttypes.
    """

    route_app_labels = {'blue'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de ler os modelos auth e contenttypes vão para blue_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "blue_db"
        return None

    def db_for_write(self, model, **hints):
        """
        As tentativas de escrever modelos auth e contenttypes vão para blue_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "blue_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permitir relações se um modelo nos aplicativos auth ou contenttypes estiver envolvido.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Certifique-se de que os aplicativos auth e contenttypes apareçam apenas no banco de dados 'blue_db'.
        """
        if app_label in self.route_app_labels:
            return db == "blue_db"
        return None    
    
class Aqua:
    """
    Um roteador para controlar todas as operações de banco de dados em modelos no
    aplicativos de autenticação e contenttypes.
    """

    route_app_labels = {'aqua'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de ler os modelos auth e contenttypes vão para aqua_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "aqua_db"
        return None

    def db_for_write(self, model, **hints):
        """
        As tentativas de escrever modelos auth e contenttypes vão para aqua_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "aqua_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permitir relações se um modelo nos aplicativos auth ou contenttypes estiver envolvido.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Certifique-se de que os aplicativos auth e contenttypes apareçam apenas no banco de dados 'aqua_db'.
        """
        if app_label in self.route_app_labels:
            return db == "aqua_db"
        return None        