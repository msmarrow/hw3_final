# File: refund_action.py
# Author: Mahjeed Marrow
# Description: handles ticket refunds
import ticket as Tix
import util

def issue_refund(ticket_id, route_ledger, ticket_records):
    count = 0
    updated_records = Tix.remove_ticket_from_records(ticket_id, ticket_records, route_ledger)
    return updated_records
