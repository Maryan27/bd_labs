from dao.panel_dao import PanelDAO

class PanelService:
    def __init__(self, mysql):
        self.dao = PanelDAO(mysql)

    def get_panels(self):
        return self.dao.get_all_panels()

    def add_panel(self, panel):
        return self.dao.insert_panel(panel)

    def add_panel_via_procedure(self, station_id, panel_type, installation_date, power, usage_duration):
        """Додає панель через збережену процедуру"""
        self.dao.call_insert_panel_procedure(station_id, panel_type, installation_date, power, usage_duration)

    def modify_panel(self, panel_id, panel):
        return self.dao.update_panel(panel_id, panel)

    def remove_panel(self, panel_id):
        return self.dao.delete_panel(panel_id)
