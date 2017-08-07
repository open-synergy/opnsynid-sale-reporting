# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    uos_id = fields.Many2one(
        string="UoS",
        comodel_name="product.uom",
    )
    product_uos_qty = fields.Float(
        string="Qty. Uos",
    )

    def _select(self):
        str_select = super(SaleReport, self)._select()
        str_select += """
            ,
            t.uos_id AS uos_id,
            SUM(l.product_uos_qty) AS product_uos_qty
            """
        return str_select

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += """
            ,
            t.uos_id
            """
        return group_by_str
