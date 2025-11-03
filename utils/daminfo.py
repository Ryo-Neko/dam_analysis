import pandas as pd


class DamInfo:
    def __init__(self, dam_id_path="../SuimonSuishituDB/fixed_out/site_ids_dam.csv"):
        self.dam_id = pd.read_csv(dam_id_path, header=0)

    def convert_id2name(self, target_id):
        return self.dam_id.loc[self.dam_id["id"] == int(target_id), "観測所名"].to_list()

    def convert_id2riverseries_name(self, target_id):
        return self.dam_id.loc[self.dam_id["id"] == int(target_id), "水系名"].to_list()

    def convert_id2river_name(self, target_id):
        return self.dam_id.loc[self.dam_id["id"] == int(target_id), "河川名"].to_list()

    def convert_rivername2id(self, rivername):
        return self.dam_id.loc[self.dam_id["河川名"] == rivername, "id"].to_list()
