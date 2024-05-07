class AuthRouter:
    """
    Um roteador para controlar todas as operações de banco de dados em modelos no
    aplicativos de autenticação e contenttypes.
    """

    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de ler os modelos auth e contenttypes vão para sds_web_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "sds_web_db"
        return None

    def db_for_write(self, model, **hints):
        """
        As tentativas de escrever modelos auth e contenttypes vão para sds_web_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "sds_web_db"
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
        Certifique-se de que os aplicativos auth e contenttypes apareçam apenas no banco de dados 'sds_web_db'.
        """
        if app_label in self.route_app_labels:
            return db == "sds_web_db"
        return None

class SdsWebRouter:
    """
    Um roteador para controlar todas as operações de banco de dados em modelos no
    aplicativos de autenticação e contenttypes.
    """

    route_app_labels = {'sds_web'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de ler os modelos auth e contenttypes vão para sds_web_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "sds_web_db"
        return None

    def db_for_write(self, model, **hints):
        """
        As tentativas de escrever modelos auth e contenttypes vão para sds_web_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "sds_web_db"
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
        Certifique-se de que os aplicativos auth e contenttypes apareçam apenas no banco de dados 'sds_web_db'.
        """
        if app_label in self.route_app_labels:
            return db == "sds_web_db"
        return None



class SdsInventarioRouter:
    """
    Um roteador para controlar todas as operações de banco de dados em modelos no
    aplicativos de autenticação e contenttypes.
    """

    route_app_labels = {'sds_inventario'}

    def db_for_read(self, model, **hints):
        """
        As tentativas de ler os modelos auth e contenttypes vão para sds_inventario_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "sds_inventario_db"
        return None

    def db_for_write(self, model, **hints):
        """
        As tentativas de escrever modelos auth e contenttypes vão para sds_inventario_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "sds_inventario_db"
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
        Certifique-se de que os aplicativos auth e contenttypes apareçam apenas no banco de dados 'sds_inventario_db'.
        """
        if app_label in self.route_app_labels:
            return db == "sds_inventario_db"
        return None    
           

